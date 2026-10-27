# Next engineering work — 17 October 2026

## 20 October checkpoint

The first bounded quality cycle is documented in [the 19–20 October report](QUALITY_CYCLE_20261019.md). Notification retrieval and repair-input gaps have targeted fixes; three source anchors were recovered without losses in 144 development questions. Alternative coverage reviewers and generation instructions failed the promotion gate. These findings close the evaluated experiments, **not** the broader completeness and answer-quality priorities.

The first live run timed out under GPU contention; the same ten-case repeat after memory became available completed generation without fallback. Next: address material eligibility omissions and source attribution, improve reviewer reliability, then obtain independent answer labels before acceptance scoring. Preserve the existing source/context budgets unless a controlled comparison justifies changing them. Final release verification remains last; GitHub publication remains separate.


The goal remains a dependable payments research assistant before building a business workflow on top. Keep the existing hybrid retrieval, reranker, bounded graph expansion, citations and natural-language answers. Context-enriched lexical retrieval and structured synthesis remain experiments, disabled in the normal flow.

This is a closure plan, not a claim that every item below has been implemented. It separates reproducible engineering work from independent payments review and usability testing.

**18 October update:** the bounded evidence-recovery fixes, targeted checker safeguards, reproducible captures and source-review queue are implemented. The latest full regression passes 375 tests. Source-anchor coverage improved from 208/223 to 212/223 without losses; final answer correctness is not thereby established. See [the closure matrix and records](READINESS_IMPROVEMENTS_20261018.md). Meaning/checker reliability remain partially open, BM25 repeatability alone was tested, and final release verification is explicitly deferred until last. The remainder of this file preserves the original work specification.

## Recommended order

**Later 18 October update:** [the corpus graph candidate and answer fixes](GRAPH_EXPANSION_20261018.md) are implemented and evaluated. Latest full regression: 390 passed. Broader graph activation is deferred for lack of demonstrated gain; the maintained graph stays enabled. The collective tax false acceptance is caught by the narrow category guard, while semantic completeness and unreliable coverage warnings remain open. Final release verification is still last.

| Priority | Demonstrated gap | Work we can do locally | Completion evidence |
|---|---|---|---|
| 1. Evidence coverage | A question about post-debit notification retrieved the pre-debit exemption but missed the indexed post-debit requirement. Another question missed the credit-card-bill row. | Trace which requested facts are missing at candidate search, reranking and bounded assembly. Test focused follow-up retrieval and preservation of relevant table headers/rows. Keep explicit filters and the existing budget. | The missing source passages are recovered on the failing questions and meaningful paraphrases, with no losses on existing controls. Save source and stage traces plus generated answers. |
| 2. Meaning and source ownership | Tests exposed category conflation, comparisons between unlike limits, and a reversed amendment chronology in the experimental synthesis arm. Some baseline answers also make unsupported interpretations. | Add minimal, source-backed regression cases for quantity, category, time and exception ownership. Improve the existing generation/checking path only where a reproducible failure demonstrates the need. Test generic behaviour rather than hardcoding circular answers. | Answers preserve the relevant distinctions and cite their own supporting source; valid answers survive checks. Unsupported conclusions are withheld or qualified explicitly. Review both successful and failed generated responses. |
| 3. Checker reliability | The same model has accepted wrong claims and raised questionable conflict warnings on a correct IPO distinction. | Separate citation validity, claim support and completeness warnings in evaluation. Build a reviewed challenge set containing valid and invalid claims; measure false acceptance and false rejection. Fix demonstrated deterministic defects without weakening numeric/scope checks. | Saved confusion counts against reviewed labels, visible timeout/unavailable states, and no known critical failure in the release regression set. Independent label approval remains a human dependency. |
| 4. Repeatability and performance | Repeated IPO requests preserved core graph evidence but changed lower-priority context near the budget boundary; the cause is not established. | Repeat frozen requests across process restarts, inspect ranking/tie behaviour and stage timings, and change ordering only if the diagnosis supports it. Measure warm/cold median and tail latency separately. | Reproducible source/config/model fingerprints, stable core coverage, explained residual variability and measured latency. Do not attribute variation to a particular component without evidence. |
| 5. Release verification and handoff | The colleague package is frozen at 10 October and predates OCR repairs, main-flow graph integration and recent fixes. Latest full-suite evidence does not replace a complete final-version browser/recovery check. | After quality fixes, rerun the essential browser journeys and offline/recovery paths; restore the repaired corpus in an isolated clean copy; verify index rebuild, activation/rollback and source hashes; refresh portable configuration and handoff documentation locally. | Saved clean-copy and browser records for the same release, including import, source inspection, summary, comparison, export and clarification continuation. The original installation stays intact. Publishing remains separate and is not authorized by this plan. |
| 6. Source-review queue | Sampled OCR corrections do not validate the entire collection. Dates, missing sources and proposed graph relationships still need review. | Produce a risk-ranked queue for amounts, table headers, response codes, dates, missing amendments and stale graph anchors. Compare available originals and retain before/after hashes for confirmed corrections; rebuild only changed embeddings. | Every correction has inspectable original evidence; uncertain or unavailable material remains flagged. Independent authority/applicability judgements cannot be automatically signed off. |

