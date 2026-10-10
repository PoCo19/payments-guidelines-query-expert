# Local model decision — 9 October 2026

The current machine has about 32 GB system RAM and an NVIDIA RTX 5070 Ti Laptop GPU with 12,227 MiB VRAM. Installed Ollama models are `qwen3.5:9b` (about 6.6 GB) and `qwen3-embedding:0.6b`. The app currently requests 16,384 context tokens and up to 3,072 output tokens. These settings and the active model have been preserved.

**Recommendation: benchmark a quantized 12–14B candidate before switching.** More parameters alone do not establish better grounded answers, particularly when comparing model generations. Keep Qwen 3.5 9B as the measured baseline.

| Candidate | Official download size at research time | Decision |
|---|---|---|
| [Qwen3 14B Q4_K_M](https://ollama.com/library/qwen3:14b) | 9.3 GB | Closest practical larger Qwen option to test. Older family than Qwen 3.5; improvement is a hypothesis. GPU headroom is tight once context and other models are loaded. |
| [Gemma3 12B Q4_K_M](https://ollama.com/library/gemma3:12b) | About 8.2 GB on the current tag | Alternative with more memory headroom than 14B. Test structured answers, citations and abstention rather than assuming superiority. |
| [Qwen3.5 27B](https://ollama.com/library/qwen3.5:27b) | About 17 GB | Weights exceed this GPU's capacity. CPU offloading is likely; not the first choice for interactive latency. |
| [Qwen3.5 35B](https://ollama.com/library/qwen3.5:35b) | About 22 GB | Also exceeds VRAM. Fewer active MoE parameters do not mean all model weights fit on the GPU. |

Download size is not runtime VRAM consumption. Context/KV cache, compute buffers, embedding-model residency and desktop graphics also consume memory. Tags can change; the benchmark records installed digests. [Ollama's context guidance](https://docs.ollama.com/context-length) confirms the memory cost of larger context and recommends checking offloading.

Start the larger-model comparison at **8,192 context / 1,024 output tokens**, with thinking disabled, against the same settings on the 9B baseline. Then test 16,384 context if residency and latency remain acceptable. This is a trial profile, not a change to the active application's settings. Longer output takes longer to generate; a larger context limit does not itself produce better evidence.

## Reproducible comparison

Observed baseline on 9 October: one UPI Circle question, 4,940 prompt tokens, 464 output tokens, 8,192 context limit. First generation took **18.839 s**, including **8.802 s** model loading; the repeated request took **8.455 s**, at approximately **56–58 output tokens/s**. Ollama reported the model's resident size entirely in VRAM. Both outputs passed structural/citation-ID checks. This is one question with repeated-prompt caching, not a general latency estimate or a correctness score. Larger candidates were not installed or benchmarked. Raw evidence: `reports/model-benchmarks/20261009T083452564728Z/` included with the colleague handoff; new reports remain ignored until deliberately selected for sharing.

`evaluation/benchmark_models.py` freezes one actual application generation request after hybrid retrieval, then sends identical evidence/schema/system instructions to each installed candidate. It does not download models or edit the live configuration.

After installing whichever candidate you choose, run from the project folder:

```powershell
.\.venv\Scripts\python.exe evaluation\benchmark_models.py --models qwen3.5:9b qwen3:14b --repeats 3 --context 8192 --output-tokens 1024
```

The first call may include model loading. Review the saved `reports/model-benchmarks/<timestamp>/results.json`: wall time, first-output time, load time, prompt/output token counts, output tokens/sec, completion reason, structural/citation-ID validity, raw drafts and post-run model residency. Errors are retained. Token rates across different tokenizers are not a complete user-experience comparison.

This measures **generation only**. It excludes retrieval and the subsequent support-check model call, so it is not the app's full answer time. A valid citation ID does not establish that its claim is supported. One question cannot determine a model winner.

Before switching, compare a reviewed set of direct questions, multi-document questions, summaries, comparisons and unanswerable cases. Use the existing [RAGAS capture/review workflow](../evaluation/RAGAS_EVALUATION.md) for generated-answer evaluation, retain human judgement and compare complete application latency. Prefer fewer unsupported claims and better qualifications at an acceptable measured delay. No latency or quality claims have been made for uninstalled candidates.

The generation model can change independently of `qwen3-embedding:0.6b`. Keep the embedding model stable during this experiment so changes in retrieval do not confound the comparison.
