# Concepts in plain language

These definitions explain how the terms are used in this project. Read [the flow](PROJECT_FLOW.md) to see how they fit together.

| Term | Meaning here | Common misunderstanding to avoid |
|---|---|---|
| Corpus / knowledge base | The imported document collection and its metadata | It is a snapshot, not every current payment rule |
| Markdown | Plain text with simple headings, lists and tables | Text in Markdown may still contain extraction errors |
| OCR | Software that reads text from a scanned image | It can confuse digits, currency symbols and table columns |
| Metadata | Details such as document ID, issuer, product, date and source URL | A known issue date does not prove an effective date |
| Chunk | A retrievable passage belonging to a document and page | A chunk is not a complete statement of all applicable requirements |
| Token | A unit of text processed by a model, often part of a word | Token count is not the same as word count |
| Embedding | A list of numbers representing text for semantic comparison | It does not store a verified answer or legal interpretation |
| Vector database / Chroma | Storage and search for embeddings with identifiers | It is not the language model |
| BM25 | Keyword ranking based on terms in the question and documents | Exact word matches can still lack context |
| Hybrid retrieval | Combining keyword and semantic search signals | It does not mean combining answers from two language models |
| Reranker | A model that reorders candidate passages for relevance | It does not independently verify their claims |
| Context window | How much text a language model can process in a request | A larger window does not guarantee the right evidence is included |
| RAG | Retrieve evidence, then ask a model to answer using that evidence | It does not eliminate hallucination |
| LLM / generation model | The model that writes an answer from the question and evidence | It is not a database of guaranteed current rules |
| Ollama | The local service that runs the chosen models | Installing Ollama does not automatically install every model |
| Claim | An individual factual statement proposed for an answer | One sentence can contain several conditions that require support |
| Citation | An identifier linking a statement to retrieved evidence | A valid citation ID does not prove the evidence supports the statement |
| Graph-assisted retrieval | Following bounded, maintained relationships between evidence | It is not an automatic map of every amendment or legal precedence |
| Anchor | A source passage used as an expected retrieval target or graph reference | Finding an anchor does not prove the final answer is correct |
| Abstention | Saying that the requested answer cannot be established from available evidence | It is sometimes the correct result, not a product failure |
| Fingerprint / hash | A digest used to detect changed content or configuration | Matching hashes establish sameness, not correctness |
| Cache | Stored results reused to avoid repeating work | A cache must match the text/model it was built for |
| Regression | A case that stops working as expected after a change, or a recorded defect to guard against | A passing unrelated test does not close it |

## The models have different jobs

`qwen3-embedding:0.6b` turns passages and questions into vectors. `qwen3.5:9b` writes answers and supports some automated checking. The separately installed local reranker orders candidate passages. We do not fine-tune these models as part of the current product.

Changing the embedding model normally means rebuilding compatible embeddings and evaluating retrieval again. Changing the generation model can affect wording, reasoning, latency and memory use. A larger model is not automatically a better product choice.

## Four kinds of checking that are easy to confuse

**Software tests** exercise code behaviour: citations resolve, states transition correctly, invalid input is rejected, and exports retain content. The current recorded suite has 465 Python tests and four JavaScript suites. These are not 465 independently verified payments answers.

**Development evaluations** compare retrieval or generated answers on saved questions. They can reveal improvements and failures, but repeated tuning on those questions makes them unsuitable as untouched final evaluation data.

**Independent human evaluation** requires a payments colleague to inspect original sources, expected answers and qualifications. The provisional 50-case acceptance set is separate from earlier development sets. Its review and acceptance remain pending.

**In-product human sign-off** records whether a person checked one saved response. It does not run the benchmark, notify a reviewer or certify the entire system.

RAGAS is an additional evaluation framework included in the repository. It can help score dimensions such as support or relevance, but a model judge has its own errors. It is not automatically run when someone asks a question or records sign-off. See [the RAGAS guide](../../evaluation/RAGAS_EVALUATION.md) for the separate evaluation workflow.

## Reading metrics correctly

One question can require several source passages. Therefore, a test set with 50 questions can have more than 50 expected evidence anchors. Report questions, anchors, negative cases and assessed claims separately, with their own denominators.

Latency measures elapsed time, not accuracy. Retrieval recall measures how much expected evidence was found, not whether the final answer applied it correctly. “No additional issue found” means an automated checker did not flag another issue; “check unavailable” means it did not reach a usable conclusion.
