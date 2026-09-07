# Example: Governed Search for a 13-Channel Sorting Network

**Workflow:** `GP-SN13-44-V1`  
**Branch:** `example/sorting-network-13`  
**Status:** authority candidate created; **not frozen; no search run**  
**Started:** 2026-09-05

This is the first Governed Pass example deliberately chosen outside the AUREA / Foundry causal-self-observation research program.

## Research target

Construct and independently verify a fixed sorting network for 13 inputs using **at most 44 comparators**.

A public 45-comparator construction is known. The standard sorting-network compilation currently displays a 44–45 size interval, but the provenance of the 44 lower bound is not treated as settled authority here. This example therefore makes a one-sided construction claim only:

> A valid <=44-comparator network would improve the public best-known upper bound.

This pass is **not authorized to prove or claim nonexistence**.

## Current artifacts

- [`authority.v1.json`](authority.v1.json) — canonical authority candidate.
- [`PASS_SPEC.md`](PASS_SPEC.md) — governed pass procedure and stop rules.
- Root [`STANDING_PROTOCOL.md`](../../STANDING_PROTOCOL.md) — standing, invalidation, evidence and freeze semantics.

Canonical authority-candidate SHA-256:

`0160eb523b452a078e50fbca40649541aacb98abdfdf673b32d0bb1246026edf`

The authority is intentionally marked `DRAFT_CANDIDATE_NOT_FROZEN`.

## Baseline

The canonical authority contains the public 45-comparator, 13-input network used as the positive control.

Before any novel search output can count, the future verifier layer must independently:

1. accept that exact network on all 8192 Boolean inputs;
2. reject all 45 single-comparator deletion mutants;
3. reject malformed candidate representations;
4. survive fresh hostile review.

The deletion mutants are deliberately strong fires-controls: if any deletion unexpectedly passes, it is itself a <=44 witness and must be escalated into the governed candidate-verification path.

## Next gate

`AUTHORITY HOSTILE REVIEW`

The next pass must review the exact `authority.v1.json` bytes, including the frontier wording and the prohibition on turning search failure into a lower-bound claim.

No verifier implementation and no search should receive standing before the authority review closes and a frozen successor authority exists.

## What success means

There are two independent outcomes.

**Framework outcome:** Governed Pass maintains correct standing, invalidation, failure preservation, review freshness and closed dispositions during a real open-problem search.

**Mathematical outcome:** a <=44 comparator witness is actually found and independently verified.

The framework can succeed even if the mathematical search ends unresolved.
