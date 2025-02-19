from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Admin Credentials (For Free Calls)
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

# Store user data (TEMPORARY - will be replaced with database later)
users = {
    "admin": {"password": "admin123", "credits": float('inf')},  # Admin has unlimited calls
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/start-call", methods=["POST"])
def start_call():
    data = request.json
    user = data.get("user")
    caller_id = data.get("caller_id")
    target_number = data.get("target_number")

    if user not in users or users[user]["credits"] <= 0:
        return jsonify({"error": "Insufficient credits"}), 403

    # Deduct credits (Admin has unlimited calls)
    if user != "admin":
        users[user]["credits"] -= 1

    return jsonify({"message": f"Calling {target_number} with spoofed ID {caller_id}!"})

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username in users and users[username]["password"] == password:
        return jsonify({"message": "Login successful", "credits": users[username]["credits"]})
    return jsonify({"error": "Invalid credentials"}), 401

if __name__ == "__main__":
    app.run(debug=True)
