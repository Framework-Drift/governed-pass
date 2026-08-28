Take full ownership of:

`C:\Projects\AUREA-Foundry Test`

for the next revision of the causal self-observation research program.

This is a **contract-repair + implementation-hardening + method-freeze pass**.

It is not a scientific confirmation run.

## Starting state

Current research lineage:

`research/causal-self-observation-v1`

Expected final R1 implementation-stop commit:

`166f07a2b4a33c11af237b4909ac7ac5edfa3b6d`

Original frozen program-contract SHA-256:

`da085fdcada82a590f859fa0ca5e151e2a8b31f6550d638553fd39f64f45e2cf`

Current disposition:

`PROGRAM_CONTRACT_REVISION_REQUIRED`

Verify all of this from Git and the committed repository before proceeding.

The R1 frozen contract, implementation evidence, hostile reviews, and stop disposition are immutable historical evidence. Do not rewrite or delete them.

Create a successor branch, preferably:

`research/causal-self-observation-v1-r2`

from the exact R1 stop commit.

Push it immediately and follow the permanent GitHub durability rule throughout the pass.

---

# 1. Purpose

R1 did **not** produce a negative scientific result.

It exposed:

* contradictions between human and machine contracts;
* ambiguous causal phenomenon definitions;
* an observer/evaluator capability leak;
* common-mode evaluator/normalizer risks;
* incomplete control/fingerprint methodology;
* invalid power/inference planning;
* insufficient Stage 0 instrumentation;
* weak custody/freeze authentication;
* incomplete secondary intervention/control execution.

At the same time, development work showed a potentially strong intervention signal.

That signal is **not evidence** and must not influence thresholds or weaken controls.

The purpose of R2 is:

> Repair the scientific authority, eliminate the identified measurement defects, and determine whether the causal-self-observation apparatus can become trustworthy enough for a later one-shot scientific execution.

Optimize for trustworthy falsification, not for preserving the promising development result.

---

# 2. Two hard phases

This pass has two sequential phases.

## Phase A — Program Contract v2

Repair and hostile-review the scientific contract.

Do not continue substantive implementation until the revised contract is internally coherent and explicitly approved.

## Phase B — Implementation R2

Only if Phase A receives a fresh hostile-review disposition equivalent to:

`COHERENT_TO_IMPLEMENT`

may you repair the implementation, rerun qualification, and attempt method freeze.

If Phase A fails, push the blocked revision and stop.

---

# PHASE A — PROGRAM CONTRACT V2

# 3. Preserve R1 authority exactly

Do not edit the historical R1 frozen contract files in place.

Preserve:

* original human contract;
* original machine contract;
* original hash;
* original hostile reviews;
* original implementation;
* original `CONTRACT_REVISION_REQUIRED.md`.

Create an explicit v2 contract lineage.

Prefer a structure such as:

`experiments/causal-self-observation-v1/contracts/v2/`

with a single canonical machine-readable source.

The exact structure may differ if repository conventions suggest something cleaner.

---

# 4. One canonical source of scientific authority

R1 failed partly because the human and machine contracts were independently authored.

Do not repeat that.

Create **one canonical contract representation**, preferably JSON or another deterministic canonical format already supported by the repository.

The canonical v2 source must own:

* program identity;
* revision;
* scientific question;
* claim ladder;
* intervention vocabulary;
* response-surface definitions;
* stage topology;
* estimands;
* thresholds;
* stop rules;
* custody;
* independent-unit semantics;
* baseline requirements;
* Claude roles;
* resource rules;
* disposition mapping.

Generate all human-readable contract prose and machine enums/tables from this canonical object wherever reasonably possible.

At minimum mechanically verify byte/semantic agreement between:

* canonical v2 source;
* generated human-readable contract;
* schema;
* stage definitions;
* intervention enums;
* phenomenon definitions.

A contradiction between representations must be mechanically impossible to freeze.

---

# 5. Canonical stage topology

Resolve the R1 Stage 4/5 contradiction explicitly.

Unless hostile review establishes a better topology, use:

### Stage 0 — Replay qualification

Exact replay and observer/evaluator isolation.

### Stage 1 — Main effects and hard nulls

