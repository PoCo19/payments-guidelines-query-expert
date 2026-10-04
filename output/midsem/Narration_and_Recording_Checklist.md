# Payments Guidelines Query Expert

Midterm narration | Suggested five speakers | Planned duration: 8 minutes

Use the revised deck. Speaker assignments are not contribution claims. Replace team details before recording. Actual duration must be checked in rehearsal.

## Slide 1 — Payments Guidelines Query Expert
Speaker 1 | 0:00–0:45

Our project is Payments Guidelines Query Expert. It helps payments professionals ask questions about documented requirements and inspect the sources behind an answer. We have started with NPCI circulars across multiple payment products. The intended product is broader, but this is the coverage implemented today. For this midterm, we are presenting a working local prototype, its design choices, a preliminary retrieval comparison and the work still needed to evaluate answer quality. The product name describes the task it supports. The output remains AI assistance that a user should review, rather than an authoritative compliance decision.

## Slide 2 — Problem Statement and Motivation
Speaker 1 | 0:45–1:40

Our intended users are product, operations and compliance teams in banks and fintechs. A question about one payment feature may require several circulars, including later clarifications. A user must first find the right documents, then identify the relevant conditions, and finally check which source supports each statement. Manual searching makes this slow, while a fluent AI answer can hide missing conditions. We want to make this question-to-source journey easier. We have not yet measured time savings. A useful outcome would be a user finding the necessary requirement with fewer searches while still checking the original guideline before acting.

## Slide 3 — Proposed Solution
Speaker 2 | 1:40–2:40

The prototype helps users ask questions, inspect sources, and summarise or compare circulars. Here the user asks: Can I use UPI Tap and Pay at a shop's card machine? No circular number is needed in the question. The recorded local response says the terminal must be NFC-enabled and appropriately certified, and cites the supporting clause. NFC is the contactless technology used for tapping a device. The response also provides merchant-only and integration conditions. The slide uses enlarged captures from the application rendering of this saved response; the answer text has not been rewritten for the presentation. This shows how the user can follow an answer back to a circular. It is one illustrative case, not an accuracy result.

## Slide 4 — Data Sources and Tools
Speaker 2 | 2:40–3:40

The knowledge base starts with Markdown circulars and product inventory records. We preserve each document and page before splitting its text. A recognised heading or numbered clause begins a new block. A long block is split into windows of at most 220 words, with 35 words repeated between adjacent windows to preserve some context. We never combine text from different circulars into one chunk. Each chunk retains its document ID, page, heading and links to its neighbours. The same text feeds BM25 keyword search and Qwen embeddings stored in Chroma. SQLite stores identities, filters and relationships. This structure lets us search by words or meaning while tracing every selected passage back to its source.

## Slide 5 — How the System Works
Speaker 3 | 3:40–5:00

At question time, product and document filters first narrow the search. BM25 finds exact words and circular references, while Qwen embeddings find passages with similar meaning. Hybrid retrieval combines these results. A local MiniLM reranker scores candidates for focused questions. Summary and comparison routes instead select evidence across document sections and bypass reranking. We assemble a bounded set of passages and pass it to Qwen3.5 through Ollama. Citation and support checks run before display, and the reader can inspect the sources. We use pretrained models without fine-tuning because our first requirement is access to attributable documents. Local inference avoids paid model calls, but the 32 GB machine limits speed and context. Automated support checks use the same model and can share its mistakes.

## Slide 6 — What the Preliminary Evaluation Tells Us
Speaker 4 | 5:00–6:20

This experiment asks whether more complex retrieval gives us better evidence than a simple keyword baseline. All four methods ran the same 50 UPI cases on the same corpus. Expected evidence found means the required source passages appeared in the retrieved context: all methods found 55 out of 55. It does not mean 55 correct AI answers. The second measure tests six cases that should return no evidence. BM25 returned nothing in all six; each semantic variant returned irrelevant passages in one case. The last column measures retrieval time only, excluding answer generation. BM25 was fastest; adding reranking to hybrid increased the median from 78 to 160.5 milliseconds without improving coverage here. The conclusion is to keep BM25 as a strong baseline and test harder cases before claiming a benefit from extra complexity. Many queries name circulars and 15 coverage routes bypass reranking. The AI-assisted dataset still needs independent review, so this cannot determine overall answer quality or the best method for every question. Some questions need more than one passage, which is why there are 55 expected evidence matches across 50 cases.

## Slide 7 — Implementation Roadmap
Speaker 5 | 6:20–7:20

The roadmap now identifies work, timing and a concrete output. The midterm milestone is complete at the prototype level: cited questions and answers, source inspection, summaries and comparisons. In the first two weeks after midterm, we plan to review the existing 50 cases with an independent reviewer and freeze unseen questions. The output is a reviewed test set and an answer-quality scorecard. In weeks three to five, we will fix source and answer failures, improve overly long summaries, and compare retrieval choices. The output is a tested revision with a documented quality and latency comparison. In weeks six to eight, payments users will try research tasks, and we will prepare reproducible setup and a final demo. The output is a user-task readout and a repeatable local demonstration. These are indicative planning windows, dependent on reviewer access. A second payments source is an optional extension after validation, not a condition for completing the core capstone.

## Slide 8 — Discussion and Feedback
Speaker 5 | 7:20–8:00

We would like feedback on three decisions. First, is this focused question-and-source workflow a useful and manageable capstone scope for payments teams? Second, which questions should the independently reviewed evaluation prioritise, especially when requirements span several documents? Third, what evidence would convince you that the assistant is useful in practice: task completion, fewer corrections, time spent, or a combination? Our immediate priority is to validate the answers and improve the failures before expanding coverage. The current prototype demonstrates a complete local RAG flow. The remaining work is to establish how reliably it answers realistic questions and how effectively users can verify those answers.

## Recording checklist
- Fill in team ID, names and the registered title if required; keep all files consistent.
- Rehearse all speakers with the same deck. Keep the final recording between 5 and 10 minutes.
- Check audio, slide transitions and readability from beginning to end.
- Keep the distinction between retrieval coverage and answer correctness.
- Test submission links from another account if sharing by link.
- Submit the recording, slides and report and retain the receipt.
- Recording, rehearsal and portal submission are still pending.