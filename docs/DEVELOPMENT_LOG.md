# 20 October 2026 — Evidence recovery and repair quality cycle

Protected at most two topic-matched notification-phase candidates already present in retrieval, allowing bounded same-document phase context to survive reranking. Preserved requested-phase evidence within the repair model's existing six-excerpt cap; added excerpt-input audit and source-specific attribution correction. Citation/numeric/scope checks remain intact. No corpus, embedding, configuration or model changes.

The 144-case paired development comparison recovered 223/234 anchors versus 220/234, three gains and no losses. Coverage-review and generation-prompt experiments failed promotion and remain outside the application. Final live captures preserve the first run's six generation timeouts and the post-contention repeat with 19/19 anchors and no generation fallback. Four coverage reviews remained unavailable; eligibility, attribution and completeness issues persist. The completed ten-case frozen reviewer comparison rejected the candidate: it missed four of five provisionally labelled gaps. Final checks: 399 Python tests and all three JavaScript suites passed. See [the cycle report](QUALITY_CYCLE_20261019.md) for exact test records, experiment outcomes and current follow-up priorities. Final release verification and publication remain deferred.

# 18 October 2026 — Corpus graph candidate and answer fixes

Implemented separately stored numbering families, explicit document references and topic mentions, including cross-family links and general documents with no feature assignment. Built a candidate over 4,832 eligible pages: 334 resolved reference occurrences / 234 unique document pairs, with unresolved and incomplete references preserved. Integrated graph preparation and unchanged-page reuse into staged document intake; active corpus/configuration unchanged.

Added category ownership checks for collective claims, safe navigation-label normalization and exact repaired-answer deduplication with retained primary-claim coverage. Removed an ineffective extra per-document model-checking experiment. The 16-claim challenge now matches all AI-assisted labels. Four live answers retain expected evidence but expose remaining incomplete-answer and coverage-review issues. Fixed a demonstrated Windows HTTP rejection-response reset. Final full regression: 390 tests passed.

The initial 138-case candidate comparison found one gain and one loss, no aggregate improvement. Changed candidate insertion to use only remaining context after existing evidence. Ten additional cases and seven targeted replays showed no losses but no new gain; the broader candidate remains disabled. Maintained pilot graph stays enabled. Final release verification and GitHub publishing remain deferred. See [full evidence, limitations and reproduction](GRAPH_EXPANSION_20261018.md).

# 18 October 2026 — Bounded readiness improvements

Added category-matched table preservation and same-document notification-phase context, preserving filters and the 18,000-character budget. Added selected-excerpt scope checks, collective citation ownership and per-claim failure diagnostics. Corrected false rejection of combined per-payment/cumulative-limit statements. Final Python regression: 375 passed.

The 138-case retrieval check recovered 212/223 anchors versus 208 previously, four gains and no losses; four paired paraphrases recovered 8/8 versus 6/8. These are development retrieval results, not independent answer scores. Saved generated successes, timeouts and interpretation failures. Prepared review queues from 4,834 pages and checked 55 graph anchors with no stale anchors; no corpus text or embeddings changed. A 28-question, three-process BM25 probe found no ordering differences, so no ranking change was made. Models/configuration remain unchanged; contextual retrieval and structured synthesis remain off, graph assistance on. Final release verification and publication remain deferred. See [implementation and limitations](READINESS_IMPROVEMENTS_20261018.md).

# 17 October 2026 — Consolidated retrieval check and closure plan

Completed 138 paired development requests (276 arm responses), combining the original UPI, mixed-payments, paraphrase and graph sets while preserving routes and filters. Both lexical-context variants found 208/223 final anchors; two anchors gained on two questions were offset by two lost on one question. All-anchor positive cases were 102/114 versus 104/114. All 12 graph controls passed in both arms. Separated 114 reranked requests from 24 bypasses; retained negative retrieval failures and the excluded Ollama-offline attempt. Recorded inputs stayed unchanged; no execution errors or fallbacks in the completed run.

Kept contextual BM25 and structured synthesis disabled. No runtime, source or dense-index changes; no full-suite rerun was needed for these evaluation/documentation additions. Reconciled the stale project status and historical validation notes; documented remaining coverage, interpretation, checker, repeatability, source-review and release-verification work with completion criteria. Independent review remains open. No GitHub push. See [comparison and decision](CONTEXT_RETRIEVAL_DECISION_20261017.md) and [next engineering work](NEXT_ENGINEERING_PRIORITIES_20261017.md).

