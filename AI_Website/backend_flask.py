from flask import Flask, request, jsonify, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://textual_detectives_db_user:twVKnWDlc2A0Ou6FfFdQjCizFVrnxGgN@dpg-chinpee4dad01anku4v0-a/textual_detectives_db'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')

    new_user = User(username=data['username'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'Registered successfully!'}), 200

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()

    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Login Unsuccessful. Please check username and password'}), 401

    login_user(user)

    return jsonify({'message': 'Login Successful!'}), 200

@app.route('/next_page')
@login_required
def next_page():
    return render_template('next_page.html', username=current_user.username)

@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect('/login')

@app.route('/create_admin', methods=['GET'])
def create_admin():
    hashed_password = generate_password_hash('cvpgm2023', method='sha256')
    new_user = User(username='admin', password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'Admin user created successfully'}), 200

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

@app.route('/teacherDashboard', methods = ['POST'])
def teacher_dashboard():
    #USE SQLALCHEMY TO ACCESS THE DATABASE

    # Import the dependencies
    from pathlib import Path
    from sqlalchemy.ext.automap import automap_base
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine
    
    # Create a reference to the dataset
    database_path = Path("!!TO ADD DATABASE PATH!!")
    # Create Database Connection
    engine = create_engine(f"sqlite:///{database_path}") 
        #MAY NEED TO REVISE THIS FOR RENDER TOO.

    # Declare a Base using `automap_base()`
    Base = automap_base()

    # Use the Base class to reflect the database tables
    Base.prepare(autoload_with=engine) 

    # Print all of the classes mapped to the Base
    Base.classes.keys()

    # Create a session
    session = Session(engine)

    # Query relevant records in the the Database
    queryDf = engine.execute("SELECT * FROM icecreamstore;")
    summaryDf = jsonify(queryDf)
    
    for record in data:
        print(record)



     

    #see https://stackoverflow.com/questions/60889087/how-to-fetch-data-from-postgresql-database-using-flask-and-display-html-tables

    #1. From  your db you read (select) your table and create a dataframe
    #2. return jsonify( version of the dataframe) convert the df into a json object 
    #that is going to be used in the js code later
    #other way to convert df to json is df.to_json()



    #push to API
    #use that dataframe in javascript code.
