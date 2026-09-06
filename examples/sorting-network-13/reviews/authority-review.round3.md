# Hostile Authority Review — GP-SN13-44-V1 — Round 3

**Reviewer:** GPT-5.6 Sol, fresh adversarial pass over canonical v3  
**Review class:** authority hostile review  
**Reviewed authority:** `examples/sorting-network-13/authority.v3.json`  
**Reviewed authority SHA-256:** `7f40a2ed6ab936e9f6c27625cc527a87e3313e866d947e79b10e71aede41b6e8`  
**Reviewed source HEAD entering review:** `acd10f84aa0608fb530ada0684342c8902f432bf`  
**Governance basis:** `STANDING_PROTOCOL.md` at base commit `b8c5b39c9d8dde990e7b59224a610b602ee9c082`, Git blob `b04c2392788f8a27cfbc7e8808f43069217b389b`  
**Frontier evidence:** `frontier-evidence.v1.json`, SHA-256 `51826968401a5ecdfead62430e912f207da04f0b5f29afaf63439d659d95bc31`  
**Search performed:** no

## Round-2 closure

- Dual-authority surface: **CLOSED.** v3 states that the JSON object is the sole operative authority. Prior `PASS_SPEC*.md` files are historical/navigation only for forward work.
- Governance-basis drift: **CLOSED.** v3 binds the exact base commit and Standing Protocol Git blob identity.
- Verifier coupling: **CLOSED.** each verifier computes local predicates without seeing the other; a separate aggregate gate reconstructs both.
- Vacuous bit-mapping fault: **CLOSED.** removed; fault set now targets semantic/coverage defects.
- Sorted-output ambiguity: **CLOSED.** explicit `output[0] <= ... <= output[12]` predicate.
- Outside-derivation evidence: **CLOSED AT AUTHORITY LEVEL / DEFERRED BY DESIGN AT CANDIDATE LEVEL.** External frontier/control evidence and a fresh exhaustive control probe are frozen for Phase A; v3 additionally defines the standing outside-derivation artifact required before candidate standing.

## Fresh attacks

### 1. False positive from 45-comparator control

PASS. The control may pass `LOCAL_SORT_PASS` but is required to fail local witness eligibility because length 45 exceeds the target. No caller mode can convert the control into a witness.

### 2. Search failure laundering into nonexistence

PASS. Nonexistence is explicitly outside scope; timeout, UNKNOWN, exhaustion, and no-candidate states cannot create lower-bound standing.

### 3. Same-family verifier consensus laundering

PASS at authority level. v3 requires structurally different decision cores, exact-source qualification, differential faults, fresh hostile verifier review, an outside-derivation PASS artifact, and independent replay before aggregate witness standing. Agreement alone is insufficient.

### 4. Candidate identity ambiguity

PASS. Canonical witness bytes, lexical restrictions, exact newline, no coercion, preserved raw search provenance, and SHA-256 candidate identity are frozen.

### 5. Verifier self-authorization / caller authority

PASS. Local verifiers cannot compute aggregate standing and the aggregate gate must reconstruct artifacts rather than accept caller booleans, hashes, modes, or prior verdicts.

### 6. Frontier/priority overclaim

PASS. Mathematical validity is explicitly independent of frontier novelty. A valid witness establishes only `S(13) <= candidate_length`; priority/novelty is prohibited absent a separate current frontier statement and is never implied by the disposition.

### 7. Authority representation drift

PASS. v3 is sole operative authority. Any human rendering is non-authoritative and must be derived from v3; canonical-byte mutation requires successor review.

### 8. Standing restoration overreach

PASS. v3 defines dependency-specific invalidation and requires minimal restoration closure rather than ceremonial whole-project reruns.

## Remaining findings

### GP-SN13-AUTH3-01 — MEDIUM — governance basis uses Git SHA-1 object identity

The bound Standing Protocol identity is an exact Git blob object plus an exact base commit, which is mechanically strong for ordinary repository integrity but uses Git SHA-1 rather than an explicit SHA-256 of the file bytes.

**Disposition:** accepted as nonblocking for this example because the immutable Git object and base commit jointly identify the exact governance bytes. Before a high-adversary deployment of Governed Pass, prefer a stronger content hash in addition to Git object identity.

### GP-SN13-AUTH3-02 — MEDIUM — conditional final-disposition bindings are declarative rather than a formal schema language

The `final_disposition.required_bindings` list uses human-readable conditional phrases such as `candidate_sha256 if witness exists`. An implementation must not interpret these loosely.

**Required implementation constraint:** the gate implementation must encode separate closed schemas for witness and exhaustion dispositions and tests must prove missing witness bindings fail closed. No authority revision is needed unless this cannot be done without changing semantics.

### GP-SN13-AUTH3-03 — LOW — cross-language availability is intentionally deferred to qualification

Whether a second standard runtime exists is not frozen yet. v3 correctly requires that availability/unavailability become evidence during verifier qualification. This is not an authority defect.

## Common-mode risks that remain explicit

- Both verifier families ultimately rely on the zero-one principle and comparator-network mathematics frozen in the authority.
- A host/runtime defect could affect multiple implementations unless the outside-derivation replay uses a genuinely separate environment or toolchain.
- A verified witness says nothing about priority or independent discovery.

## Severity count

- CRITICAL: 0
- HIGH: 0
- MEDIUM: 2
- LOW: 1

## Disposition

`AUTHORITY_COHERENT_TO_IMPLEMENT`

Phase A may proceed to create-last authority freeze bound to the exact v3 authority, this accepted review, the frozen frontier evidence, and the exact Standing Protocol governance identity. Verifier/search implementation remains prohibited until that freeze exists and authenticates.
