# Payments research workbench — action register

Updated 24 October 2026. This is the active register for Payments Query Desk and Change-Impact Briefs. Historical experiments retain their original results.

**Engineering implementation and operational checks completed; answer-quality acceptance remains open.** [Closeout and evidence](ENGINEERING_CLOSEOUT_20261024.md): 445 Python tests, four JavaScript suites, fresh pinned installation, complete cached-vector index rebuild, intake/rollback/recovery and both browser workflows. The portable archive is an engineering candidate, not a pilot-approved release.

## Completed engineering

| ID | Action | Evidence / boundary |
|---|---|---|
| E1 | Implement both supervised workflows | Local saved items, generation, source reader, edits, version history, review decisions and evidence exports. No automatic external replies or operational changes. |
| E2 | Preserve provenance and invalidate stale approval | Separate workflow database; source/corpus/model/graph snapshots; installed model digests; approval and export check freshness. One app process per workflow database. |
| E3 | Make the graph decision explicit | Maintained bounded assistance adopted with independent release review pending; automatic whole-corpus expansion not selected. Documents without graph links remain searchable. |
| E4 | Validate and package graph/source identity | Intake validates anchors and exposes degraded status. Matching development manifest and source hashes saved. This is not a release-approved package. |
| E5 | Measure maintained graph retrieval contribution | 24 October 144-case comparison: off 211/234, on 223/234; 12 gains, no losses. Graph-on matches prior results; one graph-off baseline anchor varied after rebuild. Does not measure answer correctness. |
| E6 | Classify all 11 remaining retrieval misses | Five absent from initial candidates, six lost in ranking/context selection. All quoted passages exist; no OCR changes justified by this finding. |
| E7 | Make partial answers and unavailable reviews visible | Withheld claims and advisory omissions remain visible. An unavailable review is not a passed check. |
| E8 | Prepare independent acceptance materials | Frozen provisional 50-case pack: 20 Query Desk, 10 briefs, 20 controls. All 55 graph anchors and 13 relationships included for review. Capture is blocked until the review gate is satisfied. |
| E9 | Handle internal citation labels without weakening factual checks | An exact internal document ID labelled as a document/source and attached to the claim is normalized before support checks. Original wording remains in the audit. Unknown IDs and factual numbers are not exempted. A misspelled label in the recorded failure stays rejected; its bounded repair is checked against attached evidence only. |
| E10 | Improve runtime and reviewer diagnostics | Record per-call budgets, time metadata separately, restore the previous stage after model calls, reject late completions, and distinguish timeout, invalid reviewer output and model errors. Connection-wide socket deadlines now also cover stalled headers and trickling bodies. OS suspension and total workflow scheduling remain separate limitations. |
| E11 | Prevent unrelated digits supporting monetary claims | Amount-and-unit check blocks an address digit from supporting an absent monetary limit. Three targeted regressions. Unitless tables and semantic applicability remain subject to existing checks. |
| E12 | Measure serial workflow performance | 22 attempts, no main-model failures; 10 warm observations each: Query Desk p95 26.844s, impact p95 41.046s. All 20 warm answers marked incomplete; two invalid advisory reviews. Targets met only for this small development workload. |
| E13 | Verify isolated installation and full rebuild | Fresh Python 3.12 environment, pinned dependencies, 445 tests with no skips; fresh Chroma index with 14,480 cached vectors. No live index modified. |
| E14 | Verify failure recovery and incremental intake | Actual model outage, stale graph, process interruption, synthetic one-chunk intake, activation and rollback passed. Only one embedding computed; 14,480 reused. |
| E15 | Verify browser journeys | Both workflows generated drafts, opened evidence, saved immutable edits, submitted for review and exported evidence/status. Ambiguous Tap & Pay asked for clarification; scoped revision created a new draft. No independent approval fabricated. |
| E16 | Package reproducible engineering candidate | Matching code, source/graph snapshot, available originals, cached vectors, model digests, dependency locks and evaluation records; per-file and ZIP hash verification. User workflow databases and installed Ollama weights excluded. |

## Remaining quality and independent-review gates

| ID | Status / action | Owner | Completion boundary |
|---|---|---|---|
| A1 | Targeted fixes and replay completed; material completeness still open | Engineering + payments reviewer | Review retained conditions and attribution, then fix demonstrated gaps. All 20 warm outputs remained incomplete; no general quality-pass claim. |
| A2 | Engineering runtime investigation closed | Engineering | Connection-wide timeout tests and controlled 22-attempt workload saved. Reopen on a reproducible stall; do not hide failures by increasing budgets. |
| A3 | Engineering triage complete; review 11 missing anchors | Payments reviewer, then engineering | Review queue contains exact current Markdown and stage positions. Essentiality/original verification is required before targeted ranking changes. |
| A4 | Independently review graph | Payments reviewer | Review 55 anchors and 13 relationships against originals; numbering or shared topics must not imply supersession. |
| A5 | Finalize independently reviewed 50-case pack | Payments reviewer | Verify expected outcomes, qualifications, sources and controls while preserving provisional frozen version. |
| A6 | Run reviewed paired graph answers | Engineering + payments reviewer | After A4/A5; no critical graph-induced regression. Disable graph for release if it fails. Retrieval-only ablation is already repeated. |
| A7 | Run and score reviewed 50 cases | Engineering + payments reviewer | Zero critical errors, 27/30 materially complete answers, 20/20 controls, resolvable citations and 95% supported claims are proposed gates, not achievements. |
| A8 | Development latency measurement closed | Engineering | 10 warm observations per workflow meet proposed timing targets. Repeat with accepted answers after material quality changes; current small sample is not an SLA. |
| A9 | Engineering candidate verification closed; pilot sign-off pending | Engineering + payments reviewer | Clean install/rebuild, browser, recovery and intake checks passed. Repeat affected checks after fixes; independent acceptance still prevents a release-ready claim. |
| A10 | Engineering candidate handoff closed; approved handoff pending | Engineering + payments reviewer | Portable candidate and setup/evidence are ready. A pilot-approved package requires remaining gates. No GitHub publication authorized. |

Independent review must come from a payments colleague. AI-generated expected answers, local reviewer names and successful software tests do not satisfy it.

## Reproduce the checks

See [candidate setup](../ENGINEERING_START.md) and [closeout evidence](../evaluation/engineering_20261024/README.md). The recovery runner is deliberately used only in an isolated candidate, because it tests intake activation and rollback. The latency and graph runners save timestamped raw outputs and fingerprints. The 50-case acceptance runner remains gated on independently reviewed expectations.


## Product-flow increment — 25 October 2026

Completed: distinct workbench task navigation; guided Query Desk/Change Brief setup; server-recorded research handoff; explicit baseline selection with reasoned related-source suggestions; readable drafts and citation/source inspection; analyst labels/actions/questions; version-preserving archive/trash/restore; unsaved-edit and outage controls; 457 passing Python tests and four JavaScript suites; live workflow/browser/export checks; implementation documentation and saved evidence. [Details](WORKBENCH_PRODUCT_20261025.md).

Still deferred: user-arranged independent source/graph and acceptance-case review, ensuing substantive quality fixes and final pilot acceptance. The frozen 24 October handoff was not rebuilt, and GitHub publication remains excluded.
