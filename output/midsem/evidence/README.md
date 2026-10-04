# Evidence accompanying the midterm

- [Initial 50-question catalogue](../../../evaluation/INITIAL_50_QUESTIONS.md): readable questions, draft answers, source anchors, per-case observations and independent-review guidance.
- [Retrieval summary](20261003T172349Z/SUMMARY.md): the pinned four-way comparison used in the slides and report.
- [Per-case retrieval results](20261003T172349Z/retrieval.json): denominators, negative cases, route splits and latency.
- [Run manifest](20261003T172349Z/manifest.json): dataset, corpus and configuration fingerprints.
- [Six live scenarios](20261003T172349Z/live.json): retained responses, including ambiguity and unavailable evidence.
- [Revised frontend checks](browser-query-expert/report.json): real cited answer, source inspection, export, summaries, comparison, gaps, simulated outage recovery and mobile layout.
- [Home](browser-query-expert/01-home.png), [answer](browser-query-expert/02-answer.png), [source reader](browser-query-expert/03-source.png): genuine application captures.
- [Earlier regression output](unit-tests.txt): the saved full run, including separate workflow tests. Workflow tests are not claimed as RAG evidence.

These are developer observations. Source-anchor retrieval is not answer accuracy. The AI-assisted UPI set awaits independent review. The HTTP outage was simulated in the browser; recovery used the real server. Existing `browser/` captures and `validation-source.md` describe the earlier interface; revised captures above supersede them for presentation purposes.

## Revised slide demonstration

- [Shop card-machine question](simple-demo/answer.json): genuine local question and answer used in the proposed-solution slide. [Capture record](simple-demo/capture.json) explains that the saved response was rendered in the application at a narrower width for readability; no response text was edited.
- [Friend-payment question](simple-demo-friend/answer.json): retained unsuccessful example. The model produced a feature overview rather than resolving the question. This is reported as a relevance/completeness issue, not hidden from the evidence set.
- [Deliverable checks](deliverable-checks.json): file hashes, page counts, matching metrics and notes.

These two demonstrations are separate from the frozen 50-case retrieval comparison and do not change its numbers.
