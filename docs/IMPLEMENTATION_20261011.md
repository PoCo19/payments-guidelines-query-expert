# Reliability cycle — 11 October 2026

Historical status at the time of this note: implementation and full regression rerun complete; final generation evaluation and remaining browser checks pending. This is not a production-readiness certification.

**17 October reconciliation:** a [20-case generated-answer run](../evaluation/payments_runs/20261011T140941246919Z/summary.md) subsequently completed, followed by five targeted cases. A later 20-case attempt (`20261011T142301206921Z`) stopped after ten responses and is not a completed run. Newer code has a 365-test regression record and targeted browser/API verification, but still needs final-version answer-quality acceptance and the complete release journey check. Use [current priorities](NEXT_ENGINEERING_PRIORITIES_20261017.md); the pending statements below retain the original chronology.

## Intended behaviour

A clear, supported question should receive a direct answer with evidence and necessary conditions. A materially ambiguous question should receive a useful clarification, not a guess. An unavailable or incomplete source should produce an explicit limitation. Asking users to clarify genuine ambiguity is expected behaviour; poor retrieval for a clear question is a system issue.

## Implemented changes

- **Clarification:** an unqualified Tap & Pay question offers UPI and RuPay choices and preserves the original question on resubmission. Explicit product choices and comparisons bypass this single-product question. The interaction vocabulary is configurable in `query_policies.json`; it is a reviewed policy, not a general ambiguity detector.
- **Reference resolution:** distinctive title wording can resolve otherwise repeated circular numbers. Ties remain visible. A product term in a research question helps identify a named document without excluding complementary sources from the rest of the library. Explicit filters and document selections remain boundaries.
- **Cross-document research:** naming a circular no longer restricts related research exclusively to that document. Automatic comparisons can retrieve a direction or topic without requiring two numbered circulars. This ranked comparison is explicitly partial; it is withheld when fewer than two documents or a named product side are represented. Representation alone does not prove sufficient evidence for both sides.
- **Retrieval:** the balanced seed policy protects the first lexical candidate and first two original candidates from being entirely discarded by the reranker. The final context remains within the existing character budget. Candidate ordering and protected IDs are recorded. There are no RBI/NPCI retrieval quotas. `retrieval_seed_policy: rank_only` retains the earlier selection for controlled experiments.
- **Claim support:** the checker selects stable excerpt IDs; the application copies the corresponding exact source text. This avoids requiring the model to reproduce quotes byte-for-byte. Unknown IDs, semantic rejection and unsupported numbers still withhold claims. The checker uses the same local model and is not independent verification.
- **Incomplete answers:** the generator identifies central-answer claims. If support checks remove one, the remaining background is labelled incomplete. This depends on the generator identifying central claims correctly; it is not an independent answer-completeness guarantee.
- **Evaluation:** the capture runner supports explicit method, reranking, automatic routing and product-filter overrides. It fingerprints code as well as sources, configuration and dataset. Model fallbacks invalidate a neural benchmark instead of being counted as successful model execution. Clarification, incomplete results and fallbacks are reported separately.

## Observed checks

| Check | Result | Limit |
|---|---|---|
| New reliability regressions | 15 passed | Synthetic fixtures; no accuracy claim |
| Full Python regression rerun | 275 discovered: 271 passed, four skipped, zero failures; 12.949 seconds | Four optional RBI HTML-conversion tests require the uninstalled `lxml` dependency |
| JavaScript rendering/export tests | Both suites passed | Existing renderer checks |
| Frontend syntax check | `node --check web/app.js` passed | Syntax validation only |
| Browser clarification | Product choices displayed; UPI choice preserved the question and retrieved filtered excerpts | RuPay continuation and final full journey rerun pending |
| Original 50-question retrieval regression | 55/55 anchors; 44/44 positive cases had all anchors; 5/6 negatives returned no evidence; zero request errors/fallbacks | Explicit UPI filter, evidence mode, automatic route; no new answer-correctness measurement |
| Mixed-source development retrieval | 26/34 anchors; 12/17 positive cases had all anchors; one ambiguous-reference clarification; zero request errors/fallbacks | Known development set, not held out; all three negatives returned candidate evidence |

