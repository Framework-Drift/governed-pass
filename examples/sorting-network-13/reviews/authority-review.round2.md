# Hostile Authority Review — GP-SN13-44-V1 — Round 2

**Reviewer:** GPT-5.6 Sol, fresh adversarial pass over successor authority  
**Review class:** authority hostile review  
**Reviewed authority:** `examples/sorting-network-13/authority.v2.json`  
**Reviewed authority SHA-256:** `61d68a6bc759f79e8779dbf0ac42f002881719b73a8c79005cc7bec0bd4ce40a`  
**Companion operational document inspected:** `PASS_SPEC.v2.md`  
**Search performed:** no

Round 1's four HIGH findings are materially repaired in v2: sorting-property and witness-admissibility are separated; freeze is external to canonical bytes; novelty is separated from witness validity; and the intended verifier cores are structurally differentiated. Fresh review nevertheless found a new authority-layer conflict that blocks freeze.

## Findings

### GP-SN13-AUTH2-01 — HIGH — two independently authored authority surfaces exist

`authority.v2.json` declares itself canonical, but `PASS_SPEC.v2.md` contains operative requirements that are absent from the JSON, including phase ordering, create-last freeze composition, exact result-gate requirements, search-budget freeze contents, whole-chain confirmation behavior, and durability requirements.

This recreates the failure class the Governed Pass protocol explicitly exists to prevent: human prose and machine authority can drift while each appears governing.

**Required repair:** exactly one machine-readable artifact must own every rule that can authorize, block, invalidate, or dispose work. Human-readable pass prose must either be deterministically generated from that artifact or explicitly non-authoritative navigation that adds no requirement. Freeze must verify this relationship mechanically.

### GP-SN13-AUTH2-02 — HIGH — governance basis is referenced but not hash-bound

The example repeatedly invokes root `STANDING_PROTOCOL.md`, but v2 does not bind an exact Standing Protocol identity. Future edits to the root protocol could silently change the meaning of standing/invalidation for an already-running example.

**Required repair:** canonical authority must bind the exact governance basis by repository commit plus exact file SHA-256 (or equivalent immutable byte identity). A successor Governed Pass protocol requires explicit authority revision for this workflow if adopted.

### GP-SN13-AUTH2-03 — HIGH — witness predicate couples independent verifiers

`ADMISSIBLE_WITNESS` includes the requirement that both independent verifier decision cores agree PASS. If each verifier is expected to return `ADMISSIBLE_WITNESS`, it must either know the other verifier's result or the term has two meanings (local validity vs gate-level aggregation). Either outcome weakens independence.

**Required repair:** define a local verifier predicate such as `LOCAL_WITNESS_PASS` for each verifier, computed without knowledge of the other. Define a separate gate-level `WITNESS_GATE_PASS` that independently checks exact candidate identity, both local signed/hashed evidence records, authority identity, qualification standing, and agreement. No verifier may compute the aggregate gate.

### GP-SN13-AUTH2-04 — MEDIUM — bit-to-channel inversion is a vacuous differential fault for exhaustive Boolean coverage

Reversing the mapping from the 13 bits of integer `x` to channels merely permutes the complete set of all 8192 Boolean vectors. If every vector is still enumerated exactly once, the sorting verdict is unchanged. Requiring this injected fault to change the mathematical verdict is therefore impossible.

**Required repair:** replace it with faults that actually change semantics or coverage, such as comparator-channel off-by-one/remapping, omitted-input coverage, min/max reversal, comparator skip, or state carry-over. If bit-mapping is tested, test coverage identity rather than requiring a different sorting verdict.

### GP-SN13-AUTH2-05 — MEDIUM — sorted-output order should be explicit

Comparator orientation strongly implies ascending channel order, but the canonical decision predicate should state the terminal condition directly.

**Required repair:** freeze `output[0] <= output[1] <= ... <= output[12]` as the exact sorted-output predicate.

### GP-SN13-AUTH2-06 — MEDIUM — external/outside-derivation requirement lacks an exact gate artifact

The v2 prose requires an outside-derivation check before candidate standing but does not define the record that proves it occurred or what exact material it must bind.

**Required repair:** define an `outside_derivation_review` artifact class with required reviewer/tool identity, material-manifest hash, authority hash, candidate/verifier/evidence hashes when applicable, outcome vocabulary, and unavailable-state handling. Candidate standing must require a standing instance rather than prose assertion.

## Severity count

- CRITICAL: 0
- HIGH: 3
- MEDIUM: 3
- LOW: 0

## Disposition

`AUTHORITY_NEEDS_REPAIR`

Do not implement the verifier or search against v2. Preserve v1, v2, and both rejected reviews. Build a v3 canonical authority that owns the complete executable governance surface and binds the exact Standing Protocol version, then derive any human rendering from v3 rather than authoring a second source of rules.
