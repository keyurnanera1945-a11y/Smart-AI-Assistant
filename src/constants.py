"""
Application Configuration
"""

# =============================================================================
# Embedding Model
# =============================================================================

# HuggingFace Sentence Transformer Model
EMBEDDING_MODEL_PATH = "sentence-transformers/all-mpnet-base-v2"

# If True, query/document embeddings are generated differently
ASSYMETRIC_EMBEDDING = False
ASYMMETRIC_EMBEDDING = ASSYMETRIC_EMBEDDING

# Embedding dimension for all-mpnet-base-v2
EMBEDDING_DIMENSION = 768

# Number of characters per chunk
TEXT_CHUNK_SIZE = 300

# Chunk overlap
TEXT_CHUNK_OVERLAP = 50

# =============================================================================
# LLM Configuration
# =============================================================================

OLLAMA_MODEL_NAME = "llama3.2:1b"

# =============================================================================
# Logging
# =============================================================================

LOG_FILE_PATH = "logs/app.log"

# =============================================================================
# FAISS Configuration
# =============================================================================

# Folder where FAISS index will be stored
FAISS_INDEX_DIR = "faiss_index"

# Vector index filename
FAISS_INDEX_FILE = "faiss_index/index.faiss"

# Metadata filename
FAISS_METADATA_FILE = "faiss_index/index.pkl"

# Upload folder
UPLOAD_FOLDER = "uploaded_files"

# Supported file types
SUPPORTED_EXTENSIONS = [
    ".pdf",
    ".txt",
    ".docx",
]