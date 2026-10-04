"""Build a readable catalogue from the frozen benchmark; never modify its cases."""
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STAMP = '20261003T172349Z'
DEST = ROOT / 'evaluation/INITIAL_50_QUESTIONS.md'


def build():
    raw = (ROOT / 'evaluation/rag_cases.json').read_bytes()
    checksum = hashlib.sha256(raw).hexdigest()
    assert checksum == (ROOT / 'evaluation/rag_cases.sha256').read_text().strip()
    cases = json.loads(raw)
    assert len(cases) == 50 and len({c['id'] for c in cases}) == 50
    index = {d['id']: d for d in json.loads((ROOT / 'data/index.json').read_text(encoding='utf-8-sig'))}
    pages = {(p['document_id'], p['source_page']): ' '.join(p['text'].split())
             for p in map(json.loads, (ROOT / 'data/all_circular_pages.jsonl').read_text(encoding='utf-8-sig').splitlines())}
    result = json.loads((ROOT / f'output/midsem/evidence/{STAMP}/retrieval.json').read_text())
    assert result['dataset_sha256'] == checksum
    runs = {name: {r['id']: r for r in run['rows']} for name, run in result['runs'].items()}
    methods = [('bm25', 'BM25'), ('vector', 'Vector'), ('hybrid', 'Hybrid'), ('hybrid_reranked', 'Hybrid + reranker')]
    counts = Counter(len(c['references']) for c in cases)
    assert counts == {1: 33, 2: 11, 0: 6}
    lines = ['# Initial 50-question evaluation catalogue', '',
        '**Payments Guidelines Query Expert | Frozen preliminary benchmark | Documented 4 October 2026**', '',
        'This catalogue records the original questions and draft expected answers verbatim. It explains the test design and saved retrieval observations; it is not a new evaluation run or a verified payments rulebook. All 50 cases are AI-assisted and awaiting independent review.', '',
        '## Read this first', '',
        '- **Question:** the exact input in the frozen dataset.',
        '- **Draft expected answer:** the original reference intent, not an actual model response or an independently approved answer.',
        '- **Source anchor:** a document ID, original source page number and short text fragment used to check retrieval. A fragment locates evidence; it may not support every condition in the draft answer by itself.',
        '- **Observed result:** evidence retrieval only, from the saved 3 October 2026 run. No answer-quality score is implied.',
        '- **Review status:** `draft_requires_independent_review` for every case. Fill the existing [independent review sheet](independent_review.csv); do not overwrite the frozen JSON.', '',
        '## How 50 questions produce 55 evidence checks', '',
        '| Case group | IDs | Questions | Expected anchors | Purpose |',
        '|---|---|---:|---:|---|',
        '| Focused questions | RAG-001 to RAG-032 | 32 | 32 | Find a specific requirement or responsibility |',
        '| Summaries | RAG-033 to RAG-038 | 6 | 11 | Find selected passages across a document |',
        '| Comparisons | RAG-039 to RAG-044 | 6 | 12 | Find evidence from both named circulars |',
        '| Negative cases | RAG-045 to RAG-050 | 6 | 0 | Check behaviour when the requested evidence is unavailable or unsuitable |',
        '| **Total** | | **50** | **55** | |', '',
        '**50 = 44 positive + 6 negative questions. 55 = (33 questions x 1 anchor) + (11 questions x 2 anchors).** The six negative cases are part of the 50, not six additional questions. RAG-036 is the one summary with only one anchor. These are 55 question-to-source checks, not 55 unique documents, unique passages or correct answers.', '',
        '## Scope, execution and limitations', '',
        'The set is UPI-focused, with one RuPay credit-card-on-UPI question (RAG-032). It does not establish quality across the entire multi-product corpus. The runner uses the case series when provided, otherwise UPI; thus a blank dataset series does not mean an unfiltered search in this experiment.', '',
        'RAG-001 to RAG-032 are labelled `development`; RAG-033 to RAG-050 are labelled `reserved_review`. All 50 were run and their aggregate results inspected. The latter label does not establish an untouched held-out test set. New independently reviewed questions are needed for that purpose.', '',
        'The dataset route is a descriptive label. The saved runner does not force this route; it lets the application route each question and records the observed route. Strict scope limits evidence to the selected circular scope; related scope permits bounded related evidence. Neither scope establishes supersession. The date cutoff filters available issues/revisions; it does not reconstruct all rules legally effective on that date.', '',
        'The runner uses `mode=evidence`. A positive anchor passes when a returned source has the expected document ID and page, and its whitespace-normalised text contains the recorded quote. A negative case passes the retrieval check when no sources are returned. That is different from testing whether a language model correctly declines to answer after seeing irrelevant evidence.', '',
        'Most questions explicitly name circulars. The six comparison questions also include hints that closely resemble their draft expected answers. Summary references are generic instructions rather than complete reference summaries. Selected anchors do not establish full summary coverage. These limitations make the set useful for regression checks but weak evidence of general research performance.', '',
        'Source fragments retain extraction spellings such as "empanelied" to preserve the frozen matching rule. Read the linked Markdown for surrounding context and check original page images/PDFs for critical wording, figures and qualifiers. Current links are taken from the saved inventory; live NPCI availability was not rechecked for this document.', '',
        '## Saved preliminary results', '',
        '| Method | Anchors found | Negative cases returning no sources | Median retrieval ms |',
        '|---|---:|---:|---:|']
    for key, label in methods:
        summary = result['runs'][key]['summary']
        assert sum(sum(r['anchor_hits']) for r in runs[key].values()) == summary['anchors_found']
        lines.append(f"| {label} | {summary['anchors_found']}/{summary['anchors_expected']} | {summary['negative_empty']}/{summary['negative_cases']} | {summary['median_ms']} |")
    lines += ['', 'All methods found the selected anchors. RAG-048 returned irrelevant evidence in the three semantic variants, while BM25 returned none. This does not demonstrate perfect answers or establish that BM25 is best for all questions. Timings are from one warmed, interleaved pass and exclude answer generation. Summary/comparison routes bypass reranking; 15 such routes appear in this run, including negative scenarios.', '',
        f'[Saved run and configuration](../output/midsem/evidence/{STAMP}/retrieval.json) | [Runner](midsem_check.py) | [Creation provenance](dataset_creation_provenance.txt)', '',
        '## Question directory', '', '| ID | Question |', '|---|---|']
    for c in cases:
        lines.append(f"| [{c['id']}](#{c['id'].lower()}) | {c['query'].replace('|', '&#124;')} |")
    purposes = {
        'clause': 'Locate the stated requirement in its own circular; review the answer for omitted conditions and correct participant attribution.',
        'summary': 'Retrieve the selected section/page anchors. Full summary completeness requires an additional human-authored checklist.',
        'compare': 'Retrieve both named sources and attribute each requirement separately, without inferring supersession.',
    }
    negatives = {
        'RAG-045': 'Unavailable reference in this snapshot: do not invent the contents of OC 999.',
        'RAG-046': 'Listed but unavailable content: the saved register records OC 237 without a public PDF. Do not infer its requirements from the listing.',
        'RAG-047': 'Incomplete comparison: do not provide a complete comparison when the requested OC 999 evidence is missing.',
        'RAG-048': 'Out-of-domain question: payment circulars should not be treated as evidence about quantum photosynthesis.',
        'RAG-049': 'Date-filter exclusion: OC 201A is excluded under the 2024-12-31 cutoff. Do not silently use a later circular.',
        'RAG-050': 'Near-match reference: do not silently substitute OC 186 or 186A for the requested OC 186AA.',
    }
    for c in cases:
        lines += ['', f"## {c['id']}", '', f"**Question:** {c['query']}", '',
                  f"**Test purpose:** {negatives.get(c['id'], purposes.get(c['route'], ''))}", '',
                  f"**Draft expected answer (verbatim):** {c['expected_answer']}", '',
                  f"**Settings:** dataset route `{c['route']}`; series `{c.get('series') or 'blank (runner uses UPI)'}`; scope `{c['scope']}`; cutoff `{c.get('cutoff') or 'none'}`; split `{c['split']}`.", '',
                  '**Review status:** AI-assisted; independent source and answer review pending.', '', '**Expected source anchors:**', '']
        if not c['references']:
            lines.append('None. Expected behaviour is to decline on the available evidence; the saved retrieval test measures only whether the source list is empty.')
        for a in c['references']:
            assert a['quote'] in pages[a['document_id'], a['page']]
            doc = index[a['document_id']]
            md = ROOT / 'data' / doc['markdown_file']
            assert md.is_file(), md
            lines += [f"- `{a['document_id']}`, source page **{a['page']}**: [source Markdown](../data/{doc['markdown_file']}) | [original PDF]({doc['source_pdf']}#page={a['page']}).", f"  Anchor text: {a['quote']}"]
        observations = []
        for key, label in methods:
            row = runs[key][c['id']]
            assert row['query'] == c['query']
            if c['references']:
                value = f"{sum(row['anchor_hits'])}/{len(c['references'])} anchors"
            else:
                value = 'no sources returned' if row['empty'] else 'sources returned (negative retrieval check failed)'
            observations.append(f'{label}: {value}')
        observed_routes = ', '.join(sorted({runs[k][c['id']]['route'] for k, _ in methods}))
        lines += ['', '**Saved retrieval observation:** ' + '; '.join(observations) + '.', '', f'**Observed application route:** `{observed_routes}`. Generated-answer correctness: **not scored by this run**.']
    lines += ['', '## Review procedure and next evaluation', '',
        '1. Read the complete source passages, including conditions outside the short anchor. Check the original when extraction is uncertain.',
        '2. Record reviewer identity and source verification in `independent_review.csv`. Record disagreements and resolve them explicitly.',
        '3. Write complete required-fact checklists, especially for summaries and comparisons, in a new benchmark version. Preserve these original 50 cases and their checksum.',
        '4. Capture actual generated answers and exact supplied evidence before scoring with RAGAS. Score displayed answer blocks/claims, not the API status-message field.',
        '5. Keep retrieval, answer completeness/correctness, citation support, appropriate abstention and latency separate. A valid citation ID alone does not prove support.',
        '6. Add new questions without circular-number or answer hints, plus ambiguity and incomplete-source scenarios. Reserve a genuinely unexposed set for final evaluation.', '',
        'No RAGAS scores or independent-review outcomes have been added by this documentation task.', '',
        '## Reproducibility', '',
        '[Frozen questions](rag_cases.json) | [Checksum](rag_cases.sha256) | [Human review sheet](independent_review.csv)', '',
        f'Dataset SHA-256: `{checksum}`.', '',
        'Regenerate this catalogue with `python tools/document_initial_benchmark.py`. The builder validates the frozen checksum, case IDs, source-anchor text, local source links and recorded counts before writing this Markdown. These checks establish faithful documentation, not expert verification of the source interpretation.', '']
    DEST.write_text('\n'.join(lines), encoding='utf-8')
    print(f'Created {DEST}: 50 cases, 55 anchors, 200 saved case-method observations.')


if __name__ == '__main__':
    build()
