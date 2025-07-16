# Vector DB & retriever logic
import os
from langchain.vectorstores import FAISS
from langchain.embeddings import SentenceTransformerEmbeddings

INDEX_DIR = "vector_index"

def build_or_load_vector_store(chunks=None):
    embeddings = SentenceTransformerEmbeddings(model_name="distiluse-base-multilingual-cased-v2")

    if os.path.exists(INDEX_DIR):
        db = FAISS.load_local(INDEX_DIR, embeddings, allow_dangerous_deserialization=True)
        print("✅ Loaded persisted FAISS index.")
    elif chunks:
        db = FAISS.from_documents(chunks, embedding=embeddings)
        db.save_local(INDEX_DIR)
        print("📁 New FAISS index created and saved.")
    else:
        raise ValueError("No index found and no chunks provided.")

    return db

def retrieve_context(query: str, db, top_k=3):
    results = db.similarity_search(query, k=top_k)
    return [doc.page_content for doc in results]