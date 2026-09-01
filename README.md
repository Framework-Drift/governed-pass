# A Governed Pass: One Prompt, Five Days, and an Agent That Refused to Certify Itself

*From the author:* I built this over months of failed attempts with AI agents. Every rule in the specification below exists because its absence broke something. I loaded the prompt into an agent on a Sunday; it worked alone for four and a half days and ended by correctly refusing to certify its own work. The write-up is an independent audit by a different model — the specification is mine, verbatim. The next pass gets published whether it works or not.

**A working protocol for multi-day autonomous AI research, with the exact specification that produced it and six empirical integrity findings.**

**Status:** three passes complete. Pass 2 (R2) terminated after **4 days 8 hours 53 minutes** of continuous autonomous work in **`METHOD_NEEDS_REPAIR`**, the specification's designated honest-failure outcome. Pass 3 (R3) repaired all seven blocking findings and ended in a durable, independently verified method freeze: **`METHOD_READY_FOR_SCIENTIFIC_EXECUTION`**. The sealed scientific run remains a separately authorized future pass. Full identities, runtimes, and dispositions are in [UPDATES.md](UPDATES.md), appended regardless of direction.

**Evidence repository:** currently private. Commit hashes, artifact SHA-256s, and file paths are cited throughout so the mechanics are concrete now and independently checkable later: the evidence repository will be opened when the experiment's method freeze binds pinned model identities, closing the contamination window that early publication would create for the sealed scientific run. Publishing the hashes before the repository opens is deliberate — when it opens, readers can verify nothing was retrofitted in the interim.

---

## Summary of claims

This document makes five claims, each bound to the evidence chain described below, and deliberately makes no others.

**Claim 1 — the run.** A single specification prompt (reproduced verbatim in [ORIGINAL_PROMPT.verbatim.md](ORIGINAL_PROMPT.verbatim.md)), loaded once into a consumer-plan AI agent product with no custom orchestration framework, initiated an autonomous research-engineering pass that ran continuously for 4d 8h 53m and produced: a hash-locked pre-registered experiment contract (canonical SHA-256 `2f213238d1b9977e2380d1a9ef89cf76e66aa0da7e93b67344156f1bcb9fd35f`), a hardened implementation passing a 447-test governed suite, eleven serial repair-and-requalify source commits, and eleven rounds of adversarial review (four on the contract, seven on the implementation) — with no material deviation from the specification found in a post-hoc audit conducted by a model from a different family reading the full commit history and evidence tree. Final branch HEAD: `bb1a34a673c95451c41e4c4753f589be467493a9`, 93 commits, all pushed with remote identity verified.

**Claim 2 — agreement is not independence.** During the run, adversarial review empirically caught a class of defect that internal redundancy cannot catch: two independently coded evaluators and an observer boundary all instantiated the same specification error (a frozen cost coordinate computed from the wrong underlying field), agreed with each other perfectly, passed every internal consistency gate, and were wrong together. Only a read-only probe against ground truth from outside the shared derivation chain detected it. Stated as a portable law: **agreement between instruments derived from a common specification verifies the specification's implementation, never its truth.** Every N-version design, ensemble judge, and consensus verifier inherits this exposure wherever the versions descend from a common spec.

**Claim 3 — evidence can break its own verifiability.** Committing a truthful passing test transcript into the repository added files the governance test did not admit, so the suite the evidence honestly described no longer passed at the commit carrying the evidence. Left unrepaired, a freeze could have authenticated a suite that did not pass at its actual HEAD. The class generalizes: any pipeline that both binds claims to exact commits and commits evidence artifacts must treat evidence-writing as an operation that can invalidate the claim being evidenced, and must re-verify at the evidence-bearing HEAD.

**Claim 4 — the disposition vocabulary held at termination.** The specification permitted exactly four final dispositions, none of them a success the agent could invent. Faced with a final review it could not clear, the agent did not force a freeze or soften findings: it returned `METHOD_NEEDS_REPAIR`, bound the blocking review to its SHA-256 (`df639293d887aa0a6c6cd8484c9d130893e9c7c0b595fb831c26946a08e37e94`), left the mandated remote verifier exiting `1` with `RuntimeError: R2 method freeze is absent`, pushed, and stopped. When one cross-model review lane was unreachable at the final gate, the run recorded a hashed `unavailable` artifact and $0.00 spent rather than skipping silently or fabricating. Constrained conclusion vocabularies are usually tested only on happy paths; this one was exercised at termination, on the path it exists for.

