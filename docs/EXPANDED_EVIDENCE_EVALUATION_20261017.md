# Additional contextual retrieval and structured synthesis evaluation

## Question and design

Does either optional feature improve this project's actual research flow enough to justify activation? Final answers must answer the question naturally, preserve important qualifications and cite the source that establishes each claim.

The new frozen [28-case set](../evaluation/expanded_evidence_cases_20261017.json) contains paraphrases of 20 mixed-payments cases plus eight graph-family cases. Many questions remove circular identifiers or original terminology. The 56 reference anchors are inherited from existing source-backed cases and validated against the active corpus before each run. Three questions ask for private company information absent from this public corpus. The [casebook](../evaluation/EXPANDED_EVIDENCE_CASEBOOK_20261017.md) records the question, parent case and reference passages.

This is an AI-assisted development set, not a newly independent benchmark. Rephrasing known cases does not make them held-out. Reference lists may be incomplete; absence of a proposed anchor does not automatically mean an answer is wrong.

Context comparison: baseline versus metadata-enriched BM25 inside the normal hybrid/reranked/graph flow, followed by a BM25/no-reranking diagnostic. Both use the normal auto route and unchanged context budget, source snapshot, embeddings and graph. Record initial top-six anchor retrieval separately from final assembled evidence. Initial search is not the complete multi-stage candidate pipeline; graph, follow-up and surrounding passages may recover material it misses. Existing selected-document summary/comparison bypasses cannot establish a ranking improvement.

Synthesis comparison: selected new cases and repeated earlier diagnostic cases, with retrieved sources and traces frozen identically for each baseline/structured pair. Alternate execution order. Keep the same Qwen 3.5 9B model, 16K context, output cap, claim checks and repair rules. Record generated text, withheld claims, review failures, citations and latency. Internal evidence records never directly become answer blocks.

Each run preserves configuration, dataset/source/code/model fingerprints. The runner now includes graph and source-quality inputs in its code/input record. No experiment mutates the active configuration or corpus. Latency observations are local single-run measurements; they are not statistically established speed differences. Same-model checks and this AI-assisted review do not substitute for an independent payments reviewer.

## Results and decision

**Decision: keep both experiments off in the main app. Keep graph-assisted retrieval enabled, but do not describe the overall system as ready to ship.** The wider tests reveal answer failures that retrieval-anchor scores and same-model support checks do not capture. The user's reported IPO failure is a separate regression in deterministic scope validation; see the [investigation](IPO_REGRESSION_20261017.md).

| Controlled comparison | Baseline | Experimental arm | Meaning |
|---|---:|---:|---|
| Hybrid + reranker: final evidence anchors | 46/56 | 46/56 | No aggregate gain; gains on two questions offset two lost anchors on another |
| Hybrid: all reference anchors found for a positive question | 17/25 | 19/25 | More complete reference coverage on some questions, but one capital-requirement case worsens |
| Hybrid: initial top-six search anchors | 35/56 | 36/56 | Small initial-ranking change; this is not the full pipeline |
| BM25 without reranking: final evidence anchors | 35/56 | 39/56 | Encouraging for keyword fallback; downstream graph/context assembly remains active |
| BM25: all anchors for a positive question | 12/25 | 16/25 | Four question-level gains in this development sample |
| Fourteen fixed-evidence generated answers: status-labelled incomplete | 2/14 | 2/14 | Equal status counts conceal materially different answer problems |
| Generated private-information negative case | Abstained 1/1 | Abstained 1/1 | One successful negative observation, not general reliability |

An **anchor** is a predefined document/page/quote reference, not a question or an independently verified fact. One question can require several anchors. The retrieval set contains 28 questions: 25 positive and three negative, with 56 anchors across the positive questions. The synthesis subset contains 14 questions: 13 positive and one negative, with 29 reference anchors; both arms receive identical retrieved evidence containing 24 of those anchors. That identical retrieval count says nothing about which synthesis is better.

All three negative retrieval cases returned neighbouring passages in both arms. Evidence retrieval does not itself establish abstention; only the separately tested generation negative case abstained. No claim of safe negative handling should be inferred from non-empty search results or the one successful generated negative.

Local median times: hybrid retrieval **1.44 → 1.48 seconds**, BM25 **0.071 → 0.071 seconds**, and generated answers **18.60 → 19.30 seconds**. These are single runs on this laptop with the existing models; they do not establish a statistically significant latency difference. Initial top-six diagnostic searches are timed separately and excluded from pipeline time.

## Answer review: why the experiments are not promoted

The [case-by-case review](../evaluation/expanded_review_20261017/ANSWER_REVIEW.md) examines all 14 pairs against captured source passages. It is an AI-assisted review, not independent evaluation and not an answer-accuracy percentage.

