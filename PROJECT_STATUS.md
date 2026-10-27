# Current project status — 27 October 2026

The [27 October GitHub development handoff](docs/GITHUB_HANDOFF_20261027.md) includes current code, the corrected source snapshot and matching maintained graph. Additional checks passed **465 Python tests**; negative smoke inputs abstained. A broad UPI Lite answer returned historical limits without the later amendment, and both positive smoke completeness checks were unavailable. This is an open answer-quality regression, not a production-ready release. See [saved results](evaluation/release_20261027/README.md).

Adaptive presentation closeout is complete: the final combination-of-tables-and-prose handling passed 15 focused formatting tests, all four frontend suites passed again, and the current application was restarted and checked in the browser. The preceding full suite passed 463 tests. Independent answer-quality acceptance remains separate and pending.

Latest presentation extension: [Automatic style with optional tables](docs/ADAPTIVE_ANSWER_PRESENTATION_20261026.md), consistent saved-answer rendering and Markdown export. **463 Python tests and four JavaScript suites passed.** Seven development model calls retained incomplete-answer warnings; a saved comparison produced a table through a deterministic layout-only replay. This does not establish answer-quality improvement. Corpus, embeddings, retrieval and evidence-checking logic are unchanged.

The [review clarity increment](docs/REVIEW_CLARITY_20261026.md) separates automatic answer checks, optional human sign-off on a saved response, and independent project evaluation. Query Desk leads with answers, edits and evidence export. Human sign-off and saved revisions are in collapsed sections; existing states, decision requirements, freshness guards and history are preserved.

Verification: **457 Python tests and four JavaScript suites passed**, plus isolated browser checks using saved model responses. This is interface verification, not a new answer-quality evaluation. Core backend/configuration hashes are unchanged from the start of this increment. Independent review remains deferred. No GitHub publication or frozen-handoff replacement was performed.

# Historical product increment — 25 October 2026

The [product interface increment](docs/WORKBENCH_PRODUCT_20261025.md) is implemented: a Payments Research Workbench overview, distinct Ask & Research / Query Desk / Change Briefs entry points, guided setup, research-answer handoff, confirmed comparison baselines, source inspection, analyst finding labels, and recoverable archive/trash controls. Existing RAG engine and retrieval/graph/support code are unchanged against the 24 October candidate.

Verification: **457 Python tests and all four JavaScript suites passed**, with isolated live-model/browser walkthroughs and evidence export. The three generated walkthrough answers retained incomplete-answer warnings; workflow verification is not answer-quality acceptance. Independent source/graph and acceptance-set review remains deferred at the user's request. Final pilot acceptance remains open. Nothing was published to GitHub, and the frozen 24 October handoff archive was not replaced.

# Historical engineering candidate — 24 October 2026

[Engineering closeout](docs/ENGINEERING_CLOSEOUT_20261024.md) records **445 passing Python tests**, all four JavaScript suites, a fresh pinned environment and a complete 14,480-chunk Chroma rebuild using verified cached embeddings. Model-outage, interrupted-work, stale-graph, incremental intake, activation and rollback checks passed in an isolated copy. Both supervised browser workflows were exercised with source inspection, versioned edits, review submission and evidence export.

Local-model calls now enforce a connection-wide deadline; monetary support checks reject unrelated address digits as evidence for monetary limits. Focused malformed-label repair remains bounded to attached evidence. Corpus content, live embeddings and model configuration were preserved.

The 22-attempt serial development latency run completed without main-model failure. Ten warm observations per workflow yielded p95 **26.844 seconds for Query Desk** and **41.046 seconds for briefs**. **All 20 warm responses remained marked incomplete**, and two brief completeness checks returned invalid output. This closes timing measurement, not answer-quality acceptance.

Current rebuilt-index graph ablation: **223/234 anchors on versus 211/234 off**, 12 gains and zero losses. Graph-on matches the prior 144-case result; one graph-off baseline anchor varied. Independent answer quality is not measured by this comparison.

