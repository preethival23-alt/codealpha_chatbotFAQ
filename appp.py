from flask import Flask, render_template, request, jsonify
from chatbot import get_answer

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    user_msg = request.json["message"]

    response = get_answer(user_msg)

    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)