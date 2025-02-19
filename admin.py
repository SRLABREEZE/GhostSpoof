from flask import Flask, render_template, request, redirect, url_for, session
from firebase_admin import credentials, firestore, initialize_app
import firebase_admin
from firebase_admin import auth

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure key

# Initialize Firebase
cred = credentials.Certificate("path/to/your/firebase/credentials.json")  # Update with correct path
if not firebase_admin._apps:
    firebase_app = initialize_app(cred)

db = firestore.client()
admins_ref = db.collection("admins")

# Admin authentication function
def is_admin(user_id):
    admin_doc = admins_ref.document(user_id).get()
    return admin_doc.exists and admin_doc.to_dict().get("role") == "admin"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        try:
            user = auth.get_user_by_email(email)
            session["user_id"] = user.uid
            return redirect(url_for("dashboard"))
        except auth.AuthError:
            return "Login failed. Please check your credentials."
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("login"))
    
    user_id = session["user_id"]
    if is_admin(user_id):
        return render_template("dashboard.html")
    else:
        return "Access denied. You must be an admin to access this page."

@app.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