# 14 October 2026 — OC185B Markdown repair activated

Corrected the exact tax-reference transcription from `25 lakh` to `₹5 lakh` after visual comparison with the saved PDF. Corrected the legacy Markdown reading copy and saved a reusable, page-labelled Markdown source plus before/after provenance. Activated `payments-oc185b-repair-20261014` through the existing validated-release mechanism, preserving document identity and previous corpus. One new embedding, 14,479 reused, 14,480 chunks total. The repaired hash makes the passage eligible for drafting/checking again; historical corrupt versions retain protection. Graph v3 refreshes only affected page anchors; the launcher selects it and the preview server was restarted.

All 306 Python tests passed with zero failures/skips. The repaired-corpus 40-case comparison retained 69/78 versus 78/78 source anchors, all now model-eligible, and 12/12 controls in each arm. Four targeted model requests retained the correct tax amount, but the graph IPO answer remained incomplete after claim checking. Graph remains an opt-in maintained feature; independent scope/citation and unseen-question evaluation is still required before default rollout. See [source repair and decision](SOURCE_REPAIR_AND_GRAPH_DECISION_20261014.md). No Git commit/push or frozen handoff archive update.

# 14 October 2026 — Extended graph pilot and source-quality quarantine

Expanded the opt-in graph to OC76, OC141, OC185 and IPO-limit history alongside OC128/226: 55 source anchors, 15 documents, 13 relationships and six topics. Added explicit product/topic gating, related-topic links requiring evidence at both endpoints, missing-source notices and split-table citation hints. Default model configuration, corpus and indexes remain unchanged; the separate launcher selects the extended manifest. No Git commit or push.

The 40-case development set contains 28 substantive questions, 12 routing/filter controls and 78 required source anchors. The first valid hybrid comparison recovered 69/78 anchors without the graph versus 78/78 with it; all-anchor questions improved from 21/28 to 28/28. This is a co-designed development result, not held-out answer accuracy. Full experiment records and final-code verification are linked in [the extended pilot report](GRAPH_PILOT_EXTENDED_20261014.md).

Eight paired generated scenarios exposed OCR, scope, date-check and split-table citation failures. Visual inspection confirmed OC185B's tax-reference OCR rendered a rupee sign as an extra digit. Warning text did not prevent a false 25 lakh claim. Added a hash-bound exclusion flag so that fragment is visible for inspection but cannot enter generation or support checks, including with the graph disabled. The targeted rerun removed that false amount claim, but the graph answer still misapplied a GeM EMD cumulative table entry to tax payments generally. IPO answers distinguished cumulative from per-transaction limits in both arms. Independent answer scoring remains pending; graph assistance stays opt-in.

Final application regression: 303 Python tests passed, zero failures/skips; frontend syntax and both JavaScript suites passed. A later hybrid run encountered a stopped Ollama service and was correctly marked invalid for model-based comparison; its fallback record is retained. Source repair, scope-aware table validation, independent review and the broader release gates remain open.

# 13 October 2026 — Opt-in graph pilot for UPI OC 128 and OC 226

Added a source-anchored graph overlay for OC128/128A and OC226/226A, with page-hash validation, proposed aspect-level amendment links, bounded bidirectional expansion, unchanged context budgets, partial-coverage reporting and a separate localhost launcher. Default configuration and corpus content are unchanged. No Git commit or push.

Paired hybrid retrieval on 20 AI-assisted development cases found 33/39 required anchors for the baseline versus 39/39 for the graph (7/12 versus 12/12 complete substantive questions); both passed eight routing/filter controls. Six paired generated-answer scenarios found better source coverage but mixed output quality: baseline five drafts/one incomplete, graph four drafts/two incomplete. Date-comparison checks, split-table citation selection, OCR and obligation-strength wording remain findings; this is not answer accuracy or an independent benchmark. All captures and limitations are saved in [the pilot report](GRAPH_PILOT_128_226.md).

Regression: 292 Python tests passed, zero failures/skips; both JavaScript suites and frontend syntax check passed. Source PDFs for both addenda received an AI visual check; independent human review remains pending. Earlier unfinished reliability and independent-evaluation gates are not closed by this focused pilot.