Single-component causal recovery and false-attribution restraint.

### Stage 2 — Interaction recovery

Minimal sets and non-additive coalition structure.

### Stage 3 — Confounding, temporal controls, and identifiability restraint

Reject correlated-but-inert signals and correctly refuse unsupported causal language.

### Stage 4 — Epistemic fragility

Intervention-defined robustness/sensitivity maps.

### Method and custody freeze

Freeze method/evaluator/generator/dependency/scoring/custody identities before one-shot scientific transfer.

### Stage 5 — Sealed independent-family transfer / one-shot scientific confirmation

Fresh post-freeze bank, independent mechanisms/custodians, zero-touch result.

### Stage 6 — Predictive self-model

Only after Stage 5 establishes enough causal knowledge to justify it.

### Stage 7 — Metacognitive utility

Separate future contract required.

If hostile review recommends another topology, change it only before v2 freeze and document why.

Every representation must use the exact same topology.

---

# 6. Canonical intervention vocabulary

Use exactly one vocabulary.

Primary v1/R2 scientific game:

`COGNITIVE_ACCESS_MASK`

Canonical secondary names:

* `COGNITIVE_MODULE_DISABLE`
* `COGNITIVE_BUDGET_CHANGE`
* `COGNITIVE_QUEUE_ORDER`
* `EPISTEMIC_DELAY`
* `EPISTEMIC_SUBSTITUTION`
* `CAPABILITY_AVAILABILITY`
* `SYSTEM_POLICY_SUBSTITUTION`

However, reconsider their status.

The primary R2 scientific claim should remain centered on the cleanest intervention algebra:

`COGNITIVE_ACCESS_MASK`

Unless hostile review strongly argues otherwise, mark the seven secondary classes as:

**SECONDARY / NON-REQUIRED-FOR-V1-CONFIRMATION**

or an equivalent frozen state.

They may be:

* implemented as diagnostic seams;
* tested later under separate estimands;
* retained for future research.

They should **not block the primary causal experiment merely because all seven are not fully operational**.

Do not mix secondary intervention classes into the access-mask coalition game.

---

# 7. Formal causal phenomenon definitions

Fix the R1 `joint_necessity` ambiguity mathematically.

Do not rely on natural-language labels.

For every phenomenon, define:

* intervention universe;
* factual baseline;
* exact characteristic function or response-surface constraint;
* required outcomes for all relevant coalitions;
* allowed overlap with other causal properties;
* evaluator conformance test;
* refusal condition.

Use the convention that:

`S`

denotes the set of targets whose cognitive access is masked.

For a binary outcome predicate `Y(S)` with factual all-access baseline `Y(∅)=1`, formalize at least:

## Redundant support

For targets A and B:

`Y(∅)=1`
`Y({A})=1`
`Y({B})=1`
`Y({A,B})=0`

Either support alone is sufficient.

Both must be removed to change the predicate.

## Co-necessary pair

Replace the ambiguous term `joint_necessity` unless a clearer formal name is selected.

For A and B:

`Y(∅)=1`
`Y({A})=0`
`Y({B})=0`
`Y({A,B})=0`

Both are required in the factual mechanism; removal of either breaks the predicate.

The historical R1 `joint_necessity` label should be explicitly retired or aliased only for historical navigation.

## Synergy / interaction

Do **not** assume synergy is automatically a mutually exclusive phenomenon class.

A pure AND response surface may simultaneously exhibit:

* co-necessity;
* positive higher-order interaction.

Treat these as potentially overlapping causal properties unless the contract defines an additional mathematically distinct criterion.

Define synergy using a frozen interaction measure such as a nonzero Möbius/Harsanyi term over the named predicate.

Do not force mechanisms into one interaction label if the mathematics allows multiple true properties.

Likewise define:

* suppression;
* mediation restraint;
* association-only confounding trap;
* frequent-but-inert;
* rare-but-critical;
* temporal sensitivity;
* order invariance;
* null;
* multiple-mechanism equivalence.

Every conformance rule must be declaration-specific.

If a phenomenon is not identifiable under the frozen intervention vocabulary, the correct evaluator truth must be something like:

