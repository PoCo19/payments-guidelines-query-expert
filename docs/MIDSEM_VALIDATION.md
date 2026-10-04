# Payments Guidelines Query Expert midterm validation

Revised interface and artifacts checked 4 October 2026; baseline experiment and regression run from 3 October. Scope: the original payments research application on port 8765, initially using NPCI circulars. The feature workspace is excluded from the submission and preserved separately.

## Clarity revision — 4 October

- Renamed the active frontend, deck, report, script and current documentation consistently.
- Made questions primary; moved corpus statistics to About and technical controls behind expandable settings. General notices are expandable; specific source warnings remain visible.
- Eight-slide PPTX and three-page DOCX rebuilt with matching PDFs; all slides and pages visually inspected after native PowerPoint/Word export.
- The sample presentation's Why, What, How, When, Deliverables and Feedback structure is retained. Internal submission logistics are confined to the checklist.
- Fresh [browser record](../output/midsem/evidence/browser-query-expert/report.json) includes a real model answer and mobile overflow checks. JavaScript answer-format checks passed.
- Experiment metrics remain pinned to the saved run below, not recomputed or selectively replaced.
- [Current scope](../output/midsem/CURRENT_SCOPE.md) is the common roadmap. Identity and recording remain pending.

## Earlier implementation checks

- Updated the RAG title, landing description and current documentation to payments-wide positioning with an explicit initial NPCI corpus.
- Removed the cross-functional workflow link from RAG navigation. No corpus, model configuration, storage format, public API or workspace records changed.
- Added `evaluation/midsem_check.py`: four retrieval variants on the frozen 50-case set, interleaved order, separate warm-up, timestamped results, model/config/dataset fingerprints and explicit failures.
- Added two metric tests: failed positive cases remain in recall denominators; failed negative cases cannot count as correct empty retrieval.
- Passed 103 existing RAG tests and 2 metric tests. The full 170-test suite also includes 65 separate workspace tests; those 65 are not claimed as capstone research tests.
- Existing JavaScript answer-rendering tests passed.
- Browser checks passed for a real generated answer, filtering, source reader, summary, comparison, export, ambiguity, missing evidence, partial extraction and model-error recovery. The outage response was simulated as HTTP 503 in Playwright; actual evidence-search recovery used the running server. No user Ollama service was stopped and no browser JavaScript errors occurred.

## Preliminary experiment

Recorded run: [20261003T172349Z](../output/midsem/evidence/20261003T172349Z/SUMMARY.md).

| Variant | Expected anchors found | Empty negative cases | Median engine time ms |
|---|---:|---:|---:|
| BM25 | 55/55 | 6/6 | 12.0 |
| Vector | 55/55 | 5/6 | 83.0 |
| Hybrid | 55/55 | 5/6 | 78.0 |
| Hybrid + reranker | 55/55 | 5/6 | 160.5 |

The dataset is AI-assisted and awaits independent review. There were no HTTP/runner failures. Corpus and registry fingerprints stayed unchanged. One negative question, “Explain quantum photosynthesis and chlorophyll”, received payment passages from semantic retrieval. No generation was requested in the retrieval comparison.

The 35 focused-question cases include 32 expected anchors; all four variants found them. Their median times were 13, 92, 90 and 198 ms respectively. The 8 summary and 7 comparison cases bypass reranking and together contain 23 expected anchors. Many cases name a circular directly; this set cannot establish a general quality advantage from hybrid retrieval or reranking. One warmed interleaved pass is exploratory timing, not controlled hardware benchmarking. A regression test process briefly overlapped the retrieval run, so differences should not be treated as precise performance estimates.

## Actual generation

[All six scenario responses](../output/midsem/evidence/20261003T172349Z/live.json) were retained: four generated drafts and two abstentions before generation. Direct question: 10.05 s; related evidence: 12.27 s; summary: 44.07 s; comparison: 62.90 s. Ambiguous OC 13 and unavailable OC 999 returned no generated claims. The short summary produced 13 claims; comparison produced 21. Human review remains pending, even though automated support checks retained the claims.

## Artifact verification

The sample PPTX has seven 16:9 slides covering Why, What, How, When, Deliverables and Feedback. The eight-slide adaptation retains that sequence with an extra system-flow/experiment allocation. Native PowerPoint text, flow shapes and the results table remain editable. Georgia replaces the sample's Playfair Display for consistent installed-font rendering; navy, teal and white remain. The diagram does not depend on Figma connectivity.

The presentation passed structural, slide-count, native-table, geometry and font checks. It was opened and rendered through installed PowerPoint, then all eight slide images were visually inspected. The report was rendered through installed Microsoft Word, then all four pages were checked. The packaged DOCX renderer was attempted but requires unavailable LibreOffice; native Word supplied the verified PDF instead. A visible title border and inconsistent slide title fonts were corrected during review.

Figma diagram generation is pending the user's team/organization selection in the plugin widget. No Figma diagram was claimed as generated. The local slides already contain editable preparation and question-time flow diagrams.

## Reproduce without replacing recorded evidence

With the RAG server and Ollama running, use the project Python to run `evaluation/midsem_check.py --live`. Each run creates a new UTC-stamped folder. Its warm-up requests, 200 measured retrieval requests and six live scenarios use the existing answer API. It does not rebuild indexes or change the frozen dataset. Existing source text and model names remain unchanged.

Run `run.cmd test` for the full suite. `evaluation/browser_midsem.cjs` requires bundled Node/Playwright and installed Edge; it writes its latest browser report and screenshots in the browser evidence directory. Preserve that directory before a later browser run if comparing versions.

Submission authoring uses `tools/build_midsem_content.py` with the bundled Python, `tools/build_midsem_deck.mjs` with bundled Node and `tools/render_midsem.ps1` with Word/PowerPoint. The narrative is pinned to the reviewed run rather than silently following LATEST.txt. Supply a fresh `MIDSEM_DECK_NAME` for a new deck revision because the finalizer preserves previous outputs. Update the render script's deck filename accordingly. Change team metadata before final export. Do not rerun the one-time `tools/update_midsem_docs.py` migration.

## Remaining requirements

Team ID, member names, registered title confirmation, contribution records, narration recording, timed rehearsal, link-accessibility checks and portal submission remain pending. Independent gold evaluation, a different-model judge, production observability and external user research are future work, not mid-sem achievements.

## Slide refinements

Slides 3, 4, 6 and 7 now contain a readable recorded-response demonstration, chunking/indexing details, explicit evaluation interpretations and a timed roadmap with deliverables. The report and notes match. The two additional demo responses are preserved in the current evidence package and are separate from the frozen benchmark. The friend-payment question's unfocused response is recorded as a limitation. No engine changes or new accuracy claim resulted from this work.

Rebuild artifacts with build_query_expert_content.py, build_query_expert_deck.mjs and render_query_expert.ps1; use package_query_expert.py to validate and package. The older close_query_expert_revision.py script is a historical migration and should not be rerun.
