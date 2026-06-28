from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# FAQ Questions
questions = [
    "What is Artificial Intelligence?",
    "What is Python?",
    "Who developed Python?",
    "What is Machine Learning?",
    "What is CodeAlpha?"
]

# FAQ Answers
answers = [
    "Artificial Intelligence is the simulation of human intelligence by machines.",
    "Python is a high-level programming language.",
    "Python was developed by Guido van Rossum.",
    "Machine Learning is a branch of AI that enables systems to learn from data.",
    "CodeAlpha is a software development company offering internship programs."
]

# Create TF-IDF Vectorizer
vectorizer = TfidfVectorizer()

# Convert questions into vectors
question_vectors = vectorizer.fit_transform(questions)

print("🤖 FAQ Chatbot")
print("Type 'exit' to quit.\n")

while True:
    user_question = input("You: ")

    if user_question.lower() == "exit":
        print("Bot: Goodbye!")
        break

    # Convert user question into vector
    user_vector = vectorizer.transform([user_question])

    # Calculate similarity
    similarity = cosine_similarity(user_vector, question_vectors)

    # Get best match
    best_match = similarity.argmax()

    print("Bot:", answers[best_match])