Start with priorities 1–3 as one bounded quality cycle. Gate any change on unchanged or improved source coverage, preserved valid answers and targeted generated-answer review. Then perform repeatability and release verification. Keep the source queue active without blocking all work on full-corpus review.

## What is already done

- Document intake has staging, provenance, quality triage, embedding reuse, candidate validation, activation and rollback. It is not an unattended website-monitoring service.
- The repaired `payments-ocr-audit-20261015` corpus is active. The sampled audit made source-confirmed corrections and recomputed affected embeddings; it was not a full-library certification.
- Bounded graph assistance is in the main flow. Its curated families improve development-set evidence coverage; it is not an automatic legal-precedence engine.
- The reported empty IPO answer has a documented scope/citation fix and final API/browser evidence. Broader interpretation quality is still open.
- The 17 October full Python regression passed **365 tests**; the 18 October run passed **375**. This establishes tested software behaviour, not answer accuracy.
- A 20-case generated-answer run did complete on 11 October; a later 20-case attempt stopped after ten responses. Neither is a complete final-version answer-quality acceptance run. Do not keep reporting the first run as never executed, or the interrupted later run as complete.
- A clean-copy setup/source restore was checked for the historical 10 October package. That check explicitly did not rebuild the full vector index and does not cover the current repaired release.

## Review dependencies, distinct from user testing

**Independent payments review:** approve source interpretations and expected answers, resolve disputed applicability, and review a held-out question set. Automated/RAGAS scores can assist but cannot supply independent ground truth. Agree acceptance thresholds before scoring the held-out set, and report incorrect answers, incomplete answers, false abstentions and latency separately.

**Colleague usability testing:** observe real research tasks, source inspection, corrections and time taken. This is separate from verifying whether an answer is correct.

**Deployment decision:** localhost remains the current boundary. Authentication, uploaded-document access controls and shared-service operations become a separate workstream only if shared hosting is chosen.

Do not treat larger models, larger embeddings, more context, fine-tuning or a new database as automatic next steps. The current findings first justify fixing coverage and interpretation within the existing flow. Full experimental contextual retrieval and structured synthesis are deferred until they demonstrate a repeatable benefit without material regressions.

## Evidence

- [Larger 138-case contextual retrieval check and decision](CONTEXT_RETRIEVAL_DECISION_20261017.md)
- [Expanded paired experiments and answer failures](EXPANDED_EVIDENCE_EVALUATION_20261017.md)
- [IPO regression and final verification](IPO_REGRESSION_20261017.md)
- [Graph integration](GRAPH_INTEGRATION_20261016.md)
- [Intake triage and experiments](EVIDENCE_IMPROVEMENTS_20261016.md)
- [Historical completed 20-case generation](../evaluation/payments_runs/20261011T140941246919Z/summary.md)
- [Historical clean-copy limitations](../handoff/VALIDATION.md)
- [Independent review procedure](HUMAN_REVIEW_GUIDE.md)
