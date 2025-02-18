from flask import Flask, render_template, request, redirect, session
import stripe

app = Flask(__name__)
app.secret_key = "super_secure_random_string"

# Mock User Data
users = {"test@example.com": {"password": "password", "minutes": 15}}

# Stripe API Key
stripe.api_key = "sk_live_YOUR_SECRET_KEY"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "user" not in session:
        return redirect("/")
    return render_template("dashboard.html", user=session["user"], minutes=users[session["user"]]["minutes"])

@app.route("/buy-credits", methods=["GET", "POST"])
def buy_credits():
    return render_template("buy_credits.html")

@app.route("/create-checkout-session", methods=["POST"])
def create_checkout_session():
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {"name": "GhostSpoof Minutes"},
                    "unit_amount": 500,
                },
                "quantity": 1,
            }
        ],
        mode="payment",
        success_url="https://ghostspoof.onrender.com/payment-success",
        cancel_url="https://ghostspoof.onrender.com/buy-credits",
    )
    return redirect(session.url, code=303)

if __name__ == "__main__":
    app.run(debug=True)
