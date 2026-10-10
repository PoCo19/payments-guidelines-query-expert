# Adding fresh documents: the simple version

Think of each import as preparing a new edition of the library. The current edition stays usable while we check the next one.

**Download → upload and register → review extraction → build index → activate.**

## Add a document in the app

1. Restart the app with `run.cmd` after installing these code changes, then refresh the browser. Choose **Add documents** in the main menu.
2. Upload a text-readable PDF or Markdown file. Fill in title, issuer, document type, official reference, product/topic labels, source URL and acquisition date. Add known issue/update dates and source limitations.
3. Click **Upload and preview**. Inspect the extracted text. Duplicate sources are flagged; thin or empty text is quarantined unless you explicitly accept partial extraction. Scans need OCR first.
4. Add any other files, check the review box and choose **Prepare this batch**.
5. Choose **Build index**. The app chunks the text, reuses unchanged embeddings, generates new embeddings and validates Chroma/SQLite. Keep the server running.
6. Inspect the result, choose **Activate reviewed version**, then **Confirm activate**. The running app loads the new library and refreshes automatically.
7. If needed, open **Add documents → Library versions → Roll back this activation** and confirm rollback. Both versions are retained.

Maximum 10 MB per file, 500 PDF pages and 10 uploads per batch. The preview shows at most the first three pages, so review the full source separately. Before preparation, browser reload loses the on-screen selection; upload again. Prepared releases remain in Library versions. An answer or another import cannot run during a build on the same server. Source URLs record provenance; the app does not fetch them.

## Command-line workflow and revisions

The command-line flow remains available, including reviewed replacements of an existing snapshot. Its activation requires restarting the app, unlike browser activation.

## What you provide

1. A text-readable PDF or Markdown file. Saving a file alone does not trigger indexing.
2. A small JSON **manifest**: the file's identity card. It records its title, issuer, official source link, dates and product/topic labels. One manifest can contain several documents.

The actual eight-document RBI example is [inbox/rbi-core-20261009/intake.json](../inbox/rbi-core-20261009/intake.json). Open it beside [e-mandates.md](../inbox/rbi-core-20261009/e-mandates.md) to see how the identity card points to the text. These are local files and are Git-ignored.

## What each command does

| Stage | What happens | Does the running app change? |
|---|---|---|
| `prepare` | Checks identities and dates, preserves source copies, extracts text and prepares a separate release containing old and new documents. Poor extraction is quarantined. | No |
| `build` | Runs the existing clause-aware chunker, reuses unchanged vectors, embeds new chunks with Ollama, builds Chroma and SQLite, then validates them. | No |
| `activate` | Selects the validated release in the app configuration; saves the previous configuration for rollback. | On the next restart |
| Restart `run.cmd` | Loads the selected knowledge base. New evidence becomes available to search and answers. | Yes |

For a future batch, put files and a manifest in `inbox/my-next-batch/`, then run from the project folder:

```powershell
.\ingest.cmd prepare --manifest inbox\my-next-batch\intake.json --release payments-next-batch
.\ingest.cmd build --release payments-next-batch
.\ingest.cmd status --release payments-next-batch
```

Review the candidate and its `validation.json` before activation. Stop the regular app with Ctrl+C, then:

```powershell
.\ingest.cmd activate --release payments-next-batch
.\run.cmd
```

Use a new release name for the next batch. Do not rerun the already completed RBI release as a new import. Detailed preview and rollback instructions are in [DOCUMENT_INTAKE.md](DOCUMENT_INTAKE.md).

## What actually happened with the RBI batch

- Imported the eight documents from **Direct payments core** in our source map.
- The RBI HTML bodies were accessible; their PDF download links did not return PDFs. Saved the original HTML and converted the document bodies to Markdown, preserving embedded tables, footnotes and links.
- The eight new documents produced **420 chunks and 420 new embeddings**. The build reused **14,060 existing NPCI embeddings**.
- Total candidate index: **14,480 chunks**, **1,570 searchable documents**, and **1,929 register entries** including availability gaps.
- The index is a complete new snapshot. Reusing vectors avoids running the embedding model again on unchanged text; it does not mean editing the old Chroma collection in place.

## Which file is which?

| Location | Meaning |
|---|---|
| `inbox/rbi-core-20261009/*.html` | Original RBI webpage snapshots, retained for provenance |
| `inbox/rbi-core-20261009/*.md` | Converted document text, also available for reading outside the app |
| `inbox/rbi-core-20261009/intake.json` | The eight-document registration manifest |
| `inbox/rbi-core-20261009/html_acquisition.json` | Source URLs, hashes and conversion checks |
| `data/releases/payments-rbi-core-20261009/` | Combined NPCI + RBI corpus, metadata, Chroma and validation records |
| `reports/rbi-core-20261009/validation.json` | Saved retrieval and live answer observations |

## Boundaries to remember

There is no upload screen, automatic website watcher or scheduled ingestion yet. This version is a deliberate, operator-run import. Downloading and source review precede it.

HTML-derived documents have one **logical page**, not physical PDF page numbers. Separate linked forms, annex downloads and other referenced documents are not automatically imported. The source reader and answer notices disclose this limitation.

For an updated document, register a new snapshot ID and explicitly identify the previous one using `revision_of` and its hash. This preserves history and avoids accidental replacement; it does not decide legal supersession. Changing the answer model does not require re-embedding. Changing the embedding model does.