# 11 October 2026 — Reliability cycle, validation still open

Full regression rerun completed after automatic approval succeeded: 275 Python tests discovered, 271 passed, four optional RBI HTML-conversion tests skipped because `lxml` is unavailable, zero failures (12.949 seconds). Both JavaScript test suites and `node --check web/app.js` passed. Saved raw output and code fingerprints under `evaluation/validation_runs/20261011T132442574976Z/`. This closes the suite-rerun task; generated-answer evaluation, remaining browser journeys and independent review remain open. No code changes or Git push were needed for this rerun. The blocked attempt described below is historical.

Added configurable shared-feature clarification, conservative title-based reference resolution, cross-source retrieval around named circulars, partial topic comparisons, protected retrieval candidates, stable excerpt IDs for claim checks, and central-answer retention status. Added 15 passing regressions; both JavaScript suites pass. Original-50 source retrieval found 55/55 anchors, with 5/6 empty negative results. Mixed-source development retrieval found 26/34 anchors; this is not answer accuracy. Outage fallback runs are explicitly excluded from neural comparisons. Final generated-answer evaluation, the full regression rerun and remaining browser checks are pending; automatic approval review blocked the full-suite launch due to its usage limit. No commit or push. See [implementation record](IMPLEMENTATION_20261011.md).

# 10 October 2026 — Bounded answers, evaluation and browser intake

## 10 October 2026 - colleague handoff

Frozen NPCI + eight-RBI source archive, file hashes, portable configuration, model digest checks and evaluation records are packaged for the `handoff-2026-10-10.1` Git tag. See [the handoff guide](COLLEAGUE_HANDOFF.md). Independent source/answer review remains pending.

Implemented request-local model budgets and stage/token timings, asynchronous browser jobs, keyword fallback on model failure, explicit partial-draft notices and coverage-review failure diagnostics. Added Add documents with source metadata, extraction preview, duplicate/quarantine handling, validated index build, activation and guarded rollback. Browser testing used an isolated synthetic corpus; the actual NPCI–RBI release was unchanged.

Added a frozen 20-case/34-anchor development dataset, source catalogue, snapshot-checked capture runner and human-review worksheets. All 20 generation requests completed: 18/34 anchors, 7/17 complete positive-anchor coverage, 3/3 negative abstentions and 7/17 positive abstentions. Median 24.0545s; max 65.187s. Five-question RAGAS pilot retained one scoring timeout; faithfulness 1.000 applies to one successfully scored response, not system accuracy. Independent review and retrieval/reviewer improvements remain pending. Final regression: 251 Python tests passed, four optional skips; two JS suites passed. See docs/IMPLEMENTATION_20261010.md. No model upgrade or Git push.

# 4 October 2026 — Midterm slide refinements

Reworked roadmap into indicative weeks, implementation tasks and deliverables. Explained preliminary retrieval metrics and their limits; source-anchor counts do not measure answer accuracy. Replaced the document-count panel with actual chunking and indexing steps verified in ingestion.py. Added an enlarged genuine local response to a shop card-machine question with question text visible. Preserved a second, unfocused response as a finding. Updated the three-page report, speaker notes, scope and share bundle. No model, corpus, retrieval configuration or storage changes.

# 4 October 2026 — Query Expert clarity revision

Reframed the active RAG UI and midterm package as Payments Guidelines Query Expert, with NPCI as the initial corpus. Prioritised the question flow, grouped technical controls, simplified repeated notices, and consolidated the roadmap. Rebuilt eight slides and a three-page report, matching PDFs and narration. Native renders reviewed; fresh browser journeys passed. No corpus, model or storage changes. Team identity and recording remain pending. See output/midsem/START_HERE.md.

# 2026-10-03 — payments RAG mid-sem closure

Repositioned the RAG landing and current entry documents around payments research, explicitly starting with NPCI. Removed the workflow navigation shortcut without altering its implementation or data. Added a timestamped same-snapshot four-variant evaluation runner, two metric regression tests, six saved live scenarios and a browser journey covering sources, filtering, summary, comparison, export, ambiguity, missing evidence, partial extraction and simulated model-outage recovery.

