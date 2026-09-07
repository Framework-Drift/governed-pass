# Authority Hostile Review Request — GP-SN13-44-V1

**Review class:** fresh authority review  
**Workflow:** `GP-SN13-44-V1`  
**Artifact under review:** `examples/sorting-network-13/authority.v1.json`  
**Expected SHA-256:** `0160eb523b452a078e50fbca40649541aacb98abdfdf673b32d0bb1246026edf`  
**Authority status entering review:** `DRAFT_CANDIDATE_NOT_FROZEN`

Do not review from this summary alone. Recompute the SHA-256 of the exact authority bytes and read the complete canonical artifact plus `PASS_SPEC.md` and the root `STANDING_PROTOCOL.md`.

This is an adversarial review. Do not improve the proposal silently. Identify contradictions, underspecification, authority leakage, false-positive paths, false-negative paths, and ways the search machinery could manufacture apparent success.

## Required attacks

At minimum determine:

1. whether the comparator semantics are complete and unambiguous;
2. whether zero-based channel indexing is closed and enforced;
3. whether the candidate encoding admits alternate interpretations;
4. whether the zero-one principle supports the frozen positive-witness acceptance rule;
5. whether exactly all 8192 Boolean inputs must be checked;
6. whether a stateful or input-dependent object could masquerade as a fixed network;
7. whether comparator count and depth are accidentally conflated;
8. whether the public-frontier wording overclaims the disputed 44 lower bound;
9. whether any allowed disposition could be misread as proving 45 necessary;
10. whether search exhaustion, SAT timeout, heuristic failure, or LLM judgment can leak into nonexistence standing;
11. whether either verifier can self-authorize or accept caller-provided proof of verification;
12. whether the two-verifier independence requirement is strong enough to expose common-mode implementation errors;
13. whether the 45-comparator baseline and all 45 deletion mutants are adequate fires-controls;
14. whether a candidate that passes a deletion-mutant control is correctly escalated rather than normalized away;
15. whether promising candidates can influence later verifier rules, budgets, or review thresholds;
16. whether the disposition grammar is closed enough for a failed search;
17. whether standing/invalidation dependencies are sufficiently separated between authority, verifier, search, candidate, review, and final result;
18. whether any missing dependency would allow stale evidence to retain standing.

## Severity

Use:

- `CRITICAL` — permits false mathematical standing, unauthorized optimality/nonexistence claim, or invalid authority freeze.
- `HIGH` — can materially invalidate the positive-witness verification or independence architecture.
- `MEDIUM` — important weakness that does not currently permit a false standing result.
- `LOW` — clarity, maintainability, or nonblocking hardening.

## Required output

Return a structured review containing:

- reviewer/model identity;
- exact reviewed authority SHA-256;
- exact reviewed source/commit if available;
- findings with stable IDs, severity, exploit/failure path, and required repair;
- explicit common-mode risks the proposed verifier pair still cannot detect;
- unresolved counts by severity;
- exactly one disposition:

`AUTHORITY_COHERENT_TO_IMPLEMENT`

or

`AUTHORITY_NEEDS_REPAIR`

or

`AUTHORITY_REVISION_REQUIRED`

`AUTHORITY_COHERENT_TO_IMPLEMENT` requires zero unresolved `CRITICAL` and zero unresolved `HIGH` findings.

Do not perform the search. Do not design a 44-comparator candidate. Do not treat review agreement as mathematical evidence.
