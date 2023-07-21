# from flask import Flask, request, jsonify, render_template, redirect, url_for
# from flask_sqlalchemy import SQLAlchemy
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_login import LoginManager, UserMixin, login_user, login_required
# import pandas as pd
# import secrets

# app = Flask(__name__)
# app.config['SECRET_KEY'] = secrets.token_hex(16)  # Generate a secret key
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://textual_detectives_db_user:twVKnWDlc2A0Ou6FfFdQjCizFVrnxGgN@dpg-chinpee4dad01anku4v0-a.ohio-postgres.render.com/textual_detectives_db'

# @app.route('/')
# def home():
#     return render_template('login.html')

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         first_name = request.form.get('first_name')
#         last_name = request.form.get('last_name')
#         email = request.form.get('email')
#         title = request.form.get('title')

#         if first_name and last_name and email and title:
#             # Save data to the Excel file
#             new_user_data = pd.DataFrame([{'first_name': first_name, 'last_name': last_name, 'email': email, 'title': title}])
            
#             # 'a' mode for append if file exists
#             with pd.ExcelWriter('users.xlsx', mode='a') as writer:
#                 new_user_data.to_excel(writer)
            
#             return redirect(url_for('login'))  # Redirect user to login page after successful registration
#         else:
#             return render_template('register.html', error='Please fill in all fields.')  # Return with error if any field is empty

#     return render_template('register.html')  # Render the registration form

# @app.route('/login', methods=['POST'])
# def login():
#     if request.method == 'POST':
#         data = request.get_json()
#         username = data.get('username')
#         password = data.get('password')

#         if username == 'admin' and password == 'cvpmm2023':
#             # Login successful, redirect to index.html
#             return redirect(url_for('dashboard'))
        
# @app.route('/dashboard')
# def dashboard():
#     return render_template('analysis_page.html')

# @app.route('/analysis_page', methods=['GET'])
# def analysis_page():
#     # Read the Excel file into a DataFrame
#     df = pd.read_excel('/Users/paramdeepsinghbirdi/Downloads/selected_essays.xlsx')

#     # Select the desired columns from the DataFrame
#     selected_columns = [
#         'essay_id_sql',
#         'essay_set',
#         'rare_word_count',
#         'stop_word_count',
#         'avg_word_length',
#         'avg_sentence_length',
#         'sentiment_polarity',
#         'flesch_kincaid_grade_level',
#         'TTR'
#     ]
#     data = df[selected_columns].to_dict(orient='records')

#     # Return the template with data
#     return render_template('analysis_page.html', data=data)

# if __name__ == '__main__':
#     with app.app_context():
#          app.run(host='0.0.0.0', port=8000, debug=True)
