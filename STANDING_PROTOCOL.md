# The Standing Protocol

**Authority, evidence, and revocation for agent-produced work. Draft v0.1.**

This document captures the governance method demonstrated across three autonomous research passes (R1 stop, R2 `METHOD_NEEDS_REPAIR`, R3 verified method freeze) as a reusable, domain-neutral protocol. It describes what the working system actually enforces, not an idealization. Nothing here depends on the subject matter of the experiment that produced it.

The problem it addresses: when agents (or people) produce work over time, claims about that work go quietly stale. A test transcript certifies the commit it ran against, not the commit that exists now. A review certifies the evidence it examined, not the evidence that replaced it. Most tooling tracks what changed; almost none tracks what still *counts*. This protocol makes "counts" a computable property.

## 1. Core concept: standing

**Standing** is a derived property of an artifact: whether it currently certifies what it claims to certify. Standing is never asserted; it is computed from bindings. An artifact has standing if and only if every hash it binds to still identifies the current state of the thing bound, and every artifact it depends on itself has standing.

Standing has four values:

- `STANDING` — all bindings current, all dependencies standing.
- `STALE` — the artifact is intact but something it binds to has changed. A stale artifact is history, not authority.
- `REVOKED` — standing was removed by rule (see §4), regardless of whether bytes changed.
- `MISSING` — required by the declared workflow but absent.

The protocol's one-sentence law: **location is not authority, recency is not authority, and assertion is not authority; only current bindings are authority.**

## 2. Artifact classes

Every governed workflow declares its artifacts in these classes. The classes are fixed; the instances are domain-specific.

**Source.** The versioned state being worked on. Identified by commit hash. Source is the root of every binding chain.

**Authority (contract).** The frozen statement of what the work must satisfy: definitions, thresholds, permitted vocabularies, stop rules. Exactly one canonical machine-readable authority exists per workflow; every human-readable or derived representation is generated from it, and the generator verifies the canonical hash before generating. A contradiction between representations must be mechanically impossible to freeze. Authority changes only by explicit revision, which creates a successor authority and revokes everything downstream of the old one.

**Evidence.** Records produced by executing work under an authority: test dispositions, qualification runs, measurement records. Every evidence artifact binds, by hash, the exact source commit it describes and the authority it was produced under. Evidence about one source says nothing about another.

**Review.** An adversarial examination of evidence. Every review binds, by hash, the exact evidence set it examined (an *evidence summary*: a canonical manifest of evidence paths and hashes, itself hashed). A review of different evidence is a different review. Prior review acceptance is never reused across a repair.

**Disposition.** A terminal verdict selected from a closed vocabulary (§5). Dispositions bind the reviews and evidence they rest on.

**Freeze.** A write-once record that binds an entire method state: source, authority, component and dependency manifests, evidence, reviews, and their dispositions, into a single hashed identity. Freezes are constructed create-last (§6) and verified independently (§7).

## 3. Binding rules

1. Every binding is a cryptographic hash of exact bytes, never a path, name, timestamp, or version label.
2. Bindings point downward only: reviews bind evidence, evidence binds source and authority, freezes bind everything. Nothing binds upward or laterally by reference to "current."
3. An artifact that omits a required binding has no standing, regardless of content.
4. Evidence-writing is itself an operation that can invalidate claims. After committing evidence, the workflow must re-verify at the evidence-bearing commit, because the act of recording a truthful result can change the state the result described. (Demonstrated: a passing transcript, honestly recorded, made the suite fail at the commit carrying it.)

## 4. Revocation semantics

Standing propagates destruction downward. The transitions:

- **Source changes** → all evidence bound to the prior source becomes `STALE` for the new source. It remains valid history for its own source, forever.
- **Evidence regenerates** → all reviews bound to the prior evidence summary become `STALE`. "Reviewed" always means "reviewed *this*."
- **A review goes stale** → every gate and disposition resting on it loses standing.
- **Authority revises** → everything produced under the prior authority is `REVOKED` for the successor workflow. Repairing work cannot repair a defective authority; a contradiction inside frozen authority forces a successor authority, not a patch.
- **A freeze's source moves or any bound artifact fails re-verification** → the freeze is invalid. There is no partial freeze.

Two consequences worth stating plainly. First, requalification is always at the final source only; earlier passing runs are history and cannot qualify the current state. Second, failed artifacts are never deleted or rerun-until-green: a failure is preserved under its failing identity, because the record of the workflow is forensic and append-only. It may be superseded; it may never be rewritten.

## 5. The disposition grammar

