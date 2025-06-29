from flask import Flask, request, jsonify, render_template
import requests
import os

app = Flask(__name__)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

headers = {
    "Content-Type": "application/json"
}

def talk_to_gemini(user_input):
    data = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": f"You are a loving, playful, supportive girlfriend. Respond romantically, emotionally, and naturally like a real girl would.\n\nUser: {user_input}"}]
            }
        ]
    }

    response = requests.post(
        f"{GEMINI_API_URL}?key={GEMINI_API_KEY}",
        headers=headers,
        json=data
    )

    result = response.json()
    try:
        return result['candidates'][0]['content']['parts'][0]['text']
    except:
        return "Sorry, I'm having trouble understanding you right now 😢."

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "Missing 'message' field."}), 400

    reply = talk_to_gemini(user_input)
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)