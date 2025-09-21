from flask import Flask, request, jsonify
import openai
from elevenlabs.client import ElevenLabs
import os

app = Flask(__name__)

# Get API keys from environment variables
openai.api_key = os.environ.get("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")
elevenlabs_client = ElevenLabs(api_key=os.environ.get("sk_bf456e4c06ba51e77c82341f3597a17f5e11eb205fa84114"))
voice_id = "1fz2mW1imKTf5Ryjk5su"  # Replace with your ElevenLabs voice ID

@app.route("/", methods=["GET"])
def home():
    return "✅ Skye API is running! Use POST /chat to talk."

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are Skye, a calming and empowering career coach."},
                {"role": "user", "content": user_input}
            ]
        )
        reply = response.choices[0].message.content.strip()
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
