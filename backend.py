from flask import Flask, request, jsonify
import openai
import os

# optional: uncomment if ElevenLabs is needed later
# from elevenlabs.client import ElevenLabs

app = Flask(__name__)

# Keys from environment variables
openai.api_key = os.environ.get("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")
# elevenlabs_client = ElevenLabs(api_key=os.environ.get("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"))

@app.route("/", methods=["GET"])
def home():
    return "✅ Skye API is running! Use POST /chat"

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
