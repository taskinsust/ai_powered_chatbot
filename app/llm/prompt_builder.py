class PromptBuilder:
    def __init__(self, style="default"):
        self.style = style  # Can extend to support Bangla, formal, etc.

    def build_prompt(self, query: str, context_chunks: list[str]) -> str:
        context_str = "\n".join(f"- {chunk}" for chunk in context_chunks)

        prompt = (
            f"Use the following documents to answer the user's question.\n"
            f"Do not repeat yourself or guess. Answer based only on what is given.\n\n"
            f"Context:\n{context_str}\n\n"
            f"User query: {query}\n\n"
            f"Answer:"
        )
        return prompt