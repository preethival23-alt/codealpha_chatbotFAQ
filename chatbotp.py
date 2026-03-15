import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from preprocess import preprocess

with open("faq_data.json") as f:
    data = json.load(f)

questions = [item["question"] for item in data]
answers = [item["answer"] for item in data]

processed_questions = [preprocess(q) for q in questions]

vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(processed_questions)

def get_answer(user_question):

    processed = preprocess(user_question)

    user_vec = vectorizer.transform([processed])

    similarity = cosine_similarity(user_vec, question_vectors)

    best_match = similarity.argmax()

    if similarity[0][best_match] < 0.2:
        return "Sorry, I couldn't understand your question."

    return answers[best_match]