# RBI core integration — acquired 9 October, status reconciled 10 October 2026

The release `payments-rbi-core-20261009` is activated in `config.json`. The previous NPCI corpus is retained. A running server must be restarted to load the changed configuration.

## Coverage

Eight documents from the source map's **Direct payments core** section were imported:

1. Prepaid Payment Instruments (PPIs), issued 27 August 2021, updated 30 September 2026.
2. Regulation of Payment Aggregator, 15 September 2025.
3. Bharat Bill Payment System Directions, 29 February 2024.
4. Cyber Resilience and Digital Payment Security Controls for non-bank PSOs, 30 July 2024.
5. Authentication mechanisms for digital payment transactions, 25 September 2025.
6. Digital Payments — E-mandate Framework, 21 April 2026.
7. Authorisation to operate a Payment System, 15 June 2026.
8. Access Criteria for Payment Systems, body dated 17 January 2017, updated 28 July 2021. The catalogue's 19 January issue date is recorded as a discrepancy.

Official links are in [the source map](RBI_PAYMENTS_SOURCE_MAP.md) and the actual [intake manifest](../inbox/rbi-core-20261009/intake.json). Other source-map sections have not been imported by this batch.

## Acquisition and index

Official HTML bodies were accessible; the primary PDF links returned non-PDF responses. The saved HTML was converted to Markdown while preserving the article's alphanumeric token sequence, embedded tables, footnotes and links. This structural check does not independently verify meaning or table layout. Separate linked forms and documents are not automatically included.

Each document has one logical Markdown page, explicitly distinguished from physical PDF pagination in the reader. Original HTML, Markdown, hashes, acquisition records and the manifest are retained in `inbox/rbi-core-20261009/`. These local files and corpus releases are Git-ignored.

The candidate reused 14,060 existing vectors and computed 420 new vectors with the existing Qwen embedding model. Total: 14,480 chunks, 1,570 searchable documents and 1,929 register records. The build took 54.91 seconds. Generation-model and token-limit settings were not changed.

## Validation and unresolved issues

- Structural validation, source hashes, vector counts and model digest passed before activation.
- All eight developer retrieval questions located the expected RBI document. Filtered vector search worked for each document.
- The mixed-source AutoPay/FASTag/NCMC question retrieved both RBI and NPCI evidence.
- Selected-document summary and comparison evidence routes were exercised; coverage limitations remain visible.
- Browser checks confirmed the new coverage label, topic filtering, library records and source-reader limitations.
- 230 Python regression tests passed. Four optional HTML-converter tests passed separately using the bundled runtime with lxml. Both JavaScript suites and JavaScript syntax checks passed.
- The live generated answer returned two claims accepted by the existing automated support checker, but took **718.943 seconds**. The additional completeness review was unavailable. This is a significant latency finding, not an acceptable performance baseline or proof of correctness.

Evidence: `reports/rbi-core-20261009/validation.json`, the release's `validation.json` and `embedding_build.json`. The tests are developer smoke checks; independent mixed-source answer evaluation remains pending. The original 50-case evaluation was not rerun against this expanded corpus in this intake.

## Next priorities

First instrument and bound each generation/review stage, diagnose the long live request, and make unavailable review stages explicit. Then independently review mixed-source questions for attribution, conditions, exceptions and omissions. A simple intake screen can follow the stable existing prepare/build/activate workflow. Larger-model and context experiments should use the same reviewed cases and measure end-to-end latency.

For a beginner explanation of the pipeline and commands, read [Adding documents](ADDING_DOCUMENTS_QUICKSTART.md).
