# RBI–NPCI development evaluation records

Use **20261010T081610Z** as the final 20-case generated-answer capture. References are AI-assisted; human review is pending. The dataset and original 50 UPI cases are separate.

| Folder | Purpose and status |
|---|---|
| [20261010T081610Z](20261010T081610Z/summary.md) | Final: 20 generated responses, unchanged snapshot, 18/34 anchors, 7/17 positive cases with all anchors, 3/3 negative abstentions, 7/17 positive abstentions. Median 24.0545s, max 65.187s. |
| [20261010T032145Z](20261010T032145Z/summary.md) | Snapshot-checked five-case generation pilot. Its scores subfolder contains the RAGAS pilot. |
| [RAGAS pilot](20261010T032145Z/scores-20261010T081313Z/SUMMARY.md) | Five captured cases: faithfulness scored 1, timed out 1, skipped 3; context recall scored 3, skipped 2. Same-model judge, unreviewed references. Some scoring overlapped another workload; latency is not controlled. |
| [20261010T031606Z](20261010T031606Z/summary.md) | First complete retrieval-only run: 18/34 anchors; no end-of-run fingerprint guard yet. Not eligible for RAGAS answer scoring. |
| 20261010T031759Z | Earlier five-case generation pilot before end-of-run fingerprint guard. The score runner correctly refused it. Preserved as diagnostic history. |
| 20261010T081328Z | Interrupted retrieval run during competing Ollama work; remains marked running. Do not report it as a completed experiment. |

[Review all 20 answers](20261010T081610Z/human_review.csv). Read each response beside its original sources; fill in reviewer identity, source verification, correctness, completeness and citation support. A successful app response or valid citation ID does not establish correctness.

Full inputs, outputs, source passages, retrieval traces, budgets and code/config/model fingerprints are in capture.json. Preserve raw records when diagnosing failures. Captures retain the banner text used at capture time; the later Partial draft wording does not change the claims or scores.
