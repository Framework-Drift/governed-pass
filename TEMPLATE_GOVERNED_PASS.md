# Governed Pass Template

A domain-neutral skeleton for delegating a multi-day autonomous engineering or research pass to an AI agent. Derived clause-for-clause from a specification that sustained a five-day single-prompt run with zero material deviation on post-hoc audit. Replace every «bracketed» element with your domain content. Delete nothing without deciding you can afford its failure mode.

---

Take full ownership of:

`«repository path»`

for «one-sentence purpose of this pass».

This is a **«pass type: e.g. contract-repair + implementation-hardening + freeze» pass**.

It is not a «the thing this pass must never become: e.g. scientific confirmation run / production deployment / release».

## Starting state

Expected current lineage: `«branch»`
Expected head or stop commit: `«full hash»`
Expected frozen authority identity: `«hash of contract/spec/config that governs this work»`
Expected current disposition: `«recorded state you believe the work is in»`

**Verify all of this from the repository before proceeding.** If reality disagrees with this section, stop and report; do not reconcile silently.

All prior evidence, reviews, and stop records are immutable history. Do not rewrite or delete them. Create a successor branch from the exact verified starting commit, push it immediately, and follow the durability rule (§ Durability) throughout.

---

# 1. Purpose

State what the prior attempt actually established, separating defects found from results suggested:

* «defect 1»
* «defect 2»
* «…»

If prior work showed a promising signal, state it and then bind it: **that signal is not evidence and must not influence thresholds or weaken controls.**

The purpose of this pass:

> «One sentence. Optimize for trustworthy falsification / verifiable correctness, not for preserving the promising result.»

---

# 2. Phases

Divide the pass into sequential phases, each ending at a gate.

## Phase A — «authority repair: contract / spec / design»

Repair and hostile-review the governing authority. Do not begin substantive Phase B work until Phase A's gate returns `«passing disposition, e.g. COHERENT_TO_IMPLEMENT»` from a fresh review.

## Phase B — «implementation»

Only after Phase A passes. If Phase A fails, push the blocked state and stop.

«Add phases as needed. Every phase boundary is non-delegable: the agent may not decide a gate passed.»

---

# 3. One canonical source of authority

If prior failures included contradictions between independently authored representations (human doc vs. machine config vs. schema), do not repeat that.

Create one canonical machine-readable source that owns: «identity, scope, definitions, thresholds, stop rules, roles, disposition mapping — enumerate for your domain».

Generate all human-readable and derived representations from it. Verify the canonical object's hash before generation.

**A contradiction between representations must be mechanically impossible to freeze.**

---

# 4. Definitions

Fix every term the prior pass found ambiguous. Do not rely on natural-language labels; define each with «the formal apparatus of your domain: exact predicates, schemas, response surfaces, acceptance tests».

If a question is unanswerable under the frozen vocabulary, the correct output is a typed refusal (`NOT_IDENTIFIABLE` / `NOT_DETERMINABLE`), never an invented label.

Retire ambiguous historical terms explicitly; alias them only for navigation.

---

# 5. Authority-level hostile review (gate for Phase A)

Commission a fresh, isolated hostile reviewer — and, if available, a second reviewer from a **different model family** with a pinned model identity. Instruct them to attack, enumerating the specific surfaces: «list your domain's attack surfaces».

Require **zero unresolved findings at «your blocking severities»** before the authority freezes.

Hash the frozen authority. Push. Verify remote identity. Only then continue.

---

# 6. Implementation requirements (Phase B)

«Your domain's hardening requirements. The following classes recur; keep the ones whose failure you cannot afford:»

**Isolation boundaries.** Any component that must not see privileged information must be denied it structurally (separate process, serialized typed interface, sanitized environment), not by convention. Write explicit hostile tests that attempt to breach the boundary; the boundary passes only if they fail.

**Redundancy with differential fault injection.** Where two instruments must agree, do not treat natural zero disagreement as evidence of independence. Inject one-sided faults into each instrument separately and require the other to detect them. **Document the common-mode faults neither can detect** — instruments derived from a common specification can agree and be wrong together.

**Verification at exact HEAD.** Every claim binds to the exact commit it describes. Evidence-writing is an operation that can invalidate the claim being evidenced: after committing evidence, re-verify at the evidence-bearing HEAD.

**Fail-closed gates.** Missing or indeterminate results fail; nothing passes by default or by caller assertion. No component may authorize itself.

**Margin.** Plan capacity with explicit margin for duplicates, failures, and quarantines. Exactly-at-capacity planning is unacceptable.

---

# 7. Qualification

Re-run qualification against the final source only. Earlier runs are historical and cannot qualify the current state. Preserve failed runs under their failing identity. Never rerun-until-green.

---

# 8. Fresh hostile implementation review (gate for Phase B)

After repairs, commission fresh isolated review (internal + cross-family where available). Do not reuse prior acceptance. Attack every prior finding plus «new surfaces this pass created».

Require **0 unresolved findings at «blocking severities»** before freeze.

---

# 9. Freeze

If and only if all gates survive: freeze the complete method/release. Bind and hash: «enumerate every identity that constitutes the frozen thing: source commit, authority hash, dependency lock, component hashes, review disposition, test disposition, manifests».

Push and verify remote identity.

---

# 10. Prohibitions

State what this pass must not do, as a list the agent cannot reinterpret:

* Do not «run the final confirmation / deploy / release».
* Do not issue: `«enumerate the forbidden conclusion labels explicitly»`.
* «Resource ceilings, cost ceilings, forbidden accesses.»

---

# Durability

Push every durable gate when it is reached, at minimum: «enumerate the gates». Verify remote HEAD after each freeze. Never leave the only copy of important evidence local.

---

# Required disposition

Return exactly one:

## `«HAPPY: e.g. READY_FOR_NEXT_PASS»`
«Its exact meaning and every condition it asserts.»

## `«REPAIRABLE: e.g. NEEDS_REPAIR»`
«Authority is sound; implementation has unresolved repairable defects.»

## `«AUTHORITY_DEFECT: e.g. REVISION_REQUIRED»`
«A contradiction was found that cannot be fixed without changing frozen authority.»

## `«TERMINAL: e.g. NOT_VIABLE»`
«The approach cannot be made trustworthy under this program.»

Do not issue any conclusion outside this vocabulary.

---

# Final report

Enumerate every item the report must contain, so completeness is checkable: «starting identity; branch; preserved evidence; authority design and hash; review outcomes; every gate result; unresolved findings; freeze identity if achieved; resource usage; commits; remote verification; worktree state; exact next gate».

Work as far through the phases as the gates permit in this single pass. Do not stop early if a gate passes and the next phase can continue.

**Do not preserve a promising result by weakening the instrument. If the result is real, it should survive a cleaner instrument. If it disappears, that is the result we need to know.**
