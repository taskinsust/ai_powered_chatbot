from app.llm.prompt_builder import PromptBuilder

chunks = [
    "Black T-shirt - 9.99 USD [Size: XL]",
    "We ship all orders within 48 hours.",
    "Items can be returned within 7 days."
]

builder = PromptBuilder()
prompt = builder.build_prompt("Do you sell black tees for men?")
print("\n🔍 Assembled Prompt:\n")
print(prompt)