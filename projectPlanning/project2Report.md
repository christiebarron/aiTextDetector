# Project 2 Report

For Project 2, we applied the extraction, transformation, and loading (ETL) process to the processing of AI-generated and human-written essay data. We extracted additional text data through web scraping, transformed the data using Python, developed a back-end SQL database infrastructure in Render to load the data.

### Extraction

Table 1 depicts the websites that were scraped for essay writing. This was accomplished with scripts 2a, 2b, 2c, and 2d in the [scripts](https://github.com/christiebarron/aiTextDetector/tree/main/primary/scripts) folder. In total, approximately 100 AI-generated essays and 2400 human-written essays were scraped from the internet. 

| Website | AI vs Human | Sample Size | Genres | Age |
|---| ---| ---| --- | ---|
|https://www.the-good-ai.com/examples| AI-generated | ~ 100 | Upper-secondary level | 10 academic topics (physics, enginerring, biology, economics, etc.)|  
|www.speedypaper.com/| Human | 1039 | Upper-secondary and university | 10+ academic disciplines  |   
|www.studyfy.com| Human | 1360 | Upper-secondary level | 10+ academic disciplines |  
|www.k12.thoughtfullearning.com/| Human | 50 | Elementary level  | Various writing topics (e.g., explanatory, narrative, persuasive, creative)| 

Additionally, 10 csv files with interrelationships were generated with Mockaroo to mirror the database design.

### Transformation

Python scripts were used to transform the scraped essays into a format suitable for integration into a database. 

- 1: Text data acquired from web scraping was integrating with our project 1 NLP pipeline to acquire NLP features. See script [6a](https://github.com/christiebarron/aiTextDetector/blob/main/primary/scripts/6aProject2Transform.py)

- 2: Sample 30 essays, integrating the scraped essays  with mock data to develop 10 csv files that represent different SQL tables. See the [databaseData](https://github.com/christiebarron/aiTextDetector/tree/main/primary/rawData/databaseData) folder for each of these tables.

### Loading

Loading was accomplished by using QuickDBD to develop entity relationship diagrams between the 10 tables with sample essays and mock additional data. See the [databaseDocumentation](https://github.com/christiebarron/aiTextDetector/tree/main/primary/Project2DatabaseDocumentation) folder for additional information. Figure 1 provides a depiction of the final ERD:

![Figure 1](https://github.com/christiebarron/aiTextDetector/blob/main/primary/Project2DatabaseDocumentation/Final%20Draft%20ERD.png)

Subsequently, SQL was used to create the table schemata and load the data onto the Render database. Figure 2 provides an example of the SQL query and response. In this example, the essay id variable is used to query both the essay text and the essay features extracted through the NLP pipeline. This is accomplished through an inner join of two tables.

![Figure2](https://github.com/christiebarron/aiTextDetector/blob/main/primary/output/7bQueries.png)
