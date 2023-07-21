# Project 4 Proposal

We propose extending the first 3 projects to incorporate a machine-learning component. In particular, we propose extending the full-stack data visualization web application from project 3 to incorporate machine-learning-based classification of machine-generated text. 

This project will primarily extend project 3 by adding a live text-input webpage.

## Text-input Webpage

A text-input webpage in which anyone can input written text and our app will provide a dashboard depicting:

1. The likelihood the provided text was AI-generated

2. Pedagogically-meaningful writing feedback about the submitted text (e.g., grade level, syntactic complexity, most common words, comparison to other students, showing the text itself).

3. Time-permitting, documentation that describes the NLP pipeline, ML classification algorithm, and and visualizes 

### Pre-processing
Pre-processing is required for both text classification and the pedagogical report:

- Deploy our NLP pipeline to the cloud so features can be extracted from inputted text. This may involve shifting to using SpaCy instead of NLTK.

### 1. AI-generated Classification 

- Compare several feature engineering techniques (e.g., PCA, TF-IDF vs other NLP features, removing poorly-performing features)

- Compare several classification ML algorithms (supervised) with varying hyperparameters to determine the best performing algorithm. These algorithms include logistic regression, k-nearest neighbors, random forest, neural networks, among others.

    - follow best-practices for ML. E.g., suitable train, test, validate.

- Deploy the classification algorithm to the cloud so the NLP features can be converted into a classification.

- Visualize or present the classification decision. If a probability is calculatable, provide that. If a ML algorithm that enables feature importance (e.g., Random Forest) is used, perhaps add a variable importance graph. 


### 2. Pedagogically-Meaningful Writing Feedback

- Showcase results on readily interpretable features (e.g., grade level, syntactic complexity, most common words, and percentile score comparison to other students). This will include 1) the feature score, 2) a description of the feature. 

- Provide a word cloud of words used in the text.

- Time-permitting, add additional pedagogically-relevant features (e.g., a list of mispelled words)


### 3. Documentation/Technical Report (Time-Permitting)

- Use work from all projects to develop documentation that showcases details about the website and its results. 

    - Feature comparisons between AI-generated and human-generated text from our initial data.

    - Descriptions of NLP pipeline (e.g., features), ML classification algorithm, and how classification decisions are made.

    - Time-permitting, data processing using Spark.

   