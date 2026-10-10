# Current project status — 10 October 2026

## 10 October 2026 - colleague handoff

Frozen NPCI + eight-RBI source archive, file hashes, portable configuration, model digest checks and evaluation records are packaged for the `handoff-2026-10-10.1` Git tag. See [the handoff guide](docs/COLLEAGUE_HANDOFF.md). Independent source/answer review remains pending.

**10 October priorities implemented:** shared answer/model budgets, stage progress, source fallback, explicit partial-answer/reviewer status; a frozen 20-case RBI–NPCI development dataset with full generated-answer capture, RAGAS pilot and human-review worksheet; and an Add documents screen covering preview, preparation, embedding/index build, activation and rollback. The real NPCI–RBI corpus and model choices are preserved. See [implementation and validation](docs/IMPLEMENTATION_20261010.md) and [the import walkthrough](docs/ADDING_DOCUMENTS_QUICKSTART.md).

The 20-case run found 18/34 source anchors, retrieved all anchors for 7/17 answerable questions, abstained on 3/3 negatives and also on 7/17 positives. Median request latency was 24.0545 seconds; maximum 65.187 seconds. These are development observations, not answer-accuracy scores. Five coverage reviews were unavailable. Cross-source reference filtering, reviewer reliability and independent review remain open priorities. The final Python regression run passed 251 tests with four optional skips; both JavaScript suites passed. No bigger model was installed and no Git push was performed.

The active local release remains `payments-rbi-core-20261009`: eight core RBI directions imported from official HTML-derived Markdown alongside NPCI. It adds 420 chunks and reuses 14,060 existing vectors. The prior integration request took 718.943 seconds; the new processing budgets and timings are documented separately and are not a controlled speedup comparison. Local source releases are Git-ignored. See [the integration record](docs/RBI_CORE_INTEGRATION_20261009.md).


Further implementation on 9 October: publisher-neutral topic research now avoids inferred product exclusion on broad questions, diversifies relevant evidence across documents, adds qualification passages, exposes an evidence map and checks for possible omissions/conflicts. Controlled retrieval comparison retained 55/55 provisional anchors and 5/6 empty negatives. Mixed-publisher fixtures and one real RBI/NPCI retrieval example pass; independent mixed-authority answer evaluation remains pending. See [the flow and limits](docs/TOPIC_RESEARCH.md).

## Mid-sem package status recorded 4 October 2026

**Payments Guidelines Query Expert** is the selected project. Initial corpus: multi-product NPCI circulars. Preliminary evaluation: UPI. The separate feature workflow is preserved and excluded from this submission.

The frontend now leads with the question flow; corpus statistics are in About, and advanced controls are collapsed. Revised outputs contain eight slides, a three-page report, editable originals and matching PDFs, plus narration, checklists and saved evidence. See [the current package](output/midsem/START_HERE.md) and [one agreed roadmap](output/midsem/CURRENT_SCOPE.md).

Fresh browser checks passed for cited answers, source inspection, export, summaries, comparisons, ambiguity, missing evidence, partial extraction, simulated model-outage recovery and mobile layout. Earlier regression and retrieval evidence remains unchanged. No corpus, model, API or storage changes were made in this presentation revision.

Team identity, registered title confirmation, contributions, timed rehearsal, recording and portal submission remain pending. Independent answer review is planned, not completed.

## Historical RAG release record

# Project status — v0.5.1

Updated 26 September 2026. The multi-product implementation is complete and **all-products-v1 is active** at http://127.0.0.1:8765.

- Imported the supplied 12 product inventories and preserved all 1,955 listing rows and 1,619 Markdown files.
- Preserved reviewed UPI text, all original 916 chunks, and newer retained circulars absent from the older inventory snapshot.
- Added canonical identity, multiple product memberships, stable selection, fiscal-year filters and ambiguity abstention.
- Kept blank pages and extraction gaps visible; excluded two known conflicts from retrieval.
- Built and activated 14,060 local Chroma vectors for 1,562 searchable documents and 4,826 page records. Register total: 1,921; availability gaps: 359.
- Added resumable embedding caching, guarded activation and a preserved v0.4 rollback path.
- Added library pagination, exact summaries/comparisons, source-quality notices and exported selection metadata.
- Updated the flow, beginner guide, architecture, operating instructions and validation documentation with screenshots.

Validation: **103 automated tests passed**, including 10 formatting checks; 1,631 source-copy hashes checked; SQLite integrity passed; both evaluated retrieval modes recovered all 55 frozen UPI anchors; product-isolation checks passed for all 12 imported groups. Seven live product examples and two negative cases were exercised. See docs/VALIDATION_V05.md for what these results do and do not demonstrate.

v0.5.1 adds contextual paragraph/list/mixed formatting, an optional Answer style control, retained inline citations, shared HTML/Markdown rendering and validated layout references. Three live formatting cases and browser rendering passed; corpus and embeddings are unchanged. See docs/ANSWER_FORMATTING.md.

Research still required: independent answer evaluation, source-PDF acquisition/repair, missing issue dates, quarantine resolution, broader participant labels and source-anchored cross-product relationships. New local-PDF root support is deferred because the supplied pack contains no PDFs. Imported inventories are dated 9–15 September, not verified against today's website.

Context/output limits remain 16,384/3,072 tokens with an 18,000-character evidence budget. More indexed documents do not mean sending the entire corpus to the model.

Run run.cmd. Share HOW_IT_WORKS.md, BEGINNER_GUIDE.md and docs/VALIDATION_V05.md. Existing PDFs describe earlier releases. Configuration/data rollback is documented in docs/MULTI_PRODUCT_IMPORT.md; code/config/UI documentation backups remain under versions/v0.4.0.

Formatting implementation closed on 26 September 2026. Rechecked saved passing test/live results, unchanged corpus fingerprint, documentation links and a fresh v0.5.1 server launch. No coding work remains for the requested paragraph/bullet/mixed formatting change. Precise response length remains a model limitation. Closure evidence: reports/v051_closure.json.
