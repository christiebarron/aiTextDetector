#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# FINAL CODE to Scrape the-good-ai.com's AI example essays.

#import dependencies
from splinter import Browser
from bs4 import BeautifulSoup as soup
from numpy import random
from time import sleep
import pandas as pd
import os

# Set up Splinter's browser
browser = Browser('chrome')


#create variables to save with so don't overwrite previously generated text
total_counter =  len(os.listdir('/Users/paramdeepsinghbirdi/Documents/GitHub/aiTextDetector/AI learning module/')) +2 
genre_count = 8
llm = 'the-good-ai'

#develop base_url
base_url = 'https://www.the-good-ai.com'
query1 = '/examples/'
query2 = '?category='

#loop through each genre type
genre = ['memoir', 'math', 'physics', 'philosophy', 'engineering', 'finance', 'economics', 'chemistry', 'biology', 'music', 'technology', 'comparative', 'history', 'literature', 'art', 'geography', 'religion']

# Create an empty DataFrame
df = pd.DataFrame(columns=['Essay_ID', 'Genre', 'Title', 'Essay'])

for word in genre:
    
    genre_count = genre_count + 1
    track_genre = word

    #specify the url for each genre
    url_genre = f'{base_url}{query1}{query2}{word}'

    #pause the analysis for about 20 seconds
    wait = random.normal(3, .5, 1)[0]
    sleep(wait)

    #visit the url for each genre
    browser.visit(url_genre)
    sleep(3)

    # save and Parse the html for each genre
    html = browser.html
    html_soup = soup(html, 'html.parser')   
    
    #get information about essays for a given genre
    links = html_soup.find_all('a')

    #save and extract all links for a given genre page
    post_link = []
    for link in links:
        post_link.append(link['href'])

    #filter out links to just include links to essays
    privacy_policy_keywords = ['privacy-policy', 'privacy_policy', 'terms-of-use', 'terms_of_use']
    search_term = '/post/'
    to_click = [link for link in post_link if not any(keyword in link for keyword in privacy_policy_keywords)]
    for link in post_link:
        if search_term in link:
            to_click.append(f'{base_url}{link}')
    
    #go to each link (essay) and extract relevant information
    for page in to_click:
        #pause the analysis for appx 15 sec
        wait = random.normal(3, .5, 1)[0]
        sleep(wait)

        #visit the page
        try: 
            browser.visit(page)
            sleep(3)
            #save and parse the html for given essay
            html = browser.html
            html_soup = soup(html, 'html.parser') 
            
            #extract the title
            title = html_soup.find('span', class_ = 'fancy highlighted').text

            #create list w/ title
            essay_text = []
            essay_text.append(f'{title}\n')

            #extract the paragraphs and add to list
            paragraphs = html_soup.find_all('p')
            for paragraph in paragraphs:
                essay_text.append(f'{paragraph.text}')

            #combine title
            final_essay = ''.join(essay_text)
            final_essay

            #increase counter
            
            essay_id = f'Essay-{total_counter}'
            df = df.append({'Essay_ID': essay_id, 'Genre': track_genre, 'Title': title, 'Essay': final_essay}, ignore_index=True)
            
            total_counter = total_counter + 1
            
#             save_file_path = '/Users/paramdeepsinghbirdi/Documents/GitHub/aiTextDetector/AI learning module/all_essays.xlsx'
#             df.to_excel(save_file_path, index=False)

#             #save the full document as text
#             save_path = f'../rawData/aiEssays/eid{genre_count}-{llm}_{total_counter}.txt'
#             with open(save_path, 'w') as f:
#                 f.write(final_essay)
                
        except Exception as e:
            print(f'error occurred with {page} {e}')

# Save the DataFrame to an Excel file
save_file_path = '/Users/paramdeepsinghbirdi/Documents/GitHub/aiTextDetector/AI learning module/all_essays.xlsx'
df.to_excel(save_file_path, index=False)
        
browser.quit()


# In[11]:


import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Load the scraped essays from the Excel file
essays_df = pd.read_excel('/Users/paramdeepsinghbirdi/Documents/GitHub/aiTextDetector/AI learning module/all_essays.xlsx')

