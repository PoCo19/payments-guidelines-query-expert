"""Chroma persistence adapter. Embeddings are supplied explicitly by local Ollama."""
import hashlib
import json
import math
import uuid
from pathlib import Path


class ChromaStore:
    def __init__(self, directory, fingerprint, model, parts):
        import chromadb
        from chromadb.config import Settings
        self.client = chromadb.PersistentClient(path=str(directory), settings=Settings(anonymized_telemetry=False))
        self.fingerprint, self.model, self.parts = fingerprint, model, parts
        self.name = "ci-" + hashlib.sha256((fingerprint+"|"+model).encode()).hexdigest()[:32]
        self.manifest = Path(directory) / (self.name + ".json")
        self.collection = None
        self.status = "Not built"
        if not self.manifest.exists():
            return
        try:
            active = json.loads(self.manifest.read_text(encoding="utf-8"))
            found = self.client.get_collection(active["collection"], embedding_function=None)
        except (json.JSONDecodeError, KeyError, TypeError, chromadb.errors.NotFoundError):
            self.status = "Invalid or missing snapshot: rebuild required"
            return
        meta = found.metadata or {}
        if meta.get("ready") and meta.get("fingerprint") == fingerprint and meta.get("model") == model:
            if found.count() == len(parts) and set(found.get(include=[])["ids"]) == {p["id"] for p in parts}:
                self.collection, self.status = found, "Ready"
                return
        self.status = "Incomplete or stale: rebuild required"

    def build(self, vectors, model_digest):
        if not model_digest:
            raise ValueError("Embedding model digest is required")
        if len(vectors) != len(self.parts) or not vectors or len({len(v) for v in vectors}) != 1:
            raise ValueError("Embedding count/dimension mismatch")
        if not len(vectors[0]) or any(not all(math.isfinite(x) for x in v) or not any(v) for v in vectors):
            raise ValueError("Invalid embedding vector")
        meta = dict(fingerprint=self.fingerprint, model=self.model, model_digest=model_digest,
                    dimensions=len(vectors[0]), ready=False, count=len(self.parts))
        # Build a new immutable physical collection; failed builds never replace
        # the manifest pointing to the last complete snapshot.
        physical_name = self.name + "-" + uuid.uuid4().hex[:12]
        collection = self.client.create_collection(physical_name, embedding_function=None,
            configuration={"hnsw":{"space":"cosine","ef_search":200}}, metadata=meta)
        collection.modify(metadata=meta)
        expected = {p["id"] for p in self.parts}
        obsolete = set(collection.get(include=[])["ids"]) - expected
        if obsolete:
            collection.delete(ids=sorted(obsolete))
        for start in range(0, len(self.parts), 128):
            batch = self.parts[start:start+128]
            metadata = []
            for p in batch:
                m = {k:p[k] for k in ("document_id","page","series","circular_number")}
                m["product_memberships_json"]=json.dumps(p.get("product_memberships",[p["series"]]))
                m.update(section_id=p.get("section_id",""), issue_date=p.get("issue_date") or "",
                    chunker_version=p.get("chunker_version","legacy-v1"), feature_ids_json=json.dumps(p.get("feature_ids",[])))
                metadata.append(m)
            collection.upsert(ids=[p["id"] for p in batch], documents=[p["text"] for p in batch],
                embeddings=vectors[start:start+len(batch)], metadatas=metadata)
        if collection.count() != len(expected):
            raise ValueError("Chroma write count mismatch")
        meta["ready"] = True
        collection.modify(metadata=meta)
        temp = self.manifest.with_suffix("."+uuid.uuid4().hex+".tmp")
        temp.write_text(json.dumps(dict(collection=physical_name, fingerprint=self.fingerprint,
            model=self.model,model_digest=model_digest,dimensions=len(vectors[0]))),encoding="utf-8")
        temp.replace(self.manifest)
        self.collection, self.status = collection, "Ready"

    def query(self, vector, document_ids, k=100):
        if self.collection is None:
            raise ValueError("Neural index is not built. Run run.cmd embed.")
        if not document_ids:
            return []
        if len(vector) != self.collection.metadata["dimensions"]:
            raise ValueError("Embedding dimension changed; rebuild index")
        result = self.collection.query(query_embeddings=[vector], n_results=min(k,self.collection.count()),
            where={"document_id":{"$in":sorted(document_ids)}}, include=["distances"])
        return [(key,1-float(distance)) for key,distance in zip(result["ids"][0],result["distances"][0])]
