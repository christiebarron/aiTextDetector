from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
import psycopg2
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
from collections import Counter
from nltk.tokenize import sent_tokenize
from nltk import pos_tag
import textstat
from textblob import TextBlob
import tensorflow as tf
import spacy
import numpy as np
#adding code for KNN Embedded Model
from flask import Flask, render_template, request
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import TfidfTransformer
import pandas as pd
from scipy import sparse
import pickle 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
from gensim.models import Word2Vec
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load the trained Keras model
model = tf.keras.models.load_model('my_tuned_model-2.h5')
# Initialize spaCy English model
nlp_spacy = spacy.load('en_core_web_sm')
wn = WordNetLemmatizer()  # specifying wn as the word net lemmatizer
stopwords_list = stopwords.words('english')

def clean_text(text):
    tokens = word_tokenize(text)
    return tokens 

def lemmatize_text(word_tokens):
    lem_text = [wn.lemmatize(word) for word in word_tokens]
    return lem_text

def extract_lexical_features(words):
    word_counts = Counter(words)
    unique_word_count = sum(1 for _, count in word_counts.items() if count == 1)
    stop_words = set(stopwords.words('english'))
    stop_word_count = sum(1 for word in words if word.lower() in stop_words)
    TTR = len(word_counts) / len(words)
    return {'unique_word_count': unique_word_count,
            'stop_word_count': stop_word_count,
            'TTR': TTR}
def extract_syntactic_features(text):  # pass raw text here
    doc = nlp_spacy(text)
    def calc_tree_depth(sent):
        root = [token for token in sent if token.head == token][0]
        return max([len(list(token.ancestors)) for token in sent])

    tree_depths = [calc_tree_depth(sent) for sent in doc.sents]
    avg_parse_tree_depth = np.mean(tree_depths)

    return {
        'avg_parse_tree_depth': avg_parse_tree_depth,
    }

def extract_stylistic_features(text):  # pass raw text here
    sentences = sent_tokenize(text)
    num_sentences = len(sentences)
    tokenized_sentences = [word_tokenize(sentence) for sentence in sentences]
    pos_tagged_sentences = [pos_tag(sentence) for sentence in tokenized_sentences]
    num_verbs = sum(sum(1 for word, pos in sentence if pos.startswith('VB')) for sentence in pos_tagged_sentences)
    num_nouns = sum(sum(1 for word, pos in sentence if pos.startswith('NN')) for sentence in pos_tagged_sentences)
    avg_verbs_per_sentence = num_verbs / num_sentences
    avg_nouns_per_sentence = num_nouns / num_sentences
    return {
        'avg_verbs_per_sentence': avg_verbs_per_sentence,
        'avg_nouns_per_sentence': avg_nouns_per_sentence
    }

def readability_scores(text):  # pass raw text here
    flesch_reading_ease = textstat.flesch_reading_ease(text)
    flesch_kincaid_grade_level = textstat.flesch_kincaid_grade(text)  # corrected function
    smog_index = textstat.smog_index(text)
    return {
        "flesch_reading_ease" : flesch_reading_ease, 
        "flesch_kincaid_grade_level" : flesch_kincaid_grade_level, 
        "smog_index" : smog_index
    }

def sentiment_analysis_scores(text):
    # text = ' '.join(words) 
    sentiment = TextBlob(text)
    return {
        "sentiment_polarity" : sentiment.polarity}

def predict_text(text_input):
    preprocessed_text = lemmatize_text(clean_text(text_input))

    # Feature extraction
    lexical_features = extract_lexical_features(preprocessed_text)
    syntactic_features = extract_syntactic_features(text_input)  # pass raw text
    stylistic_features = extract_stylistic_features(text_input)  # pass raw text
    readability_feature = readability_scores(text_input)  # pass raw text
    sentiment_feature = sentiment_analysis_scores(text_input)  # pass raw text

    # Combine all features into a single dictionary
    text_features = {
        **lexical_features,
        **syntactic_features,
        **stylistic_features,
        **readability_feature,
        **sentiment_feature
    }

    # Convert the features to a DataFrame with the same columns used during training
    text_features_df = pd.DataFrame([text_features])
    prediction = model.predict(text_features_df)
    return prediction, text_features


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
def main():
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

@app.route('/home', methods=['GET'])
@login_required
def home():
    return render_template('index.html')

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

# Adding KNN_Embeddings
# Preprocess the text data
def preprocess(text):
    stop_words = set(stopwords.words('english'))
    #text = text.lower()
    text = ''.join([word for word in text if word not in string.punctuation])
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(tokens)

# Vectorize the text data
def vectorize(sentence, w2v_model):
    words = sentence.split()
    words_vecs = [w2v_model.wv[word] for word in words if word in w2v_model.wv]
    if len(words_vecs) == 0:
        return np.zeros(100)
    words_vecs = np.array(words_vecs)
    return words_vecs.mean(axis=0)

@app.route("/essay" , methods=['GET', 'POST'])
@login_required
def essay():
    if request.method == 'POST':
        #Preprocessing Steps:
        value = request.form['text']
        value=[value]

        X_new = pd.DataFrame(value)  #human-generated

        #Call preprocess function:
        X_new = X_new.apply(lambda x: preprocess(x))
        sentences = [sentence.split() for sentence in X_new]

        #Vectorizing:
        w2v_model = Word2Vec(sentences, window=5, min_count=5, workers=4)

        X_new = np.array([vectorize(sentence, w2v_model) for sentence in X_new])

        loaded_model = pickle.load(open('knn_embd_model.pkl', 'rb'))
        # make a prediction
        prediction=loaded_model.predict(X_new)

        return render_template('index2.html', prediction_text=prediction)
    return render_template('index2.html')


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# @app.route('/predict_nn', methods=['GET', 'POST'])
# def predict_nn():
#     if request.method == 'POST':
#         text_input = request.form['text']
#         prediction, features = predict_text(text_input)
#         return render_template('index.html', prediction_text=prediction[0])
#     return render_template('index.html', prediction_text="")

@app.route('/predict_keras', methods=['GET', 'POST'])
def predict_keras():
    if request.method == 'POST':
        text_input = request.form['text_input']
        prediction,features = predict_text(text_input)
        # Interpret prediction
        if prediction[0] > 0.7:
            prediction_category = "AI-Generated"
        elif prediction[0] < 0.3:
            prediction_category = "Human-Written"
        else:
            prediction_category = "Intermediate"
        # Limit floats to 2 decimal places
        features = {key: round(value, 2) for key, value in features.items()}
        return render_template('result_keras.html', text_input=text_input, prediction=prediction[0], prediction_category=prediction_category, features=features)
    return render_template('predict_keras.html')

@app.route('/tableau_visualization')
@login_required
def tableau_visualization():
    return render_template('tableau_visualization.html')

@app.route('/documentation')
@login_required
def documentation():
    return render_template('project4Proposal.html')

if __name__ == "__main__":
    app.run(debug=True)