# Function to clean and preprocess the essay text
def clean_essay_text(text):
    # Remove HTML tags
    cleaned_text = re.sub('<.*?>', '', text)
    # Convert to lowercase
    cleaned_text = cleaned_text.lower()
    # Remove punctuation and special characters
    cleaned_text = re.sub('[^\w\s]', '', cleaned_text)
    # Remove leading/trailing whitespaces
    cleaned_text = cleaned_text.strip()
    return cleaned_text

# Function to perform tokenization and remove stop words
def tokenize_and_remove_stopwords(text):
    # Tokenize the text into individual words
    tokens = word_tokenize(text)
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    return tokens

# Function to perform lemmatization
def lemmatize_text(tokens):
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return lemmatized_tokens

# Apply transformations to the essay text column
essays_df['Cleaned_Essay'] = essays_df['Essay'].apply(clean_essay_text)
essays_df['Tokenized_Essay'] = essays_df['Cleaned_Essay'].apply(tokenize_and_remove_stopwords)
essays_df['Lemmatized_Essay'] = essays_df['Tokenized_Essay'].apply(lemmatize_text)

# Save the transformed data to a new Excel file
transformed_file_path = '/Users/paramdeepsinghbirdi/Documents/GitHub/aiTextDetector/AI learning module/transformed_essays.xlsx'
essays_df.to_excel(transformed_file_path, index=False)


# In[12]:


import pandas as pd
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.util import ngrams
from collections import Counter

# Function to extract lexical features
def extract_lexical_features(text):
    words = word_tokenize(text)
    sentences = sent_tokenize(text)
    
    total_word_count = len(words)
    avg_word_length = sum(len(word) for word in words) / len(words)
    avg_sentence_length = sum(len(sentence.split()) for sentence in sentences) / len(sentences)
    word_counts = Counter(words)
    TTR = len(word_counts) / len(words)
    stop_words = set(stopwords.words('english'))
    stop_word_count = sum(1 for word in words if word.lower() in stop_words)
    unique_word_count = sum(1 for _, count in word_counts.items() if count == 1)
    word_freq = word_counts
    bigram_freq = Counter(ngrams(words, 2))
    trigram_freq = Counter(ngrams(words, 3))
    rare_word_count = sum(1 for _, count in word_counts.items() if count == 1)

    return {
        'total_word_count': total_word_count,
        'avg_word_length': avg_word_length,
        'avg_sentence_length': avg_sentence_length,
        'TTR': TTR,
        'stop_word_count': stop_word_count,
        'unique_word_count': unique_word_count,
        'word_freq': word_freq,
        'bigram_freq': bigram_freq,
        'trigram_freq': trigram_freq,
        'rare_word_count': rare_word_count
    }

# Load the transformed essays from the Excel file
essays_df = pd.read_excel('/Users/paramdeepsinghbirdi/Documents/GitHub/aiTextDetector/AI learning module/transformed_essays.xlsx')

# Extract lexical features from the transformed essays
essays_df['Lexical_Features'] = essays_df['Lemmatized_Essay'].apply(extract_lexical_features)

# Save the essays with lexical features to a new Excel file
essays_df.to_excel('/Users/paramdeepsinghbirdi/Documents/GitHub/aiTextDetector/AI learning module/essays_with_lexical_features.xlsx', index=False)


# In[13]:


import pandas as pd
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.util import ngrams
from collections import Counter

# Function to extract lexical features
def extract_lexical_features(text):
    words = word_tokenize(text)
    sentences = sent_tokenize(text)
    
    total_word_count = len(words)
    avg_word_length = sum(len(word) for word in words) / len(words)
    avg_sentence_length = sum(len(sentence.split()) for sentence in sentences) / len(sentences)
    word_counts = Counter(words)
    TTR = len(word_counts) / len(words)
    stop_words = set(stopwords.words('english'))
    stop_word_count = sum(1 for word in words if word.lower() in stop_words)
    unique_word_count = sum(1 for _, count in word_counts.items() if count == 1)
    word_freq = word_counts
    bigram_freq = Counter(ngrams(words, 2))
    trigram_freq = Counter(ngrams(words, 3))
    rare_word_count = sum(1 for _, count in word_counts.items() if count == 1)

    return {
        'Total_Word_Count': total_word_count,
        'Avg_Word_Length': avg_word_length,
        'Avg_Sentence_Length': avg_sentence_length,
        'TTR': TTR,
        'Stop_Word_Count': stop_word_count,
        'Unique_Word_Count': unique_word_count,
        'Word_Frequency': word_freq,
        'Bigram_Frequency': bigram_freq,
        'Trigram_Frequency': trigram_freq,
        'Rare_Word_Count': rare_word_count
    }

