from app.embeddings.embedding_generator import EmbeddingGenerator
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class AdvancedIntentClassifier:
    def __init__(self):
        self.embedder = EmbeddingGenerator()

        self.intent_samples = {
            "business": [
                "What products do you sell?",
                "How much is this item?",
                "Do you have Jamdani sarees?",
                "Can I order online?",
                "What is the price of women's dresses?",
                "Tell me about this product"
            ],
            "casual": [
                "Hi there!",
                "How's your day?",
                "Tell me a joke",
                "Are you alive?",
                "Can we chat?",
                "What’s up?"
            ],
            "fallback": [
                "Who is the prime minister?",
                "Sing me a song",
                "Give me the weather report",
                "What is the capital of France?",
                "What’s 5 + 9?",
                "Who won the cricket match?"
            ]
        }

        # Precompute embeddings for each intent
        self.intent_vectors = {
            intent: self.embedder.generate_bulk(samples)
            for intent, samples in self.intent_samples.items()
        }

    def classify(self, query: str) -> str:
        query_vector = self.embedder.generate(query)

        scores = {}
        for intent, vectors in self.intent_vectors.items():
            sims = cosine_similarity([query_vector], vectors)
            scores[intent] = float(np.max(sims))  # Best match within that group

        best_intent = max(scores, key=scores.get)
        return best_intent