`NOT_IDENTIFIABLE`

rather than an invented causal label.

---

# 8. Multi-predicate truth

Preserve separate named outcome predicates.

Do not reduce an execution to one scalar outcome.

Causal effect on:

* disposition;
* reason;
* path;
* contradiction;
* capability use;
* cost;

must remain distinct where defined.

A component can be inert for disposition but causal for path or cost.

Blueprint identity and causal scoring must preserve those distinctions.

---

# 9. Contract-level hostile review

Before Phase B:

Commission:

* a fresh isolated internal hostile reviewer;
* Claude Role B using a pinned model if API is available.

Attack specifically:

* stage consistency;
* intervention-name consistency;
* response-surface definitions;
* redundant support versus co-necessity;
* synergy overlap;
* suppression;
* mediation identifiability;
* null definitions;
* multi-predicate ambiguity;
* observer/evaluator boundary;
* held-out custody;
* independent-unit hierarchy;
* inference;
* abstention;
* multiple comparisons;
* secondary-intervention scope.

Require:

**zero unresolved fatal/critical/blocking contract findings**

before v2 freezes.

Generate and hash the revised contract.

Push the contract freeze and verify remote identity.

Only then continue.

---

# PHASE B — IMPLEMENTATION R2

# 10. Process-isolated observer boundary

Fix the most serious R1 implementation flaw first.

The observer must never receive a Python callback, closure, evaluator object, mechanism object, generator object, repository object, or other introspectable capability that exposes evaluator-only data.

Implement a serialized capability boundary.

Preferred conceptual structure:

`observer process`
⇅
typed serialized request/response
⇅
`experiment broker`
⇅
`evaluator/replay process`

The observer receives only the observer-visible schema defined by the contract.

It returns only typed:

* causal hypotheses;
* experiment requests;
* predictions;
* abstentions;
* final reports.

The broker validates requests and asks the evaluator to execute them.

No Python function or closure crosses the boundary.

Sanitize the observer process environment:

* no API secrets unless that observer explicitly needs a governed API lane;
* no evaluator object references;
* no generator implementation;
* no truth tables;
* no hidden bank paths;
* no family/custodian metadata.

For the later scientific runner, prefer OS/container/process isolation strong enough that filesystem and environment access cannot trivially reveal held-out truth.

If robust isolation cannot be implemented on the local platform, design a fail-closed isolated execution package rather than pretending Python reflection restrictions are sufficient.

Create explicit hostile tests attempting:

* closure inspection;
* globals inspection;
* stack inspection;
* object traversal;
* filesystem access;
* environment access;
* imports of evaluator/generator modules;
* truth-file discovery;
* network access where prohibited.

The boundary passes only if the observer cannot recover evaluator-only information.

---

# 11. Dual evaluator hardening

Keep the dual evaluator architecture.

Increase actual independence.

Independently implement or separate:

* IR parsing;
* transition execution;
* masking;
* outcome extraction;
* minimal-set derivation;
* interaction derivation;
* normalization.

Shared neutral infrastructure should be minimal and enumerated.

Do not treat natural zero disagreement as sufficient evidence of independence.

Implement **differential fault injection**.

Inject one-sided defects into evaluator A and separately evaluator B, including:

* parser fault;
* transition fault;
* access-mask fault;
* receipt fault;
* outcome-extraction fault;
* reason/path extraction fault;
* capability-use fault;
* minimal-set fault;
* interaction-term fault;
* reachability fault;
* alpha-normalization fault;
* response-surface normalization fault.

The other evaluator must detect disagreement.

Common-mode faults that both evaluators cannot detect should be documented explicitly.

---

# 12. Exact outcome-preserving blueprint normalization

Repair R1 normalization.

Blueprint identity must preserve scientifically relevant equality structure for:

* disposition;
* exact normalized reason identity;
* exact normalized path identity;
* contradiction;
* capability topology/use;
* causal response surfaces.

Do not collapse all non-target reasons/paths to one constant if that merges distinct response surfaces.

Use alpha-normalized symbolic identities rather than cosmetic literal names where appropriate.

Preserve topology of capability relationships, not merely counts.

Both independent normalizers must generate identical canonical signatures.

