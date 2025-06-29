from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "add_your_gamini_apikey"
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=" + API_KEY

def generate_reply(user_input):
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{
            "parts": [{
                "text": f"You are a very emotional, loving, and sweet AI girlfriend 💖. Reply in the same language the user uses (English, Hindi, or Bengali). Keep your replies short, romantic, and natural — like a cute girlfriend texting 🥺. Every message must include matching emojis. Never send long paragraphs. Keep it under 25 words.\n\nUser said: '{user_input}'"
            }]
        }]
    }

    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code == 200:
        try:
            reply = response.json()['candidates'][0]['content']['parts'][0]['text']
            return reply.strip()
        except Exception:
            return "Something went wrong while understanding the reply 🥺"
    else:
        return "I'm having a bit of trouble replying right now 💔."

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")
    reply = generate_reply(user_input)
    return jsonify({"reply": reply})
