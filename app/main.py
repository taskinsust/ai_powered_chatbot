from fastapi import FastAPI
from app.routes import auth, chat
from app.retrieval.document_loader import load_documents_from_folder
from app.retrieval.vector_store import build_or_load_vector_store

# 🌐 Create FastAPI app
app = FastAPI()

# 📚 Load documents and build vector store
# docs_folder = "data/business_docs"
# chunks = load_documents_from_folder(docs_folder)
# vector_db = build_or_load_vector_store(chunks)

# 🔌 Inject vector_db into chat router if needed
# You can use dependency injection or global sharing depending on design

# 🚪 Include routes
app.include_router(auth.router)
app.include_router(chat.router)