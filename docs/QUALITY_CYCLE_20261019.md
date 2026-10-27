# Answer quality cycle — 19–20 October 2026

This work addresses observed evidence misses and answer-review failures. It does not change the source corpus, embeddings, model sizes or context budgets. The maintained UPI graph remains enabled; the broader corpus graph, contextual BM25 and structured synthesis remain disabled.

## Diagnosed failures

**Notification evidence was demoted, not absent from the index.** The FASTag question about a message after debit found the RBI pre-transaction clause in the hybrid candidate set, but reranking preferred several more product-specific NPCI passages. The selected context then lacked the RBI clause and its neighbouring post-transaction requirement. This is distinct from unavailable source material or missing embeddings.

**Reviewing an answer can introduce new mistakes.** Existing coverage review sometimes calls a correctly explained amendment a conflict, invents an omitted condition that the answer already states, or transfers a table category using its shared merchant code. Conversely, the credit-card-bill answer really did omit the Verified Merchant condition. Reducing warning counts alone is therefore not a success criterion.

**Source attribution remains difficult.** A later circular describing an earlier enhancement must not automatically be described as having introduced that enhancement itself. An accepted claim-check verdict does not establish that this distinction is correct.

## Changes and boundaries

Notification recovery protects at most two already-retrieved candidates that have a notification-phase heading and share a distinctive topic term with the question. An adjacent requested phase can then be included from the same document. This preserves filtering, original source text and the existing passage/character budgets. No publisher quota, circular-number answer or monetary value is encoded in this rule. Candidate protection is a retrieval heuristic, not a determination of legal applicability.

Attribution repair now requests a fresh, source-specific correction instead of copying a failed collective attribution. Notification repair preserves up to two matching phase passages from the same cited document, within its existing six-excerpt cap. It repairs the missing rule rather than repeating background already accepted in the answer. Every repair still passes the existing citation, numeric, scope and model support checks; the attempt/time limits remain unchanged. The audit records which excerpts the repair actually received.

Final review found that simultaneous phase and scope failures could remove the same prompt field twice and skip the repair attempt. A failing regression reproduced this; safe field removal corrects it without changing either check. The live ten-case run below preceded only this defensive fix; its exact code fingerprint remains in the capture.

The coverage-review candidate is **experiment-only**, in `evaluation/coverage_candidate.py` and `evaluation/coverage_review_candidate.py`. It keeps source chunks intact, asks for concrete corrections, and tests a second reading of proposed warnings. It is not imported by the application. The original reviewer remains in the normal flow. Failures are retained in the experiment captures; an empty warning list must not be interpreted as proof of completeness.

## Evaluation and review

Every question set in this cycle is AI-assisted development material, awaiting independent review. None is a held-out acceptance benchmark. Source-anchor retrieval, generated-answer quality, warning reliability and latency are different measurements.

### Paired retrieval: same corpus, settings and models

| Development set | Questions | Previous selection | Notification recovery |
|---|---:|---:|---:|
| Existing regression | 138 | 212/223 anchors | 212/223 anchors |
| Additional RBI/mixed paraphrases | 3 | 3/5 | 5/5 |
| New notification paraphrases | 3 | 5/6 | 6/6 |
| **Total** | **144** | **220/234** | **223/234** |

There were three gains, no lost anchors, no execution/model fallbacks, and no context-budget violations. The denominator is expected source passages, not questions: one question can require several passages. Eleven anchor misses remain. The comparison isolates `phase_matches`; both arms retain the maintained graph and exclude the broader candidate.

The 120 reranked routes changed from 197/209 to 200/209 anchors; the 24 routes bypassing reranking remained 23/25. The 24 negative/control cases retained their outcomes: eight empty abstentions, two clarifications and fourteen results containing source excerpts. These are evidence-mode outcomes, not a successful-generation-abstention score. Median request times were 1.562 and 1.508 seconds, with p95 2.422 and 2.469 seconds respectively; this mixed-route warm run does not establish a latency improvement or cold-start performance.

### Controlled repair

The frozen tax failure now produces a source-specific correction distinguishing the tax addendum from the hospital/education circular. Another tax repair varied between runs in both arms; do not infer deterministic answer accuracy from one accepted response.

The frozen notification failure exposed a second bottleneck: the post-transaction rule was retrieved but excluded from the repair model's first six excerpts. The new selection and narrower repair recover the missing post-transaction requirement, and the existing support checks accept it. Intermediate failed repairs, including unnecessary and inconsistent inline references, are preserved.