All variants retrieved 55/55 proposed anchors. BM25 returned no evidence for 6/6 negative cases; semantic variants did so for 5/6. No recall benefit from reranking was demonstrated. Preserved the limitation, single-pass timing caveat and human-review-pending status. Built an eight-slide reference-inspired presentation and four-page report with editable originals, PDFs and team narration. Team metadata, recording and submission remain pending. Full evidence and reproduction details are in MIDSEM_VALIDATION.md.

## 2026-10-03 - UPI Feature Workspace V2.0.0

Reframed the product for existing-feature reviews, feature changes and new launches. Rebuilt navigation and screens around the actual work order; added next-step guidance, local form errors, source previews, unsaved-edit protection and actionable stale-dialog recovery. Added exact-name/revision workspace deletion and result suppression for deleted jobs, bounded PDF/DOCX/Markdown/text upload previews, atomic batch drafting, an internal transaction-rule register and structured rule-by-rule assessment. Preserved V1 records and a pre-change backup; legacy controls are not reinterpreted as transaction rules.

Validation: 168 Python tests, existing answer-rendering JavaScript checks, a complete isolated V2 browser journey including all workspace types, role recovery and concurrent deletion, plus five real Qwen workflows. Screenshot review led to mobile navigation and notification placement fixes. Browser validation exposed and fixed a stale-delete-dialog reload race. Current product, user, implementation and validation documentation now describe V2.

## 2026-10-03 - Feature Launch Orchestrator V1.0.0

Added a separate local launch application on port 8766 with persistent SQLite state, reviewed and cited facts, four local-model workflows, explicit template demonstrations, partner/control registers, version-bound reviews, task dependencies, readiness gates, launch decisions and Markdown exports. The evidence picker imports selected UPI passages without rebuilding the research corpus or opening Chroma. Source-span selection fixed quotation paraphrasing exposed by live model tests. Scoped content invalidation and transitive task reopening were verified separately. Late generation cannot overwrite newer inputs or reviews.

Validation: 143 Python tests, existing JavaScript rendering checks, a complete isolated Edge browser journey and all five real Qwen3.5 workflows passed. Added a concise shareable product brief, beginner demonstration, technical/operations guide and validation record. This remains a local capstone with self-reported roles and evidence, not an authenticated production workflow. Original RAG v0.5.1 and its core-guide PDF remain separate.
## 2026-09-25 - all-product pack assessment (no runtime migration)

Read all 12 supplied product inventories and validation reports; audited 1,619 Markdown files / 5,059 page sections against 1,955 entries. Recorded 68 empty sections, missing structured dates/numbers, source-URL overlaps and title/reference review cases. Created repeatable audit and merge-preview scripts, reports and ALL_PRODUCTS_INTEGRATION.md. Merge preview retains all inventory rows and existing unmatched circulars, preserves converted UPI text/review IDs, and identifies one possible recovered gap. Active data, embeddings, source folders and runtime configuration remain unchanged. Source inventories date from 9-15 September; live-site completeness was not checked.

## 2026-09-25 - v0.4.0

Implemented the six RAG improvements: frozen evaluation and review worksheet; source QA overlays/workbench; adaptive clause/summary/comparison retrieval; pinned local ONNX reranker; clause/role labels and relationship review; per-claim checks with quoted evidence and withholding. Rebuilt 916 vectors, passed 59 tests and six live cases plus a contradiction check. Browser/source QA caught metadata-attribution and quotation-normalization issues; regression checks added. Updated project flow, operating/review/architecture/validation docs and shareable illustrated PDF. Full-corpus and independent evaluation review remain pending, not represented as completed expert verification.

# Development log

## 2026-09-24 — v0.3 implementation

Preserved v0.2 before changing storage or chunking. Installed Chroma in a project virtual environment and pinned its dependencies. Separated ingestion, registry, vector storage and context assembly from the HTTP/engine module.

Migrated the original 428 embeddings first, preserving the legacy chunk fingerprint. Used identical query vectors for JSON/Chroma comparisons; all 24 sampled vector/hybrid rankings matched. Then rebuilt 916 clause-aware embeddings under a new fingerprint.

Kept each chunk page-bounded and source-attributed. Recognized headings attach to their first clause. Long blocks use 220-word windows with 35-word overlap; page-to-page relationships remain explicit links. Kept OCR noise to avoid silently deleting source words. Added word-coverage and offset tests across the whole corpus.

