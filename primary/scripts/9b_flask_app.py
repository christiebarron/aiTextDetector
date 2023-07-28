from flask import Flask, render_template, request
import pandas as pd
import joblib
from nltk.tokenize import word_tokenize
from nltk import WordNetLemmatizer
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.util import ngrams
from collections import Counter
import numpy as np
from nltk.tree import Tree
import spacy
from textblob import TextBlob
import textstat
from nltk import pos_tag

app = Flask(__name__)

# Load the trained Random Forest model
model = joblib.load('best_rf_model.pkl')

# Preprocess the input text
def clean_text(text):
    text = "".join([word for word in text if word not in punctuation])
    tokens = word_tokenize(text)
    text = [word for word in tokens if word not in stopwords_list]
    return text

def lemmatize_text(word_tokens):
    lem_text = [wn.lemmatize(word) for word in word_tokens]
    return lem_text

# Feature extraction functions
def extract_lexical_features(words):
    word_counts = Counter(words)
    unique_word_count = sum(1 for _, count in word_counts.items() if count == 1)
    rare_word_count = sum(1 for _, count in word_counts.items() if count == 1)
    return {'unique_word_count': unique_word_count,
            'rare_word_count': rare_word_count}

def extract_syntactic_features(words):
    text = ' '.join(words)
    doc = nlp_spacy(text)
    def calc_tree_depth(sent):
        root = [token for token in sent if token.head == token][0]
        return max([len(list(token.ancestors)) for token in sent])

    tree_depths = [calc_tree_depth(sent) for sent in doc.sents]
    parse_tree_depth_variation = np.std(tree_depths)

    return {
        'parse_tree_depth_variation': parse_tree_depth_variation,
    }

def extract_stylistic_features(words):
    text = ' '.join(words) 
    sentences = sent_tokenize(text)
    num_sentences = len(sentences)
    tokenized_sentences = [word_tokenize(sentence) for sentence in sentences]
    pos_tagged_sentences = [pos_tag(sentence) for sentence in tokenized_sentences]
    num_adjectives = sum(sum(1 for word, pos in sentence if pos.startswith('JJ')) for sentence in pos_tagged_sentences)
    avg_adjectives_per_sentence = num_adjectives / num_sentences
    return {
        'avg_adjectives_per_sentence': avg_adjectives_per_sentence,
    }

def readability_scores(words):
    text = ' '.join(words) 
    flesch_reading_ease = textstat.flesch_reading_ease(text)
    flesch_kincaid_grade_level = textstat.text_standard(text, float_output=True)
    smog_index = textstat.smog_index(text)
    return {
        "flesch_reading_ease" : flesch_reading_ease, 
        "flesch_kincaid_grade_level" : flesch_kincaid_grade_level, 
        "smog_index" : smog_index
    }

# Function to predict human or AI text
def predict_text(text_input):
    preprocessed_text = lemmatize_text(clean_text(text_input))

    # Feature extraction
    lexical_features = extract_lexical_features(preprocessed_text)
    syntactic_features = extract_syntactic_features(preprocessed_text)
    stylistic_features = extract_stylistic_features(preprocessed_text)
    readability_feature = readability_scores(preprocessed_text)

    # Combine all features into a single dictionary
    text_features = {
        **lexical_features,
        **syntactic_features,
        **stylistic_features,
        **readability_feature
    }

    # Convert the features to a DataFrame with the same columns used during training
    text_features_df = pd.DataFrame([text_features])

    # Make predictions using the loaded model
    prediction = model.predict(text_features_df)
    probability_scores = model.predict_proba(text_features_df)
    
    return prediction, probability_scores

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text_input = request.form['text_input']

        # Perform prediction
        prediction, probability_scores = predict_text(text_input)

        # Render the HTML template with the prediction result
        return render_template('result.html', text_input=text_input, prediction=prediction[0])

    return render_template('index.html')

if __name__ == '__main__':
    # Initialize spaCy English model
    nlp_spacy = spacy.load('en_core_web_sm')
    wn = WordNetLemmatizer()  # specifying wn as the word net lemmatizer
    stopwords_list = stopwords.words('english')
    
    app.run(debug=True)
