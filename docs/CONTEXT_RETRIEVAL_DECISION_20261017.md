# Larger contextual retrieval check — 17 October 2026

**Decision: do not promote either experiment.** Metadata-enriched lexical retrieval still has no net evidence-anchor gain in the normal hybrid flow and causes a material loss on one question. Structured synthesis remains off based on its earlier mixed results and observed incorrect interpretations; it was not rerun in this retrieval-only check. Keep the existing graph-assisted flow.

## What was compared

The frozen consolidated dataset has **138 distinct request specifications**: the original 50 UPI cases, 20 RBI/NPCI cases, 28 paraphrases and 40 graph cases. It combines existing AI-assisted development cases, with related questions and graph expectations co-designed with the graph. It is **not 138 independently authored or held-out questions**.

Both arms use the same repaired corpus, vectors, hybrid search, configured local reranker, graph and 18,000-character evidence budget. Only the experimental BM25 metadata prefix differs. This tests contextual **lexical indexing**, not contextual embeddings or model-generated chunk summaries. Original routes and filters are retained, including the original UPI filter. Arm order alternates by question.

The 138 cases contain 114 positive cases with 223 document/page/quote anchors, 17 negative or clarification cases, and seven other controls. An anchor is one expected passage, not one question. Thirteen selected summary/comparison requests and other early-return cases do not exercise reranking; report those separately.

## Results

| Development family | Cases | Baseline anchors | Enriched anchors |
|---|---:|---:|---:|
| Original UPI | 50 | 55/55 | 55/55 |
| RBI/NPCI | 20 | 29/34 | 29/34 |
| Paraphrases | 28 | 46/56 | 46/56 |
| Graph scenarios and controls | 40 | 78/78 | 78/78 |
| **Total** | **138** | **208/223** | **208/223** |

- All expected anchors were found for **102/114 versus 104/114 positive cases**. This small question-level gain is real in this development run, but does not establish a consistent overall improvement.
- `X-PAY-008` and `X-PAY-010` each gain one anchor. `X-PAY-014` loses two: its final coverage falls from 2/3 to 0/3. All other final anchor vectors are identical. Gains do not cancel the practical risk of losing important evidence on another question.
- **114 requests actually reranked in both arms:** 185/198 anchors in each. **24 bypassed reranking in both:** 23/25 in each. The missing bypass anchors belong to an ambiguous-reference case; the unreviewed reference expectation is retained rather than relabelled to improve the score.
- Initial top-six diagnostic search finds **129/200 anchors in each arm**. This diagnostic excludes selected summary/comparison requests and is not the full multi-stage retrieval pipeline.
- **12/12 graph controls pass** and **2/2 required missing-source notices appear** in both arms.
- **10/17 negative/clarification requests return no evidence** in each arm. Seven still retrieve neighbouring passages. These are retrieval outcomes, **not generated-answer abstention or safety scores**.
- Overall median retrieval time is **1.930 seconds versus 2.008 seconds**; for actually reranked requests it is **2.594 versus 2.6095 seconds**. These single-run timings include warm-up/cache effects and exclude the separately timed top-six diagnostic. They do not demonstrate a meaningful speed difference.

The completed run contains all **276 arm responses**, zero execution errors, zero model fallbacks, and unchanged recorded corpus/configuration/code/dataset fingerprints. Benchmark validity here means an intact comparison, not correct answers. No answers were generated or judged in this run.

The explicit credit-card-bill question `G-LIMIT-03` finds both anchors in both arms, while its paraphrase `X-LIMIT-03` finds neither. This is a concrete reason to prioritize coverage across ordinary question wording rather than adding more metadata indiscriminately.

## Saved evidence and reproduction

- [Frozen questions](../evaluation/context_regression_20261017.json) and [provenance/fingerprints](../evaluation/context_regression_20261017.manifest.json).
- [Full paired capture](../evaluation/improvement_runs/20261017T145242617297Z/capture.json).
- [Family and execution-stratum table](../evaluation/improvement_runs/20261017T145242617297Z/comparison.md), [machine-readable metrics](../evaluation/improvement_runs/20261017T145242617297Z/stratified_summary.json), and [case-level changes](../evaluation/improvement_runs/20261017T145242617297Z/paired_cases.csv).
- Earlier run `20261017T145135924206Z` was stopped because Ollama was not running. It is explicitly marked interrupted/invalid, its response records are retained, and it is excluded. The installed local service was restarted before the successful run.

From the project folder, with the existing models and active corpus available:

```powershell
.\.venv\Scripts\python.exe -X utf8 evaluation/build_context_regression.py
.\.venv\Scripts\python.exe -X utf8 evaluation/evidence_experiments.py --kind context --dataset evaluation/context_regression_20261017.json --method hybrid --rerank
.\.venv\Scripts\python.exe -X utf8 evaluation/summarize_context_regression.py evaluation/improvement_runs/<new-run>/capture.json
```

Run one model workload at a time. Preserve historical captures and use the newly printed run directory for analysis. The experiment creates separate in-memory configurations; it does not enable the feature in the live app or rebuild the dense index.

Next work is the [engineering closure plan](NEXT_ENGINEERING_PRIORITIES_20261017.md): evidence coverage, source interpretation and checker reliability first, followed by repeatability and release verification. Independent payments review remains separate from usability testing. No GitHub publication was performed.
