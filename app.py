<<<<<<< HEAD
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to interact with backend

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ghostspoof.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    tokens = db.Column(db.Integer, default=15)  # Free 15 tokens

# Create the database tables
with app.app_context():
    db.create_all()

# User Signup Route
@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"message": "Email already registered"}), 400
    
    new_user = User(name=data['name'], email=data['email'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User registered successfully!"}), 201

# User Login Route
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email'], password=data['password']).first()
    
    if user:
        return jsonify({"message": "Login successful", "tokens": user.tokens}), 200
    return jsonify({"message": "Invalid credentials"}), 401

# Buy Tokens Route
@app.route('/buy-tokens', methods=['POST'])
def buy_tokens():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    
    if not user:
        return jsonify({"message": "User not found"}), 404

    token_packs = {
        "50": 50,
        "100": 100,
        "500": 500
    }
    
    if data["package"] in token_packs:
        user.tokens += token_packs[data["package"]]
        db.session.commit()
        return jsonify({"message": "Tokens added successfully!", "tokens": user.tokens}), 200
    
    return jsonify({"message": "Invalid package"}), 400

# Contact Form Submission
@app.route('/contact', methods=['POST'])
def contact():
    data = request.json
    # Here, you can integrate email sending or store the message in a database
    return jsonify({"message": "Message received. We'll get back to you soon!"}), 200

# Logout Route
@app.route('/logout', methods=['POST'])
def logout():
    return jsonify({"message": "User logged out successfully!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
=======
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "GhostSpoof is Live on Render!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
^O
^X

X
>>>>>>> a7244da (Fixed repository issue & added requirements.txt)
