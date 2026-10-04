"""Bounded one-hop context assembly, with a visible reason for each source."""
import re


def assemble(engine, query, method, series="", cutoff="", feature="", scope="strict", route="auto", rerank=None, fiscal_year="", document_ids=None):
    if engine.config.get("adaptive_retrieval", False):
        from adaptive_context import assemble as adaptive
        return adaptive(engine,query,method,series,cutoff,feature,scope,route,rerank,fiscal_year,document_ids)
    if scope not in ("strict", "related"):
        raise ValueError("Unknown context scope")
    seeds = engine.search(query, method, series, cutoff, 4 if scope == "related" else 6, feature)
    selected, seen, notes = [], set(), []
    budget = int(engine.config.get("context_char_budget", 12000))
    if not 2000 <= budget <= 18000:
        raise ValueError("context_char_budget must be between 2000 and 18000")
    used = 0
    def add(part, reason, via="", relation=None):
        nonlocal used
        if part["id"] in seen or len(selected) >= 10:
            return False
        cost = len(part["text"]) + len(part["title"]) + 300
        if used + cost > budget:
            notes.append("Some context was omitted to stay within the evidence character budget.")
            return False
        selected.append(dict(part, retrieval_reason=reason, via_document_id=via, relation=relation,
                             citation=f"S{len(selected)+1}"))
        used += cost
        seen.add(part["id"])
        return True

    for p in seeds:
        add(p,"direct_match")
    if scope == "related" and seeds:
        seed_docs = list(dict.fromkeys(p["document_id"] for p in seeds))
        terms = set(engine.query_terms(query))
        def relevance(p):
            # Body overlap prevents title-only matches from monopolizing expansion.
            return len(terms.intersection(engine.query_terms(p["text"])))
        def allowed(doc_id):
            d = engine.by_id[doc_id]
            return engine.eligible(d,series,cutoff) and (not feature or feature in engine.registry.features[doc_id])
        added_docs = set(seed_docs)
        links_added = 0
        for doc_id in seed_docs[:2]:
            for edge in engine.registry.edges:
                if edge["from_id"] == doc_id and edge["status"] != "resolved":
                    notes.append(f'OC {engine.by_id[doc_id]["circular_number"]} references {edge["reference"]}: {edge["status"]}. No text was inferred.')
            for target, direction, edge in engine.registry.neighboring_documents(doc_id):
                if target in added_docs or not allowed(target):
                    continue
                if links_added >= 2:
                    notes.append("Additional recorded references were omitted by the two-document expansion limit.")
                    continue
                candidates = engine.parts_by_doc.get(target, [])
                if candidates:
                    best = max(candidates, key=lambda p:(relevance(p),-p["page"]))
                    if add(best,"recorded_reference",doc_id,dict(edge,direction=direction)):
                        added_docs.add(target); links_added += 1
        # Feature labels are title-derived hints, never amendment relationships.
        query_features = {r["id"] for r in engine.registry.rules if re.search(r["pattern"],query,re.I)}
        candidates = [p for p in engine.parts if p["document_id"] not in added_docs and allowed(p["document_id"])
                      and query_features.intersection(engine.registry.features[p["document_id"]]) and relevance(p)>0]
        if candidates:
            add(max(candidates,key=relevance),"same_feature")
        # Keep surrounding text as separate, page-specific citations.
        adjacent_count = 0
        for seed in seeds:
            for key in ("previous_chunk_id", "next_chunk_id"):
                part = engine.parts_by_id.get(seed.get(key))
                if part and part["document_id"] == seed["document_id"] and part.get("section_id") == seed.get("section_id"):
                    if adjacent_count < 3 and add(part,"adjacent_context",seed["document_id"]):
                        adjacent_count += 1
    return selected, dict(scope=scope, seed_chunk_ids=[p["id"] for p in seeds],
        included_chunk_ids=[p["id"] for p in selected], evidence_characters=used, character_budget=budget,
        max_reference_hops=1, notes=list(dict.fromkeys(notes)))