Added a SQLite snapshot for documents, chunks, title features and imported references. An initial Windows file replacement failed because a SQLite connection was still open. Fixed by explicitly closing connections before replacement and revalidated the migration/build. Unique temporary filenames avoid temporary-path collision during snapshot creation.

Published Chroma collections via atomic manifests to protect the last complete snapshot from build failures. Tested failed collection creation and failed upsert. Added incomplete-record and corrupt-manifest handling, model-digest checks and a digest guard for legacy migration.

Bounded related context to one reference hop, limited related documents, optional same-feature passage and section neighbors. Filters and provenance apply throughout. Missing references are reported without fabricated text. Broadened explicit circular-number parsing so unknown suffixes/long numbers do not silently become general searches.

Added scope/feature controls, source inclusion labels, retrieval trace, chunk/edge audit panels and metadata in exported notes. Browser review found a long-line overflow in the new chunk panel; added wrapping and verified no horizontal overflow. In-app download observation timed out; Chrome export was successfully downloaded and inspected.

Updated all primary guides and added technical architecture, migration/rollback, validation and a documentation map. Preserved the earlier PDF as a clearly labelled v0.2 artifact. Final checks: 35 tests, 24 migration comparisons, three retrieval evaluations and six live answer requests. No held-out answer-quality gain is claimed.

## 2026-09-24 — context tuning

Raised configured generation context/output/evidence limits to 16384/3072/18000 after checking local RAM/GPU and running before/after plus abstention checks. Preserved original settings and raw token metrics. A stale server survived the first stop attempt; terminated its verified process tree and confirmed the replacement through a live HTTP answer and Ollama context report. See CONTEXT_TUNING.md. No embedding rebuild or global Ollama setting change was required.



## 2026-09-25 — v0.5 multi-product implementation

Staged all-products-v1 independently of the old corpus, preserving 1,955 inventory listings, 1,619 source Markdown files, old reviewed UPI chunks and newer retained entries. Same-source URL groups use canonical identities with multiple product memberships; different URLs remain distinct even when text matches. Kept unavailable ZIP/PDF records and blank-page records, quarantined two known source contradictions, and withheld the unverified 76B recovery candidate.

Added membership/fiscal-year filtering and exact-document selection. Repeated references now abstain with candidates instead of guessing; source coverage includes extraction gaps and unverified page counts. Added 18 product-scoped feature rules. Cross-product relationship inference and broader participant ontology remain review work.

Built 14,060 embeddings using local Qwen, caching 13,700 computed inputs with 360 reuse hits in about 15.4 minutes. Verified source hashes, SQLite integrity, vector ownership, model digest and corpus fingerprints before atomic configuration activation. Old corpus and versions/v0.4.0 remain intact.

Real-data testing found Unicode line separators breaking JSONL reads; fixed to split records only on newline. Browser testing found duplicate availability options and invalid unknown fiscal-year options; fixed both. Verified 50-row pagination, two NACH circulars with reference 13 compared by exact ID, AePS missing page warnings, ambiguity choices and a cited UPI generation result. No final captured browser console errors.

93 tests passed after activation, 55/55 UPI anchors retained in each evaluated retrieval mode, all 12 product-isolation checks passed, and seven product generation examples plus two abstentions were exercised. The live test assertions were corrected to the existing automated_supported label; this was a test expectation mismatch. Product-specific examples replaced two initial shared-compliance selections for more useful coverage. Tests are not expert accuracy evidence; response brevity and OCR spelling remain limitations.

Updated current flow and all entry-point docs, added architecture/validation/import guides and screenshots, and marked old PDFs/assessment as historical. Current server runs v0.5 on port 8765; stopped the temporary preview server.


## v0.5.1 — Context-sensitive answer formatting

The original schema returned claims and the browser always wrapped them in a bullet list. Added a layout of paragraph/bullets/steps referencing one-based draft claims, validated for exact coverage and legal block types. Claim filtering precedes layout materialization, with stable indices preventing reassignment after withholding. Fallbacks preserve all retained claims; explicit styles override an incompatible model layout. No unchecked prose fields or post-check rewriting call were added.

Added the style control, safe shared HTML/Markdown renderer, inline citation buttons and one support notice per answer. Kept raw model HTML/Markdown inert. Automated testing caught an explicit “bullet points only” parsing gap; fixed and verified. All 103 Python tests and renderer/export checks pass. Live Qwen cases returned paragraph, bullet-list and mixed layouts with support checks; exact brevity remains imperfect. Verified real paragraph rendering with no list elements and a working citation link. No embeddings changed; server restarted at the original localhost address. Pre-change files are in versions/v0.5.0.



