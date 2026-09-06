#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, time
from pathlib import Path

WORKFLOW_ID='GP-SN13-44-V1'
SEARCH_PASS_ID='GP-SN13-44-SEARCH-003'
AUTHORITY_SHA256='7f40a2ed6ab936e9f6c27625cc527a87e3313e866d947e79b10e71aede41b6e8'
AUTHORITY_FREEZE_SHA256='2d7fba0927d64d43c4fa6d676db80664cb011fcbc874edceaaa8c6ae3aef4416'
STARTING_SHA256='2f05525e158e7c33b1f77612fe39c1fd12c416f2c0f758540a84a02322d6807a'
WALL_LIMIT=300.0
COMPUTE_DEADLINE=298.5
CHANNELS=13
TARGET=44
PAIRS=[(i,j) for i in range(CHANNELS) for j in range(i+1,CHANNELS)]
ROOT=Path(__file__).resolve().parents[1]
START_PATH=ROOT/'search'/'run-pass2'/'best-candidate.json'
OUTDIR=ROOT/'search'/'run-pass3'
INPUTS=1<<CHANNELS
FULL=(1<<INPUTS)-1
INITIAL=[]
for c in range(CHANNELS):
    col=0
    for x in range(INPUTS):
        if (x>>c)&1: col |= 1<<x
    INITIAL.append(col)

def canon(net): return (json.dumps([list(x) for x in net],separators=(',',':'))+'\n').encode()
def sha(data): return hashlib.sha256(data).hexdigest()

def score(net):
    cols=INITIAL.copy()
    for i,j in net:
        a,b=cols[i],cols[j]
        cols[i]=a&b; cols[j]=a|b
    bad_union=0; adjacent_total=0
    for k in range(CHANNELS-1):
        inv=cols[k] & ((~cols[k+1]) & FULL)
        bad_union |= inv; adjacent_total += inv.bit_count()
    return bad_union.bit_count(), adjacent_total

def write_json(path,obj):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n',encoding='utf-8')

def checkpoint(net,sc,stage,evaluations,h1,h2,start):
    OUTDIR.mkdir(parents=True,exist_ok=True)
    data=canon(net); (OUTDIR/'best-candidate.json').write_bytes(data)
    write_json(OUTDIR/'best-checkpoint.json',{
      'schema_version':'gp-sn13-search-checkpoint.v1','workflow_id':WORKFLOW_ID,'search_pass_id':SEARCH_PASS_ID,
      'authority_sha256':AUTHORITY_SHA256,'authority_freeze_sha256':AUTHORITY_FREEZE_SHA256,
      'candidate_sha256':sha(data),'comparator_count':len(net),'score_bad_inputs':sc[0],'score_adjacent_inversions':sc[1],
      'stage':stage,'evaluations':evaluations,'hamming1_evaluated':h1,'hamming2_evaluated':h2,'elapsed_seconds':time.monotonic()-start
    })

def main():
    start=time.monotonic(); compute_stop=start+COMPUTE_DEADLINE
    OUTDIR.mkdir(parents=True,exist_ok=True)
    data=START_PATH.read_bytes()
    if sha(data)!=STARTING_SHA256: raise RuntimeError('STARTING_CANDIDATE_IDENTITY_MISMATCH')
    raw=json.loads(data.decode('utf-8')); center=[tuple(x) for x in raw]
    if len(center)!=TARGET: raise RuntimeError('STARTING_CANDIDATE_LENGTH_MISMATCH')
    center_sc=score(center)
    if center_sc!=(16,16): raise RuntimeError(f'STARTING_SCORE_MISMATCH:{center_sc}')
    best_net=list(center); best_sc=center_sc; best_stage='starting-candidate'
    evaluations=0; h1=0; h2=0; found=False; deadline_hit=False
    checkpoint(best_net,best_sc,best_stage,evaluations,h1,h2,start)

    for p in range(TARGET):
        original=center[p]
        for r in PAIRS:
            if r==original: continue
            if evaluations%256==0 and time.monotonic()>=compute_stop:
                deadline_hit=True; break
            cand=list(center); cand[p]=r
            sc=score(cand); evaluations+=1; h1+=1
            if sc<best_sc:
                best_sc,best_net,best_stage=sc,cand,f'hamming1-p{p}-{r[0]}-{r[1]}'
                checkpoint(best_net,best_sc,best_stage,evaluations,h1,h2,start)
            if sc==(0,0): found=True; break
        if found or deadline_hit: break

    if not found and not deadline_hit:
        for p in range(TARGET-1):
            op=center[p]
            for q in range(p+1,TARGET):
                oq=center[q]
                for rp in PAIRS:
                    if rp==op: continue
                    for rq in PAIRS:
                        if rq==oq: continue
                        if evaluations%256==0 and time.monotonic()>=compute_stop:
                            deadline_hit=True; break
                        cand=list(center); cand[p]=rp; cand[q]=rq
                        sc=score(cand); evaluations+=1; h2+=1
                        if sc<best_sc:
                            best_sc,best_net,best_stage=sc,cand,f'hamming2-p{p}-{rp[0]}-{rp[1]}-q{q}-{rq[0]}-{rq[1]}'
                            checkpoint(best_net,best_sc,best_stage,evaluations,h1,h2,start)
                        if sc==(0,0): found=True; break
                    if found or deadline_hit: break
                if found or deadline_hit: break
            if found or deadline_hit: break

    compute_elapsed=time.monotonic()-start
    expected_h1=TARGET*(len(PAIRS)-1)
    expected_h2=(TARGET*(TARGET-1)//2)*(len(PAIRS)-1)**2
    complete=(h1==expected_h1 and h2==expected_h2)
    best_bytes=canon(best_net); (OUTDIR/'best-candidate.json').write_bytes(best_bytes)
    prefinal=time.monotonic()-start
    result={
      'schema_version':'gp-sn13-search-result.v2','workflow_id':WORKFLOW_ID,'search_pass_id':SEARCH_PASS_ID,
      'authority_sha256':AUTHORITY_SHA256,'authority_freeze_sha256':AUTHORITY_FREEZE_SHA256,
      'starting_candidate_sha256':STARTING_SHA256,'compute_deadline_seconds':COMPUTE_DEADLINE,'wall_limit_seconds':WALL_LIMIT,
      'compute_elapsed_seconds':compute_elapsed,'prefinal_elapsed_seconds':prefinal,'evaluations':evaluations,
      'hamming1_expected':expected_h1,'hamming1_evaluated':h1,'hamming2_expected':expected_h2,'hamming2_evaluated':h2,
      'local_neighborhood_complete':complete,'compute_deadline_hit':deadline_hit,'found_internal_score_zero':found,
      'best_candidate_sha256':sha(best_bytes),'best_comparator_count':len(best_net),'best_score_bad_inputs':best_sc[0],
      'best_score_adjacent_inversions':best_sc[1],'best_stage':best_stage,
      'search_disposition':('CANDIDATE_REQUIRES_GOVERNED_VERIFICATION' if found else 'LOCAL_NEIGHBORHOOD_EXHAUSTED' if complete else 'SEARCH_BUDGET_EXHAUSTED_WITHOUT_RESOLUTION'),
      'budget_compliance':'TO_BE_DETERMINED_BY_POST_EXIT_EXECUTION_RECORD',
      'authority_note':'Local-neighborhood exhaustion is not global nonexistence evidence. Internal score grants no witness standing.'
    }
    write_json(OUTDIR/'search-result.json',result)
    print(json.dumps(result,sort_keys=True,separators=(',',':')))

if __name__=='__main__': main()
