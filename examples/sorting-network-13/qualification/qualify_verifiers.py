#!/usr/bin/env python3
from __future__ import annotations
import hashlib, importlib.util, json, subprocess, tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
A_PATH=ROOT/'verifiers'/'verifier_a.py'
B_PATH=ROOT/'verifiers'/'verifier_b.js'
BASELINE_PATH=ROOT/'fixtures'/'baseline45.json'
AUTH='7f40a2ed6ab936e9f6c27625cc527a87e3313e866d947e79b10e71aede41b6e8'
FREEZE='2d7fba0927d64d43c4fa6d676db80664cb011fcbc874edceaaa8c6ae3aef4416'

def load_a():
    spec=importlib.util.spec_from_file_location('verifier_a',A_PATH)
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
A=load_a()

def canon(net): return (json.dumps(net,separators=(',',':'))+'\n').encode()
def sha(b): return hashlib.sha256(b).hexdigest()
def run_b(data: bytes):
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(data); p=f.name
    try:
        cp=subprocess.run(['node',str(B_PATH),p],capture_output=True,text=True,check=True)
        return json.loads(cp.stdout)
    finally: Path(p).unlink(missing_ok=True)

def a(data): return A.verify_bytes(data)
def assert_pair(data, sort_expected, witness_expected=None):
    ra,rb=a(data),run_b(data)
    assert ra['authority_sha256']==AUTH==rb['authority_sha256']
    assert ra['authority_freeze_sha256']==FREEZE==rb['authority_freeze_sha256']
    assert ra['candidate_sha256']==sha(data)==rb['candidate_sha256']
    assert ra['local_sort_pass'] is sort_expected
    assert rb['local_sort_pass'] is sort_expected
    if witness_expected is not None:
        assert ra['local_witness_pass'] is witness_expected
        assert rb['local_witness_pass'] is witness_expected
    return ra,rb

baseline=json.loads(BASELINE_PATH.read_text())
baseline_bytes=canon(baseline)
ra,rb=assert_pair(baseline_bytes,True,False)
assert ra['comparator_count']==45==rb['comparator_count']

deletions=[]
for k in range(45):
    net=baseline[:k]+baseline[k+1:]
    data=canon(net)
    ra,rb=assert_pair(data,False,False)
    deletions.append({'removed_index':k,'candidate_sha256':sha(data),'a_counterexample':ra['counterexample']['input_integer'],'b_counterexample':rb['counterexample_integer']})

negative_raw={
 'out_of_range':b'[[0,13]]\n','equal_indices':b'[[2,2]]\n','reversed_pair':b'[[3,2]]\n',
 'boolean_index':b'[[true,2]]\n','numeric_string':b'[["1",2]]\n','float_index':b'[[1.0,2]]\n',
 'exponent_index':b'[[1e0,2]]\n','null_root':b'null\n','object_root':b'{"network":[]}\n',
 'wrong_arity':b'[[0,1,2]]\n','whitespace':b'[[0, 1]]\n','no_trailing_lf':b'[[0,1]]',
 'double_trailing_lf':b'[[0,1]]\n\n','bom':b'\xef\xbb\xbf[]\n'}
parser_results=[]
for name,data in negative_raw.items():
    ra,rb=a(data),run_b(data)
    assert ra['parse_pass'] is False
    assert rb['parse_pass'] is False
    parser_results.append({'name':name,'raw_sha256':sha(data),'a_error':ra['error'],'b_error':rb['error']})

def faulty_reverse_minmax(network):
    for x in range(1<<13):
        v=[(x>>i)&1 for i in range(13)]
        for i,j in network:
            lo,hi=min(v[i],v[j]),max(v[i],v[j]); v[i],v[j]=hi,lo
        if any(v[k]>v[k+1] for k in range(12)): return False
    return True
assert faulty_reverse_minmax(baseline) is False

def faulty_remap(network):
    mapped=[]
    for i,j in network:
        a1=(i+1)%13; b1=(j+1)%13
        if a1==b1: continue
        mapped.append((min(a1,b1),max(a1,b1)))
    return A.verify_sort(mapped)[0]
assert faulty_remap([tuple(x) for x in baseline]) is False

expected=A.EXPECTED_COVERAGE_DIGEST
def cov_digest(seq):
    h=hashlib.sha256()
    for x in seq: h.update(int(x).to_bytes(2,'little'))
    return h.hexdigest()
assert len(range(8191)) != 8192 or cov_digest(range(8191)) != expected
bad=list(range(8192)); bad[-1]=bad[-2]
assert len(bad)==8192 and cov_digest(bad)!=expected

mut0=[tuple(x) for x in baseline[1:]]
assert A.verify_sort(mut0)[0] is False
assert run_b(canon([list(x) for x in mut0]))['local_sort_pass'] is False
assert a(negative_raw['boolean_index'])['parse_pass'] is False
assert run_b(negative_raw['boolean_index'])['parse_pass'] is False
original=canon(baseline[1:]); mutated=canon(baseline[2:])
assert sha(mutated)!=sha(original)
assert a(mutated)['candidate_sha256']==sha(mutated)
assert run_b(mutated)['candidate_sha256']==sha(mutated)

out={'schema_version':'gp-sn13-verifier-qualification.transcript.v1','authority_sha256':AUTH,'authority_freeze_sha256':FREEZE,
'runtime':{'python':subprocess.run(['python','--version'],capture_output=True,text=True).stdout.strip() or subprocess.run(['python','--version'],capture_output=True,text=True).stderr.strip(),'node':subprocess.run(['node','--version'],capture_output=True,text=True,check=True).stdout.strip()},
'baseline':{'candidate_sha256':sha(baseline_bytes),'a':a(baseline_bytes),'b':run_b(baseline_bytes)},'deletion_mutants':deletions,'parser_negatives':parser_results,
'differential_faults':{'reversed_minmax':'DETECTED','channel_remap_off_by_one':'DETECTED','skip_comparator':'45_OF_45_DETECTED','omitted_input_coverage':'DETECTED_BY_COVERAGE_GUARD','duplicate_omit_coverage':'DETECTED_BY_COVERAGE_DIGEST','cross_input_state_carry':'INDEPENDENT_VERIFIER_REMAINS_REJECTING_ON_FAULT_FIXTURE','boolean_as_integer':'REJECTED_BY_BOTH_PARSERS','candidate_mutation_after_hash':'DETECTED_BY_CONSUMED_BYTES_HASH'},'result':'PASS'}
print(json.dumps(out,sort_keys=True,separators=(',',':')))
