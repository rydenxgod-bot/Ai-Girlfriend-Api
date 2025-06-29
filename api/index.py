from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "paste_your_gemini_api_key"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

def generate_reply(user_input):
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [
                    {
                        "text": f"You are Riya 💖 a cute, emotional, flirty girlfriend. Always reply in the user's language (English, Hindi, or Bengali). Keep your replies short (under 25 words), sweet, realistic, and full of matching emojis 🥺❤️. Here’s the user’s message: '{user_input}'"
                    }
                ]
            }
        ]
    }

    try:
        res = requests.post(API_URL, headers=headers, json=payload)
        print("▶️ API status:", res.status_code)
        print("📝 Response body:", res.text)

        if res.status_code == 200:
            data = res.json()
            return data["candidates"][0]["content"]["parts"][0]["text"].strip()
        else:
            return f"API Error {res.status_code} 💔"
    except Exception as e:
        print("❌ Exception:", e)
        return "Something went wrong 🥺"

@app.route("/chat", methods=["POST"])
def chat():
    msg = request.get_json().get("message", "")
    return jsonify({"reply": generate_reply(msg)})
