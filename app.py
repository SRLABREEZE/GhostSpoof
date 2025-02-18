import os
import stripe
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Stripe API Configuration
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")  # Load from environment

# Fake user database (Replace with actual DB later)
users = {
    "user@example.com": {"password": "password123", "minutes": 120}
}

CREDIT_PACKAGES = {
    "10": {"amount": 500, "minutes": 60},
    "30": {"amount": 1200, "minutes": 180},
    "50": {"amount": 2000, "minutes": 300},
    "100": {"amount": 3500, "minutes": 600},
    "500": {"amount": 8000, "minutes": 3000}
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard', methods=['POST'])
def dashboard():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username]["password"] == password:
        return render_template('dashboard.html', user=username, minutes=users[username]["minutes"])
    else:
        return "Invalid login. Try again."

@app.route('/buy-credits')
def buy_credits():
    return render_template('buy_credits.html')

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    selected_credits = request.form['credits']
    package = CREDIT_PACKAGES[selected_credits]

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {'name': f'{package["minutes"]} Minutes'},
                'unit_amount': package["amount"],  # Convert to cents
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=url_for('payment_success', _external=True),
        cancel_url=url_for('dashboard', _external=True)
    )

    return redirect(session.url, code=303)

@app.route('/payment-success')
def payment_success():
    # Example: Add 60 minutes (In real DB, update user balance)
    users["user@example.com"]["minutes"] += 60
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