## 2026-10-09 — Controlled document intake and model experiments

Added an operator-run PDF/Markdown intake pipeline with source provenance, page validation, quarantine, revision guards, cached embedding computation, candidate Chroma/SQLite snapshots, explicit activation and rollback. The API can serve original PDFs saved inside new corpus releases; evidence and source reader expose issuer/type metadata. Existing corpus fingerprints remain unchanged.

Added a fixed-evidence generation timing runner and researched official RBI directions in parallel. Kept the active NPCI corpus and model defaults. Larger model options remain hypotheses until tested. The live synthetic integration check computed only one new vector on its second release, verified retrieval/source/PDF access and restored its isolated config. Regression and observed model timings are documented in [the validation record](INTAKE_VALIDATION_20261009.md).


## 2026-10-09 — Publisher-neutral evidence assembly

Implemented topic research without RBI/NPCI buckets or inferred product exclusion for broad questions. Explicit filters remain boundaries. Added entity hints, relevance/diversity selection, bounded qualification/follow-up retrieval, evidence coverage UI/export and optional same-model review. Intake can retain source-quoted operator applicability labels without treating them as verified legal scope.

Initial live checks showed fabricated review quotations, so the reviewer now selects immutable excerpt IDs and the application attaches the original text. Participant misattribution and false conflict judgments still occur; they are preserved as evaluation findings rather than claimed fixed. All 228 Python tests and both browser-renderer suites pass. Frozen-set retrieval is unchanged at 55/55 anchors and 5/6 empty negatives. Active corpus, model settings and embeddings are unchanged. Changes remain local and unpushed. See TOPIC_RESEARCH_VALIDATION_20261009.md.


## 2026-10-10 — RBI intake completion record

Reconciled the 9 October activation of eight RBI core directions. Official PDF links did not return PDFs; retained official HTML and converted article bodies to Markdown with token-retention checks. Added source notes and a dynamic coverage label. The combined release has 14,480 chunks; 420 vectors were new and 14,060 cached. Eight retrieval checks, mixed-source evidence, browser source inspection, 230 Python tests, four optional conversion tests and both JS suites passed. The live generated answer took 718.943 seconds and its completeness review was unavailable; preserved this as an unresolved performance finding. Added a beginner intake guide and detailed integration record. No GitHub push performed.


## 2026-10-15 — Scope checks and sampled OCR repair

Added table category/column, named-source attribution and above-ceiling extrapolation guards, bounded same-page citation completion and one-pass claim repair with mandatory rechecking. Existing retrieval and model settings remain in place. Audited six reproducibly sampled circulars against ten original PDF pages, applied 21 explicit replacements on nine pages and activated payments-ocr-audit-20261015. Original Markdown backups, raw extraction, page images and change hashes are retained; only 13 embeddings were recomputed.

331 Python tests passed; final prompt refinement passed 25 targeted tests. Both JS suites passed. Frozen 50-case retrieval retained 55/55 anchors and 5/6 empty negatives. Live review still found IPO attribution and summary extrapolation failures: failed claims and unsuccessful repairs are withheld, not reported as corrected answers. Graph stays opt-in; independent source/answer review remains pending. No GitHub push. See [the implementation and audit report](SCOPE_CITATIONS_AND_OCR_AUDIT_20261015.md).


## 2026-10-16 — Bounded graph integration

Enabled the v3 source-anchored overlay in the active local main-app configuration at user request, retaining the repaired corpus, scope checks and bounded traversal. Full paired 40-case hybrid evidence run: 69/78 baseline versus 78/78 graph anchors; 12/12 controls in both arms; no fallback/errors. Twenty graph regression tests and JS checks passed. Live port-8765 checks confirmed graph activation for Related context and bypass for Strict. Independent answer review remains pending and known incomplete-answer cases remain documented. Historical colleague package unchanged; no GitHub push. See [integration decision](GRAPH_INTEGRATION_20261016.md).

## 2026-10-17 — Intake triage and evidence experiments

