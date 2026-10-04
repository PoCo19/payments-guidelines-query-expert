# Context/output tuning — 2026-09-24

Both v0.3 implementation items remain complete: Chroma persistence and clause-aware related retrieval with preserved document attribution. Semantic/legal review of the heuristic labels remains separate research work.

## Applied settings

| Setting | Before | After |
|---|---:|---:|
| Generation context (`num_ctx`) | 8,192 tokens | 16,384 tokens |
| Maximum generated output (`num_predict`) | 1,500 tokens | 3,072 tokens |
| Evidence character budget | 12,000 | 18,000 |

Context is the working window for prompt and generation. Output is the maximum generated length, including JSON/citation syntax. Character budget controls selected evidence before tokenization and is only an estimate. The app sends these settings per generation request; no global Ollama setting change or embedding rebuild is needed. Passage-count limits remain unchanged, so this does not promise full-document coverage.

Hardware checked live: approximately 32 GB RAM and NVIDIA RTX 5070 Ti Laptop GPU with 12 GB VRAM. Ollama reported the answer model at 16,384 context, with model allocation and GPU allocation equal (6,014,380,276 bytes), alongside the embedding model. This supports the tested configuration, not a maximum-capacity guarantee.

## Tests

A detailed OC 186A question was run with both configurations. Before: 1,633 prompt tokens, 292 generated tokens, five claims / 134 words. After: 1,633 prompt tokens, 407 generated tokens, seven claims / 190 words. Both finished normally (`done_reason=stop`), well below even the old output cap. This single comparison does not establish an accuracy gain or that the old cap caused short answers. The same evidence fitted both budgets. The longer answer also repeated the source OCR string `$5000` without qualifying that figure inside the claim. The UI retained its general OCR warning. This is an existing source-quality limitation, and the extra detail must not be presented as an accuracy improvement.

The first 16k request took about 19.3 seconds inside Ollama, including about 10.6 seconds reloading the model. An unrelated-question check at 16k abstained and completed in about 1.5 seconds. Input size and model loading affect latency. No output truncation occurred in these examples; the full 16k/3072 boundary was not stress-tested.

Raw settings, claims, sources, token counts and allocations: `evaluation/context_tuning_results.json`. Reproduce from project root with `.\.venv\Scripts\python.exe evaluation/check_context_limits.py` (requires Ollama). Original settings are saved in `evaluation/context_tuning_config_before.json`.

## Getting more useful detail

Ask a specific multipart question, for example: “Explain the supported consent, device-security and participant responsibilities in OC 186A, with citations for each point.” A larger token cap allows longer output; it does not require the model to fill that space. Retrieved evidence and question scope remain the main constraints. Avoid adding unrelated context merely to fill the window.

To revert, restore context_length=8192, max_output_tokens=1500 and context_char_budget=12000 in config.json and restart. No re-embedding is required.

References: [Ollama context/memory guidance](https://docs.ollama.com/context-length), [parameter definitions](https://docs.ollama.com/modelfile).

## Active-server verification

After replacing the stale server process, an HTTP answer request confirmed the 18,000-character evidence budget and Ollama confirmed 16,384 context. It returned three cited consent claims in approximately 15.5 seconds, including model reload. The active-server result is recorded in the same JSON report.

