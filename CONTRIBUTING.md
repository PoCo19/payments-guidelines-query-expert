# Working together

Start with [the current midterm files](output/midsem/START_HERE.md). You do not need Ollama or Python to edit the presentation, report or narration.

1. Clone the repository or download its ZIP from GitHub.
2. Make code changes on a branch and open a pull request.
3. Coordinate PowerPoint and Word edits: Git cannot reliably merge simultaneous changes to these binary files. Use one editor per file at a time.
4. Keep slides, report and narration consistent with [the agreed scope](output/midsem/CURRENT_SCOPE.md). Update matching PDFs after editing originals.
5. Record actual team contributions; speaker assignments do not establish who implemented a module.

The owner can invite colleagues through GitHub Settings → Collaborators. Their GitHub usernames are needed; no invitations are sent automatically.

## Run locally

Install Python 3.12 and Ollama. On Windows run `setup.cmd`, then:

```text
ollama pull qwen3.5:9b
ollama pull qwen3-embedding:0.6b
run.cmd embed
run.cmd
```

Open http://127.0.0.1:8765. Building the full vector index is a one-time local operation and can take time. BM25 source search works without the vector index; hybrid search needs embeddings. Models and generated indexes are not versioned.

The app uses `config.example.json` when `config.json` is absent. Copy the example to `config.json` for personal settings; Git ignores that file. Original PDFs remain accessible through official links. Optional local originals belong under the configured `source_pack` directory and are not bundled.

## Checks

Run `setup.cmd` before `run.cmd test`: one integration test requires the downloaded reranker weights. If Python dependencies are already installed, `run.cmd reranker` downloads and verifies those files separately. The full suite includes the separate workflow experiment. Tests use included text datasets and temporary storage; model generation is mocked where appropriate. Saved baseline results are preliminary, not independently established answer-accuracy scores.

## Edit submission files

Use PowerPoint/Word or compatible software to edit `.pptx` and `.docx`. Scripts in `tools/` preserve the authoring process. The deck builder requires OpenAI Artifact Tool and the Codex bundled runtime; PDF export uses Microsoft Office on Windows. These authoring tools are not prerequisites for running the RAG app or editing submission files manually. The presentation finalizer refuses to overwrite an existing final deck or validation receipt: preserve the previous revision before rebuilding.

Do not commit environments, tokens, model weights, databases, uploaded workspace documents, logs or old exports. Preserve source attribution and extraction limitations when changing the corpus.
