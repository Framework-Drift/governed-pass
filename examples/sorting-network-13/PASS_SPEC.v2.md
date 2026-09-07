# Governed Pass Example — 13-Channel Sorting Network — Pass Spec v2

**Workflow:** `GP-SN13-44-V1`  
**Pass class:** frontier snapshot + authority review/freeze + verifier qualification + bounded constructive search  
**Canonical authority candidate:** `authority.v2.json`  
**Authority v2 SHA-256:** `61d68a6bc759f79e8779dbf0ac42f002881719b73a8c79005cc7bec0bd4ce40a`  
**Status:** `AUTHORITY_V2_CANDIDATE_REVIEW_REQUIRED`

This specification supersedes `PASS_SPEC.md` for forward work while preserving v1 and its rejected authority review as immutable history.

## 1. Research target

Construct a fixed 13-channel sorting network with at most 44 comparators.

This pass is constructive only. It cannot prove or claim that 45 comparators are necessary, cannot derive any lower bound from search failure, and cannot issue an optimality claim.

A standing mathematical witness establishes only:

`S(13) <= candidate_length`

Novelty or priority is a separate external-context statement that requires a fresh frontier check at reporting time.

## 2. Phase A — authority review and create-last freeze

Hostile-review exact `authority.v2.json` bytes. Recompute its SHA-256 before review.

The authority bytes must never be edited to mark themselves frozen. If review accepts v2, create a separate `authority-freeze.v2.json` only after all authority checks pass. The freeze record must bind:

- exact v2 authority SHA-256;
- accepted hostile-review artifact SHA-256;
- branch and source commit containing both;
- external problem/control evidence identities used in the review;
- disposition `AUTHORITY_COHERENT_TO_IMPLEMENT`.

Any change to `authority.v2.json` after review creates a successor authority requiring fresh review.

## 3. Two distinct verifier decisions

Every verifier exposes conceptually separate results:

### `SORTS_ALL_13_BIT_INPUTS`

Tests only the mathematical sorting property over all 8192 Boolean inputs.

The known 45-comparator baseline MUST PASS this predicate.

All 45 single-comparator deletion mutants MUST FAIL this predicate.

### `ADMISSIBLE_WITNESS`

Requires:

- exact canonical candidate encoding;
- at most 44 comparators;
- valid comparator indices;
- `SORTS_ALL_13_BIT_INPUTS == PASS`;
- agreement of both frozen independent verifier decision cores on the exact candidate identity.

The 45-comparator baseline MUST FAIL `ADMISSIBLE_WITNESS` solely because its comparator count is 45.

No caller-selectable mode may bypass witness admissibility.

## 4. Candidate identity

Raw search output is preserved separately and has no witness standing.

The candidate canonicalizer parses only the frozen semantic shape and writes exact canonical UTF-8 JSON bytes under `authority.v2.json`. It may not reorder, reverse, repair, add, delete, deduplicate, or coerce comparators.

Canonical candidate identity is SHA-256 of those exact bytes.

Both verifiers bind and report that identity.

## 5. Verifier A

Direct exhaustive simulator.

- enumerate integer inputs `0..8191` exactly once;
- explicitly test the bit-to-channel mapping;
- reset all execution state between inputs;
- apply each comparator in order;
- return PASS only if every output is nondecreasing;
- on failure, retain an exact counterexample.

## 6. Verifier B

Verifier B must not be a second copy of A.

Use a structurally independent decision core, preferably a different language/runtime and one of:

- bit-parallel propagation of the complete truth table; or
- SAT/SMT search for an unsorted Boolean counterexample.

It may share fixture bytes and canonical candidate bytes, but not A's decision code, internal state representation, coverage accumulator, or verdict.

If a second standard runtime is unavailable, record that condition and compensate with stronger differential fixtures and an outside-derivation replay before any candidate receives standing.

## 7. Qualification fires-controls

Before search begins, both verifier paths must survive:

- exact 45-comparator positive sorting control;
- all 45 one-deletion negative sorting controls;
- out-of-range indices;
- equal indices;
- reversed comparator pairs;
- booleans masquerading as integers;
- numeric strings;
- floats and exponent forms;
- null/object/wrapper inputs;
- malformed comparator arity;
- >44 comparator witness inadmissibility;
- injected bit-to-channel inversion;
- injected comparator orientation reversal;
- injected missing Boolean input;
- injected duplicate-one/omit-one coverage;
- injected state carry-over;
- injected candidate mutation.

Fault injections must demonstrate that the relevant guard fails non-vacuously.

If any 44-comparator deletion mutant unexpectedly sorts, stop treating it as a fixture: freeze its exact bytes as a candidate and route it through the result gate.

## 8. Fresh hostile verifier review

After exact-source verifier qualification, perform fresh hostile review bound to:

- frozen authority identity;
- verifier source hashes;
- fixture manifest;
- qualification evidence manifest;
- exact repository source commit.

Require zero unresolved Critical/High findings before search.

## 9. Search pass

Only after verifier standing exists.

Before search, freeze:

- wall-clock budget;
- hardware/resource class;
- worker count;
- paid API/cloud ceiling;
- restart policy;
- random-seed policy;
- checkpoint policy.

Search methods may change aggressively but every generation is recorded. Search has no authority.

The 45-comparator baseline may be used only on a separately labeled diagnostic path to demonstrate that search reaches a known-good basin. Novel candidate emission remains `<=44`.

Every emitted candidate is preserved, canonicalized, hashed, and independently verified. Any verifier disagreement blocks candidate standing and triggers investigation.

## 10. Result gate

### `WITNESS_FOUND_AND_VERIFIED`

Requires:

- canonical candidate length <=44;
- both frozen verifiers PASS `SORTS_ALL_13_BIT_INPUTS` and `ADMISSIBLE_WITNESS` on exact candidate identity;
- fresh hostile candidate-verification review with zero unresolved Critical/High findings;
- independent replay from frozen candidate bytes;
- durable remote evidence.

Meaning only:

> A standing candidate demonstrates `S(13) <= candidate_length` under this authority.

A current-frontier check may separately state whether that result improves the public record at reporting time. It may not establish priority.

### `SEARCH_EXHAUSTED_WITHOUT_RESOLUTION`

The frozen search budget ended with no standing witness. No nonexistence or lower-bound conclusion follows.

### Other allowed dispositions

`METHOD_NEEDS_REPAIR`  
`AUTHORITY_REVISION_REQUIRED`  
`METHOD_NOT_VIABLE`

No other terminal vocabulary is authorized.

## 11. Standing and restoration closure

Apply `STANDING_PROTOCOL.md` dependency-wise, not ceremonially.

- authority change revokes downstream standing;
- verifier change stales verifier qualification and candidate evidence, not unrelated search history;
- search change stales only affected search-performance/provenance evidence;
- candidate byte change creates a new candidate;
- evidence regeneration stales dependent reviews;
- external frontier movement affects novelty context only, never mathematical witness validity.

After repairs, recompute and rerun only the minimal affected restoration closure plus the final whole-chain confirmation required by the result gate.

## 12. Durability

Push every durable gate. Preserve rejected authority candidates, failed qualifications, failed searches, unavailable external reviews, verifier disagreements, and rejected candidates. Never rewrite failed history.
