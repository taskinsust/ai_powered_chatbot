from app.llm.llama_engine import LlamaEngine
from app.llm.prompt_builder import PromptBuilder

query = "Do you sell black dresses for women?"
context_chunks = [
    "Casual Red Dress - 16.99 EUR [Size: S]",
    "Short Black Dress - 47.99 EUR [Size: M]",
    "Long Blue Dinner Dress - 103.99 USD [Size: L]"
]

prompt = PromptBuilder().build_prompt(query, context_chunks)

llama = LlamaEngine()
response = llama.infer(prompt)

print("\n🧠 LLaMA Says:\n", response)