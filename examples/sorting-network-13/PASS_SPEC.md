# Governed Pass Example — 13-Channel Sorting Network

**Workflow:** `GP-SN13-44-V1`  
**Pass class:** frontier freeze + authority review + verifier qualification + bounded constructive search  
**Domain:** computational combinatorics  
**Canonical authority candidate:** `authority.v1.json`  
**Candidate authority SHA-256:** `0160eb523b452a078e50fbca40649541aacb98abdfdf673b32d0bb1246026edf`  
**Status:** `AUTHORITY_CANDIDATE_NOT_FROZEN`

This example applies the Standing Protocol to a genuinely open problem outside the causal-self-observation program.

The research target is deliberately one-sided:

> Construct a fixed 13-channel sorting network using at most 44 comparators and verify it exhaustively.

This pass does **not** attempt to prove that no such network exists.

## 0. Starting state and frontier

The branch must descend from governed-pass `main` at:

`b8c5b39c9d8dde990e7b59224a610b602ee9c082`

Verify the branch ancestry and the exact canonical authority bytes before substantive work.

The frozen frontier claim for this pass is intentionally conservative:

- a public 45-comparator construction for 13 channels is known;
- the standard compilation currently lists the size interval as 44–45;
- the provenance of the listed 44 lower bound is disputed / not sufficiently authoritative for this pass;
- a valid network with at most 44 comparators would improve the public upper bound regardless of that lower-bound dispute.

Therefore the only novel mathematical success claim authorized by this pass is a **positive construction**.

No search failure, timeout, UNSAT result lacking an independently checkable frozen proof path, heuristic exhaustion, or model judgment may be converted into a lower-bound claim.

## 1. Phase A — authority qualification and freeze

Before writing search or verifier implementation, hostile-review the exact canonical authority candidate.

Attack at minimum:

1. comparator semantics;
2. channel indexing;
3. candidate serialization;
4. the 8192-input zero-one acceptance rule;
5. hidden input dependence;
6. variable-length or malformed candidates;
7. ambiguity between size and depth;
8. the frontier wording;
9. the prohibition on nonexistence claims;
10. the closed disposition vocabulary;
11. whether a searcher can influence its own verifier;
12. whether a promising candidate can change the acceptance predicate.

At least one major authority check must originate outside the specification's derivation chain. A fresh cross-family reviewer is preferred. Bind every review to the SHA-256 of `authority.v1.json`.

Required Phase-A disposition:

`AUTHORITY_COHERENT_TO_IMPLEMENT`

with zero unresolved Critical/High authority findings.

Only then:

- change canonical `authority_status` to a frozen state through a successor committed object or freeze record;
- record the exact authority SHA-256;
- push and verify remote identity.

If the authority requires semantic repair, preserve this candidate and create a successor. Do not edit away the failed reviewed state.

## 2. Phase B — independent verifier implementation

Implement two verifier paths with no code reuse between their decision cores.

### Verifier A — exhaustive direct simulator

Requirements:

- parse only the canonical candidate format;
- enforce `0 <= i < j <= 12`;
- enforce comparator count <= declared bound;
- enumerate all `2^13 = 8192` binary inputs;
- apply the fixed comparator sequence;
- require nondecreasing output for every input;
- on failure, emit at least one exact counterexample input;
- never repair, normalize, reorder, or complete a candidate.

### Verifier B — independent derivation

Implement separately. Cross-language is preferred if the environment supports it; otherwise use a structurally different algorithm and independent source path.

It must not import Verifier A's decision logic or accept Verifier A's boolean as evidence.

### Required qualification controls

Both verifiers must:

1. accept the exact known 45-comparator baseline;
2. reject all 45 single-comparator deletion mutants;
3. reject out-of-range channels;
4. reject reversed/invalid comparator pairs unless the canonical parser explicitly normalizes them before hash identity is assigned;
5. reject malformed candidate structure;
6. reject a candidate with more comparators than its claimed identity permits;
7. return the same verdict on every qualification fixture.

The 45 deletion mutants are fires-controls. If any deletion mutant sorts, stop immediately: that object is itself a <=44 witness and must enter the candidate-verification path rather than being treated as a test fixture.

Qualification evidence must bind exact verifier source, exact authority, exact fixtures, and exact source commit.

## 3. Phase C — verifier hostile review

After qualification, commission fresh hostile implementation review.

Attack:

- candidate parser bypasses;
- accidental candidate normalization;
- incomplete zero-one enumeration;
- state leakage across inputs;
- incorrect comparator orientation;
- off-by-one channel errors;
- mutation of candidate during verification;
- shared-core/common-mode defects between verifiers;
- false acceptance of deletion mutants;
- false rejection of the known baseline;
- caller-supplied `verified=true` or equivalent authority;
- evidence not bound to the exact implementation.

Require zero unresolved Critical/High findings before search begins.

## 4. Phase D — bounded constructive search

Search is subordinate to verification. It may be changed aggressively provided every search-method revision is recorded.

Authorized method families include:

- SAT/SMT;
- constraint programming;
- local/evolutionary search;
- prefix/suffix decomposition;
- symmetry reduction;
- learned heuristics;
- LLM-designed search strategies.

The search objective is only to emit candidate comparator sequences of length <=44.

Search outputs have **no standing** until independently verified.

### Baseline before novelty

Before claiming useful search behavior, reproduce or rediscover at least one valid 45-comparator network under the search representation, or otherwise demonstrate that the search machinery can reach a known-good basin under a frozen diagnostic budget.

This is a search diagnostic, not a requirement that the novel search originate from the baseline.

### Candidate handling

Every <=44 candidate emitted by any searcher is:

1. serialized canonically;
2. hashed before verification;
3. preserved whether accepted or rejected;
4. passed independently to both verifiers;
5. rejected on any disagreement pending investigation.

A candidate must never receive multiple adaptive verification standards.

## 5. Phase E — result gate

### `WITNESS_FOUND_AND_VERIFIED`

May be issued only if:

- candidate length <=44;
- canonical candidate bytes are frozen and hashed;
- both independent verifiers pass all 8192 inputs;
- fresh hostile review finds no unresolved Critical/High defect in the candidate-verification chain;
- an independent replay from the frozen candidate reproduces PASS;
- the exact candidate and verification evidence are durable on the remote.

Meaning:

> A new <=44 comparator upper-bound witness has been constructed and verified under this protocol.

It does **not** establish optimality.

### `SEARCH_EXHAUSTED_WITHOUT_RESOLUTION`

Use if the authorized search budget ends without a standing witness.

Meaning:

> No standing <=44 witness was found under this search. The mathematical problem remains unresolved.

It carries no lower-bound authority.

### `METHOD_NEEDS_REPAIR`

Use when the authority is coherent but verifier/search/evidence/review machinery has repairable defects.

### `AUTHORITY_REVISION_REQUIRED`

Use when the frozen problem or acceptance authority itself is defective or contradictory.

### `METHOD_NOT_VIABLE`

Use when the chosen approach cannot be made trustworthy within declared constraints.

No other final disposition may be invented.

## 6. Standing and invalidation

Apply `STANDING_PROTOCOL.md` directly.

At minimum:

- search-code changes invalidate search-performance evidence, not verifier evidence unless a declared dependency crosses that boundary;
- verifier changes invalidate candidate-verification evidence and every review/disposition depending on it;
- authority changes revoke all downstream standing under the superseded authority;
- evidence regeneration makes prior reviews stale;
- candidate bytes changing creates a different candidate;
- a final result is valid only against the exact evidence-bearing source it binds.

Compute the minimal restoration closure after every repair. Do not rerun unrelated work merely for ceremony.

## 7. Durability

Push at every durable gate:

1. authority candidate/review;
2. frozen authority;
3. verifier implementation;
4. verifier qualification;
5. verifier hostile review;
6. each material search-method generation;
7. every <=44 candidate;
8. final independent verification;
9. final disposition.

Preserve failures as failures. Never force-push, rewrite, or delete a failed research lineage.

## 8. Resource rule

Do not silently expand to effectively unbounded compute.

Before Phase D, freeze:

- wall-clock budget;
- CPU/GPU resource class;
- maximum concurrent workers;
- any paid-cloud/API ceiling;
- restart policy;
- seed policy;
- checkpoint policy.

A larger search budget is a successor search pass, not an invisible extension of this one.

## 9. What would count as a successful Governed Pass test?

The framework test and mathematics test are distinct.

Governed Pass succeeds as a framework test if it can:

- maintain exact authority and evidence standing across a nontrivial search;
- preserve failed search/review/qualification history;
- prevent search failure from becoming a false nonexistence claim;
- detect stale evidence after repairs;
- independently verify any candidate;
- stop honestly under its closed disposition grammar.

Finding a <=44 network would additionally constitute a mathematical advance.

Not finding one does not make the governance experiment a failure.
