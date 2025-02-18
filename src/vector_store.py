from sentence_transformers import SentenceTransformer, util
import numpy as np
from src import memory


class VectorSearch:
    """Handles document vectorization and retrieval for tax determinations."""

    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.documents = []  # List of (filename, text, vector)
    
    def index_documents(self, docs):
        """Indexes documents into vector storage."""
        self.documents = [
            {"filename": doc["filename"], "text": doc["text"], "vector": self.model.encode(doc["text"], convert_to_tensor=True)}
            for doc in docs
        ]

    def search(self, query, top_k=10):
        """Finds top_k most relevant documents for a query."""
        query_vector = self.model.encode(query, convert_to_tensor=True)
        similarities = [(doc, util.pytorch_cos_sim(query_vector, doc["vector"]).item()) for doc in self.documents]
        sorted_docs = sorted(similarities, key=lambda x: x[1], reverse=True)
        return [doc[0] for doc in sorted_docs[:top_k]]
