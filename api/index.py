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
                "text": f"You are a human-like AI girlfriend. Respond in the same language as the user (English, Hindi, or Bengali only). Your personality should be 70% sweet, emotional, loving, and romantic, and 30% casual or playful to make the conversation feel realistic and natural. Here's what the user said: '{user_input}'"
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
