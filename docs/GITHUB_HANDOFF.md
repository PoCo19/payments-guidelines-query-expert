# GitHub collaboration handoff

Repository: https://github.com/PoCo19/payments-guidelines-query-expert

The current RAG code, raw Markdown, inventory and page text, tests, and current editable submissions are versioned. Local model weights, vector and metadata databases, personal configuration, stored workflow uploads, logs, old exports and backups are excluded.

Current submission files: [start here](../output/midsem/START_HERE.md). Local setup and team editing: [contribution guide](../CONTRIBUTING.md).

The 124 MB `Demo_Payments_Query.mp4` remains on the original machine and is excluded from Git. This does not mark the required team recording as complete or submitted. Share large recordings separately when needed.

Older releases and exports were moved into the ignored `.local-archive/pre-github/` folder. Windows kept `output/launch-v2/` open, so it remains locally in place and is ignored. No original corpus, model or stored workspace data was deleted.

Validation: 171 tests pass on the original machine. All 171 tests also pass in a separate clean checkout using the existing Python environment after running `download_reranker.py`, the model-download step included in `setup.cmd`. The suite includes portable configuration fallback and local override checks. This does not claim a new Python environment was installed from scratch. Without the downloaded reranker files, the real-model integration test cannot run.

Anyone can read a public repository. Colleagues can fork it and open pull requests; direct push access requires a collaborator invitation. Coordinate binary PowerPoint and Word edits to avoid conflicts.
