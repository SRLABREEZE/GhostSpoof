from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Route for Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Route for Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Dummy Authentication Logic
        if email == 'test@ghostspoof.com' and password == 'password':
            session['user'] = email
            return redirect(url_for('dashboard'))
        else:
            return "Invalid Credentials! Try Again."
    return render_template('login.html')

# Route for Signup Page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Here you would handle user registration logic
        return redirect(url_for('login'))
    return render_template('signup.html')

# Route for Dashboard Page (After Login)
@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return f"Welcome {session['user']}! This is your dashboard."
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
