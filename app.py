from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Make sure this is secure in production

# Home Page (Login & Signup)
@app.route('/')
def index():
    return render_template('index.html')

# Signup Route (Processes Signup Form)
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # In production, store user in a **database** instead of session
        session['username'] = username
        return redirect(url_for('dashboard'))

    return render_template('signup.html')

# Login Route (Handles Login)
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # In a real app, verify the username and password from a database
    if username:  
        session['username'] = username
        return redirect(url_for('dashboard'))

    return redirect(url_for('index'))

# Dashboard Route (After Login/Signup)
@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html', username=session['username'])
    return redirect(url_for('index'))

# Call Page (After Login)
@app.route('/call')
def call_page():
    if 'username' in session:
        return render_template('call.html')
    return redirect(url_for('index'))

# Buy Credits Page
@app.route('/buy_credits')
def buy_credits():
    if 'username' in session:
        return render_template('buy_credits.html')
    return redirect(url_for('index'))

# Logout Route
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
