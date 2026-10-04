"""Product memberships, stable selections and ambiguity-safe reference resolution."""
import re
ALIASES={'AePS':r'\baeps\b','BHIM Aadhaar':r'\bbhim\s+aadhaar\b','CTS':r'\bcts\b','e-KYC Setu':r'\be[ -]?kyc\s+setu\b','e-RUPI':r'\be[ -]?rupi\b','IMPS':r'\bimps\b','NACH':r'\bnach\b','NETC':r'\bnetc\b|\bfastag\b','NFS':r'\bnfs\b','RuPay':r'\brupay\b','UPI':r'\bupi\b'}
def memberships(doc):return doc.get('product_memberships') or [doc['series']]
def number(value):
 value=str(value or '').upper().strip();m=re.fullmatch(r'0*(\d+)([A-Z]*)',value)
 return str(int(m[1]))+m[2] if m else value

def fiscal_year(doc):
 if doc.get('fiscal_year'):
  return doc['fiscal_year'] if re.fullmatch(r'\d{4}-\d{2}',str(doc['fiscal_year'])) else ''
 date=doc.get('issue_date')
 if not date:return ''
 year=int(date[:4])-(int(date[5:7])<4);return f'{year}-{str(year+1)[-2:]}'

def resolve(engine,query,numbers,series,cutoff,feature,year='',document_ids=None):
 if year and not re.fullmatch(r'\d{4}-\d{2}',year):raise ValueError('Fiscal year must use YYYY-YY, for example 2018-19')
 if document_ids is not None and (not isinstance(document_ids,list) or len(document_ids)>4 or not all(isinstance(x,str) for x in document_ids) or len(set(document_ids))!=len(document_ids)):raise ValueError('Select up to four distinct circulars')
 notes=[];ambiguous=[];missing=[]
 inferred=[name for name,pattern in ALIASES.items() if re.search(pattern,query,re.I)]
 if not series and len(inferred)==1:
  series=inferred[0];notes.append('Product inferred from the question: '+series+'. Use the Product selector to override.')
 if not year:
  match=re.search(r'\bFY\s*(\d{4}-\d{2})\b',query,re.I)
  if match:year=match[1]
 def eligible(d):return engine.eligible(d,series,cutoff) and (not year or fiscal_year(d)==year) and (not feature or feature in engine.registry.features[d['id']])
 requested=[]
 if document_ids:
  for key in document_ids:
   d=engine.by_id.get(key)
   if not d or not eligible(d) or d['availability']!='converted':missing.append(key)
   else:requested.append(key)
 else:
  for ref in numbers:
   found=[d for d in engine.docs if number(d['circular_number'])==number(ref) and eligible(d)]
   if len(found)>1:
    ambiguous.extend(dict(id=d['id'],series=d['series'],reference=d.get('reference_label',d['circular_number']),fiscal_year=fiscal_year(d),title=d['subject'],availability=d['availability']) for d in found)
   elif len(found)==1 and found[0]['availability']=='converted':requested.append(found[0]['id'])
   else:missing.append(ref)
 if ambiguous:notes.append('Circular reference is ambiguous. Choose a product/fiscal year or select the exact document in the library. No answer was attempted.')
 if missing:notes.append('Required circulars are missing, unavailable, awaiting source review, or excluded by filters: '+', '.join(missing)+'.')
 return dict(requested=list(dict.fromkeys(requested)),series=series,fiscal_year=year,notes=notes,ambiguous=ambiguous,missing=missing,eligible_ids={d['id'] for d in engine.docs if eligible(d) and d['availability']=='converted'})

def source_coverage(engine,docid):
 d=engine.by_id[docid];pages=[p for p in engine.pages_by_doc[docid]]
 declared=d.get('source_coverage',{});empty=[p['source_page'] for p in pages if not p['text'].strip()]
 return dict(total_pages=len(pages),empty_pages=empty,thin_pages=declared.get('thin_pages',[]),page_count_verified=declared.get('page_count_verified',bool(d.get('page_count'))),metadata_quality=d.get('metadata_quality','existing_source_metadata'))

def feature_applies(rule,doc):
    return not rule.get("products") or bool(set(rule["products"]).intersection(memberships(doc)))