### Final live run: generation verification did not pass

The ten-case capture found **19/19 expected source anchors**, but **six requests timed out** and returned the explicit model-unavailable fallback. Two requests produced drafts (summary and comparison), one nonexistent reference abstained, and one ambiguous reference requested clarification. The comparison's coverage review also timed out. The unrelated-topic negative case is among the model timeouts; it must not be counted as a successful semantic abstention.

A subsequent read-only GPU check found almost-full GPU memory and a game resident alongside both Ollama models. This is a plausible contributor, not an isolated causal measurement. The saved median of 63.719 seconds and p95 of 64.953 seconds reflect this unsuccessful run and must not be advertised as representative performance. This prompted the repeat described below; the failed run alone supports no generation-quality or normal-latency conclusion.

The [raw run](../evaluation/quality_runs/20261020T072515613851Z/capture.json), [summary](../evaluation/quality_review_20261019/final_live_summary.json), [GPU snapshot](../evaluation/quality_review_20261019/gpu-load-20261020.txt) and [blank independent-review worksheet](../evaluation/quality_review_20261019/human_review_final.csv) are retained. This is a failure finding, not a release pass.

### Repeat after GPU memory became available

After the user agreed to close the game, the GPU snapshot showed approximately 4.96 GB free and 0% utilisation before the run. The process still appeared in the process list, so this is an observed reduction in contention, not a certified isolated-hardware benchmark.

The final-code [ten-case repeat](../evaluation/quality_runs/20261020T073818315407Z/capture.json) found **19/19 anchors with no generation fallbacks**. Both negative cases abstained and the ambiguous reference requested clarification. Median total request time was **18.594 seconds**, p95 **33.828 seconds**, across all ten routes including immediate abstention/clarification. Do not compare this mixed-route timing with generation-only throughput.

Notification repair successfully replaced the wrong post-debit exemption with the post-transaction requirement. However, this was **not a complete answer-quality pass**:

- The credit-card-bill answer still omitted the merchant eligibility condition.
- The tax answer retained questionable collective source attribution; a separate misleading cumulative-tax claim was withheld.
- The IPO answer distinguished cumulative and per-transaction limits but omitted earlier mandate-specific history even though its source was retrieved.
- Four coverage reviews were unavailable: two timed out and two produced invalid single-passage conflict findings. Other warnings also contained questionable reasoning.

See the [case-by-case observations](../evaluation/quality_review_20261019/rerun_live_summary.json) and [new independent-review worksheet](../evaluation/quality_review_20261019/human_review_rerun.csv). These observations are AI-assisted development review, not independent source verification or a numerical correctness score.

### Experiments not promoted

Keeping chunks intact did not by itself make coverage review reliable. A second model reading removed some false warnings but also dismissed a real missing eligibility condition. Requiring an exact answer quotation did not establish semantic correctness. These variants remain experiment-only.

The additional **ten-case frozen coverage challenge is now complete** (20 reviewer responses). The first resource-contended attempt is retained separately. The completed [capture](../evaluation/quality_runs/20261020T124418596737Z/capture.json) and [summary](../evaluation/quality_review_20261019/coverage_challenge_summary.json) show:

| Provisional development-label group | Normal reviewer | Experimental reviewer |
|---|---:|---:|
| Five answers with a material gap: any warning raised | 4/5 | 1/5 |
| Five answers with a material gap: no warning raised | 0/5 | 4/5 |
| Five answers labelled complete: any warning raised | 5/5 | 1/5 |
| Reviewer unavailable | 1 (gap case) | 0 |

The experimental reviewer reduces warnings on complete answers but misses four of five labelled gaps. The normal reviewer over-warns and has one unavailable result. Neither is established as reliable. These counts compare warning presence against **AI-assisted, provisional labels**; they do not score whether each warning's reasoning is correct and are not independent accuracy figures. The candidate remains outside the application.

Additional generation instructions also failed the promotion gate: the four-case paired run still omitted the merchant restriction and introduced worse wording in the deemed-debit and IPO answers. **The application's generation prompt and coverage reviewer remain unchanged.** More instructions and another model call are not automatically improvements.

Independent review should inspect the question, original source, actual answer, withheld claims and warning proposals. The reviewer worksheet leaves all judgements and reviewer identity blank. The [review guide](HUMAN_REVIEW_GUIDE.md) defines the criteria and release dependencies.

