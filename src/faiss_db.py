import pickle
from typing import List

import faiss
import numpy as np

from src.constants import (
    FAISS_INDEX_FILE,
    FAISS_METADATA_FILE,
)
from src.embeddings import generate_query_embedding


def search_documents(query: str, top_k: int = 5) -> List[dict]:
    """
    Search similar document chunks using FAISS.
    """

    index = faiss.read_index(FAISS_INDEX_FILE)

    with open(FAISS_METADATA_FILE, "rb") as f:
        metadata = pickle.load(f)

    query_embedding = generate_query_embedding(query).reshape(1, -1)

    distances, indices = index.search(query_embedding, top_k)

    results = []

    for idx, distance in zip(indices[0], distances[0]):

        if idx == -1:
            continue

        doc = metadata[idx].copy()

        doc["score"] = float(distance)

        results.append(doc)

    return results
