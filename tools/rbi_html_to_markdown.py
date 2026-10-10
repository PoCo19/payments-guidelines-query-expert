"""Convert acquired RBI article bodies to Markdown (requires lxml).

Uses the unique tablecontent2 article, not navigation. Does not infer PDF pages.
Retains inline links, footnotes, headings and table rows. Saved HTML is evidence.
"""
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import urljoin


def clean(text):
    return re.sub(r'\s+', ' ', text or '').strip()


def convert(raw, source_url):
    from lxml import html
    tree = html.fromstring(raw.decode('utf-8-sig'))
    bodies = tree.xpath('//tr[contains(concat(" ",normalize-space(@class)," ")," tablecontent2 ")]')
    if len(bodies)!=1:
        raise ValueError('Expected exactly one RBI article body')
    body = bodies[0]
    titles=tree.xpath('//td[contains(@class,"tableheader")]/b')
    if not titles:
        raise ValueError('Article title missing')
    title=clean(titles[0].text_content())

    def render(e):
        tag=e.tag.lower() if isinstance(e.tag,str) else ''
        if tag in ('script','style'):
            return ''
        inner=(e.text or '')+''.join(render(c)+(c.tail or '') for c in e)
        if tag=='br':return '\n'
        if tag=='a':
            href=e.get('href','')
            if not clean(inner):return ''
            return f'[{clean(inner)}]({urljoin(source_url,href)})' if href else inner
        if tag=='sup':return ' ['+clean(inner)+'] '
        if tag in ('b','strong'):return '**'+clean(inner)+'**'
        if tag=='img':
            raise ValueError('Article contains an image: review image content before import')
        if tag=='table' and not e.xpath('.//table'):
            rows=[]
            for row in e.xpath('./tr|./tbody/tr|./thead/tr|./tfoot/tr'):
                cells=row.xpath('./td|./th')
                rows.append([clean(render(cell)).replace('|','\\|') for cell in cells])
            if not rows:return inner
            width=max(map(len,rows))
            if width==1:
                return '\n\n'+'\n\n'.join(row[0] for row in rows if row)+'\n\n'
            # Avoid inventing labels: first source row stays the first row.
            lines=['| '+' | '.join(row+['']*(width-len(row)))+' |' for row in rows]
            return '\n\n'+lines[0]+'\n| '+' | '.join(['---']*width)+' |\n'+'\n'.join(lines[1:])+'\n\n'
        if tag in ('p','h1','h2','h3','h4'):
            if 'head' in e.get('class','').split() or tag.startswith('h'):
                return '\n\n## '+clean(inner).strip('*')+'\n\n'
            return '\n\n'+inner.strip()+'\n\n'
        if tag=='li':return '\n- '+inner.strip()+'\n'
        if tag=='hr':return '\n\n---\n\n'
        return inner

    markdown='# '+title+'\n\n'+render(body)
    markdown=re.sub(r'\n[ \t]+','\n',markdown)
    markdown=re.sub(r'\n{3,}','\n\n',markdown).strip()+'\n'
    # Every alphanumeric source token must remain in the conversion, in order.
    original=re.findall(r'\w+',' '.join(body.itertext()).casefold())
    rendered=re.findall(r'\w+',markdown.casefold())
    at=0
    for word in original:
        while at<len(rendered) and rendered[at]!=word:at+=1
        if at==len(rendered):raise ValueError('Source token sequence lost at '+word)
        at+=1
    return title,markdown,dict(source_words=len(original),retained_source_token_sequence=True,
                               tables=len(body.xpath('.//table[not(.//table)]')),
                               page_basis='logical_markdown',pdf_pagination_verified=False)


def main():
    import argparse
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('directory',type=Path)
    args=parser.parse_args();records=json.loads((args.directory/'acquisition.json').read_text(encoding='utf-8'))
    for record in records:
        raw=(args.directory/(record['slug']+'.html')).read_bytes()
        title,md,qa=convert(raw,record['source_url'])
        target=args.directory/(record['slug']+'.md');target.write_text(md,encoding='utf-8')
        record.update(status='html_converted_pending_review',title=title,file=target.name,
                      html_sha256=hashlib.sha256(raw).hexdigest(),markdown_sha256=hashlib.sha256(target.read_bytes()).hexdigest(),
                      extraction_qa=qa,pdf_status=record.get('error','PDF unavailable'))
        print(record['slug'],qa,flush=True)
    (args.directory/'html_acquisition.json').write_text(json.dumps(records,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')


if __name__=='__main__':main()
