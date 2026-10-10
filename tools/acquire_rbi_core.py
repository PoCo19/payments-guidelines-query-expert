"""Acquire the eight explicitly selected RBI core sources; no automatic activation.

Keeps HTML provenance and the PDF linked by the official page. Review these
snapshots before creating an intake manifest. This is not a website monitor.
"""
import concurrent.futures
import datetime
import hashlib
from html.parser import HTMLParser
import io
import json
from pathlib import Path
import urllib.request
from urllib.parse import urljoin, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SOURCES = [('12156','ppi'), ('12896','payment-aggregators'), ('12616','bbps'),
           ('12715','nonbank-pso-cyber'), ('12898','authentication'),
           ('13374','e-mandates'), ('13502','authorisation'), ('10833','access-criteria')]


class PDFLinks(HTMLParser):
    def __init__(self):
        super().__init__(); self.links = []

    def handle_starttag(self, tag, attrs):
        href = dict(attrs).get('href','')
        if tag == 'a' and urlsplit(href).path.lower().endswith('.pdf'):
            self.links.append(href)


def get(url):
    parsed = urlsplit(url)
    if parsed.scheme != 'https' or parsed.hostname not in ('www.rbi.org.in','rbidocs.rbi.org.in'):
        raise ValueError('Only the selected official RBI hosts are allowed')
    with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'}),timeout=45) as response:
        if urlsplit(response.url).hostname not in ('www.rbi.org.in','rbidocs.rbi.org.in'):
            raise ValueError('Unexpected source redirect')
        return response.read()


def acquire(item, destination):
    from pypdf import PdfReader
    page_id, slug = item
    url = 'https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id='+page_id
    result = dict(page_id=page_id, slug=slug, source_url=url,
                  retrieved_at=datetime.datetime.now(datetime.timezone.utc).isoformat())
    try:
        html = get(url)
        (destination/(slug+'.html')).write_bytes(html)
        parser = PDFLinks(); parser.feed(html.decode('utf-8',errors='replace'))
        # The primary document must be a notification PDF, not a sidebar/annex link.
        links = list(dict.fromkeys(urljoin(url,h) for h in parser.links if '/notification/' in h.lower()))
        if not links:
            raise ValueError('No primary notification PDF found; manual source review needed')
        pdf_url = links[0]
        raw = get(pdf_url)
        if not raw.startswith(b'%PDF-'):
            raise ValueError('Official PDF link did not return a PDF')
        pdf = PdfReader(io.BytesIO(raw))
        pages = [p.extract_text() or '' for p in pdf.pages]
        if not pages or sum(len(p.split()) for p in pages)<100:
            raise ValueError('PDF extraction is empty or implausibly short')
        (destination/(slug+'.pdf')).write_bytes(raw)
        (destination/(slug+'.md')).write_text('\n\n'.join(f'<!-- Page {i+1} -->\n\n{text}' for i,text in enumerate(pages))+'\n',encoding='utf-8')
        result.update(status='downloaded_pending_review', pdf_url=pdf_url, file=slug+'.pdf',
                      pdf_sha256=hashlib.sha256(raw).hexdigest(), html_sha256=hashlib.sha256(html).hexdigest(),
                      pages=len(pages), words=sum(len(p.split()) for p in pages),
                      thin_pages=[i+1 for i,p in enumerate(pages) if len(p.split())<15],
                      first_page=pages[0][:3000], last_page_end=pages[-1][-500:])
    except Exception as exc:
        result.update(status='unavailable',error=str(exc))
    return result


def main():
    destination = ROOT/'inbox'/('rbi-core-'+datetime.date.today().strftime('%Y%m%d'))
    destination.mkdir(parents=True,exist_ok=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        results = list(pool.map(lambda item:acquire(item,destination),SOURCES))
    (destination/'acquisition.json').write_text(json.dumps(results,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    for r in results:
        print(r['slug'], r['status'],r.get('pages'), r.get('error',''),flush=True)
    print('Saved:',destination)


if __name__=='__main__':
    main()