# Load the transformed essays from the Excel file
essays_df = pd.read_excel('/Users/paramdeepsinghbirdi/Documents/GitHub/aiTextDetector/AI learning module/transformed_essays.xlsx')

# Extract lexical features from the transformed essays
lexical_features = essays_df['Lemmatized_Essay'].apply(extract_lexical_features)

# Create separate columns for each lexical feature
lexical_features_df = pd.DataFrame(list(lexical_features))
essays_df = pd.concat([essays_df, lexical_features_df], axis=1)

# Save the essays with lexical features to a new Excel file
essays_df.to_excel('/Users/paramdeepsinghbirdi/Documents/GitHub/aiTextDetector/AI learning module/essays_with_lexical_features.xlsx', index=False)


# In[17]:


import pandas as pd
import numpy as np
import spacy

# Function to extract syntactic features
def extract_syntactic_features(text):
    doc = nlp(text)

    # Calculate average sentence length
    sentence_lengths = [len(sent) for sent in doc.sents]
    avg_sentence_length = np.mean(sentence_lengths)

    # Calculate parse tree depth
    def calc_tree_depth(sent):
        root = [token for token in sent if token.head == token][0]
        return max([len(list(token.ancestors)) for token in sent])

    tree_depths = [calc_tree_depth(sent) for sent in doc.sents]
    avg_parse_tree_depth = np.mean(tree_depths)
    parse_tree_depth_variation = np.std(tree_depths)

    return {
        'Avg_Sentence_Length': avg_sentence_length,
        'Avg_Parse_Tree_Depth': avg_parse_tree_depth,
        'Parse_Tree_Depth_Variation': parse_tree_depth_variation,
    }

# Load the transformed essays from the Excel file
essays_df = pd.read_excel('/Users/paramdeepsinghbirdi/Documents/GitHub/aiTextDetector/AI learning module/transformed_essays.xlsx')

# Load the language model for syntactic analysis (e.g., spaCy)
nlp = spacy.load('en_core_web_sm')

# Extract syntactic features from the transformed essays
syntactic_features = essays_df['Lemmatized_Essay'].apply(extract_syntactic_features)

# Create separate columns for each syntactic feature
syntactic_features_df = pd.DataFrame(list(syntactic_features))
essays_df = pd.concat([essays_df, syntactic_features_df], axis=1)

# Save the essays with lexical and syntactic features to a new Excel file
essays_df.to_excel('/Users/paramdeepsinghbirdi/Documents/GitHub/aiTextDetector/AI learning module/essays_with_lexical_syntactic_features.xlsx', index=False)


# In[20]:


import pandas as pd
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
import string

# Function to extract stylistic features
def extract_stylistic_features(text):
    sentences = sent_tokenize(text)
    num_sentences = len(sentences)
    
    tokenized_sentences = [word_tokenize(sentence) for sentence in sentences]
    pos_tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
    
    num_adjectives = sum(sum(1 for word, pos in sentence if pos.startswith('JJ')) for sentence in pos_tagged_sentences)
    num_adverbs = sum(sum(1 for word, pos in sentence if pos.startswith('RB')) for sentence in pos_tagged_sentences)
    num_verbs = sum(sum(1 for word, pos in sentence if pos.startswith('VB')) for sentence in pos_tagged_sentences)
    num_nouns = sum(sum(1 for word, pos in sentence if pos.startswith('NN')) for sentence in pos_tagged_sentences)

    avg_adjectives_per_sentence = num_adjectives / num_sentences
    avg_adverbs_per_sentence = num_adverbs / num_sentences
    avg_verbs_per_sentence = num_verbs / num_sentences
    avg_nouns_per_sentence = num_nouns / num_sentences
    
    return {
        'Avg_Adjectives_per_Sentence': avg_adjectives_per_sentence,
        'Avg_Adverbs_per_Sentence': avg_adverbs_per_sentence,
        'Avg_Verbs_per_Sentence': avg_verbs_per_sentence,
        'Avg_Nouns_per_Sentence': avg_nouns_per_sentence,
    }