**Claim 5 — heterogeneous adversarial review is cheap.** Cross-family hostile review for the entire pass — eight pinned-model review calls with hash-bound material manifests and structured findings — cost **$6.25** total. The "adversarial review is too expensive" objection does not survive contact with the receipt.

## The problem this addresses

The field has converged on a diagnosis: autonomous research agents produce work faster than anyone verifies it. Surveys of the area describe a verification gap in which the dominant quality signal remains fluency-based judging. Documented failure modes include p-hacking by autonomous AI scientists, correlated errors escaping same-family generator/validator pairs, and quiet drift over long horizons — agents that look excellent in demos and degrade subtly when allowed to run. The proposed fixes (pre-registration, adversarial review, evidence discipline) exist largely as position papers arguing that someone should build the thing. This repository documents a built instance, run at a multi-day horizon, with its audit trail intact and its initiating specification included so the protocol can be lifted rather than reconstructed.

## The protocol

Seven mechanisms carry the load. None is individually novel; the working, machine-enforced combination is the contribution.

**One canonical source of authority, hash-locked.** The experiment contract exists as a single canonical machine-readable object. Every human-readable document, schema, and enum table is generated from it, and the generator's first act is to verify the canonical object's hash against the reviewed lock — a mutated contract fails to generate anything. Deviation is not *detectable*; it is *unexecutable*. The design rule from the specification, verbatim: *a contradiction between representations must be mechanically impossible to freeze.*

**Phase gates with fail-stop semantics.** Sequential phases, each terminated by a gate with an explicit disposition. Phase B work may not begin until Phase A's gate passes fresh review; a failed gate is pushed and stopped on, not argued with. Judgment inside a phase is delegated broadly; crossing between phases is not delegated at all.

**A closed disposition vocabulary.** The agent's final report must be exactly one of four pre-enumerated states, none of which is a scientific claim. The agent cannot conclude anything the specification did not authorize — converting "the agent decided how it did" into "the agent selected from outcomes priced in advance."

**Isolated, heterogeneous hostile review.** Review is a distinct role with read-only access, run fresh at each gate, instructed to attack, and staffed heterogeneously: an isolated internal reviewer plus a second reviewer from a different model family with a pinned identity, hash-bound material manifests, temperature 0, and structured findings. Prior acceptance is never reused across a repair. (Claim 2 is what this catches that nothing else does.)

**Serial repair-and-requalify cycles with commit-bound evidence.** Every qualification artifact is bound to the exact source commit it describes, hashed, and committed. A repair invalidates prior qualification for changed surfaces; evidence is regenerated at the new source, never carried forward. In this pass: eleven named source commits in five days, each a diagnose–repair–requalify cycle, forming a chain in which any claim can be checked against the tree state it was made about.

**Failure preservation.** Failed qualification runs are archived under their failing source identity, not rerun-until-green. An unavailable review round is recorded as a hashed `unavailable` artifact. The record is forensic: superseded, never rewritten. This property is what makes post-hoc audit possible at all.

**A durability rule.** Every durable gate is pushed immediately and remote HEAD identity verified after each freeze. No important evidence exists only locally at any point.

## Case study

The specification took ownership of a repository whose previous attempt (R1) ended in a recorded stop: independent review had found the frozen human and machine experiment contracts in contradiction — unrepairable without new contract authority. R2's task: repair the scientific authority, harden the implementation, and attempt a method freeze, under the explicit instruction to optimize for trustworthy falsification and treat the prior attempt's promising development signal as motivation to *tighten* the instrument.

| Day | Activity |
|---|---|
| 0 | Starting state verified from Git; successor branch created from the exact prior stop commit `166f07a2b4a33c11af237b4909ac7ac5edfa3b6d`; pushed |
| 0–1 | Phase A: canonical contract v2 authored and generated; four hostile-review rounds (internal + cross-family, pinned model); converged to zero findings at all severities; hash-locked and frozen |
| 1–3 | Phase B: process-isolated observer boundary (12/12 hostile isolation attacks defeated), dual-evaluator hardening with 24/24 differential fault injections detected, normalization repair, hierarchical power planning; serial source commits with per-source qualification evidence; failures archived as failures |
| 3–4 | Implementation review rounds 6–7, surfacing the findings below; final-source Stage 0 engineering qualification passed (replay equality 1.0, 1,000 unique execution identities; record SHA-256 `59b45fbeff2eedae75cb03f3a30545eb7ccaf82ceb153b6e667881052319e8d6`) |
| 4+ | Round-7 review blocks freeze (3 HIGH / 4 MEDIUM); agent returns `METHOD_NEEDS_REPAIR`, binds all identities, leaves the freeze verifier failing loudly, pushes final HEAD `bb1a34a6…`, stops |

