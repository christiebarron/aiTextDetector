# Project Proposal

- project title
- team members
- project description/outline
- research questions to answer
- datasets to be used
- rough breakdown of tasks

## Project Title
Detecting machine-generated written essays: an integration of Natural Language Processing and Machine Learning.

## Team Members

- Vareesha Shakeel
- Paramdeep Sing Birdi
- Maisam Alam
- Gayan Meerigama
- Christie Barron

## Project Description & Outline
The goal of this project is to develop a machine learning algorithm to detect whether a given text may be machine-generated. It will use natural language processing to extact features from an essay. It will then use a classification machine learning algorithm to classify written text as either authentic human-written text or machine-generated text. In its current iteration, it is mostly capable of differentiating between essays written by students in grades 7-10 and machine-generated text from large-language models. 


## Research Questions to Answer for Project 1

- Feature engineering: what writing features are most useful at distinguishing between human-written and machine-generated text? 
    - What are the characteristics of human-written essays of students in grades 7-10? What are the characteristics of machine-generated essays composed by large language models?


Data visualizations:

- Word frequency, grouped by writer (human vs AI)
- Correlation matrix and heatmap of the relationships between features.
- distributions of the various features grouped by writer (human vs AI): histograms or density plots: Maisam.
- means on the features grouped by writer (human vs AI): barplot or Cleveland dot plot
- table of point-biserial correlations between a feature and writer status (human vs AI): 
- table of descriptive statistics on the features grouped by writer status (human vs AI): mean, standard devaition, min, max. Gayan will do this.


## Datasets to be used

Context 1: Student essay writing 
- Kaggle ASAP student writing dataset for human-written essays.
- API from a large-language model to generate similar essay prompts for machine-written essays. 
    - Using either 1) Open AI's GPT-3 DaVinci3 large language model, or 2) Chat-GPT. 
    -  Will use prompt engineering to get it to generate as realistic text as possible.


## Rough Breakdown of Tasks

Steps we will likely need to take for written text processing:

- read data into python
- create the automatically generated text. Use an API to provide a large-language model with similar prompts and context as those written by humans.
- Preliminary data cleaning: 
    - tokenization
    - removing stop words
    - lemmatization
    - POS tagging (if relevant)
    - developing bags of words (where reasonable?)
    - Descriptive statistics and visualization of response characteristics
- Feature engineering
    - Selection of relevant features 
    - Compute feature scores for all text stimuli.
    - descriptive statistics and data visualization comparing human and machine scores on features.
- Supervised Machine Learning: classification
    - split into k folds for cross validation
    - test out a variety of ML classification models (e.g,. logistic regression, decision trees, random forest, etc.)
    - visualize output: various performance criteria for each classification model (confusion matrix, f1, precision, recall, specificity, sensitivity)
- Turn into a website/app where it can output predicted possibility of text being a human vs machine generated? (or whatever it happens to be) 

### Project 1 Task Breakdown:
- Data visualization: Maisam, Gayan & Vareesha
- Descriptive statistics: Gayan & Vareesha
- API for AI text generation: Christie & Maisam
- Feature engineering: Paramdeep

## Notes on Projects 3-4 
- ML Classification RQ: How well can a machine learning algorithm detect machine-generated written text? Does classification accuracy systematically vary based on context?

## Project Requirements
- Note these mostly don't address comments from the rubrics. Will add later.

### Project 1
#### Data Analysis and Coding
- Use Pandas to clean and format your dataset or datasets.
- Create a Jupyter notebook describing the data exploration and cleanup process.
- Create a Jupyter notebook illustrating the final data analysis.
- Use Matplotlib to create 6 to 8 visualizations. At least 2 visualizations per “question”.
- Save PNG images of your visualizations to distribute to the class and instructional team—and for inclusion in your presentation.
- Create a write-up summarizing your major findings. This should include a heading for each “question” that you asked your data as well as a short description of your findings and any relevant plots.
- Bonus Use at least one API—if you can find one with data pertinent to your primary research questions.

#### Powerpoint Presentation
- Questions that you found interesting and what motivated you to answer them
- Where and how you found the data you used to answer these questions
- The data exploration and cleanup process (accompanied by your Jupyter notebook)
- The analysis process (accompanied by your Jupyter notebook)
- Your conclusions, including a numerical summary and visualizations of the summary
- The implications of your findings: what do your findings mean?


### Project 2
#### Data Analysis and Coding
- Citing the data sources (2+ data sources required)
- Extracting the data from those sources
- Transforming the data (cleaning, joining, filtering, aggregating, etc.)
- Loading the data into a database (relational or non-relational)

#### Documentation
- Create documentation including: 
        - Datasets used, their sources, how they were formatted -- the extract piece
        - Types of data wrangling performed (data cleaning, joining, filtering, aggregating -- the transform piece
        - The schemata used in the final production database. final database, tables/collections, and why they were chosen. -- the load piece

### Project 3
#### Summary Requirements
- tell a story using data visualization
- add interactivity to graphs
- create a 10-min presentation 

#### Detailed Requirememnts
- Your visualization must include a Python Flask–powered API, HTML/CSS, JavaScript, and at least one database (SQL, MongoDB, SQLite, etc.). 01
- Your project should fall into one of these tracks:
    - A combination of web scraping and Leaflet or Plotly
    - A dashboard page with multiple charts that update from the same data
- Your project should include at least one JS library that we did not cover.
- Your project must be powered by a dataset with at least 100 records.
- Your project must include some level of user-driven interaction (e.g., menus, dropdowns, textboxes).
- Your final visualization should ideally include at least three views.

### Project 4
- Find suitable problem
- Use ML (Scikit learn or another ML library)
- Use two of: Pandas, HTML/CSS/Bootstrap, Matplotlib, JavaScript Plotly, JavaScript Leaflet, Tableau, SQL Database, MongoDB Database, Google Cloud SQL, Amazon AWS
- 5 categories of work: data/data delivery, back end ETL, visualizations, group presentations (everyone present), slide deck

