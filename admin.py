from flask import Flask, render_template, redirect, url_for, request, flash from flask_admin import Admin from flask_admin.contrib.sqla import ModelView from flask_sqlalchemy import SQLAlchemy from flask_login import UserMixin, LoginManager, login_user, logout_user, login_required, current_user from flask_bcrypt import Bcrypt import firebase_admin from firebase_admin import credentials, firestore

Initialize Flask App

app = Flask(name) app.secret_key = "your_secret_key" app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db" db = SQLAlchemy(app) bcrypt = Bcrypt(app)

Firebase Setup

cred = credentials.Certificate("firebase_credentials.json") firebase_admin.initialize_app(cred) firestore_db = firestore.client()

Flask-Login Setup

login_manager = LoginManager() login_manager.init_app(app) login_manager.login_view = "login"

User Model

class User(db.Model, UserMixin): id = db.Column(db.Integer, primary_key=True) email = db.Column(db.String(150), unique=True, nullable=False) password = db.Column(db.String(255), nullable=False) is_admin = db.Column(db.Boolean, default=False)

Load User

@login_manager.user_loader def load_user(user_id): return User.query.get(int(user_id))

Admin Panel Protection

class AdminModelView(ModelView): def is_accessible(self): return current_user.is_authenticated and current_user.is_admin def inaccessible_callback(self, name, **kwargs): return redirect(url_for("login"))

Routes

@app.route("/") @login_required def dashboard(): if not current_user.is_admin: flash("Access Denied!", "danger") return redirect(url_for("login")) return render_template("admin_dashboard.html")

@app.route("/login", methods=["GET", "POST"]) def login(): if request.method == "POST": email = request.form["email"] password = request.form["password"] user = User.query.filter_by(email=email).first() if user and bcrypt.check_password_hash(user.password, password): login_user(user) return redirect(url_for("dashboard")) else: flash("Invalid credentials!", "danger") return render_template("login.html")

@app.route("/logout") @login_required def logout(): logout_user() return redirect(url_for("login"))

Flask Admin Setup

admin = Admin(app, name="GhostSpoof Admin", template_mode="bootstrap3") admin.add_view(AdminModelView(User, db.session))

if name == "main": db.create_all() app.run(debug=True)