## The six findings — an empirical defect taxonomy for agentic pipelines

Each was caught in a real codebase by the protocol's own machinery, and each generalizes past the domain.

1. **Shared-specification errors defeat dual verification** (Claim 2). Redundant instruments descended from one spec agree when the spec's reading is wrong. Detection requires a probe from outside the derivation chain.
2. **Evidence commits can invalidate verification at the HEAD they document** (Claim 3). Re-verify after evidence-writing, at the evidence-bearing commit.
3. **A permissive gate survives until someone attacks it.** The freeze builder would have authorized freezing while a required downstream apparatus (sealed-transfer scoring, materialization, orchestration) was incomplete — self-asserted authorization that survived five review rounds before the sixth-and-seventh caught it. Gates must independently verify every binding; caller-asserted authority is prohibited.
4. **Nominal independence is not independence.** "Independent" custody sources turned out to be synthetic relabels of one source — diversity by labeling, not by construction. Any pipeline claiming ensemble/source diversity should have to demonstrate it mechanically.
5. **Review freshness must be cryptographically bound.** Reviews not bound to the exact evidence hashes they examined allow "reviewed" to drift from "reviewed *this*." Bind review records to material manifests by SHA-256 (the cross-family review lane here did exactly that; the internal lane's gap was itself flagged and is queued for repair).
6. **Status surfaces drift from ground truth.** The repository's operator-facing status still routed readers to the superseded attempt while the successor was mid-execution — flagged independently by both the external audit and the internal reviewer. Status surfaces need supersession pointers as a mechanical rule.

## Using this

Take [TEMPLATE_GOVERNED_PASS.md](TEMPLATE_GOVERNED_PASS.md) — the specification's skeleton with domain content bracketed — and keep the structure: verification-first entry, immutable history, canonical hash-locked authority, phase gates, closed dispositions, heterogeneous hostile review, commit-bound evidence, failure preservation, durability. Replace the domain content. Expect your first pass to surface which clauses your domain is missing; record those failures, and your second specification will be the one that holds.

The method's governance semantics are also captured as a standalone, domain-neutral specification in [STANDING_PROTOCOL.md](STANDING_PROTOCOL.md): artifact classes, hash-binding rules, revocation semantics, the closed disposition grammar, gate construction, independence requirements, and a minimal conformance checklist for implementations.

A candid note on provenance: the initiating specification was not designed in one sitting. Nearly every clause distills a specific recorded failure from months of prior human–agent engineering under a similar governance regime. The template transfers the *classes* of those lessons cheaply; knowing which clauses your domain needs, and at what strictness, remains judgment the template cannot supply.

## What we are not claiming

One instance cannot rule out survivorship — parallel multi-day runs that quietly failed under similar specifications would not be published, and parallel successes inside labs would not be public. The defensible claim is *working and undocumented in public*, not unprecedented. Duration alone is claimed to be nothing: agent processes that run for days are commonplace; the claimed conjunction is single-prompt initiation, no mid-run human steering outside pre-authorized gates, and integrity that an adversarial post-hoc audit could not fault — with the protocol, not the model, as the hypothesized cause, a hypothesis exactly one instance deep. And no scientific result is claimed or implied: the underlying experiment's development-phase numbers are deliberately absent because they carry no scientific authority under the experiment's own contract, and reporting them here would be the precise overclaim the protocol exists to prevent. The sealed scientific phase has not run. When it runs, its disposition will be reported regardless of direction; a rigorous negative is a first-class outcome of this protocol, not a failure of it.

## Updates

Subsequent passes append to [UPDATES.md](UPDATES.md): disposition, runtime, findings, and the evidence identities to check them against — regardless of how they turn out. Star or watch the repository if you want the next result; there will be no announcement machinery beyond this file.

---

*Prepared from a post-hoc audit of the full repository history, review records, and qualification evidence by a model from a different family than the one that executed the run. The initiating prompt is reproduced unmodified in [ORIGINAL_PROMPT.verbatim.md](ORIGINAL_PROMPT.verbatim.md). Documentation licensed under CC BY 4.0 — see [LICENSE.md](LICENSE.md).*


## Stack

The prompt was written with ChatGPT Classic 5.6 Sol (extra high reasoning). The run itself was ChatGPT work 5.6 Sol (extra high) on the $100 pro plan, with no custom harness. The cross-model hostile reviews were Claude (claude-opus-4-6, pinned identity) over the Anthropic API. The post-hoc audit was also Claude.
