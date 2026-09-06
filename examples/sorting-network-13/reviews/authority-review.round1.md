# Hostile Authority Review — GP-SN13-44-V1 — Round 1

**Reviewer:** GPT-5.6 Sol, fresh adversarial pass  
**Review class:** authority hostile review  
**Reviewed authority:** `examples/sorting-network-13/authority.v1.json`  
**Reviewed authority SHA-256:** `0160eb523b452a078e50fbca40649541aacb98abdfdf673b32d0bb1246026edf`  
**Reviewed branch:** `example/sorting-network-13`  
**Reviewed source HEAD entering review:** `5e334231e7448f4b436d8539ced67874e4106ebb`  
**Scientific/mathematical search performed:** no

The authority bytes were independently SHA-256 checked. The embedded 45-comparator control was separately replayed against all 8192 Boolean inputs and sorts correctly. All 45 single-comparator deletion mutants were separately replayed and each fails on at least one Boolean input. These checks are review probes only; they are not verifier qualification evidence.

## Findings

### GP-SN13-AUTH-01 — HIGH — baseline acceptance contradicts candidate admissibility

The authority requires every verifier to enforce the target comparator bound `<=44` while also requiring both verifiers to "accept" the exact 45-comparator baseline. Those requirements cannot both mean the same verifier decision.

**Failure path:** an implementation must either weaken the target-bound check to admit 45, or reject the positive control and fail qualification. A caller-selectable `qualification_mode` would create an authority-bypass surface unless its semantics are frozen.

**Required repair:** split the decision into two independent predicates:

1. `SORTS_ALL_13_BIT_INPUTS` — mathematical sorting property, applicable to the 45-comparator control and candidates;
2. `ADMISSIBLE_WITNESS` — requires the sorting property plus canonical structure and comparator count `<=44`.

The 45 baseline must PASS the first predicate and FAIL witness admissibility solely because its count is 45. Each 44-comparator deletion mutant must FAIL the sorting predicate.

### GP-SN13-AUTH-02 — HIGH — reviewed authority can be mutated to mark itself frozen

`PASS_SPEC.md` permits changing canonical `authority_status` to a frozen state after review. Any byte change produces a new authority hash, so the accepted review would no longer bind the authority being frozen.

**Failure path:** review `authority.v1.json`, alter only its status field, then freeze the altered bytes while citing the earlier review.

**Required repair:** the reviewed canonical authority bytes are immutable. Freeze must be a separate create-last record binding the exact reviewed authority SHA-256 and accepted review SHA-256. If canonical authority bytes change for any reason, that is a successor authority requiring fresh review.

### GP-SN13-AUTH-03 — HIGH — novelty claim can go stale during the run

`WITNESS_FOUND_AND_VERIFIED` currently states that a valid <=44 witness "establishes an improved upper bound." The frontier snapshot is frozen at pass start, but another party could publish a <=44 network before this pass terminates.

**Failure path:** our candidate is mathematically valid, but the final disposition overclaims novelty/priority because the external frontier moved after the frozen snapshot.

**Required repair:** separate mathematical validity from frontier novelty. `WITNESS_FOUND_AND_VERIFIED` may establish only existence of the frozen witness and hence `S(13) <= candidate_length`. A distinct final frontier-freshness check may state whether the witness improves the best public upper bound at reporting time. No priority claim is authorized by this protocol.

### GP-SN13-AUTH-04 — HIGH — verifier independence is under-specified

"Separately implemented" plus "no code reuse" does not prevent both verifiers from instantiating the same indexing, enumeration, or comparator-semantics error from the common specification. The Standing Protocol explicitly rejects agreement as independence.

**Failure path:** A and B are line-by-line-independent implementations of the same mistaken interpretation and agree on every candidate and control.

**Required repair:** freeze structurally different decision cores. Recommended minimum:

- Verifier A: direct per-input exhaustive simulator over exactly the set `{0,...,8191}`;
- Verifier B: bit-parallel/vector truth-set propagation or SAT/SMT counterexample search, independently implemented and not calling A;
- require differential fixtures targeted at indexing, comparator orientation, incomplete input coverage, state carry-over, and parser-type confusion;
- require one major review/check outside the implementation derivation chain before candidate standing.

Cross-language implementation should become mandatory when the environment provides a second standard runtime; otherwise the deviation must be recorded and compensated by stronger independent derivation and review.

### GP-SN13-AUTH-05 — MEDIUM — candidate canonical bytes are not fully specified

The authority says candidate representation is an ordered JSON array and that candidates are serialized canonically, but does not define exact canonical bytes.

**Failure path:** semantically identical candidates acquire different identities through whitespace, newline, numeric or parser representation differences; review/evidence bindings can drift between raw and normalized forms.

**Required repair:** define one exact candidate byte encoding (UTF-8, no BOM, JSON integers only, compact separators, no insignificant whitespace, exact trailing-newline rule). Preserve raw search output separately; verification binds only the canonical candidate bytes.

### GP-SN13-AUTH-06 — MEDIUM — JSON type semantics need explicit closure

The comparator definition says integer indices, but common language runtimes can treat booleans as integers (`true == 1` in some type systems) or coerce numeric strings/floats.

**Required repair:** canonical parser must accept only JSON number tokens denoting mathematical integers in `0..12`; reject booleans, strings, floats/exponents, nulls, objects, extra fields, and all non-array comparator shapes. No coercion.

### GP-SN13-AUTH-07 — MEDIUM — public-frontier facts are not themselves standing dependencies

The mathematical witness check does not require the disputed lower bound, but the authority still carries frontier prose and URLs without an explicit distinction between frozen navigation/context and result-bearing evidence.

**Required repair:** mark frontier snapshot inputs as contextual external evidence. Bind the exact retrieved evidence or record immutable content hashes where practical, and require a separate current-frontier check only for a novelty statement. Mathematical witness validity must not depend on a live web page.

## Common-mode risks remaining even after required repair

- Both verifiers still rely on the zero-one principle and the same mathematical definition of comparator networks. A defect in the frozen authority's mathematical premise is upstream of both.
- Both may share host/runtime defects if executed on one machine.
- The embedded 45-comparator control validates a known-good region but cannot prove every possible implementation bug absent.
- A valid witness can be independently verified without establishing who discovered it first or whether an equivalent witness was already privately known.

## Severity count

- CRITICAL: 0
- HIGH: 4
- MEDIUM: 3
- LOW: 0

## Disposition

`AUTHORITY_NEEDS_REPAIR`

The problem target itself remains coherent. Preserve `authority.v1.json` and this review unchanged. Create a successor authority candidate incorporating the repairs, then obtain a fresh hostile review against the successor hash before verifier implementation begins.
