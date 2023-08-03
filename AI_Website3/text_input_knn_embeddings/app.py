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

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/essay" , methods=['GET', 'POST'])
def essay():
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

    return render_template('index.html', prediction_text=prediction)

# Preprocess the text data
def preprocess(text):
    stop_words = set(stopwords.words('english'))
    #text = text.lower()
    text = ''.join([word for word in text if word not in string.punctuation])
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(tokens)
    #Ai-generated

# Vectorize the text data
def vectorize(sentence, w2v_model):
    words = sentence.split()
    words_vecs = [w2v_model.wv[word] for word in words if word in w2v_model.wv]
    if len(words_vecs) == 0:
        return np.zeros(100)
    words_vecs = np.array(words_vecs)
    return words_vecs.mean(axis=0)


if __name__ == '__main__':
    app.run(debug=True)
