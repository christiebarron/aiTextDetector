# Project 4 Proposal

## Write-up

We propose extending the first 3 projects to incorporate a machine-learning component. In particular, we propose extending the full-stack data visualization web application from project 3 to incorporate machine-learning-based classification of machine-generated text. 

This project will primarily extend project 3 by adding a live text-input webpage.

### Text-input Webpage

A text-input webpage in which anyone can input written text and our app will provide a dashboard depicting:

1. The likelihood the provided text was AI-generated

2. Pedagogically-meaningful writing feedback about the submitted text (e.g., grade level, syntactic complexity, most common words, comparison to other students, showing the text itself).

3. Time-permitting, documentation that describes the NLP pipeline, ML classification algorithm, and and visualizes 

#### Pre-processing
Pre-processing is required for both text classification and the pedagogical report:

- Deploy our NLP pipeline to the cloud so features can be extracted from inputted text. This may involve shifting to using SpaCy instead of NLTK.

#### 1. AI-generated Classification 

- Compare several feature engineering techniques (e.g., PCA, TF-IDF vs other NLP features, removing poorly-performing features)

- Compare several classification ML algorithms (supervised) with varying hyperparameters to determine the best performing algorithm. These algorithms include logistic regression, k-nearest neighbors, random forest, neural networks, among others.

    - follow best-practices for ML. E.g., suitable train, test, validate.

- Deploy the classification algorithm to the cloud so the NLP features can be converted into a classification.

- Visualize or present the classification decision. If a probability is calculatable, provide that. If a ML algorithm that enables feature importance (e.g., Random Forest) is used, perhaps add a variable importance graph. 


#### 2. Pedagogically-Meaningful Writing Feedback

- Showcase results on readily interpretable features (e.g., grade level, syntactic complexity, most common words, and percentile score comparison to other students). This will include 1) the feature score, 2) a description of the feature. 

- Provide a word cloud of words used in the text.

- Time-permitting, add additional pedagogically-relevant features (e.g., a list of mispelled words)


#### 3. Documentation/Technical Report (Time-Permitting)

- Use work from all projects to develop documentation that showcases details about the website and its results. 

    - Feature comparisons between AI-generated and human-generated text from our initial data.

    - Descriptions of NLP pipeline (e.g., features), ML classification algorithm, and how classification decisions are made.

    - Time-permitting, data processing using Spark.
 
## Design

### Introduction

Our final product is a web application that aims to analyze and provide insights on essays or text data provided by users. The application will leverage natural language processing (NLP) techniques and machine learning algorithms to extract features, perform analysis, and generate predictions. This report provides an overview of how the final product will look like and the technologies we will be using.

### Web Application: 
Our application will be accessible through a web browser, providing a user-friendly interface for users to interact with. The web application will consist of different pages/screens to facilitate seamless user experience and efficient data processing.

### User Interface: 
The user interface (UI) of our web application will comprise of intuitive input fields and forms for users to submit their essays or text data. Users will have the option to select specific features or perform actions such as feature engineering. The UI will be designed to ensure ease of use and clarity of instructions.

### Backend: 
The backend of our application will handle the processing and analysis of the text data. It will be responsible for receiving user input, performing feature extraction, applying feature engineering techniques, and generating predictions based on machine learning models. We will be utilizing Flask, a Python web framework, to develop the backend of our application.

### Flask: 
Flask is a lightweight and versatile web framework in Python. It will serve as the foundation for our backend development. Flask allows us to handle HTTP requests, define routes, manage application logic, and communicate with other components of our application. It provides a flexible and scalable architecture for building web applications.

### Natural Language Processing (NLP) Libraries: 
To process and analyze text data, we will be utilizing popular NLP libraries in Python, such as NLTK, spaCy, and scikit-learn. These libraries offer a wide range of functions and algorithms for tasks like tokenization, stemming, lemmatization, and feature extraction. Leveraging these libraries will enable us to efficiently preprocess and analyze the text data provided by users.

### Feature Engineering: 
Feature engineering techniques will be employed to enhance the predictive power of our machine learning models. We will leverage scikit-learn's preprocessing and feature selection modules to engineer and select relevant features from the text data. Feature engineering will help us extract meaningful insights and improve the accuracy of our predictions.

### Machine Learning Model: 
Our final product will incorporate a machine learning model trained on a labeled dataset. The model will be designed to make predictions based on the extracted and engineered features. 

### JSON APIs: 
To facilitate communication between the frontend and backend, we will be using JSON (JavaScript Object Notation) APIs. JSON APIs allow structured data transfer and ensure seamless exchange of information between different components of our application. This will enable efficient integration of the frontend user interface with the backend data processing and prediction modules.

### Deployment: 
Our web application will be deployed on a web server or cloud platform, making it accessible to users over the internet. 

### Conclusion: 
Our final product, a web application for text analysis and prediction, will leverage Flask, NLP libraries, and machine learning models. The application will provide users with an intuitive interface to submit essays, extract features, perform analysis, and generate predictions. By combining the power of NLP and machine learning, our goal is to deliver a valuable tool for users to gain insights from their text data.

## Work Breakdown


|Task | Person | Deadline|
| ----------- | ----------- |  ----------- |
|Backend: NLP Pipeline     |  Christie   |  Thurs July 27   |
|Front End     |  Maisam   |  Thurs July 27 |
|Data Visualizations     |  Vareesha   |  Thurs July 27th  |
|Machine learning     |  Gayan   |  Thurs July 27th  |
|Machine learning     |  Paramdeep   |  Thurs July 27th  |


