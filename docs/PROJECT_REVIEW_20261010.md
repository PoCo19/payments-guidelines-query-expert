# Project review and recommended next steps

Reviewed 10 October 2026 against commit `79c303a2d13386f363daab4314240377bba61a4b` (`handoff-2026-10-10.1`).

**Assessment:** a substantial, reproducible capstone implementation with useful source and operational controls. End-to-end answer reliability is still insufficient for unsupervised payments research. The next milestone should be a demonstrably more reliable research assistant, with reviewed evidence and measurable user benefit.

## Review scope

Reviewed retrieval, reference resolution, chunking, reranking, context selection, generation, claim checking, runtime budgets, intake documentation and raw evaluation captures. Reconstructed the frozen corpus without model calls, audited metadata and reproduced selected routing/ranking behaviour. Checked current primary RAGAS documentation for metric interpretation.

No new full generated-answer/RAGAS benchmark, independent regulatory-source review, security audit or browser usability study was performed. Regression results below are the saved handoff checks, not a newly executed full suite. Targeted diagnostics used BM25 and the installed reranker; they do not constitute a new four-way benchmark or a measured hybrid improvement.

## What is already valuable

- Source ownership is preserved through document identity, page/section labels, chunk links, source hashes and provenance.
- Keyword, vector and hybrid retrieval, a local reranker, cited generation, source inspection, summaries/comparisons and export are implemented.
- Document intake supports preview, preparation, embedding reuse/build, activation and rollback. Uploads do not silently enter the active corpus.
- Processing budgets, stage progress, partial-answer labels and source fallback improve operational usability.
- The tagged handoff includes source snapshots, configuration, dependency locks, model digests, datasets and raw experiment records.
- Saved final handoff regression: 260 tests discovered, 256 passed, four optional conversion tests skipped; both JavaScript suites passed. This establishes implementation behaviour, not answer accuracy.

## What the current evaluation establishes

The final mixed-source capture is [20261010T081610Z](../evaluation/payments_runs/20261010T081610Z/capture.json). Its 20 development cases contain 17 answerable cases, three negatives and 34 expected source anchors. References are AI-assisted and not independently reviewed.

| Measure | Observation | Interpretation |
|---|---:|---|
| Requests completed | 20/20 | Processing completed; answers may still be incomplete, withheld or wrong. |
| Expected anchors retrieved | 18/34 (52.9%) | Nearly half of the annotated evidence was absent from final context. |
| Answerable cases with every anchor | 7/17 (41.2%) | Complete annotated evidence coverage is inconsistent. |
| Answerable cases abstained | 7/17 (41.2%) | Substantial lost utility; includes ambiguity/filter blocks and model abstentions. |
| Negative cases abstained | 3/3 | Encouraging, but all three concern unavailable fictional-company information; this does not establish difficult-negative robustness. |
| Request latency | Median 24.05 s; maximum 65.19 s | Single development run, including two near-zero routing exits; not a controlled service-level measurement. |
| Coverage review unavailable | 5/20 | Automated review has operational/reliability gaps. |

Within that capture, RBI-direct cases retrieved 9/12 anchors, RBI–NPCI cases 5/12, the single RBI cross-document case 0/3, and scope/qualification cases 4/7. These small subgroups identify investigation areas, not robust generalisation estimates.

The five-case RAGAS pilot scored faithfulness on only one response (one error, three skips). Its 1.0 result is not system-wide accuracy. RAGAS faithfulness assesses support in retrieved context; factual correctness compares against a reference answer. Neither metric alone proves that the central question was answered. See the official [faithfulness](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/faithfulness/) and [factual correctness](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/factual_correctness/) documentation.

## Concrete findings

### 1. Reference resolution and product inference can remove required sources

Current reproduction of PAY-009 inferred NETC from FASTag and rejected OC 207 before retrieval. In `product_scope.resolve`, inferred product is applied as an eligibility filter. In `adaptive_context.assemble`, an explicitly requested circular restricts the initial candidate document set. This can exclude a second source needed to answer a question naming both an RBI direction and an NPCI circular.

Recommended design: resolve named references separately from general topic retrieval; use named documents as required evidence candidates, while searching for the rest of the question across eligible sources. Preserve explicit user filters. Treat inferred product as a ranking hint where possible, and ask for clarification when document identity remains genuinely ambiguous. Do not infer legal precedence from publisher names.

### 2. Reranking is not uniformly beneficial

Targeted current diagnostic: BM25 top-64 candidates followed by the pinned reranker and existing diversity selection:

| Case / anchor | BM25 rank | Reranked position | In selected six seeds? |
|---|---:|---:|---|
| PAY-001, full-KYC balance | 4 | 3 | Yes |
| PAY-002, PA capital milestones | 1 | 9 | No |
| PAY-014, generic authorisation requirement | 59 | 26 | No |
| PAY-014, PA capital milestones | 5 | 8 | No |

This diagnoses a ranking/selection failure on specific cases. It does not prove BM25 is globally better or identify the cause of every historical hybrid miss. Add stage-level anchor tracking: candidate retrieval → reranking → evidence selection → prompt. Compare the same corpus, routes and cases across BM25, vector, hybrid and hybrid plus reranking. Tune only after locating losses.

