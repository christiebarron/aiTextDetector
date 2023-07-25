import dash
from dash import Dash, dcc, html,dash_table, Input, Output,State, callback
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import TfidfTransformer
import pandas as pd
import pickle   


app = Dash(__name__)

app.layout = html.Div([
      
    dcc.Textarea(
        id='textarea-example',
        value='Your Essay',
        style={'width': '60%', 'height': 300},
    ),
    
    html.H1(id='textarea-example-output', style={'whiteSpace': 'pre-line'}),
                         
    
    html.H1(children='Cookie policy | Privacy policy | Terms of use |', style={'font-color':'red'})

])

@callback(
    Output('textarea-example-output', 'children'),
    Input('textarea-example', 'value')
)
def update_output(value):
        
        value = [value]

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

        # load the vectorizer
        X_new_counts = count_vect.transform(value)
        X_new_tfidf = tfidf_transformer.transform(X_new_counts)

        # load the model
       #loaded_model = joblib.load('finalized_model.sav')

        # make a prediction

        predictions=clf.predict(X_new_tfidf)
       # print(predictions)

    #    return predictions   

        return 'This essay is from : \n{}'.format(predictions)

if __name__ == '__main__':
    app.run(debug=True)
