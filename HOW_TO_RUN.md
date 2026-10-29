# How to run the current project on Windows

Use this guide for a fresh Git checkout. Run each command separately in **PowerShell** and stop if it reports an error. Do not paste the whole guide into a terminal.

## 1. Prerequisites

Install Git, Python **3.12, 64-bit**, and Ollama. Open Ollama before installing or using the models. Check that these commands work in a newly opened PowerShell window:

```powershell
git --version
python --version
ollama --version
```

The complete local model setup requires substantial download space and available memory. Speed depends on the computer, GPU and other programs sharing it. We have not certified a minimum hardware specification for every teammate. Do not substitute models silently when comparing evaluation results.

Node.js is only needed to run the JavaScript developer tests, not to serve the application. There is no separate frontend build or paid API key required for normal local use. First-time dependency/model downloads require internet access; opening external original-document links also requires it.

## 2. Get the files

Choose a short path, such as `C:\work\payments`. Long paths can make some source filenames inaccessible on Windows. Use another short writable folder if necessary and adjust the later `cd` commands.

```powershell
git clone https://github.com/PoCo19/payments-guidelines-query-expert.git C:\work\payments
cd C:\work\payments
git rev-parse HEAD
```

Keep the commit identifier with any test results. `main` can change; a commit identifies the exact code you used.

## 3. Install the runtime

```powershell
.\setup.cmd
```

This creates a project-specific Python environment in `.venv`, installs pinned dependencies and downloads the hash-checked CPU reranker. A successful run ends with `Setup complete`. It does not install the main language model or the embedding model.

We use `.cmd` launchers and the environment's Python executable directly. You do not need to activate a virtual environment or change PowerShell's script execution policy.

## 4. Restore the source library

```powershell
.\.venv\Scripts\python.exe tools\handoff.py restore --workbench
```

This checks the source archive, restores the corrected library and verifies the matching maintained graph. Expect JSON containing `"status": "passed"`. The packaged library reconstructs 1,929 register records, 4,834 page records and 14,480 chunks; not every register record has searchable text. Restoration does not create embeddings or certify the contents as legally current.

The command leaves personal configuration untouched. It refuses to overwrite changed restored source files. If it reports a mismatch, keep your changes and investigate; do not delete the folder to make the warning disappear.

## 5. Install and verify the two Ollama models

With Ollama running:

```powershell
ollama pull qwen3.5:9b
ollama pull qwen3-embedding:0.6b
.\.venv\Scripts\python.exe tools\handoff.py models --workbench
```

The first model writes answers. The second converts text into vectors for semantic search. Expect `models_match` and `reranker_matches` to be true. Tags can point to different weights over time; if the digest check fails, tell the team and record the difference. A matching name alone is not an identical experiment.

## 6. Build the vector index once

```powershell
.\.venv\Scripts\python.exe app.py embed --config config.workbench.json
.\.venv\Scripts\python.exe tools\handoff.py verify --workbench
```

Leave embedding generation running until it finishes successfully. Its first run can take time. It generates the vectors and local Chroma index; this is not model training. The package does not include a transferred vector cache. Subsequent unchanged text can reuse the local cache.

The second command checks the restored package and runtime fingerprints; it is **not itself proof that every embedding exists**. Check successful embedding-command completion and the app's vector status before relying on hybrid retrieval. A keyword-only fallback is not equivalent to the full setup.

## 7. Start the application

```powershell
.\.venv\Scripts\python.exe app.py serve --config config.workbench.json
```

Keep this terminal open. Visit:

- `http://127.0.0.1:8765/` — Ask a question.
- `http://127.0.0.1:8765/work` — Saved work.
- `http://127.0.0.1:8765/work?kind=impact` — Understand a change.

Leave **Answer style → Automatic** to let the answer use suitable prose, lists or tables. Start with a specific question, inspect at least one citation and read any warnings. Use the [application guide](docs/team/USING_THE_APP.md) for the first walkthrough. Press **Ctrl+C** in the server terminal to stop it.

## Everyday startup

After the first setup, start Ollama and run only:

```powershell
cd C:\work\payments
.\.venv\Scripts\python.exe app.py serve --config config.workbench.json
```

Do not rebuild embeddings every time you ask a question. Old saved answers are not automatically regenerated after code changes. Refresh the browser after an update, and stop/restart the server after changing Python code.

## If you want to add documents

`config.workbench.json` is the versioned source-handoff configuration. Keep it unchanged. Stop the server, and create a personal configuration only if one does not already exist:

```powershell
if (Test-Path config.json) { throw 'A personal config already exists. Preserve it and check with the team.' }
Copy-Item config.workbench.json config.json
.\run.cmd
```

Now use the staged [document intake guide](docs/ADDING_DOCUMENTS_QUICKSTART.md). Review the extracted content, build and validate the candidate before activation. New or changed chunks need embeddings; unrelated unchanged chunks can reuse their cache. Adding a document does not automatically add reviewed links to the maintained graph. Personal configuration and uploads stay out of Git.

## Common problems

| Symptom | What to do |
|---|---|
| Python, Git or Ollama is not recognised | Install it, reopen PowerShell and repeat the version check. |
| `run.ps1` is blocked | Use the `.cmd` commands above; do not change system security policy. |
| Restore says the checkout path is too long | Use a shorter folder; the preflight check protects the files. |
| Model service unavailable | Open Ollama. `ollama list` should show both configured models. |
| Model digest mismatch | Record the mismatch and ask the team before treating results as reproducible. |
| Vectors unavailable or only keyword retrieval works | Check step 6 and confirm you used the same configuration for embedding and serving. |
| Port 8765 is already in use | Check whether your existing server is running. Stop it, or use `serve --config config.workbench.json --port 8767` and open port 8767. |
| An answer is incomplete or a check is unavailable | Inspect the evidence and report the case; restarting or approving it does not establish correctness. |
| Graph status is degraded | Check source/graph verification. Ordinary retrieval can still work, but do not claim full graph assistance. |
| Output is slow | Close unnecessary GPU-heavy programs and retry one request. Record timing and hardware; do not increase token limits blindly. |

Keep source files, saved work and error messages when asking for help. Do not share credentials or personal documents in a public issue.
