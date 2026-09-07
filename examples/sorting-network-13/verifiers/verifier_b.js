#!/usr/bin/env node
'use strict';
const fs=require('fs');
const crypto=require('crypto');
const AUTHORITY_SHA256='7f40a2ed6ab936e9f6c27625cc527a87e3313e866d947e79b10e71aede41b6e8';
const FREEZE_SHA256='2d7fba0927d64d43c4fa6d676db80664cb011fcbc874edceaaa8c6ae3aef4416';
const CHANNELS=13, TARGET_MAX=44, INPUTS=1<<CHANNELS;
const CANON=/^\[(?:\[(?:0|[1-9][0-9]*),(?:0|[1-9][0-9]*)\](?:,\[(?:0|[1-9][0-9]*),(?:0|[1-9][0-9]*)\])*)?\]\n$/;
const digest=b=>crypto.createHash('sha256').update(b).digest('hex');
function parseCanonical(buf){
  if(buf.length>=3 && buf[0]===0xef && buf[1]===0xbb && buf[2]===0xbf) throw new Error('NON_CANONICAL_ENCODING');
  const s=buf.toString('utf8');
  if(!CANON.test(s)) throw new Error('NON_CANONICAL_ENCODING');
  const x=JSON.parse(s);
  if(!Array.isArray(x)) throw new Error('ROOT_NOT_ARRAY');
  return x.map(c=>{
    if(!Array.isArray(c)||c.length!==2) throw new Error('BAD_COMPARATOR_SHAPE');
    const [i,j]=c;
    if(!Number.isInteger(i)||!Number.isInteger(j)) throw new Error('INDEX_NOT_INTEGER');
    if(!(0<=i && i<j && j<CHANNELS)) throw new Error('BAD_COMPARATOR_INDEX');
    return [i,j];
  });
}
function initialColumns(){
  const cols=Array(CHANNELS).fill(0n);
  for(let x=0;x<INPUTS;x++){
    const bit=1n<<BigInt(x);
    for(let c=0;c<CHANNELS;c++) if((x>>c)&1) cols[c] |= bit;
  }
  return cols;
}
const FULL_MASK=(1n<<BigInt(INPUTS))-1n;
function verifySort(network){
  const cols=initialColumns();
  for(const [i,j] of network){
    const a=cols[i], b=cols[j];
    cols[i]=a & b;
    cols[j]=a | b;
  }
  for(let k=0;k<CHANNELS-1;k++){
    const bad=cols[k] & ((~cols[k+1]) & FULL_MASK);
    if(bad!==0n){
      let idx=0n, t=bad;
      while((t&1n)===0n){t >>= 1n; idx++;}
      return {pass:false,counterexample_integer:Number(idx)};
    }
  }
  return {pass:true,counterexample_integer:null};
}
function verifyBytes(buf){
  const candidateSha=digest(buf);
  let network;
  try{ network=parseCanonical(buf); }
  catch(e){return {verifier:'B',authority_sha256:AUTHORITY_SHA256,authority_freeze_sha256:FREEZE_SHA256,candidate_sha256:candidateSha,parse_pass:false,error:e.message,local_sort_pass:false,local_witness_pass:false};}
  const r=verifySort(network);
  const witness=r.pass && network.length<=TARGET_MAX;
  return {verifier:'B',authority_sha256:AUTHORITY_SHA256,authority_freeze_sha256:FREEZE_SHA256,candidate_sha256:candidateSha,parse_pass:true,comparator_count:network.length,state_representation:'8192-bit BigInt column truth sets',local_sort_pass:r.pass,local_witness_pass:witness,witness_failure_reason:witness?null:(r.pass?'COMPARATOR_COUNT_EXCEEDS_TARGET':'DOES_NOT_SORT'),counterexample_integer:r.counterexample_integer};
}
if(require.main===module){
  if(process.argv.length!==3){console.error('usage: verifier_b.js <canonical-network.json>');process.exit(2);}
  const buf=fs.readFileSync(process.argv[2]);
  console.log(JSON.stringify(verifyBytes(buf)));
}
module.exports={parseCanonical,verifySort,verifyBytes};
