#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, re, sys
from pathlib import Path

AUTHORITY_SHA256 = '7f40a2ed6ab936e9f6c27625cc527a87e3313e866d947e79b10e71aede41b6e8'
FREEZE_SHA256 = '2d7fba0927d64d43c4fa6d676db80664cb011fcbc874edceaaa8c6ae3aef4416'
CHANNELS = 13
TARGET_MAX = 44
CANON_RE = re.compile(rb'^\[(?:\[(?:0|[1-9][0-9]*),(?:0|[1-9][0-9]*)\](?:,\[(?:0|[1-9][0-9]*),(?:0|[1-9][0-9]*)\])*)?\]\n$')

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def parse_canonical(data: bytes):
    if data.startswith(b'\xef\xbb\xbf') or not CANON_RE.fullmatch(data):
        raise ValueError('NON_CANONICAL_ENCODING')
    obj = json.loads(data.decode('utf-8'))
    if not isinstance(obj, list):
        raise ValueError('ROOT_NOT_ARRAY')
    out=[]
    for c in obj:
        if not isinstance(c, list) or len(c)!=2:
            raise ValueError('BAD_COMPARATOR_SHAPE')
        i,j=c
        if type(i) is not int or type(j) is not int:
            raise ValueError('INDEX_NOT_INTEGER')
        if not (0 <= i < j < CHANNELS):
            raise ValueError('BAD_COMPARATOR_INDEX')
        out.append((i,j))
    return out

def coverage_digest() -> str:
    h=hashlib.sha256()
    for x in range(1<<CHANNELS):
        h.update(x.to_bytes(2,'little'))
    return h.hexdigest()

EXPECTED_COVERAGE_DIGEST = coverage_digest()

def verify_sort(network):
    seen=0
    h=hashlib.sha256()
    for x in range(1<<CHANNELS):
        h.update(x.to_bytes(2,'little'))
        seen += 1
        values=[(x >> i) & 1 for i in range(CHANNELS)]
        for i,j in network:
            a,b=values[i],values[j]
            if a>b:
                values[i],values[j]=b,a
        if any(values[k] > values[k+1] for k in range(CHANNELS-1)):
            return False, {'input_integer':x,'input_bits':[(x>>i)&1 for i in range(CHANNELS)],'output':values}, seen, h.hexdigest()
    digest=h.hexdigest()
    if seen != (1<<CHANNELS) or digest != EXPECTED_COVERAGE_DIGEST:
        raise RuntimeError('COVERAGE_GUARD_FAILED')
    return True, None, seen, digest

def verify_bytes(data: bytes):
    candidate_sha=sha256(data)
    try:
        network=parse_canonical(data)
    except Exception as e:
        return {'verifier':'A','authority_sha256':AUTHORITY_SHA256,'authority_freeze_sha256':FREEZE_SHA256,'candidate_sha256':candidate_sha,'parse_pass':False,'error':str(e),'local_sort_pass':False,'local_witness_pass':False}
    sort_pass,counterexample,count,cov=verify_sort(network)
    return {
        'verifier':'A','authority_sha256':AUTHORITY_SHA256,'authority_freeze_sha256':FREEZE_SHA256,
        'candidate_sha256':candidate_sha,'parse_pass':True,'comparator_count':len(network),
        'coverage_count':count,'coverage_digest':cov,'local_sort_pass':sort_pass,
        'local_witness_pass': bool(sort_pass and len(network)<=TARGET_MAX),
        'witness_failure_reason': None if sort_pass and len(network)<=TARGET_MAX else ('COMPARATOR_COUNT_EXCEEDS_TARGET' if sort_pass else 'DOES_NOT_SORT'),
        'counterexample':counterexample
    }

def main():
    if len(sys.argv)!=2:
        raise SystemExit('usage: verifier_a.py <canonical-network.json>')
    data=Path(sys.argv[1]).read_bytes()
    print(json.dumps(verify_bytes(data),sort_keys=True,separators=(',',':')))

if __name__=='__main__': main()
