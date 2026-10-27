# Current workbench setup

For the latest code, corrected source snapshot and maintained graph, follow [the 27 October handoff](docs/GITHUB_HANDOFF_20261027.md). Earlier handoff tags remain historical. This is a development build with documented answer-quality limitations.

# Working together

Start with [the current midterm files](output/midsem/START_HERE.md). You do not need Ollama or Python to edit the presentation, report or narration.

1. Clone the repository or download its ZIP from GitHub.
2. Make code changes on a branch and open a pull request.
3. Coordinate PowerPoint and Word edits: Git cannot reliably merge simultaneous changes to these binary files. Use one editor per file at a time.
4. Keep slides, report and narration consistent with [the agreed scope](output/midsem/CURRENT_SCOPE.md). Update matching PDFs after editing originals.
5. Record actual team contributions; speaker assignments do not establish who implemented a module.

The owner can invite colleagues through GitHub Settings → Collaborators. Their GitHub usernames are needed; no invitations are sent automatically.

## Run locally

Follow [the frozen colleague handoff](docs/COLLEAGUE_HANDOFF.md) for the exact version, source restoration, Python/model setup and evaluation commands. Use `config.handoff.json` explicitly for reproducible comparisons. Your personal `config.json` remains ignored.

## Checks

Run `setup.cmd` before `run.cmd test`: one integration test requires the downloaded reranker weights. If Python dependencies are already installed, `run.cmd reranker` downloads and verifies those files separately. The full suite includes the separate workflow experiment. Tests use included text datasets and temporary storage; model generation is mocked where appropriate. Saved baseline results are preliminary, not independently established answer-accuracy scores.

## Edit submission files

For generated-answer evaluation, see [the RAGAS guide](evaluation/RAGAS_EVALUATION.md). Use `setup-eval.cmd` and `run-eval.cmd` for its separate environment. The default is a 12-case local pilot; human reference review remains pending. Do not present automated pilot scores as independent answer accuracy.

Use PowerPoint/Word or compatible software to edit `.pptx` and `.docx`. Scripts in `tools/` preserve the authoring process. The deck builder requires OpenAI Artifact Tool and the Codex bundled runtime; PDF export uses Microsoft Office on Windows. These authoring tools are not prerequisites for running the RAG app or editing submission files manually. The presentation finalizer refuses to overwrite an existing final deck or validation receipt: preserve the previous revision before rebuilding.

Do not commit environments, tokens, model weights, databases, uploaded workspace documents, logs or old exports. Preserve source attribution and extraction limitations when changing the corpus.
