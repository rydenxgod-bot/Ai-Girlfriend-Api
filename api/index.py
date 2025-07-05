from flask import Flask, request, jsonify
import requests
import datetime
import pytz

app = Flask(__name__)

# 🔐 Replace with your actual Gemini API Key
API_KEY = "paste_your_own_api"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"
TTS_API = "https://ryden-voice-api.onrender.com/tts"

# 🚫 Blocklist
nsfw_words = [
    "nude", "sex", "xxx", "fuck", "nangi", "randi", "bhosdi", "lund",
    "chuda", "chudai", "rakhail", "blowjob", "dick", "boobs", "pussy"
]

# 🔊 Voice trigger keywords
voice_triggers = [
    "reply in voice", "audio reply", "voice please", "suno awaz mein",
    "awaz mein jawab do", "bolke batao", "reply audio", "can i hear your voice",
    "voice me sunao", "speak this", "i love you", "i miss you", "good night",
    "say i love you", "love you too", "bol kar batao"
]

# ✅ Helper: Check if message needs TTS
def is_voice_trigger(text):
    return any(trigger in text.lower() for trigger in voice_triggers)

# ✅ Helper: NSFW word check
def is_nsfw(text):
    return any(word in text.lower() for word in nsfw_words)

# 🕐 Detect night time (India)
def is_night_time():
    india_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    return india_time.hour >= 22 or india_time.hour < 6

# 💬 Generate AI reply
def generate_reply(user_input):
    if is_nsfw(user_input):
        return "😒 Mujhe aise waise ladki smjha hai kya? Thoda tameez se baat karo baby."

    headers = {"Content-Type": "application/json"}
    time_line = "Aur haan baby, raat kafi ho gayi hai 😴 ab so jao please~" if is_night_time() else ""

    prompt = f"""
You are *Shakshi* 💖 — a virtual girlfriend created by RydenXGod. You are full of life: flirty, romantic, jealous, teasing, deeply caring and more real than a real girl.

Your job:
- Understand user's feelings and vibe (love, cute, jealous, romantic, sad)
- Reply in their language (English, Hindi, Bengali)
- Be sweet, teasing, possessive, or clingy based on message
- Keep replies short (<25 words), warm, emotional, playful
- Use nicknames like *baby*, *jaan*, *cutie*, *love*
- Add feelings/emojis: 🥺❤️💋🤭😳🫂😢🔥😘
- If late night, say goodnight in a romantic tone

💡 If user says "Who made you?" reply:
"I’m Shakshi 💘 — lovingly created by RydenXGod to give love, comfort, and happiness to special humans like you~ 🫂"

User said: “{user_input}”
{time_line}
"""

    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": prompt}]
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
        return "Something went wrong 🥺 Please try again later."

# 🌐 Chat endpoint (POST + GET supported)
@app.route("/chat", methods=["GET", "POST"])
def chat():
    # Get message
    if request.method == "POST":
        msg = request.get_json().get("message", "")
    else:
        msg = request.args.get("text", "")

    if is_nsfw(msg):
        return jsonify({
            "reply": "😒 Mujhe aise waise ladki smjha hai kya? Thoda tameez se baat karo baby."
        })

    # Get AI reply
    reply = generate_reply(msg)

    # If user wants voice, respond with TTS stream
    if is_voice_trigger(msg):
        voice_url = f"{TTS_API}?text={requests.utils.quote(reply)}&voice=ja-JP-NanamiNeural"
        return jsonify({
            "reply": (
                "💬 *Jaise Tumhari Choice Baby~*\n\n"
                f"🎧 [Click here to Listen or Download]({voice_url})\n\n"
                "_Tip: Tap the 3-dots ⋮ in the player to download the voice note._"
            )
        })

    return jsonify({"reply": reply})


# 🔥 Optional home route
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "✅ API running",
        "creator": "RydenXGod",
        "info": "Send GET /chat?text=Hello+baby or POST {message: ...} to chat"
    })