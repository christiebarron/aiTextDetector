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
from imblearn.over_sampling import SMOTE
import tensorflow as tf
from tensorflow import _keras

app = Flask(__name__)

# from tensorflow.keras.models import load_model

# Load the trained Keras model
model = tf.keras.saving.load_model('my_tuned_model-2.h5')

# Load the trained Random Forest model
# model = joblib.load('best_rf_model.pkl')
# model = joblib.load('improved_random_forest_model-2.pkl')
# import pickle

# # Load the model
# with open('improved_random_forest_model.pkl', 'rb') as f:
#     model = pickle.load(f)
# model = load_model('my_tuned_model.h5')

# Preprocess the input text
# def clean_text(text):
#     text = "".join([word for word in text if word not in punctuation])
#     tokens = word_tokenize(text)
#     text = [word for word in tokens if word not in stopwords_list]
#     return text

# def clean_text(text):
#     text = "".join([word for word in text if word not in punctuation])
#     tokens = word_tokenize(text)
#     words = [word for word in tokens if word not in stopwords_list]
#     sentences = sent_tokenize(text)
#     return words, sentences, text

def clean_text(text):
    tokens = word_tokenize(text)
    return tokens 

def lemmatize_text(word_tokens):
    lem_text = [wn.lemmatize(word) for word in word_tokens]
    return lem_text

# Feature extraction functions
# def extract_lexical_features(words):
#     word_counts = Counter(words)
#     unique_word_count = sum(1 for _, count in word_counts.items() if count == 1)
#     stop_words = set(stopwords.words('english'))
#     stop_word_count = sum(1 for word in words if word.lower() in stop_words)
#     word_counts = Counter(words)
#     TTR = len(word_counts) / len(words)
#     return {'unique_word_count': unique_word_count,
#             'stop_word_count': stop_word_count,
#             'TTR': TTR}

def extract_lexical_features(words):
    word_counts = Counter(words)
    unique_word_count = sum(1 for _, count in word_counts.items() if count == 1)
    stop_words = set(stopwords.words('english'))
    stop_word_count = sum(1 for word in words if word.lower() in stop_words)
    TTR = len(word_counts) / len(words)
    return {'unique_word_count': unique_word_count,
            'stop_word_count': stop_word_count,
            'TTR': TTR}

# def extract_syntactic_features(words):
#     text = ' '.join(words)
#     doc = nlp_spacy(text)
#     def calc_tree_depth(sent):
#         root = [token for token in sent if token.head == token][0]
#         return max([len(list(token.ancestors)) for token in sent])

#     tree_depths = [calc_tree_depth(sent) for sent in doc.sents]
#     avg_parse_tree_depth = np.mean(tree_depths)
#     parse_tree_depth_variation = np.std(tree_depths)

#     return {
#         'avg_parse_tree_depth': avg_parse_tree_depth,
#     }

# def extract_syntactic_features(sentences):
    
#     def calc_tree_depth(sent):
#         root = [token for token in sent if token.head == token][0]
#         return max([len(list(token.ancestors)) for token in sent])
#     tree_depths = [calc_tree_depth(nlp_spacy(sent)) for sent in sentences]
#     avg_parse_tree_depth = np.mean(tree_depths)
#     return {
#         'avg_parse_tree_depth': avg_parse_tree_depth,
#     }

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

# def extract_stylistic_features(sentences):
#     # text = ' '.join(words) 
#     # sentences = sent_tokenize(text)
#     num_sentences = len(sentences)
#     tokenized_sentences = [word_tokenize(sentence) for sentence in sentences]
#     pos_tagged_sentences = [pos_tag(sentence) for sentence in tokenized_sentences]
#     num_adjectives = sum(sum(1 for word, pos in sentence if pos.startswith('JJ')) for sentence in pos_tagged_sentences)
#     num_verbs = sum(sum(1 for word, pos in sentence if pos.startswith('VB')) for sentence in pos_tagged_sentences)
#     num_nouns = sum(sum(1 for word, pos in sentence if pos.startswith('NN')) for sentence in pos_tagged_sentences)
#     avg_adjectives_per_sentence = num_adjectives / num_sentences
#     avg_verbs_per_sentence = num_verbs / num_sentences
#     avg_nouns_per_sentence = num_nouns / num_sentences
#     return {
#         'avg_verbs_per_sentence': avg_verbs_per_sentence,
#         'avg_nouns_per_sentence': avg_nouns_per_sentence
#     }

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

# def readability_scores(text):
#     # text = ' '.join(words) 
#     flesch_reading_ease = textstat.flesch_reading_ease(text)
#     flesch_kincaid_grade_level = textstat.text_standard(text, float_output=True)
#     smog_index = textstat.smog_index(text)
#     return {
#         "flesch_reading_ease" : flesch_reading_ease, 
#         "flesch_kincaid_grade_level" : flesch_kincaid_grade_level, 
#         "smog_index" : smog_index
#     }

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
        # "sentiment.subjectivity" : sentiment.subjectivity}

# Function to predict human or AI text
# def predict_text(text_input):
#     words, sentences, text = clean_text(text_input)
#     lemmatized_words = lemmatize_text(words)
#     # preprocessed_text = lemmatize_text(clean_text(text_input))

#     # Feature extraction
#     # lexical_features = extract_lexical_features(preprocessed_text)
#     # syntactic_features = extract_syntactic_features(preprocessed_text)
#     # stylistic_features = extract_stylistic_features(preprocessed_text)
#     # readability_feature = readability_scores(preprocessed_text)
#     # sentiment_feature = sentiment_analysis_scores(preprocessed_text)

#     lexical_features = extract_lexical_features(lemmatized_words)
#     syntactic_features = extract_syntactic_features(sentences)
#     stylistic_features = extract_stylistic_features(sentences)
#     readability_feature = readability_scores(text)
#     sentiment_feature = sentiment_analysis_scores(text)
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

    # Make predictions using the loaded model
    # text_features_array = np.array(text_features_df).reshape(-1, 10, 1)
    # prediction = model.predict(text_features_array)
    prediction = model.predict(text_features_df)
    # probability_scores = model.predict(text_features_df)
    
    return prediction, text_features

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text_input = request.form['text_input']

        # Perform prediction
        prediction,features = predict_text(text_input)

        # Render the HTML template with the prediction result
        return render_template('result.html', text_input=text_input, prediction=prediction[0],features=features)

    return render_template('index.html')

if __name__ == '__main__':
    # Initialize spaCy English model
    nlp_spacy = spacy.load('en_core_web_sm')
    wn = WordNetLemmatizer()  # specifying wn as the word net lemmatizer
    stopwords_list = stopwords.words('english')
    
    app.run(debug=True)
