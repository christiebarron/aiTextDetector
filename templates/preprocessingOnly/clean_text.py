import json
import nltk
import spacy
import string
import warnings

from nltk.corpus import words, wordnet
from nltk.stem import WordNetLemmatizer

warnings.filterwarnings('ignore')

punctuations = string.punctuation
lemmatizer = WordNetLemmatizer()
stop_words = spacy.lang.en.stop_words.STOP_WORDS
vocab = set(w.lower() for w in words.words())

with open('contraction_words.json', 'r') as file:
    contractions = json.load(file)

def get_wordnet_pos(treebank_tag):

    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

# Cleans the text based on several specifications
def clean_text(text, remove_punct=True, expand_contractions=True, remove_stopwords=True, keep_propNouns=True, remove_nonwords=True, lemmatize=True, tokenize=True, lower=True):
    '''
    Cleans an input text for various nlp processing ends. Text should be a single string containing at least one word. Each subsequent argument can be turned off or on, described below.
    remove_punct: Removes punctuation
    expand_contractions: Expands contractions words (e.g., turns "it's" to "it is")
    remove_stopwords: Removes stopwords based on spacy.lang.en.stop_words.STOP_WORDS]
    keep_propNouns: Removes proper nouns (based on words with first letter capatalized not following a period, can have errors)
    remove_nonwords: Removes words that are not recognized (in nltk.corpus.words)
    lemmatize: Lemmatizes words based on nltk.stem.WordNetLemmatizer
    tokenize: Converts string to list of words
    lower: Converts all letters to lower-case
    '''
    if expand_contractions:
        text = nltk.word_tokenize(text)
        for i in range(len(text)):
            word = text[i]
            if word in contractions.keys():
                if type(contractions[word]) == list:
                    text[i] = contractions[word][0]
                else:
                    text[i] = contractions[word]
        text = ' '.join(text)

    if remove_punct:
        text = text.translate(str.maketrans('','',punctuations.replace('-','')))
    
    if remove_stopwords:
        text = [i for i in nltk.word_tokenize(text) if i.lower() not in stop_words]
        text = ' '.join(text)
    
    if not keep_propNouns:
        pos_tags = nltk.pos_tag(text.split())
        text = [pos[0] for pos in pos_tags if pos[1] != 'NNP']
        text = ' '.join(text)

    if remove_nonwords:
        text = nltk.word_tokenize(text)
        pos_tags = nltk.pos_tag(text)
        t = []
        for pos in pos_tags:
            if pos[1] == 'NNP':
                t.append(pos[0])
            else:
                lemma = lemmatizer.lemmatize(pos[0], pos=get_wordnet_pos(pos[1]))
                if lemma.lower() in vocab:
                    t.append(pos[0])
        text = ' '.join(t)

    if lemmatize:
        text = nltk.word_tokenize(text)
        pos_tags = nltk.pos_tag(text)
        text = [lemmatizer.lemmatize(i[0], pos=get_wordnet_pos(i[1])) for i in pos_tags]
        text = ' '.join(text)

    if tokenize:
        if lower:
            text = nltk.word_tokenize(text.lower())
        else:
            text = nltk.word_tokenize(text)
    else:
        if lower:
            text = text.lower()

    return text
