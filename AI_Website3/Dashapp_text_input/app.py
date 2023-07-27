from flask import Flask, render_template, request
import joblib
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import TfidfTransformer
import pandas as pd
from scipy import sparse
import pickle 
import torch


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/essay" , methods=['GET', 'POST'])
def essay():
        #value = ['Modern terrorism is attracted to the media, and some extreme terrorist groups use it since it is the role of the media to report on any significant event. Moreover, extreme terrorist acts use the media since spectacular and dramatic terrorism aspects fascinate the public. However, terrorism should not impact the']
        #value = ['Technology has revolutionized various aspects of our lives, and one domain that has witnessed significant transformation is education. The integration of technology in educational settings has redefined the learning experience, enhancing access to information, fostering interactive engagement, and promoting personalized instruction. In this essay, we will explore the profound impact of technology on education, including its role in expanding educational opportunities, improving teaching methods, and preparing students for the demands of the 21st century']

        # load the vectorizer
        value = request.form['text']
        value=[value]
        df = pd.read_csv("nn_file.csv")
        X_train, X_test, y_train, y_test = train_test_split(df['without_stopwords'], df['HumanVsAi'], random_state=0)

        count_vect = CountVectorizer()
        X_train_counts = count_vect.fit_transform(X_train)

        # transform a count matrix to a normalized tf-idf representation (tf-idf transformer)
        tfidf_transformer = TfidfTransformer()
        X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

        classifier= KNeighborsClassifier(n_neighbors=2)

        # training our classifier ; new_df['essay'] will be having numbers assigned for each category in train data
        clf = classifier.fit(X_train_tfidf,y_train)
        

        #count_vect = CountVectorizer()
        X_new_counts = count_vect.transform(value)

        #tfidf_transformer = TfidfTransformer()
        X_new_tfidf = tfidf_transformer.transform(X_new_counts)

        #loaded_model = torch.load('model_pytorch.pt')
        #loaded_model = pickle.load(open('knnpickle_file', 'rb'))       
        #loaded_model = joblib.load('finalized_model.sav')

        # make a prediction
        prediction=clf.predict(X_new_tfidf)

        return render_template('index.html', prediction_text=prediction)

if __name__ == '__main__':
    app.run(debug=True)
