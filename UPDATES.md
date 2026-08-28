# Updates

Append-only record of pass dispositions, runtimes, and evidence identities. Newest first. Entries are added regardless of outcome; a rigorous negative is a first-class result.

## 2026-08-28 — Pass 2 (R2): `METHOD_NEEDS_REPAIR`

- Runtime: 4d 8h 53m 36s continuous, single initiating prompt, no mid-run human steering outside pre-authorized gates
- Branch: `research/causal-self-observation-v1-r2`, final HEAD `bb1a34a673c95451c41e4c4753f589be467493a9`, 93 commits, remote identity verified
- Canonical contract v2 SHA-256: `2f213238d1b9977e2380d1a9ef89cf76e66aa0da7e93b67344156f1bcb9fd35f` (four review rounds to zero findings at all severities)
- Governed suite at final source: 447 passed / 0 failed
- Final-source Stage 0 engineering qualification: passed; record SHA-256 `59b45fbeff2eedae75cb03f3a30545eb7ccaf82ceb153b6e667881052319e8d6`
- Blocking review: round 7, `BLOCK_METHOD_FREEZE`, 3 HIGH / 4 MEDIUM; SHA-256 `df639293d887aa0a6c6cd8484c9d130893e9c7c0b595fb831c26946a08e37e94`
- Terminal behavior: designated unhappy disposition returned; freeze verifier left exiting `1` (`R2 method freeze is absent`); unavailable cross-family review lane recorded as a hashed `unavailable` artifact with $0.00 spent
- Cross-family hostile-review cost for the whole pass: $6.25 (eight pinned-model calls, hash-bound manifests)
- No scientific execution; no scientific disposition exists

## Planned — Pass 3 (R3)

Repair the seven round-7 findings (3 HIGH / 4 MEDIUM), regenerate all affected source-bound evidence, obtain fresh hostile reviews at zero unresolved critical/high, then attempt method freeze. Disposition and runtime will be recorded here when the pass terminates.

## Later — sealed scientific execution

Separately authorized after method freeze. Its disposition — supported, refused, or archived — will be recorded here either way.