The original 50 questions contain 44 positives with 55 total evidence anchors and six negatives. A question may require several anchors. An evidence-mode negative that returns passages must still be checked for generated-answer abstention; retrieval alone cannot establish safe answer behaviour.

The prior 10 October generation run found 18/34 anchors. The new 26/34 result also changes routing from the frozen cases' clause override to the normal automatic route, so it is a combined development improvement, not an isolated reranker comparison or answer-accuracy score.

Within this cycle, live hybrid retrieval with the earlier seed selection found 23/34 anchors, versus 26/34 with protected seeds. This is a single development-set observation. All eight missing anchors remain findings, including two in a legitimately ambiguous reference case; the frozen dataset has not been relabelled to improve the score.

## Saved evidence

The completed full-suite rerun is recorded in [validation.json](../evaluation/validation_runs/20261011T132442574976Z/validation.json), with the [raw Python test output](../evaluation/validation_runs/20261011T132442574976Z/python-tests.txt), code fingerprints and JavaScript check outcomes. Automatic approval succeeded on the retry; the earlier approval-service blockage is resolved for this run. No implementation fixes were needed after the suite passed.

All paths below are relative to `evaluation/payments_runs/` and contain `capture.json`, `summary.md` and an uncompleted human review worksheet:

| Run | Purpose | Status |
|---|---|---|
| `20261011T070105578877Z` | BM25 without reranking, auto route | Source-only baseline, 23/34 anchors |
| `20261011T070134423601Z` | Intended hybrid with reranking | Ollama was stopped; fallback run, exclude from neural comparisons |
| `20261011T070305022587Z` | Intended hybrid without reranking | Ollama was stopped; fallback run, exclude from neural comparisons |
| `20261011T070417260677Z` | Live hybrid without reranking | 23/34 anchors |
| `20261011T070523145488Z` | Live hybrid with earlier seed selection | 23/34 anchors |
| `20261011T070604612459Z` | Live vector without reranking | 24/34 anchors |
| `20261011T070718364637Z` | Hybrid with balanced seeds | 26/34 anchors |
| `20261011T071243742098Z` | Original 50, explicit UPI, auto route | 55/55 anchors |

The first outage captures predate the benchmark-validity guard. Their historical completion label does not make them valid neural benchmarks. Preserve the raw files and use the classifications above.

The balanced 20-case capture precedes the final missing-product comparison guard and trace-field changes; the original-50 capture uses those changes. Final code must receive a fresh generation run before closing this cycle.

## Reproduction

With the active corpus, pinned local models and reranker installed:

```powershell
.\.venv\Scripts\python.exe -X utf8 evaluation/payments_eval.py --mode generate --route auto --method hybrid --rerank
.\.venv\Scripts\python.exe -X utf8 evaluation/payments_eval.py --dataset evaluation/rag_cases.json --series UPI --mode evidence --route auto --method hybrid --rerank
.\.venv\Scripts\python.exe -X utf8 -m unittest discover -s tests -v
```

These commands describe how to reproduce checks; the first command has not yet completed for this revision. Source/configuration/dataset hashes and model digests are stored in each capture. The default balanced policy is defined by the recorded code version and appears in the retrieval trace.

## Remaining work before closing this cycle

1. Run and inspect all 20 mixed-source generated answers, including central-answer retention, false positives, legitimate clarification and checker failures. Also run the original-50 negative case that still retrieved passages. Save failures and timings.
2. Verify the RuPay clarification continuation and refresh the end-to-end browser checks on the final backend.
3. Review remaining retrieval failures, then decide which need a fix and which require source or dataset review. Do not tune away findings by silently changing references.
4. Complete independent source/answer review, held-out acceptance and colleague trials before an operational release. Use [the human-review guide](HUMAN_REVIEW_GUIDE.md). Run the four optional HTML-conversion checks in an environment with `lxml` before relying on that acquisition helper for a new capture.

No model upgrade, corpus migration or new embeddings were required for these changes. The existing `handoff-2026-10-10.1` tag remains the frozen colleague release. This reliability cycle has not been committed or pushed, and no new release is declared.
