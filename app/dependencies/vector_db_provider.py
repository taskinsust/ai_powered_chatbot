from app.retrieval.document_loader import load_documents_from_folder
from app.retrieval.vector_store import build_or_load_vector_store

# Load once during app startup

docs_folder = "data/business_docs"
chunks = load_documents_from_folder(docs_folder)
vector_db = build_or_load_vector_store(chunks)

def get_vector_db():
    return vector_db