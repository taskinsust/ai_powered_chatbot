from llama_cpp import Llama

class LlamaEngine:
    def __init__(self,
                 model_path= "llama_models/meta-llama-3-8b-q4_k_m.gguf",
                 n_ctx=2048,
                 n_threads=8,
                 temperature= 0.7,
                 max_tokens=512
                 ):
# 🔌 Load model with quantized settings
        self.llm =Llama(
            model_path=model_path,
            n_ctx=n_ctx,
            n_threads=n_threads,
            verbose=False
        )
        self.temperature = temperature
        self.max_tokens = max_tokens

    def infer(self, prompt: str) -> str:
        output = self.llm(
            prompt=prompt,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
            stop=["User:", "Context:"]
        )
        return output["choices"][0]["text"].strip()
