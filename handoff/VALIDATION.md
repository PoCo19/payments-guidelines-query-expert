# Handoff validation — 10 October 2026

This record covers the source/configuration handoff and the current implementation. Earlier generated-answer evaluations remain separate historical records.

| Check | Observed result |
|---|---|
| Clean export | Exported staged Git files into an empty directory, with no personal `config.json`, local release, embedding cache or environment. |
| Source restore | Verified 1,665 archive members and restored the frozen sources. Corpus and registry fingerprints match the original release. |
| Reconstructed inputs | 1,929 register records; 4,834 page records; 14,480 chunks. All 20 mixed-source cases' reference anchors validated. Both frozen dataset checksums preserved. |
| Fresh setup | Ran `setup.cmd` in the clean copy. Created a new Python 3.12.14 environment; installed the pinned dependencies and downloaded/verified reranker weights/tokenizer. `pip check`: no broken requirements. Cached package downloads were reused, but the environment was new. |
| Python regression suite | 259 discovered; **255 passed, 4 skipped**. The skips are optional `lxml` conversion checks. [Full log](validation/python-tests.txt). |
| JavaScript regression suites | Both answer formatting and research coverage rendering suites passed. |
| HTTP smoke | Homepage, stats, RBI PPI source reader and BM25 evidence answer all returned HTTP 200 from the clean-copy server. The answer returned 15 source passages. This checks operation, not answer correctness. [Raw record](validation/http.json). |
| Models | Installed Qwen generation and embedding digests match the manifest; fresh-copy reranker assets match their pinned hashes. Ollama 0.34.3 on Windows 11. |
| Archive regression checks | Idempotent restore, refusing changed-source overwrite, corrupt archive/member rejection and unsafe path rejection all passed. |

Corpus fingerprint: `12baf1b5415006535c91ef99d2604ac6cb949eeb90acc9253998f1d62d8e1682`
Registry fingerprint: `41d838e42cedf7bb619b1b7adbc6bb1d1cfd8fd003223d2a026a861a2102d7b5`

The clean-copy check did **not** rebuild all 14,480 vectors or rerun a full generated-answer/RAGAS evaluation. The regression suite exercises Chroma writes on small fixtures; saved full-corpus embedding and generated-answer records are included separately. Colleagues must run the documented `embed` command before reproducing hybrid retrieval. No model weights or generated vector database are in Git.

Source copies and existing review annotations are packaged, but independent review of the complete sources and answer references is pending. Automated pilot metrics are not human-validated accuracy. This release does not certify that source snapshots are current or legally authoritative.

See [the handoff guide](../docs/COLLEAGUE_HANDOFF.md) for exact commands and the frozen Git tag.
