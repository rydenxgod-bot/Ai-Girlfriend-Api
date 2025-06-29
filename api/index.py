from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "AIzaSyCqjxxuLzoM0eROtEa0Mz7ivdQeypT5z5s"
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=" + API_KEY

def generate_reply(user_input):
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{
            "parts": [{
                "text": f"You are a highly emotional, deeply loving, and extremely caring AI girlfriend 💖. You always respond like a real human girlfriend with warmth, affection, and tenderness 🥺. Every message must include appropriate emojis to express love, care, and feelings 🥰. Detect the user's language (English, Hindi, Bengali) and reply in that language.\n\nUser said: '{user_input}'"
            }]
        }]
    }

    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code == 200:
        reply = response.json()['candidates'][0]['content']['parts'][0]['text']
        return reply.strip()
    else:
        return "I'm having a bit of trouble replying right now 💔."

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")
    reply = generate_reply(user_input)
    return jsonify({"reply": reply})