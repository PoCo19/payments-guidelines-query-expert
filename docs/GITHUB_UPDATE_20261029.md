# Development update — 29 October 2026

This update packages the product-clarity implementation, targeted amendment-context repair, teammate guides, demonstration outline and raw evaluation evidence. It is a development milestone, not production certification.

## Publication checks

- Refreshed GitHub `origin/main` before publication; no divergent teammate commits were present.
- Re-ran all 474 Python tests and four JavaScript suites successfully on the publication candidate and isolated staged-source export. The export used the existing pinned Python environment and locally cached reranker assets verified against the manifest; this was not a fresh internet dependency installation.
- Restored the portable source package from a short temporary checkout: 1,929 register records, 4,834 pages, 14,480 chunks and 20 mixed-source reference cases validated, with matching corpus/registry fingerprints and no model calls. The original nested test path correctly triggered the documented Windows path-length guard.
- Reviewed the changed-file inventory and checked credential patterns: no matching tokens, private keys or credential assignments found. This is a publication check, not an exhaustive security audit.
- Personal configuration, environments, model weights, embeddings, local workflow databases, original-PDF cache and temporary files remain excluded by Git ignore rules.
- Retained final and failed intermediate evaluation records, with their interpretation in the evaluation README. The two full retrieval comparison records (approximately 17.4 MB each uncompressed) are packaged losslessly in `retrieval-records.zip`, with their internal paths retained and SHA-256 equivalence verified. Local uncompressed copies are ignored; no evidence is omitted.
- Existing portable source archive, graph manifest, model configuration and dependency locks are unchanged.

The earlier 144-question paired evaluation retained 223/234 expected passages in both arms, with zero losses. This retrieval result does not establish answer correctness. Final seven model probes still included scope/novelty errors, incomplete answers and noisy completeness findings. Independent payments acceptance remains pending.

## Teammate update

From an existing clone, first preserve any local work with a commit or stash, then run:

```powershell
git pull --ff-only
```

Restart the application and refresh the browser. The existing model and source setup still applies; this update does not require an embedding rebuild or database migration. First-time users should follow [TEAM_START_HERE](../TEAM_START_HERE.md) and [HOW_TO_RUN](../HOW_TO_RUN.md).

The two main tasks are Ask a question and Understand a change. Saved work supports both. See [using the app](team/USING_THE_APP.md), [demonstration](team/DEMONSTRATION.md) and [verification evidence](../evaluation/product_maturity_20261027/README.md).
