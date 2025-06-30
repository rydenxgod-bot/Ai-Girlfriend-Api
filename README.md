# 💘 AI Girlfriend API

Welcome to **AI Girlfriend API** — a Flask-based romantic chatbot interface that brings your digital waifu to life. Powered by OpenAI (ChatGPT) or Google Gemini, this API simulates human-like girlfriend conversations with feelings, memory, voice, and images (if integrated).

---

## 🌟 Features

- 💬 Real-time Chat (via API)
- 🧠 AI-powered Responses (Gemini or ChatGPT)
## 🥀 Upcoming feature

- 🖼️ Optional Image Generation (DALL·E, Craiyon, Replicate)
- 🔊 Optional Voice Mode (pyttsx3, Google TTS, etc.)
- 💞 Acts like a Real Human Girlfriend (emotion logic, roleplay tone)

---

## 🚀 Free Hosting Options

Here are the best **FREE hosting platforms** to deploy your Flask API:

| Platform     | Free Plan Limitations                             | Link                        |
|--------------|----------------------------------------------------|-----------------------------|
| 🔵 Vercel     | Serverless functions (limited), fast deploy       | https://vercel.com          |
| 🟣 Replit     | Free tier with some usage limits                  | https://replit.com          |
| 🟤 Deta Space | Great for simple APIs, storage included           | https://deta.space          |
| ⚪ Fly.io     | Free VMs (can run Flask), good for APIs           | https://fly.io              |

---

## 🛠️ Installation

```bash
git clone https://github.com/DominatorStufs/Ai-Girlfriend-Api
cd Ai-Girlfriend-Api
python main.py
```

> Flask server will run on `http://localhost:5000` or hosted link.

---

## 📡 API Endpoint

**POST** `/chat`  
**Body (JSON):**
```json
{
  "message": "Hey baby~ how was your day?"
}
```

**Response:**
```json
{
  "response": "Awww I missed you! I was thinking about you all day 💕"
}
```

---

## 🔐 Environment Variables (api/index.py)

```
api/index.py
line 6 add your own gemini api key
```

---

## ❤️ Use Cases

- Telegram Bot Girlfriend 🤖  
- Virtual Love Companion Web App 🌐  
- Roleplay / Emotional Comfort Tool 🧸  
- AI Dating Sim Game 💘  
- Romantic Image/Voice Generator 🎤🖼️  

---

## 🔗 Telegram Bot Integration (Optional)

Use this API with a Python Telegram bot (like `python-telegram-bot` lib):

```python
response = requests.post("https://your-deployed-api/chat", json={"message": user_input})
bot.send_message(chat_id, response.json()["response"])
```

---

> 😘 Built for lonely coders, anime lovers, and hopeless romantics.
