import logging
from typing import List

import numpy as np
import streamlit as st
from sentence_transformers import SentenceTransformer

from src.constants import EMBEDDING_MODEL_PATH
from src.utils import setup_logging

# Initialize logger
setup_logging()
logger = logging.getLogger(__name__)


@st.cache_resource(show_spinner=False)
def get_embedding_model() -> SentenceTransformer:
    """
    Load and cache the SentenceTransformer model.
    """
    logger.info(f"Loading embedding model: {EMBEDDING_MODEL_PATH}")
    return SentenceTransformer(EMBEDDING_MODEL_PATH)


def generate_embeddings(chunks: List[str]) -> np.ndarray:
    """
    Generate embeddings for multiple text chunks.

    Returns:
        numpy.ndarray of shape (num_chunks, embedding_dimension)
    """
    model = get_embedding_model()

    embeddings = model.encode(
        chunks,
        batch_size=32,
        show_progress_bar=False,
        convert_to_numpy=True,
        normalize_embeddings=True,
    )

    logger.info(f"Generated {len(chunks)} embeddings.")

    return embeddings.astype(np.float32)


def generate_query_embedding(query: str) -> np.ndarray:
    """
    Generate embedding for a user query.
    """

    model = get_embedding_model()

    embedding = model.encode(
        query,
        convert_to_numpy=True,
        normalize_embeddings=True,
    )

    return embedding.astype(np.float32)
