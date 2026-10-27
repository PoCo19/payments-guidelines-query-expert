# Workbench product verification — 25 October 2026

These records verify workflow engineering. They do not establish answer accuracy, independent graph validity or pilot acceptance.

| Evidence | Result / purpose |
|---|---|
| [Final Python log](python-tests-final.txt) | 457 tests passed in 18.462 seconds |
| [Final JavaScript log](javascript-tests-final.txt) | Four suites passed |
| [Scope comparison](scope-check.json) | Engine AST unchanged and eight core retrieval/graph/support files byte-identical to the frozen 24 October candidate |
| [Implementation hashes](implementation-files.sha256.json) | Identifies the tested runtime and new/updated test files |
| [Real walkthrough records](live-workflow-records.json) | Three saved work items; includes the model-outage attempt, successful generated drafts, source snapshots and review/visibility events |
| [Downloaded query export](query-export.md) | Actual browser-downloaded Markdown with Needs review status, citations, source extracts and snapshot |
| [Live-record preservation](live-record-preservation.json) | Normal-port startup retained two items, six versions and thirteen events |
| [Overview](overview.png) | Final running application on port 8765 |
| [Query Desk](query-desk.png), [answer/evidence layout](query-desk-evidence.png) | Isolated workflow page screenshots |

## Browser walkthroughs performed

- Query Desk: define question/product/audience, skip optional document selection, confirm scope, create, generate, reload during generation, inspect cited passage and source reader, send for review, archive and restore.
- Change Brief: block missing baseline; search real UPI Lite documents; choose OC169A as document under investigation; inspect suggestions with explicit references and numbering-family reasons; choose OC169 as baseline; block missing selection confirmation; confirm; create and generate.
- Analyst work: classify a generated finding as unresolved, add an explicitly engineering-only review note, verify unsaved export is blocked, save a new version and export.
- Research handoff: ask about OC186A in Ask & Research, save the existing answer to Query Desk, verify copied claims/citations and initial Draft status. No second model generation is used for handoff.
- Recovery: cancel trash confirmation leaves the item unchanged; confirm trash preserves versions/review status; restore returns the same Needs review version. The final in-page dialog passed after native confirmation stalled automation.
- Download: the browser produced a local Markdown file; its review status, sources, snapshot and citations were inspected.
- Final normal-port overview loaded with the original two user work items; inspected browser console had no errors. QA items were not copied into the user's work database.

## Findings retained

Ollama was initially not running. The workflow preserved source excerpts and the outage state. After starting the existing installation, Query Desk, Change Briefs and the research handoff produced drafts. All three successful responses retained `incomplete` status from the advisory reviewer. No answer was declared independently correct or approved. The initial UI mislabelled an outage message as an AI draft and enabled review too early; both controls were corrected and regression-tested.

The review/approval lifecycle is tested with synthetic evidence in unit/API tests. Real walkthroughs stop short of approval: a payments colleague's source inspection is still required.

The full suite initially encountered sandbox temporary-directory/socket restrictions. It then passed using a workspace-local temporary directory and authorized localhost access. No source/model changes were made to make the tests pass.

## Re-run

Use the project's Python environment to run `python -m unittest discover -s tests -p 'test_*.py' -q`; run each `tests/test_*.js` file with Node. On restricted Windows environments, select a writable temporary directory and allow the suite's local HTTP connections. Do not run the live-model walkthroughs in the same workflow database as user work.

See [implementation and action items](../../docs/WORKBENCH_PRODUCT_20261025.md). The frozen 24 October candidate remains separate and predates this UI increment.