Final browser/recovery/clean-install verification remains the last release step. GitHub publication is separate. No shipping-readiness or full-corpus source-accuracy claim is made by this cycle.

## Evidence and reproduction

- [Full paired retrieval capture](../evaluation/quality_runs/20261019T181403217201Z/capture.json) and [route-separated summary](../evaluation/quality_review_20261019/retrieval_summary.json).
- [Earlier five live answers, including the still-incomplete notification answer](../evaluation/quality_runs/20261019T181209842063Z/capture.json).
- [Tax and notification repair comparison, 20 October](../evaluation/quality_runs/repair-20261020T072215379338Z/capture.json).
- [Final frozen notification repair](../evaluation/quality_runs/repair-20261020T072419482924Z/capture.json).
- [Generation instruction experiment](../evaluation/quality_runs/generation-20261019T182137210890Z/capture.json) and [decision](../evaluation/quality_review_20261019/generation_experiment_decision.json).
- [Coverage variant with intact chunks](../evaluation/quality_runs/20261019T180515147325Z/capture.json), [narrower instruction](../evaluation/quality_runs/20261019T180722082988Z/capture.json), [second reading](../evaluation/quality_runs/20261019T180911848194Z/capture.json), and [exact-answer-quotation variant](../evaluation/quality_runs/20261019T181023948077Z/capture.json).
- [Provisional coverage challenge labels](../evaluation/coverage_cases_20261019.json).

```powershell
.\.venv\Scripts\python.exe -X utf8 evaluation/quality_cycle.py --mode retrieval --dataset evaluation/context_regression_20261017.json --dataset evaluation/reference_graph_rbi_cases_20261018.json --dataset evaluation/notification_paraphrases_20261019.json
.\.venv\Scripts\python.exe -X utf8 evaluation/repair_replay.py
.\.venv\Scripts\python.exe -X utf8 evaluation/quality_cycle.py --mode coverage --coverage-cases evaluation/coverage_cases_20261019.json
```

Each run writes a new timestamped capture with configuration, source/code fingerprints and installed model identities. Frozen input captures and pre-change modules are retained. The four early coverage experiments record hashes and outputs of intermediate variants; only the final experiment code is retained as a directly rerunnable candidate. No claim is made that an intermediate prompt version can be recovered from its hash alone.


## Closure and next action

**Completed:** the bounded production fixes, the 144-question paired retrieval comparison, frozen repair checks, the unsuccessful generation-instruction and coverage-review experiments, the ten-case live capture, and final software checks. All **399 Python tests** pass after the combined-reason fix; all three JavaScript suites pass. See the [test log](../evaluation/quality_review_20261019/regression-tests-closed.txt), [frontend record](../evaluation/quality_review_20261019/frontend-tests.txt), and [final hashes and closure manifest](../evaluation/quality_review_20261019/closure_manifest.json). Production changes relative to the pre-cycle snapshot are limited to `adaptive_context.py`, `evidence_focus.py`, and `claim_repair.py`. The original application generation prompt, support checker and coverage reviewer are unchanged.

**Also completed after GPU contention cleared:** the final-code ten-case live repeat and the ten-case paired frozen coverage challenge. Both have unchanged-input fingerprints and saved outputs. Generation completed without fallback on the repeat, but this does not close the answer-quality acceptance gate. The [interrupted challenge attempt](../evaluation/quality_runs/20261020T073307070766Z/capture.json) and failed live run remain as historical findings. No user application was stopped by this task.

**Still open:** material eligibility omissions, source-establishment attribution, lost historical detail in synthesis, remaining retrieval misses, and unreliable completeness warnings. Prioritise those demonstrated defects next, obtain independent payments review, then perform final browser/recovery/clean-copy release verification last. Do not increase model size or response budgets as an untested workaround. The running frontend was not restarted by this cycle; it must be relaunched to load changed Python modules. No GitHub push was made.

```powershell
.\.venv\Scripts\python.exe -X utf8 evaluation/quality_cycle.py --mode generate --ids X-LIMIT-03,G-DD-01,G-LIMIT-04,G-IPO-02,RBI-REF-03,RAG-037,RAG-043,RAG-045,RAG-048,G-CTRL-01
.\.venv\Scripts\python.exe -X utf8 evaluation/quality_cycle.py --mode coverage --coverage-cases evaluation/coverage_cases_20261019.json
```
