# Speaker notes: slides 8–12

**Presentation:** Payments_Guidelines_Query_Expert_v3.pptx
**Audience:** Midterm capstone evaluators
**Delivery:** Approximately 4–5 minutes at a measured pace, including slide transitions. Notes follow the supplied v3 deck; the slide file has not been changed.

## Slide 8 — Preliminary retrieval evaluation

We first evaluated whether the system could find the evidence needed to answer a question. We compared keyword search, vector search, hybrid search, and hybrid search with reranking, using the same 50 questions and corpus.

Of those 50 questions, 44 were expected to have supporting evidence and six were negative cases. Some questions needed two passages, giving us 55 expected evidence matches in total.

All four methods found those 55 matches. BM25 returned no evidence for all six negative cases; the other methods returned irrelevant evidence for one case. Adding reranking increased median retrieval time from 78 to about 161 milliseconds without improving this coverage measure.

This makes BM25 a useful baseline, but does not prove it is always the best method. Many questions name the circular directly, and summary and comparison routes bypass reranking. These results measure evidence retrieval, not answer correctness. That brings us to our answer-quality pilot.

## Slide 9 — RAGAS answer-quality pilot

We then used RAGAS with a local language model to evaluate actual answers on 12 selected cases: eight focused questions, one summary, one comparison and two negative cases.

Faithfulness averaged 0.97 across the ten answered cases. This asks whether the claims are supported somewhere in the retrieved evidence. Citation support averaged 0.92 and checks the narrower question: does each claim's own citation support it?

The system declined both negative cases: a missing circular and an unrelated question. Factual correctness scored 0.38 across eight cases, but that comparison was affected by incomplete draft references. For example, “P2M only” leaves out context present in a fuller answer. We cannot interpret this as 62 percent of answers being wrong.

These are provisional model judgements, not independently verified accuracy. The same model generates and judges, and the questions were already seen. We also retained a separate demo failure where a friend-payment question received a feature overview. Our next step is human review, stronger references and unseen questions.

## Slide 10 — Implementation roadmap

Our roadmap follows the gaps identified in evaluation. The prototype and initial evaluation pipelines are already working.

In the first two weeks after midterm, we plan to review the 50 cases independently and freeze a new set of unseen questions. This gives us a stronger basis for judging improvements.

In weeks three to five, we will fix demonstrated source and answer failures, shorten long summaries, and compare retrieval settings on both quality and response time.

In weeks six to eight, payments users will try representative research tasks, and we will package a repeatable local demonstration.

These timings depend on reviewer and user access. Adding another payments source is an optional later extension; our immediate priority is validating the existing system.

## Slide 11 — Key deliverables

The deliverables show what is complete and what evidence we still need.

Today, we have a working local application, the frozen 50-question benchmark, a four-way retrieval comparison, a RAGAS evaluation pipeline and a passing regression suite.

The next deliverables are a reviewed test set and answer-quality scorecard, a tested revision with a quality-versus-latency comparison, and user-task results supported by a repeatable demonstration. Each deliverable is tied to a specific stage of the roadmap.

## Slide 12 — Discussion and feedback

We would value feedback on three remaining gaps.

First, answer quality still needs independent review. Which multi-document and missing-evidence questions should we prioritise?

Second, evaluation is UPI-focused, while 359 register entries are unavailable or excluded from searchable content, and many dates remain unverified. Is our question-to-source workflow a useful and manageable capstone scope?

Third, we have not yet measured usefulness with real payments users. Which outcomes would best demonstrate value: task completion, fewer corrections, or time saved?

Your feedback will help us prioritise validation and user testing before expanding the product. Thank you.

## Presenter reminders — not part of the spoken script

- Slide 8's 55/55 is evidence matching, not 55 correct answers. The six negatives are included in the 50 questions. “No result” is a retrieval outcome, not a generated-answer refusal.
- Slide 9's two negative cases are not both unrelated questions. One requests an unavailable circular. Say “the system declined to answer”; the unrelated case did invoke the model, which abstained.
- Do not present 0.97 faithfulness as 97% overall accuracy. Short references demonstrably affected correctness scoring, but human review is still required to resolve individual disagreements.
- The friend-payment failure was a separate saved demonstration, not one of the 12 pilot questions.
- Say “UPI-focused” rather than “UPI-only”: the initial benchmark includes a RuPay-card-on-UPI question. The 359 entries include unavailable and excluded records, not just missing PDFs.
- The week ranges are indicative weeks after midterm, not fixed delivery dates.,
