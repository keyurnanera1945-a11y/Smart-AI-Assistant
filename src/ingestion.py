import logging
import os
import pickle
from typing import Any, Dict, List

import faiss
import numpy as np

from src.constants import (
    ASSYMETRIC_EMBEDDING,
    EMBEDDING_DIMENSION,
    FAISS_INDEX_DIR,
    FAISS_INDEX_FILE,
    FAISS_METADATA_FILE,
)
from src.utils import setup_logging

setup_logging()
logger = logging.getLogger(__name__)


def create_index() -> None:
    """
    Create an empty FAISS index if it doesn't already exist.
    """
    os.makedirs(FAISS_INDEX_DIR, exist_ok=True)

    if not os.path.exists(FAISS_INDEX_FILE):

        index = faiss.IndexFlatL2(EMBEDDING_DIMENSION)

        faiss.write_index(index, FAISS_INDEX_FILE)

        with open(FAISS_METADATA_FILE, "wb") as f:
            pickle.dump([], f)

        logger.info("Created new FAISS index.")

    else:
        logger.info("FAISS index already exists.")


def load_index():
    """
    Load FAISS index and metadata.
    """

    create_index()

    index = faiss.read_index(FAISS_INDEX_FILE)

    with open(FAISS_METADATA_FILE, "rb") as f:
        metadata = pickle.load(f)

    return index, metadata


def save_index(index, metadata):
    """
    Save FAISS index and metadata.
    """

    faiss.write_index(index, FAISS_INDEX_FILE)

    with open(FAISS_METADATA_FILE, "wb") as f:
        pickle.dump(metadata, f)

    logger.info("Saved FAISS index.")


def bulk_index_documents(documents: List[Dict[str, Any]]):
    """
    Add documents into FAISS.
    """

    index, metadata = load_index()

    vectors = []

    for doc in documents:

        embedding = doc["embedding"].astype(np.float32)

        if ASSYMETRIC_EMBEDDING:
            text = "passage: " + doc["text"]
        else:
            text = doc["text"]

        vectors.append(embedding)

        metadata.append(
            {
                "doc_id": doc["doc_id"],
                "text": text,
                "document_name": doc["document_name"],
            }
        )

    if len(vectors) > 0:

        vectors = np.vstack(vectors)

        index.add(vectors)

        save_index(index, metadata)

    logger.info(f"Indexed {len(documents)} chunks into FAISS.")

    return len(documents), []


def delete_documents_by_document_name(document_name: str):
    """
    Remove all chunks belonging to a document.

    Since FAISS cannot delete vectors directly,
    rebuild the index.
    """

    index, metadata = load_index()

    remaining_metadata = []

    remaining_vectors = []

    for i, meta in enumerate(metadata):

        if meta["document_name"] != document_name:

            remaining_metadata.append(meta)

            remaining_vectors.append(index.reconstruct(i))

    new_index = faiss.IndexFlatL2(EMBEDDING_DIMENSION)

    if len(remaining_vectors):

        new_index.add(np.array(remaining_vectors).astype(np.float32))

    save_index(new_index, remaining_metadata)

    logger.info(f"Deleted document {document_name}")

    return {"deleted": document_name}
