from flask import Flask, request, jsonify

app = Flask(__name__)

# Temporary in-memory storage for users & credits (Replace with a database later)
users = {
    "admin": {"password": "admin123", "credits": float('inf')}  # Admin has unlimited calls
}

@app.route("/")
def home():
    return jsonify({"message": "👻 Welcome to GhostSpoof API - Stay Anonymous!"})

@app.route("/signup", methods=["POST"])
def signup():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username in users:
        return jsonify({"error": "🚫 Username already exists. Try logging in."}), 400

    users[username] = {"password": password, "credits": 10}  # New users start with 10 free credits
    return jsonify({"message": "✅ Sign-Up Successful! Enjoy 10 Free Minutes of GhostSpoof."})

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username not in users or users[username]["password"] != password:
        return jsonify({"error": "🚫 Invalid login. Please check your credentials."}), 401

    return jsonify({"message": "🔓 Login successful!", "credits": users[username]["credits"]})

@app.route("/start-call", methods=["POST"])
def start_call():
    data = request.json
    username = data.get("username")
    caller_id = data.get("caller_id")
    target_number = data.get("target_number")

    if username not in users or users[username]["credits"] <= 0:
        return jsonify({"error": "❌ Insufficient credits. Please add funds to continue."}), 403

    # Deduct credits (Admin has unlimited calls)
    if username != "admin":
        users[username]["credits"] -= 1

    return jsonify({"message": f"📞 Calling {target_number} with spoofed ID {caller_id}!"})

if __name__ == "__main__":
    app.run(debug=True)
