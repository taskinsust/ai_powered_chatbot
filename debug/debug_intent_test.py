from app.classifiers.intent_classifier import IntentClassifier

clf = IntentClassifier()

print(clf.classify("Can I track my order?"))          # Expected: 'business'
print(clf.classify("Hi, how are you doing?"))         # Expected: 'casual'
print(clf.classify("What's the weather today?"))      # Expected: 'irrelevant'