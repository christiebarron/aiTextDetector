from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://textual_detectives_db_user:twVKnWDlc2A0Ou6FfFdQjCizFVrnxGgN@dpg-chinpee4dad01anku4v0-a.ohio-postgres.render.com/textual_detectives_db'

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username == 'admin' and password == 'cvpmm2023':
        # Login successful
        return jsonify({'message': 'Login successful'}), 200
    else:
        # Login unsuccessful
        return jsonify({'message': 'Login unsuccessful'}), 401
    return render_template('login.html')
@app.route('/analysis_page')
def analysis_page():
    return render_template('analysis_page.html')

if __name__ == '__main__':
    with app.app_context():
         app.run(host='0.0.0.0', port=5000, debug=True)
