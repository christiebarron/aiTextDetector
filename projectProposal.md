# Project Proposal

- project title
- team members
- project description/outline
- research questions to answer
- datasets to be used
- rough breakdown of tasks

## Project Title
Detecting machine-generated written text: an integration of NLP and ML

## Team Members

- Vareesha Shakeel
- Paramdeep Sing Birdi
- Maisam Alam
- Gayan Meerigama
- Christie Barron

## Project Description & Outline
To add.


## Research Questions to Answer

- Feature engineering: what features are most useful at distinguishing between human-written and machine-generated text? Do these features vary based on the context (aka dataset utilized)?
- ML Classification: How well can a machine learning algorithm detect machine-generated written text? Does classification accuracy systematically vary based on context?

## Datasets to be used

Context 1: Student essay writing 
- Kaggle ASAP student writing dataset for human-written essays.
- API from a large-language model to generate similar essay prompts for machine-written essays.

Context 2: To be determined. 
- (social media posts? news articles? job posts? wikipedia articles?). To add.


## Rough Breakdown of Tasks

Steps we will likely need to take for written text processing:

- read data into python

- create the automatically generated text. Use an API to provide a large-language model with similar prompts and context as those written by humans.

- Preliminary data cleaning: 

    - Lemmatization

    - tokenization 

    - POS tagging (if relevant)

    - removing stop words

    - Stemming

    - developing bags of words (where reasonable?)

    - Descriptive statistics and visualization of response characteristics
    
- Feature engineering:

    - Selection of relevant features 

    - Compute feature scores for all text stimuli.

    - descriptive statistics and data visualization comparing human and machine scores on features.

- Supervised Machine Learning: classification

    - split into k folds for cross validation
    
    - test out a variety of ML classification models (e.g,. logistic regression, decision trees, random forest, etc.)
    
    - visualize output: various performance criteria for each classification model (confusion matrix, f1, precision, recall, specificity, sensitivity)
    
- Turn into a website/app where it can output predicted possibility of text being a human vs machine generated? (or whatever it happens to be) 

## Project Requirements

### Project 1

### Project 2

### Project 3

### Project 4
- Use ML (Scikit learn or another ML library)
- Use two of: Pandas, HTML/CSS/Bootstrap, Matplotlib, JavaScript Plotly, JavaScript Leaflet, Tableau, SQL Database, MongoDB Database, Google Cloud SQL, Amazon AWS

- 5 categories of work: data/data delivery, back end ETL, visualizations, group presentations (everyone present), slide deck
