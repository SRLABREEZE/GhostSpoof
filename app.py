from flask import Flask, render_template, request, redirect, url_for, session, flash
import firebase_admin
from firebase_admin import credentials, auth, firestore

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Initialize Firebase Admin SDK
cred = credentials.Certificate("firebase_credentials.json")  # Ensure correct path
firebase_admin.initialize_app(cred)

# Firestore database reference
db = firestore.client()


# Homepage - Index
@app.route("/")
def home():
    return render_template("index.html")


# Login Page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        try:
            user = auth.get_user_by_email(email)
            session["user"] = user.uid  # Store UID in session
            return redirect(url_for("dashboard"))
        except firebase_admin.auth.AuthError:
            flash("Invalid credentials. Please try again.", "danger")
            return render_template("login.html")

    return render_template("login.html")


# Signup Page
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        try:
            user = auth.create_user(email=email, password=password)
            db.collection("users").document(user.uid).set({"email": email})  # Save user to Firestore
            flash("Account created successfully! Please login.", "success")
            return redirect(url_for("login"))
        except Exception as e:
            flash(f"Error: {e}", "danger")
            return render_template("signup.html")

    return render_template("signup.html")


# Dashboard Page (Restricted to Logged-in Users)
@app.route("/dashboard")
def dashboard():
    if "user" in session:
        user_id = session["user"]
        user_doc = db.collection("users").document(user_id).get()

        if user_doc.exists:
            user_data = user_doc.to_dict()
            return render_template("dashboard.html", user=user_data)
    
    flash("You must be logged in to access this page.", "warning")
    return redirect(url_for("login"))


# Logout
@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("Logged out successfully.", "info")
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
