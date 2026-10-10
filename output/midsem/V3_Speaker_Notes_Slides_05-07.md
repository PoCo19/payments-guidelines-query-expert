# Speaker notes: slides 5–7

**Presentation:** Payments_Guidelines_Query_Expert_v3.pptx
**Audience:** Midterm capstone evaluators
**Delivery:** Approximately 3 minutes at a measured pace. These notes lead into the [notes for slides 8–12](V3_Speaker_Notes_Slides_08-12.md).

## Slide 5 — Data sources and technology stack

Our initial knowledge base contains NPCI circulars. RBI documents are a planned extension and are not currently indexed.

The register has 1,921 records, of which 1,562 documents are searchable. These contain 4,826 pages and 14,060 chunks. The remaining 359 records are unavailable or excluded. This is a saved snapshot, not a continuously updated archive.

During preparation, we preserve each circular's identity, page and source. We split text at page, heading and clause boundaries. Longer blocks use approximately 220 words with 35 words of overlap, so adjacent chunks retain some shared context. A chunk never combines different circulars or pages.

SQLite stores metadata and relationships. BM25 finds exact terms, while Qwen embeddings in Chroma find similar meanings. MiniLM reranks relevant candidates, and Qwen, served locally through Ollama, drafts the answer. Citation and support checks run before display.

## Slide 6 — How a question moves through the system

This diagram separates preparation from answering a question.

The top row prepares the knowledge base: preserve document identity, create chunks, build search indexes and store source links. We repeat this when the corpus changes, rather than rebuilding everything for each question.

The bottom row starts with the user's question and filters. The system retrieves candidate passages, ranks them, and selects evidence that fits within the model's limits. The model then drafts an answer, and claim-level checks determine what can be shown with citations.

Summaries and comparisons need evidence across document sections, so they use a different selection route and bypass reranking.

If a circular reference is ambiguous, the app asks the user to narrow the selection. If evidence is unavailable, it reports that limitation. The source reader lets users inspect the evidence themselves.

## Slide 7 — Why these choices, and their trade-offs

We chose pretrained models without fine-tuning because the immediate challenge is finding and attributing changing requirements. Retrieval supplies document evidence without retraining the model whenever a circular changes.

Local inference gives us control over the data and avoids paid inference API calls, but it introduces hardware and speed constraints. Our machine has about 32 gigabytes of RAM and 12 gigabytes of GPU memory.

The model has a 16,384-token context window, with output capped at 3,072 tokens. We also limit selected evidence to 18,000 characters.

In the recorded runs, a direct question took about ten seconds, while summaries and comparisons took substantially longer. These are observations, not guaranteed response times.

The support checker uses the same model as the answer generator, so it can share its mistakes. That is why we separately evaluate retrieval and answer quality, starting with the next slide.

## Presenter reminders — not part of the spoken script

- The searchable corpus currently contains NPCI documents. RBI coverage is planned, not delivered.
- The 359 records include unavailable and excluded/quarantined entries; they are not all missing PDFs.
- Chunk overlap applies to long blocks within a page; it does not merge different pages or circulars. A relationship between circulars does not by itself prove supersession.
- “Prepare once” means indexing ahead of queries, with rebuilding or updating when inputs change.
- Distinguish ambiguity from missing evidence: ambiguity can offer choices; an unavailable document may offer no usable source to select.
- The 16,384-token value is the context window, not a promise of 16,384 input tokens plus 3,072 additional output tokens. The character budget is a separate evidence-selection limit.
- “Local” describes model inference and storage. Installation, model downloads and opening official source links can require network access.
- The latency figures on the slide are from recorded scenarios, not a general performance benchmark. Automated support checks do not replace independent review.
