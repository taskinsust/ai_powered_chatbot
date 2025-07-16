from sentence_transformers import SentenceTransformer
from sympy import false

# - Model distiluse-base-multilingual-cased-v2 is lightweight, fast, and supports Bangla + English.
class EmbeddingGenerator:
    # sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
    # distiluse-base-multilingual-cased-v2
    def __init__(self, model_name = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"):
        self.model = SentenceTransformer(model_name)

    # Commenting the underlying code due to the upper model
    # use following code for this distiluse-base-multilingual-cased-v2
    # def generate(self, text: str):
        #return self.model.encode(text, convert_to_tensor=False)

    def generate(self, text: str):
        return self.model.encode(text, normalize_embeddings=True)

    def generate_bulk(self, texts: list[str]):
        return self.model.encode(texts, normalize_embeddings=True)
