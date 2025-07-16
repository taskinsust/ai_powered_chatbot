## 📘 LLM-Powered Business Chatbot

### 🧠 Overview

A FastAPI-based, on-premises chatbot solution that handles business queries using a **Retrieval-Augmented Generation (RAG)** pipeline and local **LLaMA 3 inference** via `llama-cpp-python`. It supports Bangla and English seamlessly, optimized for modularity, scalability, and data privacy.

---

## 📦 Tech Stack

- **FastAPI** — Modular backend framework  
- **FAISS** — Local vector store for semantic retrieval  
- **Sentence Transformers** — Embeddings (multilingual support)  
- **llama-cpp-python** — Fast local LLaMA 3 inference  
- **Pydantic / JWT** — Auth & request validation  
- **BeautifulSoup, pdfplumber, PyMuPDF** — Document parsing  
- **scikit-learn, numpy** — Advanced intent classification  

---

## 🧱 Architecture Overview

```
Query → IntentClassifier → Embedding → Vector DB → Context Chunks
      → PromptBuilder → LLaMAEngine → Final Response
```

Handles:
- Business queries with RAG + LLM  
- Casual queries with personality  
- Fallbacks gracefully  
- Fully local execution — no external API calls

---

## 🧩 Modules

| Module                       | Description |
|------------------------------|-------------|
| `app/routes/chat.py`        | Unified `/chat` endpoint |
| `app/classifiers/advanced_intent_classifier.py` | Embedding-based intent detection |
| `app/embeddings/embedding_generator.py` | Embedding engine (bulk + single) |
| `app/retrieval/document_loader.py` | PDF, HTML, JSON loader |
| `app/retrieval/vector_store.py` | FAISS vector DB for chunk search |
| `app/llm/prompt_builder.py` | Formats prompt using user query + context |
| `app/llm/llama_engine.py`   | Runs `.gguf` LLaMA 3 model locally |
| `app/dependencies/`         | Injects singleton vector DB instance |
| `debug/`                    | Test scripts for isolated modules |

---

## 💬 Intent Handling

- **Business**: Retrieves chunks → builds prompt → uses LLaMA to answer
- **Casual**: Lightweight prompt → LLaMA responds warmly
- **Fallback**: Polite guidance back to business domain

Intent classifier uses semantic embeddings and cosine similarity for flexible phrasing and regional language support.

---

## 📂 Setup Instructions

1. **Install Dependencies**

```bash
pip install -r requirements.txt
```

2. **Download Quantized Model (GGUF)**
Place in `models/` folder and update `model_path` in `llama_engine.py`

3. **Run FastAPI**
```bash
uvicorn app.main:app --reload
```

4. **Run Debug Scripts**
```bash
python -m debug.test_advanced_classifier
```

---

## 📈 Future Enhancements

- Token streaming for smoother UX  
- Product-level semantic search  
- Query logging and feedback loop  
- Context-aware personalization  
- Embedding-based product tagging