Run metamorphic tests showing that:

### Must collapse

* UUID renaming;
* variable alpha-renaming;
* serialization order;
* dead/unreachable code;
* wrapper differences;
* commutative operand order;
* cosmetic token renaming.

### Must remain distinct

* different reachable control/data flow;
* different exact outcome equality structure;
* different capability topology;
* different primary response surface;
* different minimal-set structure;
* different interaction structure.

---

# 13. Phenomenon conformance repair

Rewrite generator/evaluator qualification around the v2 formal definitions.

Do not trust generator declarations.

For every generated blueprint:

1. execute full primary response surface;
2. derive evaluator truth;
3. evaluate exact phenomenon predicates;
4. accept only if it satisfies the declared construction requirements;
5. quarantine or reject mismatches.

Make conformance tests specific.

Do not reuse one invariant for:

* redundancy and co-necessity;
* frequent-inert and rare-critical;
* association trap and generic inertness.

Association-only traps must actually demonstrate observational association under the declared context distribution while remaining intervention-inert for the causal estimand.

---

# 14. Fingerprint methodology repair

R1's fingerprint audit was incomplete because it mainly attacked metadata rather than the selected observer itself.

Fix that.

For each allowed transformation, rerun:

* selected SOP;
* paired trace-only condition;
* important controls;
* relevant scorers.

Required transformations should include:

* semantic token rename;
* ID rekey;
* serialization shuffle;
* wrapper substitution;
* irrelevant-field removal;
* trace-field ablation;
* metadata stripping;
* generator/family label removal;
* custodian label removal.

Measure whether outputs change improperly.

A classifier being at chance is insufficient if the actual observer is sensitive to shortcuts.

All gates must fail closed on missing/indeterminate results.

---

# 15. Power and inference repair

Discard the invalid R1 power result as freeze authority.

Build the power simulation around the actual hierarchy.

Represent at least:

`custodian`
→ `generator family`
→ `blueprint/template`
→ dependent intervention/query measurements.

Use empirically plausible or conservatively swept:

* intraclass correlations;
* family effects;
* custodian effects;
* phenomenon strata;
* null/non-null strata.

Do not average hierarchy away.

Standardize effect-size distances.

Simulate the actual planned analysis:

* blueprint-clustered intervals;
* family/custodian sensitivity;
* leave-family-out;
* leave-custodian-out;
* phenomenon-stratified estimates;
* null-specific estimates.

Report power by frozen criterion, not only minimum aggregate power.

Select planned bank size only if there is adequate margin for:

* duplicates;
* quarantines;
* generator failures;
* evaluator disagreements.

The 399/400 FSM uniqueness result means exactly-at-capacity planning is unacceptable.

---

# 16. Stage 0 instrumentation repair

Stage 0 must measure what it claims.

Instrument directly:

* replay equality;
* uncontrolled call attempts;
* invariant violations;
* receipt mismatches;
* network attempts;
* state-hash mismatches;
* dual evaluator disagreement;
* dual normalizer disagreement;
* unexpected filesystem/observer boundary violations.

Do not initialize unmeasured counters to zero.

An exception should preserve its typed failure class rather than collapsing all failures into `replay_mismatch`.

Rerun Stage 0 against the final R2 source only.

Earlier R1 Stage 0 runs remain historical and cannot qualify R2.

Require the frozen Stage 0 threshold exactly.

---

# 17. Freeze and custody authentication

Repair the self-asserted freeze/materialization gates.

No caller should be able to pass:

`freeze_valid=True`

or provide an arbitrary freeze hash and thereby authorize bank materialization.

The bank materializer must independently verify:

* current source commit;
* current clean worktree;
* remote branch/head;
* canonical v2 contract hash;
* dependency lock;
* evaluator hashes;
* normalizer hashes;
* selected observer/policy hash;
* baseline/control hashes;
* hostile-review disposition;
* test disposition;
* freeze timestamp/identity;
* post-freeze unpredictable seed/value;
* bank nonexistence before materialization.

Use write-once bank/run identities.

A method revision after bank reveal requires a new bank identity.

---

# 18. Secondary interventions

Do not let secondary interventions derail the clean primary experiment.