Implemented hashed page-quality triage, structural quarantine, reviewed companion PDFs, browser warnings and candidate integrity checks. Added optional metadata-enriched BM25 and bounded verbatim/table evidence records before natural-language synthesis. Paired retrieval results were unchanged: 55/55 UPI anchors, 29/34 payments anchors, with negative retrieval limitations retained. Six fixed-evidence generation cases showed no consistent benefit and one incomplete variant comparison; both experimental flags remain off. Fixed allowed-citation constraints and narrow source-owned monetary attribution based on observed failures. 348 Python tests and three JS suites passed; real browser intake warning verified without activating test material. Corpus and embeddings unchanged; no GitHub push. [Full evidence and decision](EVIDENCE_IMPROVEMENTS_20261016.md).

## 2026-10-17 — Expanded evaluation and reported IPO regression

Completed paired contextual retrieval on 28 development paraphrases in hybrid and keyword-only diagnostic configurations, plus 14 broader and six earlier fixed-evidence synthesis pairs. Hybrid reference-anchor retrieval stayed 46/56; the keyword diagnostic improved 35/56 to 39/56. Real answer review found exemption transfer, chronology reversal and category conflation, including wrong claims accepted by same-model checks. Both optional experiments remain off; the bounded graph overlay remains active. These are not held-out answer-accuracy results.

Reproduced the exact IPO empty-answer failure. Corrected scope checks for compact circular identifiers, joined OCR acronyms/codes, plural scope words and redundant inline citation labels. Kept monetary attribution and semantic checks. Clarified source-specific explanation instructions and closed a phrase gap in the existing above-ceiling guard. The exact frontend question now produces a cited answer. 365 Python tests pass. All failed model attempts remain saved; completeness-review false positives and broader answer failures remain release blockers. Corpus, embeddings and configured models are unchanged; no GitHub push. See [regression investigation](IPO_REGRESSION_20261017.md) and [expanded evaluation](EXPANDED_EVIDENCE_EVALUATION_20261017.md).


## 20–22 October 2026 — supervised workflows and maintained graph decision

Implemented Query Desk and Change-Impact Briefs, separate versioned SQLite records, review state transitions, evidence exports, source/configuration/model-digest/graph invalidation, local HTTP routes and UI. Fixed stale-read regeneration races and reserved impact prompt space. Added visible partial-answer status without promoting the rejected reviewer. Intake bundles and validates the maintained graph; current-facing labels describe supported graph-assisted retrieval. Broader automatic expansion is not selected for release.

430 Python regressions passed after model tracking; four JavaScript suites passed. Current-code 144-case graph ablation: 212/234 off, 223/234 on, eleven gains and no losses. Classified all eleven existing misses. Prepared the provisional 50-case independent review pack plus 55 graph anchors/13 relationships and a capture runner that refuses unreviewed packs. Independent answer/source review and final release verification remain pending. No source, embedding, model-size/budget change or GitHub push.

## 22 October 2026 — follow-up reliability and citation diagnostics

Added exact attached-ID normalization, source-focused bounded repair for malformed registry labels, explicit model metadata/call budget timing, rejection of late model responses and typed unavailable-review causes. Preserved strict factual-number and source-support checks. Six known-failure repeats had no model timeouts but retained incomplete answers and invalid reviews. A generation-prompt instruction failed to recover history and was removed. An exact frozen-claim repair recovered the earlier circular's provision under automated checking; complete-answer quality and independent gates remain open. See [diagnostic records](../evaluation/readiness_diagnostics/README.md) and [all action items](ACTION_ITEMS_20261022.md). No source/embedding/configuration changes or publication.

## 23 October 2026 — implementation-round closeout

Reconciled the final 438-test regression record, all diagnostic attempts and the final live API smoke answer. Current Python hashes match the API capture. That answer retained the earlier provision but remained incomplete; the open action register explicitly preserves quality, independent-review, latency and release gates. Updated current documentation and checked relative links. No GitHub push.


## 24 October 2026 — engineering closeout

Added total local-model HTTP deadlines, amount/unit evidence checks and attached-evidence repair isolation. Verified 445 Python tests and four JavaScript suites, fresh pinned installation, full cached-vector index rebuild, incremental intake and recovery. Saved controlled workflow timings and browser exports. See [closeout](ENGINEERING_CLOSEOUT_20261024.md) for evidence and limitations. Independent payments acceptance and material completeness remain open; no GitHub publication.
