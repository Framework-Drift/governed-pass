#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, math, random, time
from pathlib import Path

WORKFLOW_ID='GP-SN13-44-V1'
SEARCH_PASS_ID='GP-SN13-44-SEARCH-001'
AUTHORITY_SHA256='7f40a2ed6ab936e9f6c27625cc527a87e3313e866d947e79b10e71aede41b6e8'
AUTHORITY_FREEZE_SHA256='2d7fba0927d64d43c4fa6d676db80664cb011fcbc874edceaaa8c6ae3aef4416'
SEED=13044
WALL_LIMIT=300.0
CHANNELS=13
TARGET=44
PAIRS=[(i,j) for i in range(CHANNELS) for j in range(i+1,CHANNELS)]
BASELINE=[(0,12),(1,10),(2,9),(3,7),(5,11),(6,8),(1,6),(2,3),(4,11),(7,9),(8,10),(0,4),(1,2),(3,6),(7,8),(9,10),(11,12),(4,6),(5,9),(8,11),(10,12),(0,5),(3,8),(4,7),(6,11),(9,10),(0,1),(2,5),(6,9),(7,8),(10,11),(0,1),(2,5)]
# The line above is never used as authority; baseline is reloaded below from the frozen fixture.
ROOT=Path(__file__).resolve().parents[1]
BASELINE_PATH=ROOT/'fixtures'/'baseline45.json'
OUTDIR=ROOT/'search'/'run-pass1'

# 8192-bit truth sets for each channel.
INPUTS=1<<CHANNELS
FULL=(1<<INPUTS)-1
INITIAL=[]
for c in range(CHANNELS):
    col=0
    for x in range(INPUTS):
        if (x>>c)&1: col |= 1<<x
    INITIAL.append(col)

def canon(net):
    return (json.dumps([list(x) for x in net],separators=(',',':'))+'\n').encode()

def sha(data): return hashlib.sha256(data).hexdigest()

def score(net):
    cols=INITIAL.copy()
    for i,j in net:
        a,b=cols[i],cols[j]
        cols[i]=a&b; cols[j]=a|b
    bad_union=0
    adjacent_total=0
    for k in range(CHANNELS-1):
        inv=cols[k] & ((~cols[k+1]) & FULL)
        bad_union |= inv
        adjacent_total += inv.bit_count()
    return bad_union.bit_count(), adjacent_total

def write_json(path,obj):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n',encoding='utf-8')

def checkpoint(net,sc,stage,evaluations,start):
    data=canon(net)
    (OUTDIR/'best-candidate.json').write_bytes(data)
    write_json(OUTDIR/'best-checkpoint.json',{
        'schema_version':'gp-sn13-search-checkpoint.v1','workflow_id':WORKFLOW_ID,'search_pass_id':SEARCH_PASS_ID,
        'authority_sha256':AUTHORITY_SHA256,'authority_freeze_sha256':AUTHORITY_FREEZE_SHA256,
        'stage':stage,'seed':SEED,'evaluations':evaluations,'elapsed_seconds':time.monotonic()-start,
        'candidate_sha256':sha(data),'comparator_count':len(net),'score_bad_inputs':sc[0],'score_adjacent_inversions':sc[1]
    })

def load_baseline():
    raw=json.loads(BASELINE_PATH.read_text(encoding='utf-8'))
    net=[tuple(x) for x in raw]
    if len(net)!=45 or score(net)!=(0,0): raise RuntimeError('BASELINE_CONTROL_FAILED')
    return net

def mutate(net,rng,count=1):
    out=list(net)
    positions=rng.sample(range(TARGET),count)
    for p in positions:
        old=out[p]
        choices=PAIRS
        while True:
            c=choices[rng.randrange(len(choices))]
            if c!=old: break
        out[p]=c
    return out

