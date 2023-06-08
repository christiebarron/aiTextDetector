# Project 2 Proposal

We propose utilizing the extraction, transformation, and loading (ETLT) process in the context of processing AI-generated and human-written essay data. Project 2 aims to process additional text data and develop preliminary back-end SQL database infrastructure to support the development of an application. 

We propose:

- Extraction: data extraction through web scraping and data-generation with [Mockaroo](https://www.mockaroo.com/).

- Transformation: data transformation using Python to prepare the data for the SQL database. Randomly sample 30 essays for a proof-of-concept.

- Loading: data loading using [QuickDBD](https://www.quickdatabasediagrams.com/) and [Render](https://render.com/) with subsequent SQL queries.

### Extraction:

In addition to data collected through project 1, we propose using ethical web scraping with Python's BeautifulSoup library to collect data from 4 additional sources for Project 2: 

| Website | AI vs Human | Data Extracted 
|---| ---| ---|
|https://www.the-good-ai.com/examples| AI-generated | Approximately 100 AI-generated essays on 10 different topics written at the upper secondary level. |
|www.speedypaper.com/| Human | Approximately X human-written essays on a multitude of topics written at the upper secondary and university levels  |
|www.studyfy.com| Human | Approximately X human-written essays on a multitude of topics written at the upper secondary level  |
|www.k12.thoughtfullearning.com/| Human | Approximately X human-written essays on a multitude of topics written at the grade 1-6 level  |

This data was intentionally chosen to increase the representaivenes and generalizability of project 1 results. These websites allow sampling from populations (e.g., students in grades 1-6 and 11-12) and topics (e.g., history, geography) that weren't represented in the Kaggle ASAP data used in project 1.

### Transformation

As part of Project 2 data transformation, we propose developing NLP features and generating a proof of concept two steps. 

- 1: Integrating the text data acquired from web scraping with our project 1 NLP pipeline to acquire NLP features. 

- 2: Sample 30 essays, integrating this data with mock data to develop 10 csv files that represent different tables. 

### Load

For Project 2's loading stage, we propose using Render to create the SQL database, and QuickDBD to develop corresponding entity relationship diagrams. We will subsequently conduct a few simple queries to ensure the database is functional.

