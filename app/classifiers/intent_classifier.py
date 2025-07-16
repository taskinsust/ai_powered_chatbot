class IntentClassifier:
    def __init__(self):
        self.business_keywords = ["product", "order", "price", "return", "tracking", "store"]
        self.casual_keywords = ["hello", "hi", "how are you", "who are you", "your name"]

    def classify(self, query: str) -> str:
        query_lower = query.lower()

        # Check business keywords
        if any(keyword in query_lower for keyword in self.business_keywords):
            return "business"

        # Check casual keywords
        if any(keyword in query_lower for keyword in self.casual_keywords):
            return "casual"

        # Otherwise, irrelevant
        return "irrelevant"