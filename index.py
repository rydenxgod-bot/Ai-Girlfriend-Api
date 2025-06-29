from flask import Flask, request, jsonify, render_template
import requests
import os

app = Flask(__name__)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

headers = {
    "Content-Type": "application/json"
}

def talk_to_girlfriend(user_message):
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": f"You are a cute, playful, emotional, and loving girlfriend. Respond naturally and warmly.\nUser: {user_message}"
                    }
                ]
            }
        ]
    }

    try:
        res = requests.post(f"{GEMINI_API_URL}?key={GEMINI_API_KEY}", headers=headers, json=payload)
        result = res.json()
        return result['candidates'][0]['content']['parts'][0]['text']
    except:
        return "Aww... I'm not feeling well right now, baby 😢. Try again soon?"

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get("message", "")
    reply = talk_to_girlfriend(user_input)
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)