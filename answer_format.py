"""Presentation references checked claims; it cannot introduce new answer text."""
import re

STYLES = ('auto', 'paragraphs', 'bullets', 'mixed')
BLOCK_TYPES = ('paragraph', 'bullets', 'steps')
FORMAT_INSTRUCTIONS = (
    'Separate factual content from presentation. Return claims and a layout. '
    'Each claim is a short, self-contained plain-text statement with its citations; '
    'do not put Markdown, bullet markers, headings or citation labels inside claim text. '
    'Keep closely related sentences fluent when read together, without repetitive introductions. '
    'Layout blocks have type paragraph, bullets or steps and claim_indices containing '
    'one-based positions in claims. Include every claim exactly once in reading order. '
    'A paragraph block joins its claims as prose; a bullets/steps block makes one item per claim. '
    'Use paragraphs for explanations and short direct answers; bullets for genuinely parallel '
    'requirements/checklists; steps only for a supported ordered procedure; mix prose and lists '
    'when an overview plus details helps. Do not automatically turn each claim into a bullet. '
    'Honor requested answer_style and explicit formatting requests in the question. '
    'For paragraphs use paragraph blocks only; for bullets use bullets only; for mixed use '
    'a paragraph overview followed by a list when there is enough supported material. '
    'Do not invent extra claims merely to fill a format, and respect requested brevity. '
    'Use an empty layout when abstaining.'
)

def answer_schema():
    return {'type':'object','properties':{
        'abstain':{'type':'boolean'},
        'claims':{'type':'array','items':{'type':'object','properties':{
            'text':{'type':'string'},'sources':{'type':'array','items':{'type':'string'}}},
            'required':['text','sources'],'additionalProperties':False}},
        'layout':{'type':'array','items':{'type':'object','properties':{
            'type':{'type':'string','enum':list(BLOCK_TYPES)},
            'claim_indices':{'type':'array','minItems':1,'items':{'type':'integer','minimum':1}}},
            'required':['type','claim_indices'],'additionalProperties':False}}
        },'required':['abstain','claims','layout'],'additionalProperties':False}

def requested_style(value, query):
    if value not in STYLES:
        raise ValueError('Answer style must be auto, paragraphs, bullets or mixed')
    if value != 'auto':
        return value
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

    Only surviving claims are materialized. Layout never carries independent text,
    and failed/omitted/repeated references fall back without losing checked claims.
    """
    valid = isinstance(layout,list) and bool(layout)
    indices = []
    if valid:
        for block in layout:
            if (not isinstance(block,dict) or set(block) != {'type','claim_indices'}
                or block['type'] not in BLOCK_TYPES or not isinstance(block['claim_indices'],list)
                or not block['claim_indices'] or any(type(i) is not int for i in block['claim_indices'])):
                valid = False
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
    for block in layout:
        kept=[by_index[i] for i in block['claim_indices'] if i in by_index]
        if kept:
            blocks.append(dict(type=block['type'],claims=kept))
    if style=='mixed' and len(claims)>1 and not (any(b['type']=='paragraph' for b in blocks) and any(b['type'] in ('bullets','steps') for b in blocks)):
        return fallback_blocks(claims,style,route),'fallback'
    return blocks,'model_layout'
