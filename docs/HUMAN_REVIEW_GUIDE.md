# Independent review and release decisions

The intended behaviour is to answer a clear, supported question, ask for a necessary clarification, or explain why evidence is insufficient. A clarification is not automatically a failure. A fluent cited answer is not automatically a success.

## Review a saved run

1. Open the run's `human_review.csv` and `capture.json`. Keep the original capture unchanged. Save completed worksheets under a new reviewer/version name.
2. Read the question before reading the AI-assisted reference. Decide whether product, participant, document identity or date is materially ambiguous.
3. Verify the relevant original sources, including tables, exceptions, amendments and extraction gaps. Indexed text alone does not establish source accuracy or current applicability.
4. Check the draft reference. Record corrections rather than treating the reference as ground truth. If it changes, create a new dataset version; preserve the frozen original for historical comparisons.
5. Review the displayed answer, its source excerpts and any withheld statements. Enter your name, source verification, correctness, completeness and citation support in the worksheet. In notes, record the classification below and any missing central answer.

## Outcome classifications

| Classification | Expected behaviour |
|---|---|
| Clear and answerable | Direct answer with supporting sources and essential qualifications. |
| Product ambiguous | Short clarification with usable choices; preserve the original question after selection. Example: Tap & Pay without UPI/RuPay context. |
| Reference ambiguous | Show matching documents and request selection; never silently pick a year/version. |
| Evidence unavailable | Say what could not be established. Do not invent internal policies, missing clauses or future revisions. |
| Evidence partial | Identify the missing requested fact or qualification; background alone must not look like a complete answer. |
| Sources differ in scope | Preserve the separate entities, channels, products and dates; do not merge them into a universal rule. |
| Model/checker unavailable | Clearly return source access or an incomplete result. Do not count fallback as a successful neural benchmark. |

A question whose reference is ambiguous can legitimately request clarification even if its current provisional dataset entry is marked positive. Record that disagreement for dataset review; do not silently relabel it to improve scores.

## Questions for every answer

- Does it answer the main question, rather than merely discuss the topic?
- Are the number, unit, entity, action, date and exception supported together?
- Does each citation support its attached statement?
- Does a missing quote or reviewer timeout incorrectly remove an otherwise supported central answer?
- Does the answer claim completeness or current applicability beyond the available evidence?
- Would a payments colleague know the next useful action: use the answer, inspect the source, clarify, or obtain another document?

Have a second reviewer assess all critical disagreements and a sample of the remaining cases. Record both judgements and the resolution. Automated models cannot supply human reviewer names or complete this independent-review step.

## Shipping gates

Before describing the application as ready for external operational use:

1. Close reproducible routing, citation and answer-handling failures, and test both clarification choices, summaries, comparisons, import, activation, rollback and export.
2. Agree numerical quality and latency targets before the final test. Evaluate on independently reviewed questions that were not used for tuning; report scored, failed, skipped, clarified and abstained cases separately.
3. Review the sources used by that benchmark and record unresolved extraction/date/applicability gaps.
4. Have colleagues complete real research tasks and record corrections, completion and time taken.
5. Verify a clean installation, restore and full embedding build on a colleague's machine.
6. Decide the deployment boundary. This implementation is a localhost application. Shared/public hosting requires a separate assessment of authentication, access to uploaded documents, isolation, retention, backups, monitoring and operational ownership.

Current automated checks support continued local testing. Independent source/answer review, held-out acceptance and colleague validation remain explicit release gates, not completed claims.
