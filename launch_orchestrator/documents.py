"""Preview bounded text from uploaded documents without retaining uploaded binaries."""
import base64
import io
import zipfile
from pathlib import Path
from xml.etree import ElementTree


def extract_document(payload):
    name=payload.get('name','')
    if not isinstance(name,str) or not 1<=len(name)<=200:raise ValueError('Choose a document with a valid filename')
    suffix=Path(name).suffix.lower()
    if suffix not in ('.txt','.md','.pdf','.docx'):raise ValueError('Choose a PDF, DOCX, Markdown or text document')
    try:data=base64.b64decode(payload.get('data',''),validate=True)
    except Exception as exc:raise ValueError('The uploaded file could not be read. Choose it again.') from exc
    if not 0<len(data)<=5*1024*1024:raise ValueError('Choose a file smaller than 5 MB')
    note='';pages=None
    try:
        if suffix in ('.txt','.md'):text=data.decode('utf-8-sig')
        elif suffix=='.docx':
            with zipfile.ZipFile(io.BytesIO(data)) as archive:
                info=archive.getinfo('word/document.xml')
                if info.file_size>4*1024*1024:raise ValueError('The document text is too large. Upload a shorter document.')
                xml=archive.read(info)
                if b'<!DOCTYPE' in xml or b'<!ENTITY' in xml:raise ValueError('Unsupported document XML')
                root=ElementTree.fromstring(xml);ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
                text='\n\n'.join(''.join(t.text or '' for t in p.findall('.//w:t',ns)) for p in root.findall('.//w:p',ns))
            note='Text and table paragraphs extracted. Images, comments and layout are not included.'
        else:
            from pypdf import PdfReader
            reader=PdfReader(io.BytesIO(data),strict=False)
            if reader.is_encrypted:raise ValueError('Upload an unencrypted copy of this PDF')
            pages=len(reader.pages)
            if pages>60:raise ValueError('Choose a PDF with at most 60 pages or upload the relevant pages separately')
            parts=[]
            for n,page in enumerate(reader.pages):
                stream=page.get_contents()
                if stream is not None and len(stream.get_data())>8*1024*1024:raise ValueError('This PDF page is too complex to extract safely. Upload a text or Markdown version.')
                parts.append(f'[Page {n+1}]\n'+(page.extract_text() or ''))
                if sum(len(x) for x in parts)>100000:break
            text='\n\n'.join(parts);note='PDF text extracted; verify reading order and tables. Scanned images are not OCRed.'
            if not any((p.split('\n',1)[1]).strip() for p in parts):raise ValueError('This PDF has no readable text. Upload an OCRed PDF or its Markdown/text version.')
    except ValueError:raise
    except ImportError as exc:raise ValueError('PDF extraction is not installed. Run setup.cmd or upload Markdown/text.') from exc
    except Exception as exc:raise ValueError('This file could not be extracted. Try an unencrypted PDF, DOCX or UTF-8 text file.') from exc
    if not text.strip():raise ValueError('No readable text was found in this document')
    return {'name':name,'text':text[:24000],'truncated':len(text)>24000,'characters':len(text),'pages':pages,'note':note}