A portable engineering candidate is documented in [ENGINEERING_START.md](ENGINEERING_START.md). Independent source/graph review, reviewed paired answers, the reviewed 50-case acceptance benchmark and resulting quality fixes remain open. The candidate is not pilot-approved and has not been published to GitHub. See the [active action register](docs/ACTION_ITEMS_20261022.md) for exact completion boundaries.

# Historical project status — 23 October 2026

**Latest follow-up:** [action register](docs/ACTION_ITEMS_20261022.md) now identifies all completed engineering and remaining gates. Exact internal citation labels no longer create false factual-number failures; a focused attached-evidence repair addresses malformed labels without accepting their digits. Timing records separate metadata/retrieval/model calls, late completions are rejected, and unavailable reviewer causes are classified. A six-answer repeat completed without timeouts, but incompleteness and invalid reviews remain. A subsequent exact-claim replay recovered the earlier source provision; it is not independent answer validation. [All diagnostic attempts and limitations](evaluation/readiness_diagnostics/README.md) are saved. The added generation instruction did not show a completeness benefit and was removed.

Final follow-up regression: **438 Python tests passed** in `evaluation/workbench_20261020/tests-readiness-fixes-final.txt`. The JavaScript/UI code was unchanged in this follow-up; its four prior suites remain the recorded UI checks. This is not final release verification.

The restarted server's saved IPO smoke answer retained the OC185B distinction and OC127 provision in 19.406 seconds. It remained incomplete with two other statements withheld. Current code hashes match that capture; no claim of complete-answer or pilot acceptance is made.

[Payments Query Desk and Change-Impact Briefs](docs/SUPERVISED_WORKBENCH_20261020.md) are implemented locally with separate SQLite persistence, immutable drafts, review decisions, source/model/graph snapshots, stale-approval checks and evidence exports. Their initial impact actions are explicitly generic analyst checklists, not inferred institutional instructions.

**Graph decision:** maintain bounded graph-assisted retrieval; automatic whole-corpus graph expansion is not selected for this release. Current-code 144-case retrieval ablation found **223/234 anchors on versus 212/234 off**, eleven gains, zero losses. Routes/filter controls were preserved. This is development retrieval evidence, not answer correctness or independent release approval. All 55 anchors and 13 relationships are in the independent-review pack; relationship review remains pending.

**Verification:** 430 Python tests passed after model-fingerprint checks. Four JavaScript suites and syntax checks passed before the final documentation pass. The eleven earlier misses are classified: five initial candidate-pool misses and six ranking/context-selection misses. All quoted text exists in the source corpus. Incomplete answers and unavailable completeness checks remain visible; eligibility, attribution and historical-completeness failures are not claimed solved.

The six-attempt development graph-answer run had three model timeouts; the other answers remained incomplete. It is not an answer-quality or latency pass. The frozen provisional 50-case pack and guarded capture runner are prepared. Independent payments review, paired graph-relevant answer review, acceptance scoring and controlled generation-latency measurement remain open. Final clean-install/full-rebuild/recovery verification and a release handoff remain last. No GitHub publication has been made. The corpus, embeddings, model sizes and budgets are unchanged.

The following entries are historical records with their original dates and metrics.

# Historical project status — 20 October 2026

The [19–20 October quality cycle](docs/QUALITY_CYCLE_20261019.md) retains bounded notification-evidence recovery and source-specific claim repair. The maintained UPI graph remains on. Broader graph expansion, contextual BM25 and structured synthesis remain off. The source corpus, embeddings, configuration and model choices are unchanged.

The paired 144-question development check found **223/234 source anchors versus 220/234**, with three gains and no losses. This measures retrieval, not answer correctness. Original 138-case coverage remained 212/223. Coverage-review and generation-instruction experiments did not show reliable improvement and were not promoted. The completed ten-case frozen reviewer challenge found that the experimental reviewer missed four of five provisionally labelled gaps, despite reducing warnings on complete answers. These labels await independent review.

