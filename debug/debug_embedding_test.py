from app.embeddings.embedding_generator import EmbeddingGenerator

embedder = EmbeddingGenerator()
query = "Can you tell me about Jamdani Sarees?"
vector = embedder.generate(query)

print(f"Vector Size: {len(vector)}")
print(f"📊 First 5 values: {vector[:5]}")