- **Incorrect exemption transfer, both arms (X-PAY-015):** answers incorrectly extend a pre-debit notification exemption to the message after debit. The retrieved RBI excerpt concerns pre-transaction notification. Section 7 of the indexed source explicitly requires post-transaction notification but was not retrieved. Both wrong answers passed the same-model support check. This is both a retrieval coverage failure and an unsupported inference.
- **Reversed amendment chronology, structured arm (X-DD-01):** the generated answer says codes 59/K1 were included before the addendum and excluded afterwards. The captured sources state the opposite. The baseline retains the later inclusion but withholds the earlier exclusion. Structured synthesis and its repair/checking stages are not reliable on this case.
- **Unsupported reconciliation (X-PAY-012):** the structured answer calls older issuer-only onboarding consistent with newer third-party discovery without establishing that reconciliation. The baseline also needs caution about differing channels and versions. Neither justifies a blanket supersession claim.
- **Quantity mismatch (X-PAY-011):** the baseline juxtaposes a single-payment limit with a monthly transfer limit. The structured arm withholds a problematic comparison. An incomplete status can reflect a useful safeguard, not simply worse quality.
- **Missing evidence (X-LIMIT-03):** both arms miss the credit-card-bill limits required by the question. Better synthesis cannot recover an absent rule safely.
- **Useful but limited observations:** structured synthesis is more focused on alternative authentication (X-PAY-005); both arms distinguish balance versus transaction limits, reproduce the biometric limit change, and distinguish IPO/RDS purpose codes in their captured responses. These successes do not cancel the failures above.

The structured experiment adds verbatim records, not a verified rule engine. It can still change the model's attention, conflate historical and operative text, or generate an unsupported conclusion. Valid citations, unchanged fingerprints and a completed run are not proofs of correctness.

## Saved evidence and reproducibility

| Run | Saved capture |
|---|---|
| Hybrid/context, 28 paired cases | [20261017T023947481452Z](../evaluation/improvement_runs/20261017T023947481452Z/capture.json) |
| BM25/context, 28 paired cases | [20261017T024135344737Z](../evaluation/improvement_runs/20261017T024135344737Z/capture.json) |
| Broader synthesis, 14 paired cases | [20261017T024213481303Z](../evaluation/improvement_runs/20261017T024213481303Z/capture.json) |
| Six earlier diagnostics, after reference/OCR guard fixes and attribution instruction | [20261017T072925288317Z](../evaluation/improvement_runs/20261017T072925288317Z/capture.json) |

The six-case rerun had 12/12 identical evidence anchors, one negative abstention in each arm, and no status-labelled incomplete answers. Median times were 22.71 seconds baseline and 19.99 seconds structured. **That is not six correct answers.** Review found an unsupported baseline summary inference (“beyond which” authentication may be required) and a structured tax answer that incorrectly describes the Government e-Market Place row as Tax Payments. The baseline tax answer also overgeneralises the original OC185's scope. Both comparison answers keep the original NFC and later device-lock requirements separate in this run. The baseline IPO answer distinguishes OC185B's cumulative measure from OC127's specific rule after repair; the structured IPO answer distinguishes the columns but does not reproduce the full earlier history.

The summary finding exposed a missing phrase in the existing above-ceiling guard. `beyond which` now receives the same guard treatment as `above which`, with a regression check preserving explicitly supported above-ceiling rules. Final live verification is separate from this earlier run. The category conflation and broader semantic failures remain release blockers; they were not removed from the report or labelled successful because the model accepted them.

All three completed runs report unchanged recorded inputs, no execution errors and no model fallback. An earlier interrupted run, `20261017T023727426194Z`, is retained but excluded: Windows temporarily blocked atomic checkpoint replacement. A bounded retry and regression tests now cover that writer failure. It was not an answer-quality result.

```powershell
.\.venv\Scripts\python.exe -X utf8 evaluation/evidence_experiments.py --kind context --dataset evaluation/expanded_evidence_cases_20261017.json
.\.venv\Scripts\python.exe -X utf8 evaluation/evidence_experiments.py --kind context --dataset evaluation/expanded_evidence_cases_20261017.json --method bm25 --no-rerank
.\.venv\Scripts\python.exe -X utf8 evaluation/evidence_experiments.py --kind synthesis --dataset evaluation/expanded_evidence_cases_20261017.json --ids X-PAY-001,X-PAY-002,X-PAY-005,X-PAY-006,X-PAY-009,X-PAY-011,X-PAY-012,X-PAY-015,X-PAY-016,X-PAY-018,X-BIO-01,X-DD-01,X-LIMIT-03,X-IPO-04
```

Rerunning after code changes creates a new timestamped experiment; it does not recreate the historical code automatically. Compare saved code hashes as well as configuration, corpus and dataset fingerprints. Run model experiments serially and avoid concurrent interactive model usage when measuring latency.

## Next release gate

1. Close the exact IPO failure with spelling/attribution regression checks and live verification; retain failed attempts.
2. Improve evidence coverage for contrasting conditions and check temporal/scope contradictions using the failures above as development cases. Require source-specific support rather than inferring that an omitted rule does not exist.
   Also investigate repeatability: two later UPI-filtered live captures retained the same core graph passages but selected different lower-priority passages near the context boundary. Their generated wording changed. The paired synthesis experiments freeze evidence specifically to avoid attributing that difference to synthesis. The cause of this cross-run tail variation has not been isolated.
3. Have a payments reviewer assess correctness, material completeness and citation ownership on a fresh held-out set. Keep automated retrieval, answer quality and latency measures separate.
4. Retest contextual retrieval only after addressing its lost capital-requirement anchors; consider the keyword-fallback use case separately. Revisit structured synthesis only if its chronology and scope failures are resolved without degrading controls.

The graph overlay was verified active through the running app. It remains bounded to the source-anchored pilot families, with independent relationship review pending; it is neither a universal knowledge graph nor a guarantee that the generator interprets retrieved evidence correctly.