# Load the transformed essays from the Excel file
essays_df = pd.read_excel('/Users/paramdeepsinghbirdi/Documents/GitHub/aiTextDetector/AI learning module/transformed_essays.xlsx')

# Extract stylistic features from the transformed essays
stylistic_features = essays_df['Lemmatized_Essay'].apply(extract_stylistic_features)

# Create separate columns for each stylistic feature
stylistic_features_df = pd.DataFrame(list(stylistic_features))
essays_df = pd.concat([essays_df, stylistic_features_df], axis=1)

# Function to count punctuation
def count_punctuation(text):
    punctuation_count = sum(1 for char in text if char in string.punctuation)
    punct_length = sum(1 for char in text)
    punctuation_proportion = punctuation_count / punct_length
    return {"Punctuation_Proportion": punctuation_proportion}

# Extract punctuation features from the transformed essays
punctuation_features = essays_df['Lemmatized_Essay'].apply(count_punctuation)

# Create separate columns for punctuation features
punctuation_features_df = pd.DataFrame(list(punctuation_features))
essays_df = pd.concat([essays_df, punctuation_features_df], axis=1)

# Save the essays with lexical, syntactic, stylistic, and punctuation features to a new Excel file
essays_df.to_excel('/Users/paramdeepsinghbirdi/Documents/GitHub/aiTextDetector/AI learning module/essays_with_stylistic_features.xlsx', index=False)


# In[25]:


import pandas as pd
import spacy
from textblob import TextBlob
import textstat

# Initialize spaCy English model
nlp_spacy = spacy.load('en_core_web_sm')

# Function to count passive sentences
def count_passive_sentences(text):
    passive_sentences = 0
    doc = nlp_spacy(text)
    for token in doc:
        if token.dep_ == 'nsubjpass':
            passive_sentences += 1
    return passive_sentences

# Function to calculate readability scores
def readability_scores(text):
    flesch_reading_ease = textstat.flesch_reading_ease(text)
    flesch_kincaid_grade_level = textstat.text_standard(text, float_output=True)
    smog_index = textstat.smog_index(text)
    return {
        "Flesch_Reading_Ease": flesch_reading_ease,
        "Flesch_Kincaid_Grade_Level": flesch_kincaid_grade_level,
        "SMOG_Index": smog_index
    }

# Function to calculate sentiment analysis scores
def sentiment_analysis_scores(text):
    sentiment = TextBlob(text)
    return {
        "Sentiment_Polarity": sentiment.polarity,
        "Sentiment_Subjectivity": sentiment.subjectivity
    }

# Load the transformed essays from the Excel file
essays_df = pd.read_excel('/Users/paramdeepsinghbirdi/Documents/GitHub/aiTextDetector/AI learning module/transformed_essays.xlsx')

# Calculate passive sentences for the transformed essays
essays_df['Passive_Sentences'] = essays_df['Lemmatized_Essay'].apply(count_passive_sentences)

# Calculate readability scores for the transformed essays
readability_scores = essays_df['Lemmatized_Essay'].apply(readability_scores)
readability_scores_df = pd.DataFrame(list(readability_scores))
essays_df = pd.concat([essays_df, readability_scores_df], axis=1)

# Calculate sentiment analysis scores for the transformed essays
sentiment_scores = essays_df['Lemmatized_Essay'].apply(sentiment_analysis_scores)
sentiment_scores_df = pd.DataFrame(list(sentiment_scores))
essays_df = pd.concat([essays_df, sentiment_scores_df], axis=1)

# Save the essays with all features to a new Excel file
essays_df.to_excel('/Users/paramdeepsinghbirdi/Documents/GitHub/aiTextDetector/AI learning module/essays_with_all_features.xlsx', index=False)


# In[ ]:




