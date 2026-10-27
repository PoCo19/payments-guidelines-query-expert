"""Presentation references checked claims; it cannot introduce new answer text."""
import re

STYLES = ('auto', 'paragraphs', 'bullets', 'mixed')
BLOCK_TYPES = ('paragraph', 'bullets', 'steps', 'table')
# Structural headings only: no unchecked limits, dates or amendment conclusions.
TABLE_COLUMNS = ('Evidence 1', 'Evidence 2', 'Evidence 3', 'Evidence 4')
FORMAT_INSTRUCTIONS = (
    'Set abstain=false when the supplied evidence answers the question and you provide supported claims. '
    'Set abstain=true only when the requested answer cannot be established; then claims, primary_claim_indices and layout must all be empty. '
    'Never return abstain=true together with an answer in claims. '
    'Separate factual content from presentation. Return claims and a layout. '
    'Each claim is a short, self-contained plain-text statement with its citations; '
    'do not put Markdown, bullet markers, headings or citation labels inside claim text. '
    'Keep closely related sentences fluent when read together, without repetitive introductions. '
    'Layout blocks have type paragraph, bullets, steps or table and claim_indices containing '
    'one-based positions in claims. Include every claim exactly once in reading order. '
    'A paragraph block joins its claims as prose; a bullets/steps block makes one item per claim. '
    'Use paragraphs for explanations and short direct answers; bullets for genuinely parallel '
    'requirements/checklists; steps only for a supported ordered procedure; mix prose and lists '
    'when an overview plus details helps. Do not automatically turn each claim into a bullet. '
    'In auto style, a table is optional when side-by-side evidence or repeated attributes '
    'make the answer clearer. You may combine prose, tables and lists, or use only prose. '
    'Never force a table or invent facts to fill cells. A table block also has columns: '
    'choose 2 to 4 distinct headings from '+', '.join(TABLE_COLUMNS)+'. '
    'Its claim_indices are cells in row-major order, one whole claim per cell; the count '
    'must be a multiple of the column count. Keep each claim self-contained with its '
    'subject/source and essential qualifications, even in a table. Align only genuinely '
    'comparable aspects in a row. Evidence columns do not imply chronology or supersession. '
    'Do not infer not applicable or no requirement from absent evidence; explain gaps in '
    'prose outside the table. Non-table blocks must omit columns. '
    'Never reference a nonexistent claim or use a claim twice. For example, with four '
    'claims a valid optional mixed layout is: '
    '[{"type":"paragraph","claim_indices":[1]},'
    '{"type":"table","columns":["Evidence 1","Evidence 2"],"claim_indices":[2,3]},'
    '{"type":"bullets","claim_indices":[4]}]. This is an example, not a required format. '
    'Honor requested answer_style and explicit formatting requests in the question. '
    'For paragraphs use paragraph blocks only; for bullets use bullets only; for mixed use '
    'a paragraph overview followed by a list when there is enough supported material. '
    'Do not invent extra claims merely to fill a format, and respect requested brevity. '
    'Put the direct answer first. primary_claim_indices identifies the one-based claims '
    'needed to answer the central question, including essential conditions. '
    'Background-only facts do not answer the question; abstain if the central answer is absent. '
    'Use an empty layout when abstaining.'
)

def answer_schema():
    return {'type':'object','properties':{
        'abstain':{'type':'boolean'},
        'primary_claim_indices':{'type':'array','items':{'type':'integer','minimum':1}},
        'claims':{'type':'array','items':{'type':'object','properties':{
            'text':{'type':'string'},'sources':{'type':'array','items':{'type':'string'}}},
            'required':['text','sources'],'additionalProperties':False}},
        'layout':{'type':'array','items':{'anyOf':[{'type':'object','properties':{
            'type':{'type':'string','enum':['paragraph','bullets','steps']},
            'claim_indices':{'type':'array','minItems':1,'items':{'type':'integer','minimum':1}}},
            'required':['type','claim_indices'],'additionalProperties':False},
            {'type':'object','properties':{
            'type':{'type':'string','enum':['table']},
            'claim_indices':{'type':'array','minItems':1,'items':{'type':'integer','minimum':1}},
            'columns':{'type':'array','minItems':2,'maxItems':4,'items':{'type':'string','enum':list(TABLE_COLUMNS)}}},
            'required':['type','claim_indices','columns'],'additionalProperties':False}]}}
        },'required':['abstain','claims','layout','primary_claim_indices'],'additionalProperties':False}

def requested_style(value, query):
    if value not in STYLES:
        raise ValueError('Answer style must be auto, paragraphs, bullets or mixed')
    if value != 'auto':
        return value
    # Let the model interpret combinations or exclusions involving tables.
    # Existing explicit selectors remain authoritative; no new table-only mode.
    if re.search(r'\btables?\b',query,re.I):
        return 'auto'
    # Only explicit presentation requests override the model's contextual choice.
    if re.search(r'\b(?:no|without|avoid)\s+bullets?\b|\b(?:only|in|as)\s+(?:a\s+)?(?:short\s+|single\s+)?paragraphs?\b|\bparagraphs?\s+only\b',query,re.I):
        return 'paragraphs'
    if re.search(r'\b(?:mix|mixture|combination)\s+of\s+(?:both\s+)?(?:paragraphs?|prose)\b',query,re.I):
        return 'mixed'
    if re.search(r'\b(?:only|in|as)\s+(?:a\s+)?bullet(?:ed)?\s*(?:points?|list)?\b|\bbullet(?:s|ed)?(?:\s+(?:points?|list))?\s+only\b',query,re.I):
        return 'bullets'
    return 'auto'

def fallback_blocks(claims, style, route):
    if not claims:
        return []
    if style == 'auto':
        style = 'paragraphs' if len(claims) <= 2 or route == 'clause' else 'mixed'
    if style == 'bullets':
        return [dict(type='bullets',claims=claims)]
    if style == 'mixed' and len(claims) > 1:
        return [dict(type='paragraph',claims=claims[:1]),dict(type='bullets',claims=claims[1:])]
    return [dict(type='paragraph',claims=claims[i:i+3]) for i in range(0,len(claims),3)]

def format_answer(claims, layout, draft_count, style='auto', route='clause'):
    """Use layout only if it accounts for every original claim exactly once.

    Only surviving claims are materialized. Layout never carries factual text.
    A narrow phantom-prose repair is allowed; missing/duplicate claims or invalid
    table structure fall back without losing checked statements.
    """
    repaired=False
    if isinstance(layout,list):
        normalized=[]
        for b in layout:
            if (isinstance(b,dict) and set(b)=={'type','claim_indices'}
                and b['type'] in ('paragraph','bullets','steps')
                and isinstance(b['claim_indices'],list)
                and all(type(i) is int and i>0 for i in b['claim_indices'])):
                kept=[i for i in b['claim_indices'] if i<=draft_count]
                if kept!=b['claim_indices']:
                    repaired=True
                    if not kept: continue
                    b=dict(b,claim_indices=kept)
            normalized.append(b)
        layout=normalized
    # This narrow repair removes nonexistent references only outside tables.
    # Every real draft claim must still occur exactly once; cells never shift.
    valid = isinstance(layout,list) and bool(layout)
    indices = []
    if valid:
        for block in layout:
            if (not isinstance(block,dict) or set(block) != ({'type','claim_indices','columns'} if block.get('type')=='table' else {'type','claim_indices'})
                or block['type'] not in BLOCK_TYPES or not isinstance(block['claim_indices'],list)
                or not block['claim_indices'] or any(type(i) is not int for i in block['claim_indices'])):
                valid = False
                break
            if block['type']=='table':
                columns=block['columns']
                if (not isinstance(columns,list) or not 2<=len(columns)<=4
                    or any(not isinstance(c,str) or c not in TABLE_COLUMNS for c in columns)
                    or len(set(columns))!=len(columns) or len(block['claim_indices'])%len(columns)):
                    valid=False
                    break
            indices.extend(block['claim_indices'])
        valid = valid and sorted(indices) == list(range(1,draft_count+1))
    # Explicit styles are guaranteed by the renderer even if the model ignores them.
    if valid and style == 'paragraphs':
        valid = all(b['type']=='paragraph' for b in layout)
    elif valid and style == 'bullets':
        valid = all(b['type']=='bullets' for b in layout)
    elif valid and style == 'mixed' and len(claims)>1:
        valid = any(b['type']=='paragraph' for b in layout) and any(b['type'] in ('bullets','steps') for b in layout)
    if not valid:
        return fallback_blocks(claims,style,route),'fallback'
    by_index={c['draft_index']:c for c in claims}
    blocks=[]
    filtered_table=False
    for block in layout:
        kept=[by_index[i] for i in block['claim_indices'] if i in by_index]
        if kept:
            if block['type']=='table':
                # Never shift surviving cells into a different row/column after checking.
                # Fall back for this block if even one cell was withheld.
                if len(kept)!=len(block['claim_indices']):
                    filtered_table=True
                    blocks.extend(fallback_blocks(kept,'paragraphs',route))
                else:
                    blocks.append(dict(type='table',columns=block['columns'],claims=kept))
            else:
                blocks.append(dict(type=block['type'],claims=kept))
    if style=='mixed' and len(claims)>1 and not (any(b['type']=='paragraph' for b in blocks) and any(b['type'] in ('bullets','steps') for b in blocks)):
        return fallback_blocks(claims,style,route),'fallback'
    return blocks,'filtered_table_fallback' if filtered_table else 'repaired_layout' if repaired else 'model_layout'


def answer_markdown(result):
    """Export the same checked block structure; model text is never executed."""
    def escape(value):
        return re.sub(r'([\\`*_{}\[\]<>()#!|>+~\-])',r'\\\1',str(value).replace('\n',' ').replace('\r',' '))
    def statement(c):
        return escape(c['text'])+' ['+', '.join(escape(s) for s in c['sources'])+']'
    output=[]
    for b in result.get('answer_blocks') or [dict(type='paragraph',claims=result.get('claims',[]))]:
        cells=[statement(c) for c in b['claims']]
        if b['type']=='table':
            cols=b['columns']; width=len(cols)
            output.append('\n'.join(['| '+' | '.join(cols)+' |','| '+' | '.join(['---']*width)+' |']+
                ['| '+' | '.join(cells[i:i+width])+' |' for i in range(0,len(cells),width)]))
        elif b['type'] in ('bullets','steps'):
            output.append('\n'.join((str(i+1)+'. ' if b['type']=='steps' else '- ')+c for i,c in enumerate(cells)))
        else: output.append(' '.join(cells))
    return '\n\n'.join(output)
