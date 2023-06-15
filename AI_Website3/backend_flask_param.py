from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required
import pandas as pd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://textual_detectives_db_user:twVKnWDlc2A0Ou6FfFdQjCizFVrnxGgN@dpg-chinpee4dad01anku4v0-a.ohio-postgres.render.com/textual_detectives_db'
@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if username == 'admin' and password == 'cvpmm2023':
            # Login successful, redirect to index.html
            return redirect(url_for('dashboard'))
        else:
            # Login unsuccessful
            return jsonify({'message': 'Login unsuccessful'}), 401

@app.route('/dashboard')
def dashboard():
    return render_template('index.html')

@app.route('/data', methods=['GET'])
def get_data():
    # Read the Excel file into a DataFrame
    df = pd.read_excel('selected_essays.xlsx')

    # Select the desired columns from the DataFrame
    selected_columns = [
        'essay_id_sql',
        'essay_set',
        'rare_word_count',
        'stop_word_count',
        'avg_word_length',
        'avg_sentence_length',
        'sentiment_polarity',
        'flesch_kincaid_grade_level',
        'TTR',
        'smog_index'
    ]
    data = df[selected_columns].to_dict(orient='records')

    # Return the JSON response
    return jsonify(data)

@app.route('/live_app', methods=['GET', 'POST'])
def live_app():
    if request.method == 'POST':
        essay = request.form.get('essay')
        # Process the essay and perform AI or human essay detection
        # Generate the appropriate output
        # Return the result to be displayed on the Live App page

    return render_template('live_app.html')

@app.route('/word_cloud.html')
def word_cloud():
    return render_template('word_cloud.html')

@app.route('/teacherDashboard.html')
def teacherDashboard():
    return render_template('teacherDashboard.html')

# @app.route('/analysis_page')
# def analysis_page():
#     return render_template('analysis_page.html')

if __name__ == '__main__':
    with app.app_context():
         app.run(debug=True)