If v2 marks them non-required for confirmation:

* preserve their schemas/interfaces where useful;
* implement end-to-end only where economical;
* label incomplete lanes honestly;
* do not claim them;
* do not block access-mask method freeze merely because they are deferred.

If hostile review decides one secondary class is essential to a required phenomenon, implement only that frozen requirement.

---

# 19. Controls

Complete the controls required for the **primary access-mask scientific question** as genuine equal-information/equal-budget runners.

Prioritize:

* trace frequency;
* correlation;
* logistic association;
* random intervention;
* leave-one-out;
* exhaustive singleton;
* approximate Shapley;
* exact evaluator/oracle ceilings;
* CAR-like intervention replay;
* paired SOP trace-only condition;
* paired SOP experimental condition;
* Claude Role C trace-only;
* Claude Role D experimental scientist where used.

Ensure:

* same visible state;
* same intervention budget where applicable;
* same full-universe scoring;
* no self-selected query advantage.

Secondary lanes not required by v2 need not block the method.

---

# 20. Observer development

Retain the promising R1 `hypothesis_elimination.v2` only as an exploratory starting point.

Do not preserve it by privilege.

Re-evaluate it after:

* process isolation;
* corrected normalization;
* corrected phenomena;
* corrected fingerprint tests.

Compare with serious simple strategies.

It is acceptable for R2 development performance to collapse.

Do not tune to recreate 0.973.

The primary scientific comparison remains:

**same SOP algorithm trace-only**
versus
**same SOP algorithm with intervention access**.

The experimental advantage must come from intervention information, not architecture differences.

---

# 21. Claude usage

Continue using Claude where scientifically useful.

Role B:

* hostile review.

Role C:

* trace-only causal explanation.

Role D:

* experimental scientist allowed to request bounded interventions.

Use pinned exact model identities.

Track:

* prompt hash;
* configuration;
* token usage;
* cost;
* response hash.

Never expose the API key.

Keep each lane below its frozen $100 ceiling.

Claude never determines truth.

---

# 22. Generator/custodian qualification

Re-run generator independence after all v2 changes.

Require:

* four computational families;
* required custody sources;
* evaluator-derived phenomenon conformity;
* blueprint uniqueness margin;
* family/custodian fingerprint attacks;
* actual observer transformation sensitivity tests.

Do not call separate source files independent by default.

Document execution-semantic differences.

---

# 23. Development qualification

Only after the apparatus is repaired:

Run development-only qualification sufficient to answer:

> Is there still a plausible causal observer worth freezing?

Use no final held-out bank.

Measure:

* main-effect recovery;
* false attribution;
* hard-null behavior;
* minimal sets;
* interactions;
* full-universe counterfactual prediction;
* experiment-budget efficiency;
* trace-only versus experimental uplift.

Preserve all runs.

Do not turn these into scientific confirmation.

---

# 24. Fresh hostile implementation review

After repairs, commission:

* fresh isolated internal hostile review;
* fresh Claude Role B review.

Do not reuse R1 review acceptance.

Attack every R1 finding plus:

* canonical-contract generation;
* process/RPC boundary;
* filesystem/env isolation;
* evaluator differential faults;
* outcome-preserving normalization;
* formal phenomenon conformance;
* observer-sensitive fingerprinting;
* hierarchical power simulation;
* Stage 0 instrumentation;
* freeze authentication;
* bank materialization.

Require:

**0 unresolved critical/high implementation findings**

before method freeze.

---

# 25. Method freeze R2

If and only if all gates survive:

Freeze the complete primary causal method.

Bind:

* canonical program contract v2;
* generated human contract;
* BSEM-IR;
* dual evaluators;
* normalizers;
* replay;
* access-mask intervention engine;
* observer broker/process boundary;
* selected SOP;
* trace-only counterpart;
* primary controls;
* scoring;
* inference;
* generator interfaces;
* custodian identities;
* dependency lock;
* Claude protocols/model IDs if relevant;
* power plan;
* bank materializer;
* hostile-review disposition;
* complete source/test manifest.

Create:

* governed source commit;
* machine freeze record;
* SHA-256 sidecar;
* dependency manifest;
* evaluator manifest;
* observer manifest;
* generator/custodian manifest;
* test manifest.

Push and verify remote identity.

---

# 26. Qualification bank

After R2 method freeze, you may materialize the **engineering/qualification bank** authorized by the program if needed to verify:

* evaluator agreement;
* replay;
* generator operation;
* isolation;
* bank materialization;
* independence/fingerprint controls.

Do not open or materialize the later Stage 5 scientific bank.

No causal-self-observation scientific disposition may be issued in this pass.

Any method repair after qualification-bank reveal requires a new R2 method revision and a fresh qualification bank.

---

# 27. Do not run scientific Stage 1–5 confirmation

This is critical.

You may use development worlds to diagnose whether the method is worth freezing.

You may run Stage 0 engineering qualification.

You may run a non-scientific post-freeze qualification bank if the contract authorizes it.

Do **not** perform the one-shot scientific result.

Do not issue:

* `CAUSAL_SELF_OBSERVATION_SUPPORTED`
* `EPISTEMIC_FRAGILITY_SUPPORTED`
* `PREDICTIVE_SELF_MODEL_SUPPORTED`
* `MECHANISM_ONLY`
* `ARCHIVE`

Those belong to the later scientific execution pass.

---

# 28. Resource handling

Continue CPU-first.

Use all reasonable local cores.

Instrument:

* CPU time;
* wall time;
* peak RAM;
* disk;
* Claude cost.

No cloud/GPU spending.

If implementation becomes unexpectedly expensive, optimize the deterministic engine without changing causal semantics.

---

# 29. GitHub durability

Push every major durable gate.

At minimum:

1. v2 contract draft;
2. v2 hostile-reviewed contract freeze;
3. process/evaluator hardening;
4. generator/power/Stage 0 qualification;
5. hostile-review repairs;
6. method freeze if achieved;
7. final disposition.

Verify remote HEAD after each freeze.

Never leave the only copy of important evidence locally.

---

# 30. Required disposition

Return exactly one:

## `METHOD_READY_FOR_SCIENTIFIC_EXECUTION`

Contract v2 is coherent, implementation is hardened, Stage 0 passes final source, hostile review is clear, method freeze exists, custody is mechanically enforced, and the apparatus is ready for a separately authorized scientific run.

## `METHOD_NEEDS_REPAIR`

Contract v2 is coherent but implementation still has repairable unresolved defects.

## `PROGRAM_CONTRACT_REVISION_REQUIRED`

A new scientific ambiguity or contradiction was discovered that cannot be fixed without changing frozen v2 authority.

## `METHOD_NOT_VIABLE`

The experimental apparatus cannot be made trustworthy or meaningful under the revised program.

Do not issue a scientific hypothesis result.

---

# 31. Final report

Report:

1. starting R1 stop identity;
2. new branch;
3. preserved R1 evidence;
4. canonical contract v2 design;
5. exact v2 contract hash;
6. generated human/machine consistency;
7. stage topology;
8. intervention vocabulary;
9. formal causal phenomena;
10. overlap/non-identifiability treatment;
11. contract hostile review;
12. process-isolation architecture;
13. isolation attack results;
14. dual evaluator architecture;
15. differential fault-injection results;
16. blueprint normalization;
17. generator conformance;
18. generator/custodian diversity;
19. fingerprint/observer sensitivity;
20. power/inference redesign;
21. Stage 0 final-source result;
22. controls completed;
23. observer development result;
24. trace-only versus intervention-access development uplift;
25. Claude C/D comparison if run;
26. hard-null result;
27. interaction result;
28. hostile implementation review;
29. unresolved findings;
30. method-freeze identity/hash if achieved;
31. qualification-bank identity if materialized;
32. CPU/RAM/disk usage;
33. Claude usage/cost;
34. commits;
35. remote verification;
36. worktree state;
37. exact next gate.

Work as far through both phases as reasonably possible in this single pass.

Do not stop after repairing the documents if Phase A passes and Phase B can continue.

Do not preserve the promising development score by weakening the experiment.

If the strong signal is real, it should survive a cleaner instrument.

If it disappears, that is the result we need to know.
