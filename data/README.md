# Included research data

The active application uses `all-products-v1/`: 1,921 register records, 1,562 searchable documents and 4,826 source pages. The corpus is an imported snapshot of NPCI circulars, with 359 unavailable or excluded records. Availability and extraction limitations are retained.

- [Structured register](all-products-v1/index.json)
- [Page text](all-products-v1/all_circular_pages.jsonl)
- [Source Markdown](all-products-v1/sources/circulars/)
- [Product inventories](all-products-v1/sources/inventory/)
- [Source hashes](all-products-v1/source_manifest.json)

The small original UPI dataset directly in this directory is retained for regression tests and provenance comparisons. It is not the active application corpus.

Original PDFs remain at their recorded official URLs. Models, Chroma indexes and generated SQLite databases are excluded from Git; build vectors locally with `run.cmd embed`. Do not treat a missing document as evidence that no requirement exists, or a reference link as proof of supersession.

The circular content originates from NPCI; this independent capstone does not imply NPCI affiliation or ownership of the source documents. Preserve source attribution when reusing it.
