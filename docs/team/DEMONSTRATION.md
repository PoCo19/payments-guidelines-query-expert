# Six-minute team demonstration

Demonstrate a supervised research prototype, not certified payments advice. Rehearse on the presentation machine and retain failed results.

| Time | Show | Explain |
|---|---|---|
| 0:00–0:45 | Home and two task links | Teams need to understand both a requirement and a change. NPCI and selected RBI snapshots are our initial library. |
| 0:45–2:00 | Ask a question | Ask “What is UPI Lite? Answer briefly.” Read the actual result and warnings. Retrieved passages support the cited explanation. |
| 2:00–2:45 | Citation and Save answer | Evidence stays attached. Saving does not regenerate. Human sign-off is optional and separate from evaluation. |
| 2:45–4:15 | Understand a change | Choose OC169A as the changed document and OC169 as baseline. Inspect both, confirm, then prepare the summary. |
| 4:15–5:15 | Comparison and source reader | Check earlier/revised figures, Lite versus LiteX, and issue dates versus referenced dates and deadlines. |
| 5:15–6:00 | Saved work and export | Both tasks share one engine. Exports retain evidence and actual review status. State open quality limitations. |

The checkpoint for these selected documents is OC169's ₹500 per-transaction / ₹2,000 total UPI Lite limits versus OC169A's ₹1,000 / ₹5,000. OC169A separately leaves LiteX at ₹500 / ₹2,000. This checks the imported documents, not universal current applicability.

OC169A is issued 27 February 2025; 4 December 2024 refers to an RBI notification. The limit change says immediately; dormant-account changes have a 30 June 2025 deadline. Do not infer unstated retroactivity rules. Verify in the source reader before presenting.

If generation fails, show the failure and sources, then use a clearly labelled saved result to explain the workflow. Do not present saved output as a fresh live run or remove incomplete-answer warnings.

## Explain the engineering in one minute

Documents retain identity, pages and provenance. Clause-aware chunks feed keyword search and Chroma semantic search. Hybrid retrieval and a local reranker select candidates; bounded neighbouring and maintained graph evidence add context. Local Qwen writes the answer. Citation, support and advisory completeness checks expose some problems. The source reader lets a person inspect the evidence.

The 144-case development check measures expected-passage retrieval, not answer correctness. Independent review remains pending. See [implementation and verification](../PRODUCT_MATURITY_20261028.md).