Every gate's outcome is one of a closed, pre-enumerated set of verdicts, fixed in the authority before work begins. The demonstrated grammar has four shapes, and most workflows need exactly these:

- **READY** — all gates passed; the next phase is authorized. Never a substantive success claim beyond what the gates test.
- **NEEDS_REPAIR** — authority is sound; the work has repairable defects. The designated honest-failure outcome.
- **AUTHORITY_DEFECT** — a contradiction was found that cannot be fixed without revising frozen authority. Stops the pass.
- **NOT_VIABLE** — the approach cannot be made trustworthy under this authority. Terminal.

The point of the closed grammar: the worker cannot invent a success category, soften a finding into a new intermediate state, or conclude anything the authority did not price in advance. The grammar was exercised on its unhappy path in the demonstration (a pass ended by returning NEEDS_REPAIR against its own five days of work) and on its happy path only after two further gates.

## 6. Gates and fail-closed construction

A **gate** is a boundary that work cannot cross without a computed check passing. Requirements:

1. Gates fail closed. Missing, indeterminate, or unparseable inputs fail; nothing passes by default.
2. No self-assertion. A gate must independently verify every binding it depends on; no caller may pass a boolean, a hash, or a prior disposition as proof. (Demonstrated failure: a permissive gate accepting caller-asserted authorization survived five review rounds before adversarial review caught it.)
3. Construction is create-last. An artifact that certifies (a freeze, a signed disposition) performs all verification and reconstruction *before* creating any output, so a failure at any step leaves nothing partial in existence. The demonstration's first freeze attempt failed closed on a missing retained field and created no freeze directory at all.
4. Independent reconstruction over trust. The strongest gates re-derive what they were handed: the demonstrated freeze builder reconstructed every packaged evidence member, every retained fixture, and the evidence summary itself from raw inputs, and compared hashes, before writing anything.

## 7. Independence requirements

1. **Agreement is not independence.** Instruments derived from a common specification can agree perfectly and be wrong together, because the error lives upstream of both. Redundancy verifies implementation of the specification, never its truth. (Demonstrated: two independently coded evaluators shared one misreading; every internal consistency check passed; every dependent result was wrong.)
2. Therefore at least one check at every major gate must come from **outside the derivation chain**: a different model family, a read-only probe against ground truth, or an implementation built from the phenomenon rather than the spec.
3. Claimed diversity must be demonstrated, not labeled. Independent sources that are relabels of one source are one source. (Demonstrated and repaired: nominally independent custodians were synthetic relabels.)
4. Redundant instruments must be qualified by **differential fault injection**: inject one-sided defects into each instrument separately and require the other to detect them, and document the common-mode faults neither can detect.
5. Reviews must be **fresh and hash-bound**: performed against the current evidence summary, binding its hash, at a stated commit, with the reviewer's identity pinned. A review's freshness is mechanical, not asserted.

## 8. The record

The workflow's history is append-only and durable. Every durable gate is pushed to a remote immediately and the remote identity verified. Failed runs, failed attempts, and unavailable reviews are recorded as first-class artifacts (a review that could not be obtained is recorded as *unavailable*, hashed, never skipped silently or fabricated). Status surfaces that route readers to superseded state are defects of the same class as stale evidence and are repaired with supersession pointers, not deletion.

## 9. Minimal conformance

An implementation of this protocol must be able to answer, for a given repository and declared workflow, entirely from hashes:

1. For every declared artifact: `STANDING`, `STALE` (with the specific broken binding), `REVOKED` (with the rule that fired), or `MISSING`.
2. The minimal set of work that must be rerun, in dependency order, to restore standing.
3. Whether any gate ahead is currently passable, and if not, exactly which binding blocks it.

A conforming implementation must refuse to compute standing for a workflow whose authority fails its own hash check, and must treat that refusal as the answer.

## Provenance

This protocol is a description of enforced behavior, not a proposal. It was extracted from the repository history, review records, freeze builder, and verifier of a three-pass autonomous research program (final verified freeze `9bb658b87318eb1c71b8fa1c6a576f5cb3abecc4e6e0e4ba0b419a3565d54470` at source `d027e19a…`; public case study and initiating specification: https://github.com/Framework-Drift/governed-pass, DOI 10.5281/zenodo.22151892). Every "demonstrated" parenthetical above corresponds to a finding or repair in that record. The protocol makes no claim about the scientific hypothesis the program investigates; the governance layer is independent of it by construction.

*Draft v0.1. Terminology, conformance language, and the artifact-class taxonomy are open to revision; the binding and revocation semantics describe running code and should be treated as the stable core.*
