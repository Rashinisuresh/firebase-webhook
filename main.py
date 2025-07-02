from flask import Flask, request, jsonify

app = Flask(_name_)

@app.route('/')
def home():
    return "✅ Hello! Rashini AI is working."

# Optional POST route
@app.route('/save', methods=['POST'])
def save_data():
    data = request.get_json()
    return jsonify({"received": data}), 200

# Only used for local testing — Render doesn't use this line
if _name_ == '_main_':
    app.run(debug=True)
