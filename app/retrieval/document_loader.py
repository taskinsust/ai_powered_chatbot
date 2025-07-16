# document_loader.py

import os
import json
from langchain.schema import Document
from langchain.document_loaders import TextLoader, PyMuPDFLoader, UnstructuredHTMLLoader
from langchain.text_splitter import CharacterTextSplitter

splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)

def load_custom_json(file_path: str):
    with open(file_path, "r", encoding="utf8") as f:
        data = json.load(f)

    products = []

    def extract_items(node, path=""):
        if isinstance(node, dict):
            for key, value in node.items():
                if key == "categories" and isinstance(value, list):
                    for item in value:
                        extract_items(item, path)
                elif key == "name":
                    name_path = f"{path} > {value}" if path else value
                    extract_items(node.get("categories", []), name_path)
                elif key == "amount":
                    item_text = f"{path} → {node.get('name')} - {node['amount']} {node['currency']} [Size: {node.get('size', 'N/A')}]"
                    products.append(item_text)

        elif isinstance(node, list):
            for item in node:
                extract_items(item, path)

    extract_items(data.get("catalog", {}))
    return [Document(page_content=product) for product in products]

def load_documents_from_folder(folder_path: str):
    all_chunks = []

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if filename.endswith(".txt"):
            loader = TextLoader(file_path, encoding="utf8")
            docs = loader.load()

        elif filename.endswith(".pdf"):
            loader = PyMuPDFLoader(file_path)
            docs = loader.load()

        elif filename.endswith(".html"):
            loader = UnstructuredHTMLLoader(file_path)
            docs = loader.load()

        elif filename.endswith(".json"):
            docs = load_custom_json(file_path)

        else:
            continue

        chunks = splitter.split_documents(docs)
        all_chunks.extend(chunks)

    return all_chunks