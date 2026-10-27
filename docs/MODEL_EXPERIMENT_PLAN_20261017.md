# Model choices and next experiments

Verified on 17 October 2026: Intel Core Ultra 9 275HX (24 cores), approximately 32 GB system RAM, NVIDIA GeForce RTX 5070 Ti Laptop GPU with 12,227 MiB VRAM. Installed Ollama models: `qwen3.5:9b` (6.6 GB) and `qwen3-embedding:0.6b` (639 MB). Active project context is 16,384 tokens and maximum answer output is 3,072 tokens. No model was downloaded or switched during this assessment.

## Larger embedding model

Embeddings affect which passages are found. They do not fix incorrect source text, mistaken amendment applicability or a model combining two correctly retrieved rules. The synthesis experiment already supplied the necessary anchors but still exposed attribution and relevance weaknesses, so generation deserves priority.

`qwen3-embedding:4b` is a reasonable candidate to benchmark against 0.6B. The [Ollama package](https://ollama.com/library/qwen3-embedding:4b) is approximately 2.5 GB at Q4_K_M. The [publisher's model card](https://huggingface.co/Qwen/Qwen3-Embedding-4B) lists up to 2,560 dimensions versus 1,024 for 0.6B. Larger model capacity is a hypothesis for better paraphrase/semantic matching, not proof for this corpus. Quantized local performance may differ from published benchmarks.

Use a separate Chroma collection/release and separate candidate configuration. Re-embed every indexed chunk with the candidate model and use that same model for queries; never mix 0.6B and 4B vectors even if dimensions are reduced to match. Current corpus has 14,480 chunks. At full dimensions, raw float32 vector storage alone grows from roughly 57 MiB to 141 MiB; Chroma metadata and index overhead are additional. Indexing time, query embedding time and GPU pressure also need measurement.

Hold chunking, source snapshot, graph, reranker and query set fixed. Compare vector-only and full hybrid results, anchor recall, ranking quality, hard-negative behaviour and cold/warm latency. Use realistic paraphrases and an independently reviewed held-out set: reference-heavy questions already at ceiling cannot establish improvement. Keep 0.6B unless 4B demonstrates a useful trade-off.

## A 12B answer model

A quantized 12B model is a plausible experiment on this laptop, but GPU-only operation at the project's context is not yet measured. [Gemma 3 12B Q4_K_M](https://ollama.com/library/gemma3:12b) is a concrete candidate, currently about 8.2 GB downloaded. Runtime memory also includes cache, buffers, other models and display use. This is a different model family, not a guaranteed upgrade over Qwen 3.5 9B. [The official Qwen 3.5 listing](https://ollama.com/library/qwen3.5) has no 12B size; its 27B package starts around 17 GB and exceeds this GPU's VRAM before runtime overhead.

For a fair first comparison, retain the same 16K context, evidence, output cap and validation flow. Check JSON/schema compatibility and any unsupported thinking options before running the full evaluation. Measure prompt processing, generation tokens/second, total answer time, checker/repair time and cold/warm model loading. Inspect `ollama ps` and GPU memory during generation; a CPU/GPU split can materially increase latency. [Ollama's context documentation](https://docs.ollama.com/context-length) explains the memory effect and offload check.

If 16K causes memory pressure, test an 8K resource-constrained profile with an appropriately smaller evidence and output budget as a separate experiment. Do not silently truncate input or compare different evidence budgets as a pure model-quality test. Avoid loading the 4B embedding candidate and 12B generation candidate together initially; their weights plus runtime allocations can exceed available VRAM. Model unloading/reloading trades memory for latency.

There is no measured 12B speed estimate on this machine yet. Parameter count does not reliably predict relative speed across architectures, quantizations, output lengths or repair frequency. A more accurate model could reduce repair calls, but that too must be measured.

## Recommended order

1. Keep the validated intake checks and current graph/hybrid path. Leave both new retrieval/synthesis switches off until they justify promotion.
2. Independently review the six saved synthesis cases, then add held-out multi-document questions with expected material conditions and source ownership. Score useful answer completion, unsupported claims, missing qualifications, relevance and citation correctness separately.
   Prioritise scope-aware evidence selection for both synthesis and completeness review. The final browser check answered the PoS question directly, but the reviewer raised a false conflict using unrelated P2P guidance. A conflict should require overlapping subject, actor, condition and temporal scope supported by the text, not merely shared payment terminology. Test this without publisher-specific hardcoding or hiding genuine amendments.
3. Benchmark the current 9B model against one 12B candidate on fixed evidence. Refine internal evidence selection/source-specific claims as a separate arm. Keep paragraph/bullet/mixed answers driven by the question.
4. Benchmark 4B embeddings on the retrieval misses and new paraphrases in an isolated index; adopt only on measured benefit.
5. Promote a candidate only after regression checks, no newly observed critical amount/scope misattributions in the reviewed set, acceptable latency and documented remaining failures. Retain the old configuration/index for rollback.

This is a staged experiment plan, not a claim that the project is already production-certified or that all retrieval/generation failures are solved.
