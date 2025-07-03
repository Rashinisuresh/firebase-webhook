from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "✅ HerPath Backend is Live!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(force=True)
    print("📥 Data received from webhook:", data)

    # Add logic to handle Firebase input or Google AI Studio data
    # For example, saving to Firebase, logging, etc.

    return jsonify({"status": "success", "message": "Data received"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
