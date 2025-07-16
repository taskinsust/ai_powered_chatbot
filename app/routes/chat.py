from fastapi import APIRouter, Depends
from app.core.security import verify_token
from app.classifiers.intent_classifier import IntentClassifier
from app.embeddings.embedding_generator import EmbeddingGenerator
from app.dependencies.vector_db_provider import get_vector_db
from app.retrieval.vector_store import retrieve_context
from app.llm.prompt_builder import PromptBuilder
from app.llm.llama_engine import LlamaEngine

router = APIRouter()
classifier = IntentClassifier()
embedder = EmbeddingGenerator()
prompt_builder = PromptBuilder()
llama_engine = LlamaEngine()

@router.post("/chat")
def unified_chat(
    query: str,
    user: str = Depends(verify_token),
    vector_db=Depends(get_vector_db)
):
    intent = classifier.classify(query)
    embedding = embedder.generate(query)
    response_payload = {"user": user, "intent": intent}

    if intent == "business":
        context = retrieve_context(query, vector_db)
        prompt = prompt_builder.build_prompt(query, context)
        reply = llama_engine.infer(prompt)

        response_payload.update({
            "context_used": context,
            "response": reply
        })

    elif intent == "casual":
        prompt = (
            f"You are a helpful assistant having a casual chat with the user.\n"
            f"User: {query}\n\n"
            f"Assistant:"
        )
        reply = llama_engine.infer(prompt)
        response_payload["response"] = reply

    else:  # fallback / unknown
        prompt = (
            f"The user asked: \"{query}\"\n"
            f"Kindly let them know you're trained to answer questions related to XYZ Enterprise.\n"
            f"Reply politely and guide them to ask a product or business-related query."
        )
        reply = llama_engine.infer(prompt)
        response_payload["response"] = reply

    return response_payload