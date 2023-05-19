# Project 2 Report

For Project 2, we applied the extraction, transformation, and loading (ETLT) process to the processing of AI-generated and human-written essay data. We extracted additional text data through web scraping, transformed the data using Python, developed a back-end SQL database infrastructure in Render to load the data.

### Extraction

Table 1 depicts the websites that were scraped for essay writing. This was accomplished with scripts 2a, 2b, 2c, and 2d in the [scripts](https://github.com/christiebarron/aiTextDetector/tree/main/primary/scripts) folder. In total, approximately 100 AI-generated essays and GAYAN AND VAREESHA TO ADD human-written essays were scraped from the internet. 

| Website | AI vs Human | Sample Size | Genres | Age |
|---| ---| ---| --- | ---|
|https://www.the-good-ai.com/examples| AI-generated | ~ 100 | 10 topics | Upper secondary level. |
|www.speedypaper.com/| Human | GAYAN TO ADD | Upper secondary and university | GAYAN TO ADD |   
|www.studyfy.com| Human | GAYAN TO ADD | upper secondary level | GAYAN TO ADD |  
|www.k12.thoughtfullearning.com/| Human | VAREESHA TO ADD | Grade 1-6 level  | VAREESHA TO ADD| 

Additionally, 10 csv files with interrelationships were generated with Mockaroo to mirror the database design.

### Transformation

Python scripts were used to transform the scraped essays into a format suitable for integration into a database. 

- 1: Integrating the text data acquired from web scraping with our project 1 NLP pipeline to acquire NLP features. 

- 2: Sample 30 essays, integrating this data with mock data to develop 10 csv files that represent different tables. 

The essays extracted were subsequently integrated into the NLP pipeline. 

### Loading

