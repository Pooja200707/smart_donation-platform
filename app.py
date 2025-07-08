from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

# Dummy credentials (testing purpose)
users = {
    "admin": "password123",
    "user": "donate2025"
}

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            return f"Welcome, {username}! 🎉"
        else:
            error = "Invalid Username or Password"
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)