### 3. Supported background can survive while the central answer disappears

In saved PAY-004, both expected anchors were retrieved. The draft included the requested deadline, but exact-quote validation rejected its supporting quotation. Background claims survived, leaving the question unanswered. Across the saved run, 11 draft claims were withheld; eight recorded exact supporting quote validation failures, two unavailable/malformed checks and one number absent from cited text. These counts do not prove all withheld claims were correct.

Keep evidence safeguards, but replace model-retyped quotations with selection of immutable source spans/IDs where appropriate. Validate semantics as well as span existence. Add a post-check for whether the surviving answer addresses the user's requested fact and qualifications. If the central answer was withheld, say so explicitly instead of presenting only background. Evaluate false acceptance and false rejection of claims, including tables and typography.

### 4. The evaluation does not yet mirror normal automatic routing

All 20 case payloads explicitly use `route=clause`. A fresh PAY-012 diagnostic with `route=auto` selects comparison but blocks with "Name at least two circular numbers for comparison", although the question names an NPCI circular and an RBI direction. This is a reference-resolution/usability limitation not exercised by the forced-route capture.

Keep diagnostic routes, but add a separate end-to-end benchmark using the default frontend route and settings. Include summaries, comparisons, clarification and user-selected documents. Report route-dependent bypasses rather than blending them into a reranker score.

### 5. Source metadata limits applicability and historical answers

The reconstructed snapshot has 1,570 searchable documents; 1,455 lack an issue date (92.7%). No document has a populated document-level `effective_date` field. Dates may exist inside source text, so this is a metadata finding, not a statement that dates are absent from the documents. Page review labels are: 4,575 imported/unverified; 240 machine extraction not verified word-for-word; 11 source-image-checked transcriptions; eight intake/unverified logical pages.

Prioritise review of the eight RBI directions and documents used by evaluation questions. Store verified issue, revision, effective-from/to and entity scope separately; effective dates may apply to individual clauses rather than entire documents. Preserve unknowns. Review source-supported amendment/repeal relationships instead of deriving supersession from chronology. Broader ingestion should follow quality checks on this reviewed slice.

### 6. Documentation needs a clear current-status view

The top of `PROJECT_STATUS.md` records the published handoff, while a following paragraph still says no Git push was performed and quotes the earlier test count. Historical evidence should stay immutable, but the current status summary should point to the latest tagged release and label older observations with their dates. Submission documents should remain identified as the midterm snapshot unless deliberately revised.

## Recommended sequence

| Priority | Work package | Completion evidence |
|---|---|---|
| 1 | Fix reference resolution, inferred filters and automatic mixed-document comparison. | Reproduced failures covered by regression cases; named and complementary sources remain retrievable; real ambiguity still requests clarification. |
| 2 | Repair claim quotation selection and central-answer handling. | Human-labelled supported/unsupported claims, including tables, pass measured acceptance/rejection checks; critical-answer removal produces an explicit incomplete response. |
| 3 | Establish a reviewed evaluation baseline, alongside priorities 1–2. | Domain reviewers verify the 20 references and score saved answers for correctness, completeness, applicability and citation support. Record disagreements. Preserve original data; publish revisions under a new dataset version. |
| 4 | Run controlled retrieval and context experiments. | Same source/model settings across four variants; per-stage recall and document coverage; separate normal-route results; repeatable latency without concurrent workloads. Use the original 50 cases as a separate regression set. |
| 5 | Review source quality, dates and relationships for the evaluation slice. | Verified provenance and qualifications; fewer date/relationship failures on reviewed cases. |
| 6 | Test practical usefulness with payments colleagues. | Three to five users perform lookup, cross-source research and comparison tasks; record completion, corrections, source inspections and time relative to manual research. |
| 7 | Benchmark a larger model or larger context only after evidence delivery is reliable. | Fixed evidence prompts isolate generation ability; compare central-answer correctness, completeness, citation support, median/p95 latency and failures. Keep a change only if the trade-off helps the intended users. |

After tuning, create a separately authored, independently reviewed held-out set (for example 25–30 questions), including realistic false premises, missing amendments, entity-specific exceptions, date ambiguity and incomplete sources. Do not tune on its results. A different judge can reduce same-model dependence but does not replace human review. Report scored, skipped, failed and abstained cases with every automated mean.

For a small capstone team, engineering can work on priorities 1–2 while domain reviewers prepare priority 3. Set acceptance targets before the final held-out run; do not choose thresholds after observing its scores.

## Best subsequent product feature

A saved, reviewable **payments research brief** fits the existing product: question and entity → direct answer → applicable conditions → source passages → unresolved questions → reviewer status → export. It adds practical team value without requiring a separate orchestration application. Prioritise it after answer reliability improves and the colleague pilot confirms that this workflow is useful.

New vector databases, multi-agent orchestration, fine-tuning, broad source expansion and public deployment are not justified as immediate responses to the failures observed here. The demonstrated bottlenecks are evidence selection, reference resolution, central-answer preservation and evaluation validity.
