# RAGAS pilot evidence - 4 October 2026

**Status: implemented and exercised locally; independent evaluation pending.** These records are separate from the midterm's original 50-case retrieval-only comparison. The slides and report have not been changed to claim these as validated answer-quality results.

## Main 12-case pilot

[Application responses and configuration](pilot12-20261004/capture.json) | [Score summary](pilot12-20261004/scores-20261004T084425Z/SUMMARY.md) | [Per-case scores](pilot12-20261004/scores-20261004T084425Z/scores.json) | [Judge requests and outputs](pilot12-20261004/scores-20261004T084425Z/judge_calls.jsonl) | [Human review sheet](pilot12-20261004/human_review.csv)

The application used hybrid retrieval with reranking enabled where supported, and Qwen3.5 9B for generation. RAGAS used the same local model as judge, at temperature 0. The corpus fingerprints remained unchanged during capture. All 12 application requests completed: eight focused questions, one summary, one comparison and two negative cases.

| Metric | Mean of successful eligible scores | Scored cases | Skipped cases | Evaluator errors |
|---|---:|---:|---:|---:|
| Faithfulness | 0.967 | 10 | 2 | 0 |
| Factual correctness against draft references | 0.375 | 8 | 4 | 0 |
| Context recall against draft references | 1.000 | 8 | 4 | 0 |
| Context precision against draft references | 0.951 | 8 | 4 | 0 |
| Citation support | 0.924 | 10 | 2 | 0 |

There are **44 applicable metric scores**, not 44 questions. The remaining 16 case-metric combinations are explicitly skipped: negative cases are assessed separately, and the summary/comparison references are insufficient for reference-based scoring. No cases or metric errors were silently dropped. There were no positive-case abstentions; both negative cases abstained (2/2).

## What this reveals

1. **The evaluation pipeline works end to end.** Real application outputs were captured, adapted from displayed claims, scored locally and retained with source context. This demonstrates integration, not independently established accuracy.
2. **Reference quality is a blocker for correctness scoring.** Draft answers such as “P2M only.” omit the subject and conditions supplied by the question. The judge rejected a fuller answer against that short reference despite finding it supported by the retrieved evidence. The factual-correctness mean of 0.375 is therefore a diagnostic disagreement, not evidence that 62.5% of answers are wrong. Complete references and human adjudication are needed before using this metric for selection.
3. **Citation-specific checks add information.** Citation support was lower than whole-context faithfulness. A claim can be supported somewhere in the supplied evidence while its selected citation is less convincing to the judge. Inspect per-claim details before deciding whether this is an app error, extraction problem or evaluator error.
4. **Retrieval and refusal differ.** RAG-048 retrieved irrelevant payment passages, but the model declined to answer the unrelated question. The earlier empty-source retrieval check and the generated-answer abstention check legitimately measure different behaviour.
5. **Coverage remains narrow.** These are previously seen AI-assisted questions, often naming circulars. The same model both generates and judges. This pilot does not demonstrate broad payments accuracy, independent agreement or the superiority of hybrid retrieval over BM25.

## Additional retained evidence

- [Initial four-case integration capture](local-pilot-20261004/capture.json) and [scores](local-pilot-20261004/scores-20261004T083909Z/SUMMARY.md): retained rather than replaced by the larger pilot, including the poor draft-reference correctness scores.
- [Synthetic judge controls](synthetic-controls-20261004T084932Z/controls.json): one explicitly supported fictional claim scored 1.0; one explicitly contradicted participant assignment scored 0.0. These are sanity checks, not application questions or independent human calibration.
- The application test suite passed **184 tests**, including **13 evaluation-integrity tests**. These exercise status-banner rejection, source/page matching, citation IDs, abstention handling, inadequate summary references, metric denominators and resume configuration checks.
- `setup-eval.cmd` completed successfully; dependency checking found no broken requirements. The evaluation environment is separate from the application's environment.
- Resuming the completed 12-case scoring run made no new judge calls; the judge-log hash was unchanged. The original 50-question dataset checksum was unchanged.

## Next review step

Use the prefilled human review sheet to inspect the ten generated answers and the two refusals. Have two reviewers independently assess source support, omitted conditions, participant attribution and citation quality; resolve disagreements. Create a new version of the reference set, then rerun scoring. Keep an unexposed set of new questions for final testing. Do not retroactively edit these saved answers or judge logs.

[Setup, commands and metric definitions](../RAGAS_EVALUATION.md)
