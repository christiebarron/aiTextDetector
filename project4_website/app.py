import psycopg2
from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user

# Setup Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

# Setup Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# Setup database connection
conn = psycopg2.connect("postgres://textual_detectives_db_user:twVKnWDlc2A0Ou6FfFdQjCizFVrnxGgN@dpg-chinpee4dad01anku4v0-a.ohio-postgres.render.com/textual_detectives_db")

# Create users table if it does not exist
cur = conn.cursor()
try:
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users
        (id SERIAL PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL)
    ''')
    conn.commit()
except Exception as e:
    print("Couldn't create table: ", e)
class User(UserMixin):
    def __init__(self, id):
        self.id = id

# This would be replaced by your user loading function
@login_manager.user_loader
def load_user(user_id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user_data = cur.fetchone()
    return User(user_data[0]) if user_data else None
@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password') # You should hash and check the password in a real scenario
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user_data = cur.fetchone()
        if user_data:
            user = User(user_data[0])
            login_user(user)
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error="Invalid username or password. Please try again.")  
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password') # You need to hash this password before saving it
        cur = conn.cursor()
        cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        return redirect(url_for('login'))
    else:
        return render_template('register.html')  # assuming you have a 'register.html' in templates folder


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
