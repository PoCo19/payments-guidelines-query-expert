# V2 validation — 3 October 2026

## Results

| Check | Result |
|---|---|
| Python regression suite | **168 tests passed**: 103 original research tests, 40 V1 workflow tests and 25 V2 tests. |
| Existing answer-rendering JavaScript tests | Passed. |
| V2 JavaScript syntax | Passed. |
| V2 browser journey | Passed in installed Microsoft Edge through Playwright, using an isolated database/server. |
| Real local model workflows | **5 of 5 completed** with Qwen3.5 9B and validated structured references. |
| Responsive viewport | No horizontal page overflow at 390 px; navigation and notifications were corrected after screenshot review. |

These are developer validation results, not a guarantee of zero defects or an independently established business-accuracy score.

## Browser flow and recovery

The test creates an existing-feature workspace, follows the missing-evidence guidance to the actual Sources screen, uploads Markdown, previews and saves text, adds a cited fact and deliberately submits an incorrect quote. The error remains inside the editor and the entered values survive correction.

It then approves the brief, queues all four example drafts atomically, records the four reviews, completes actions, records the final review and downloads the pack. It adds internal transaction-rule evidence and a structured rule, checks the rule-by-rule assessment and verifies that the prior decision reopens. It searches the real UPI collection and imports a passage with provenance.

Deletion is tested with an incorrect name and then the correct confirmation. Additional scenarios create feature-change and new-launch workspaces, follow role guidance to the reviewer selector, and trigger a concurrent-update conflict while the delete dialog is open. The error exposes a working **Reload delete confirmation** control. A reload race was found in that concurrent-delete scenario: old fields could still receive input while the new confirmation was loading. Replacing those fields with a loading state fixed it, and the complete test passed on the final run. No browser JavaScript errors occurred.

All browser data is synthetic and stored under `output/launch-v2/`. Existing user workspaces are not used as destructive test fixtures. The browser workflow uses explicitly labelled example templates for repeatability; actual Ollama generation is checked separately below.

## Real AI drafting

The existing-feature example uses synthetic source evidence and one documented transaction rule. The test removes the prepared facts, extracts them with Qwen, then exercises all four team workflows. Test-only approval/disposition records are explicitly labelled automated; they are not presented as human business approval.

| Workflow | Time observed | Result |
|---|---:|---|
| Fact extraction | 8.01 s | Completed; unresolved ownership/routing questions retained. |
| Customer Success | 15.95 s | Completed; no placeholder “no questions” item. |
| Marketing | 13.48 s | Completed; missing evidence stayed explicit. |
| Partners & BD | 14.80 s | Completed; participant context remained qualified. |
| Transaction Risk | 18.42 s | Completed; assessed the supplied rule and requested threshold/configuration evidence. |

The rule assessment identified relevant documented logic but no verified deployment evidence. It recommended review and requesting configuration evidence rather than claiming the rule was active. Narrative risk scenarios are model proposals, not established findings about a live UPI service. Times are one local run's observations, not performance guarantees.

## Important test coverage

- Existing/change/new-launch modes and backward-compatible reads of V1 records.
- Atomic batch queuing, duplicate prevention and role responsibility checks.
- Exact-name/revision deletion; deleting during a running job cannot resurrect the workspace.
- Rule-source validation, rejection of public-only active-rule evidence, mandatory deployment notes and complete rule-assessment coverage.
- Rule/source changes, source-removal effects, retained exports after a referenced rule is removed and scoped prompt inputs.
- Text/BOM, DOCX paragraphs and real PDF text extraction; explicit preview truncation; malformed, empty, oversized, unsupported and image-only files.
- Existing revision, approval, task dependency, model failure, source quotation and late-result protection tests remain passing.

## Evidence and repeatability

Reports: [Python tests](../output/launch-v2/tests.txt), [browser checks](../output/launch-v2/browser-report.json), [live AI report](../output/launch-v2/live-report.json), [live review pack](../output/launch-v2/live-review.md).

Run Python checks with `run.cmd test`. Run `evaluation/live_launch_v2.py` with the project Python for the opt-in Ollama test. `evaluation/browser_launch_v2.cjs` uses the bundled Node/Playwright runtime and installed Edge; it starts its own server on port 8767 and closes it after testing.

Screens inspected during validation:

![V2 overview and ordered workflow](../output/launch-v2/05-overview.png)

![Transaction-rule register](../output/launch-v2/06-transaction-rules.png)

![Inline citation error with preserved form fields](../output/launch-v2/02-inline-error.png)

## Remaining boundaries

No production transaction engine, actual internal NPCI rule catalog, external team systems, enterprise identity or live transaction dataset was connected. Rule status/evidence is user-reported. Source extraction and model interpretation still need human checking. There is no comprehensive semantic contradiction detector or independently reviewed accuracy benchmark. Uploads have no OCR and complex layout extraction is not guaranteed. The local role selector does not provide authenticated access control.

See [implementation](V2_IMPLEMENTATION.md) for operational constraints and [the user guide](V2_USER_GUIDE.md) for current recovery steps.