Final software regression: **399 Python tests and all three JavaScript suites passed**. An initial ten-case live run had six model timeouts under observed GPU contention. The repeat after memory became available found **19/19 anchors, no generation fallbacks, two correct negative abstentions and one clarification**. Four coverage reviews remained unavailable, and eligibility, attribution and answer-completeness issues remain. This is not an independent answer-accuracy pass. Raw responses and separate review worksheets preserve both runs. The application server has not been restarted as part of this cycle.

**Still open:** reliable completeness checking, remaining evidence misses and eligibility omissions, repeatable performance under controlled GPU load, independent source/answer review, held-out acceptance, colleague trials and final release verification. Final browser/recovery/clean-copy verification remains the last step as requested. No new GitHub release or push has been made.

The following entries retain their original dates and counts; they are historical evidence.

# Historical engineering status — 18 October 2026

**Payments Guidelines Query Expert** remains a local payments research assistant using NPCI circulars and eight imported RBI core directions. The active corpus is `payments-ocr-audit-20261015`; bounded graph assistance uses `pilot/upi_extended_graph_v3.json`. The generation model remains Qwen 3.5 9B, embeddings Qwen3 0.6B, with unchanged context/output budgets.

**Context-enriched BM25 and structured evidence synthesis remain disabled.** Prior paired experiments did not demonstrate a consistent improvement in the normal flow. The empty IPO response regression has been fixed and verified through final API and browser captures. Wider tests still expose missing evidence, unsupported interpretations and unreliable same-model checking; the product is not yet validated for operational use.

Latest saved full Python regression: **390 passed**, zero failures. This is software verification, not answer accuracy. The [broader graph and answer-fix iteration](docs/GRAPH_EXPANSION_20261018.md) adds a corpus reference-graph candidate, intake maintenance, literal category ownership, citation-label normalization and exact repaired-claim deduplication. The maintained graph remains enabled; the broader candidate remains disabled because its evaluations do not yet demonstrate added benefit.

The earlier [readiness iteration](docs/READINESS_IMPROVEMENTS_20261018.md) improved source coverage from 208/223 to 212/223. A later 138-case comparison of the broader graph found one gain and one loss, with both arms at 212/223; expansion was moved after existing evidence to prevent displacement. Ten new cases then found 15/15 anchors in both arms, and seven targeted replays preserved the previously lost evidence without establishing a new gain. The final ordering was not rerun across all 138 cases.

The 16-claim development challenge now matches all expected labels after a conservative category-ownership fix. Four final live answers retrieved 13/13 anchors without generation fallback or unavailable support checks. The incorrect collective tax assertion was withheld, leaving that answer incomplete. Coverage reviewers still produced questionable interpretations; independent correctness and reliable completeness review remain open. All successes, failures and reverted experiments are preserved.

Three additional RBI/mixed-source paraphrases found 3/5 anchors in both candidate and baseline modes, including one notification question missing both required passages. Graph v4 tightens cross-product topic annotation; its explicit reference edges are identical to evaluated graph v3. It does not change answer retrieval or active configuration.

The earlier [138-case contextual retrieval comparison](docs/CONTEXT_RETRIEVAL_DECISION_20261017.md) found 208/223 anchors in each arm, with two gains offset by two losses. That experiment is distinct from the later focused evidence-recovery changes. Contextual BM25 and structured synthesis remain off; graph assistance remains on. These are development questions, not independent answer-accuracy evidence. Final end-to-end release verification remains deferred by request.

The colleague handoff below remains the historical 10 October package. Current local changes have not been published as a new release. Independent source/answer review, held-out acceptance, colleague trials and final-version release verification remain open. The records below preserve their original dates and metrics; they are not current performance claims.

## Historical status — 10 October 2026

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
