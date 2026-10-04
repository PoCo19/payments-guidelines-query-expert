# Source and conversion quality notes

Issue-date coverage: **2023-01-01 through 2026-09-22**. Archive filters 2023, 2024, 2025 and 2026 account for **129 entries**: **107 converted PDFs**, **20 without a public PDF**, **one cancelled entry**, and **one failed public PDF link**. The main date window contains **106 converted circulars / 250 pages**; OC 160 (one page, dated 2022) is retained separately. The 2023 archive adds 31 converted PDFs / 59 pages.

## Collection and provenance

The 2023 archive was fully paginated on 23 September 2026 (39 rows); 2024–2026 listings and sources were collected on 22 September 2026 (32, 41 and 17 rows). Only the Circulars tab and those year filters are covered. This is not a claim to possess non-public circulars, every historic parent, or material from other archive tabs. Public originals are preserved unchanged with SHA-256 hashes in index.json.

All 31 added PDFs were parsed successfully and all 31 issue dates were checked against source page headers. Original circular references were recovered for the two compliance listings that omitted numbers. PCOMP-Q4 and PCOMP-Q2Q3 remain only in stable local record IDs; official_reference records the actual identifiers. RuPay 022 remains a separate series from UPI circulars.

## Date and version exceptions

- OC 160: filed in 2023, issued 28 December 2022; retained separately.
- OC 165 and OC 187: originally issued 19 April and 26 December 2023; current public versions explicitly updated on 23 February 2026.
- OC 193A: listed under 2025/FY 2025-26; PDF is dated 10 September 2024/FY 2024-25.
- OC 193B: listed under 2025/FY 2025-26; PDF is dated 4 December 2024/FY 2024-25.
- OC 76B: unavailable public source; date 23 August 2024 cited in OC 76C.
- OC 166: cancelled in the 2023 listing; its text and date are not inferred.

## Extraction and limits

The 107 source PDFs contain 251 pages: 203 OCR pages and 48 pages with embedded text. Every page has a source image. Reading copies organize paragraphs, clauses and page boundaries. Letterhead noise and postal footers are removed where reliably detected. Raw extraction is retained in JSONL; for manually corrected pages, text contains the corrected reading copy and raw_extracted_text preserves the original extraction.

This is not a word-for-word certified edition. Rupee symbols can be mistaken for digits; scanned table cells, screenshots and diagrams can be flattened or incomplete. High OCR confidence does not establish accuracy. Verify amounts, deadlines, codes and table relationships against the supplied originals. Native-text tables are explicitly labelled as automatic extractions. No provisions were deliberately replaced by summaries.

## Source-checked reading copies

The following page transcriptions were checked against source images and selected errors corrected. This limited review does not certify the other pages.

- 2026-OC-235, page 2
- 2026-OC-226A, page 1
- 2026-OC-177A, page 1
- 2025-OC-185B, page 2
- 2025-OC-169A, page 1
- 2023-UPI-151A, page 1
- 2023-UPI-151A, page 2
- 2023-UPI-151A, page 3
- 2023-UPI-181, page 1
- 2023-UPI-177, page 2
- 2023-UPI-169, page 1

## Pages requiring priority review

Original OCR confidence below 80, excluding pages subsequently source-checked. Other pages can still contain errors.

| Record | Page | Engine confidence | Source |
|---|---|---|---|
| 2026-OC-229A | 3 | 74 | [Page image](page_images/2026-08-24_OC-229A-p003.jpg) |
| 2026-OC-229A | 4 | 68 | [Page image](page_images/2026-08-24_OC-229A-p004.jpg) |
| 2026-OC-229A | 5 | 75 | [Page image](page_images/2026-08-24_OC-229A-p005.jpg) |
| 2026-OC-229A | 6 | 71 | [Page image](page_images/2026-08-24_OC-229A-p006.jpg) |
| 2026-OC-229A | 7 | 73 | [Page image](page_images/2026-08-24_OC-229A-p007.jpg) |
| 2026-OC-234 | 2 | 73 | [Page image](page_images/2026-06-05_OC-234-p002.jpg) |
| 2026-OC-208C | 6 | 72 | [Page image](page_images/2026-04-23_OC-208C-p006.jpg) |
| 2025-OC-229 | 3 | 74 | [Page image](page_images/2025-11-12_OC-229-p003.jpg) |
| 2025-OC-229 | 5 | 58 | [Page image](page_images/2025-11-12_OC-229-p005.jpg) |
| 2025-OC-222A | 2 | 72 | [Page image](page_images/2025-10-29_OC-222A-p002.jpg) |
| 2025-OC-222 | 2 | 73 | [Page image](page_images/2025-09-12_OC-222-p002.jpg) |
| 2025-OC-221 | 4 | 70 | [Page image](page_images/2025-09-12_OC-221-p004.jpg) |
| 2025-OC-208A | 2 | 72 | [Page image](page_images/2025-06-30_OC-208A-p002.jpg) |
| 2025-OC-208A | 3 | 71 | [Page image](page_images/2025-06-30_OC-208A-p003.jpg) |
| 2025-OC-208A | 4 | 76 | [Page image](page_images/2025-06-30_OC-208A-p004.jpg) |
| 2025-OC-184B | 3 | 49 | [Page image](page_images/2025-06-26_OC-184B-p003.jpg) |
| 2025-OC-216 | 2 | 57 | [Page image](page_images/2025-06-06_OC-216-p002.jpg) |
| 2025-OC-216 | 3 | 45 | [Page image](page_images/2025-06-06_OC-216-p003.jpg) |
| 2024-OC-208 | 5 | 65 | [Page image](page_images/2024-10-03_OC-208-p005.jpg) |
| 2024-OC-198 | 2 | 72 | [Page image](page_images/2024-06-21_OC-198-p002.jpg) |
| 2024-OC-197 | 2 | 78 | [Page image](page_images/2024-06-14_OC-197-p002.jpg) |
| 2023-UPI-175 | 3 | 77 | [Page image](page_images/2023-10-27_2023-UPI-175-p003.jpg) |
| 2023-UPI-175 | 4 | 66 | [Page image](page_images/2023-10-27_2023-UPI-175-p004.jpg) |
| 2023-UPI-175 | 5 | 54 | [Page image](page_images/2023-10-27_2023-UPI-175-p005.jpg) |
| 2023-UPI-175 | 6 | 74 | [Page image](page_images/2023-10-27_2023-UPI-175-p006.jpg) |
