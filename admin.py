from flask import Flask, render_template, redirect, url_for
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
import stripe

app = Flask(__name__)
app.secret_key = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

# Stripe API Key
stripe.api_key = "your_stripe_secret_key"

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    credits = db.Column(db.Integer, default=0)
    is_banned = db.Column(db.Boolean, default=False)

# Transactions Model
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    amount = db.Column(db.Float)
    status = db.Column(db.String(50))

# Add to Admin Panel
admin = Admin(app, name="GhostSpoof Admin", template_mode="bootstrap3")
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Transaction, db.session))

@app.route("/")
def dashboard():
    total_revenue = db.session.query(db.func.sum(Transaction.amount)).scalar() or 0
    users = User.query.count()
    return render_template("admin_dashboard.html", total_revenue=total_revenue, users=users)

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
