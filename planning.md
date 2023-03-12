# Project Planning Document

## NLP and Coding Pipeline

### Project Descriptions

1.  Your first project will focus on extracting some data and outputting it on Excel.
2.  Your second project will focus on extracting some data, transforming it, and loading it into SQL/noSQL.
3.  Your third project will focus on data visualization using web visualizations
4.  Your final project will focus on all of the above, and transformations that are augmented with machine learning.

The project should encompass at least one of the following 5 major machine learning modalities:  regression problems (supervised ML), classification problems (supervised ML), clustering/segmentation (unsupervised ML), computer vision (object ID), Natural language processing. 

### Datasets

- select relevant Kaggle datasets. See the "datasetsNotes.xlsx" file. 

    - Can also scrape writing from websites, but there are no available classification (e.g., no guarantee writing is not machine-generated). Could perhaps web scrape Wikipedia snippets, LinkedIn posts, Medium.com blogs or the like. 

- select relevant APIs or develop programs to create machine-generated text (i.e., the text we want to detect).

    - ChatGPT and its analogues (e.g, GPT-3.5) are one great option. "OpenAI's GPT-3 playground"

    - the [Babel](https://lesperelman.com/writing-assessment-robo-grading/babel-generator/) system will generate essays that are syntactically accurate but semantically nonsensical. If they have an API, this is another option. 

    - Other options I'm haven't looked into yet (e.g., Microsoft's AI-bing, Google's Bard, etc.)
    
    - Potential modalities of machine-generated text: 1) high-quality ChatGPT-like text; 2) real-word, syntactically correct, but gibberish content (i.e., Babel); 3) explicitives, threats, harassment/discrimination; 4) 

- Organize the data into a suitable database (maybe simple excel file, maybe more advanced SQL database)

### Natural Language Processing Feature Extraction

- Conceptual: Read literature and determine suitable NLP features we may want to try (NLP feature conceptualization)

    - [Dr. Jiangan Huo at ETS](https://www.linkedin.com/pulse/detecting-chatgpt-generated-essays-high-stakes-applications-hao/?trackingId=weuMN%2FEBRM2p6Rz%2Fc8Bohg%3D%3D) has identified "essay perplexity based on the GPT2 language model" as one prominent feature useful for predicting AI essay generation. 

    - [Chen and associates at ETS](http://onlinelibrary.wiley.com/doi/abs/10.1002/ets2.12198) describe filter models on page 17, and describe scoring features utilized for spoken responses. Some may be applied to writing (see p. 23, table 14). This is in the context of speech assessment though.

    - [Zechner and Evanini at ETS](https://www.routledge.com/Automated-Speaking-Assessment-Using-Language-Technologies-to-Score-Spontaneous/Zechner-Evanini/p/book/9781138056879) describe features for vocabulary and grammar (chapter 7) and content and discourse coherence (chapter 8). Filter models are also described in chapter 5. This is all in the context of speech assessment.

- Application: find python packages (e.g., the natural language toolkit - nltk) to operationalize the features identified in the literature.

- Create python scripts and/or jupyter notebooks that will run the feature extraction. 

### Big picture NLP pipeline

Steps we will likely need to take for written text processing:

- read data into python

- create the automatically generated text. Use an API to provide a large-language model with similar prompts as those given to students.

- Preliminary data cleaning: 

    - Lemmatization

    - tokenization 

    - POS tagging (if relevant)

    - removing stop words

    - Stemming

    - part-of-speech tagging

    - developing bags of words (where reasonable?)
    
- Feature engineering

- Supervised Machine Learning: classification

    - split into n fold for cross validation
    
    - test out a variety of ML classification models (e.g,. logistic regression, decision trees, random forest, etc.)
    
    - visualize output: various performance criteria for each classification model (confusion matrix, f1, precision, recall, specificity, sensitivity)
    
- Potentially turn into a website/app where it can output predicted possibility of text being a human vs machine generated? (or whatever it happens to be) 

## Next Step To-Dos:

- read data into python

- very basic descriptive/summary statistics (e.g., average length of text)

- very basic data cleaning (e.g., lemmatization/tokenization/stemming)

- **spend time on feature engineering**