def main():
    start=time.monotonic(); deadline=start+WALL_LIMIT
    rng=random.Random(SEED)
    baseline=load_baseline()
    evaluations=0
    best_net=None; best_sc=(10**9,10**9); best_stage='none'

    deletion_seeds=[]
    for k in range(45):
        net=baseline[:k]+baseline[k+1:]
        sc=score(net); evaluations+=1
        deletion_seeds.append((sc,net,k))
        if sc<best_sc:
            best_sc,best_net,best_stage=sc,list(net),f'deletion-{k}'
            checkpoint(best_net,best_sc,best_stage,evaluations,start)
        if sc==(0,0): break

    found=(best_sc==(0,0))

    # Exhaust the Hamming-1 comparator-replacement neighborhood of every deletion seed.
    if not found:
        for seed_sc,seed_net,k in sorted(deletion_seeds,key=lambda t:t[0]):
            for pos in range(TARGET):
                old=seed_net[pos]
                for pair in PAIRS:
                    if time.monotonic()>=deadline: break
                    if pair==old: continue
                    cand=list(seed_net); cand[pos]=pair
                    sc=score(cand); evaluations+=1
                    if sc<best_sc:
                        best_sc,best_net,best_stage=sc,cand,f'hamming1-delete-{k}-pos-{pos}'
                        checkpoint(best_net,best_sc,best_stage,evaluations,start)
                    if sc==(0,0): found=True; break
                if found or time.monotonic()>=deadline: break
            if found or time.monotonic()>=deadline: break

    # Seeded beam + perturbation search. Score is search-only and grants no authority.
    if not found and time.monotonic()<deadline:
        ranked=sorted(deletion_seeds,key=lambda t:t[0])
        population=[list(x[1]) for x in ranked[:24]]
        pop_scores=[x[0] for x in ranked[:24]]
        generation=0
        while time.monotonic()<deadline and not found:
            generation += 1
            pool=[]
            # retain elites
            for sc,net in sorted(zip(pop_scores,population),key=lambda z:z[0])[:8]:
                pool.append((sc,list(net)))
            # produce deterministic seeded children with 1-4 replacements
            while len(pool)<160 and time.monotonic()<deadline:
                parent=population[rng.randrange(len(population))]
                r=rng.random()
                nmut=1 if r<0.50 else 2 if r<0.82 else 3 if r<0.96 else 4
                cand=mutate(parent,rng,nmut)
                sc=score(cand); evaluations+=1
                pool.append((sc,cand))
                if sc<best_sc:
                    best_sc,best_net,best_stage=sc,cand,f'beam-generation-{generation}'
                    checkpoint(best_net,best_sc,best_stage,evaluations,start)
                if sc==(0,0): found=True; break
            if found: break
            # dedupe exact networks and retain score-diverse beam
            uniq={}
            for sc,net in pool:
                key=tuple(net)
                if key not in uniq or sc<uniq[key]: uniq[key]=sc
            ranked_pool=sorted(((sc,list(key)) for key,sc in uniq.items()),key=lambda z:z[0])
            population=[net for sc,net in ranked_pool[:48]]
            pop_scores=[sc for sc,net in ranked_pool[:48]]
            # periodic basin escape from current best and top deletion seeds
            if generation%20==0 and population:
                for _ in range(min(8,len(population))):
                    base=list(best_net if rng.random()<0.7 else ranked[rng.randrange(min(12,len(ranked)))][1])
                    nmut=3+rng.randrange(4)
                    population[-1-rng.randrange(min(8,len(population)))]=mutate(base,rng,min(nmut,TARGET))
                pop_scores=[score(net) for net in population]; evaluations+=len(population)
                for sc,net in zip(pop_scores,population):
                    if sc<best_sc:
                        best_sc,best_net,best_stage=sc,list(net),f'escape-generation-{generation}'
                        checkpoint(best_net,best_sc,best_stage,evaluations,start)
                    if sc==(0,0): found=True; break

    elapsed=time.monotonic()-start
    best_bytes=canon(best_net)
    result={
        'schema_version':'gp-sn13-search-result.v1','workflow_id':WORKFLOW_ID,'search_pass_id':SEARCH_PASS_ID,
        'authority_sha256':AUTHORITY_SHA256,'authority_freeze_sha256':AUTHORITY_FREEZE_SHA256,
        'seed':SEED,'wall_limit_seconds':WALL_LIMIT,'elapsed_seconds':elapsed,'evaluations':evaluations,
        'found_internal_score_zero':bool(found),'best_candidate_sha256':sha(best_bytes),'best_comparator_count':len(best_net),
        'best_score_bad_inputs':best_sc[0],'best_score_adjacent_inversions':best_sc[1],'best_stage':best_stage,
        'search_disposition':'CANDIDATE_REQUIRES_GOVERNED_VERIFICATION' if found else 'SEARCH_EXHAUSTED_WITHOUT_RESOLUTION',
        'authority_note':'Internal score is search evidence only. A score-zero candidate has no witness standing until the frozen verifier and review gates pass.'
    }
    write_json(OUTDIR/'search-result.json',result)
    (OUTDIR/'best-candidate.json').write_bytes(best_bytes)
    print(json.dumps(result,sort_keys=True,separators=(',',':')))

if __name__=='__main__': main()
