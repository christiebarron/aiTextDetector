# Project 2 Proposal DRAFT

### Extraction:

In addition to data collected through project 1, we used ethical web scraping to collect data from 4 additional sources for Project 2: 

| Website | AI vs Human | Data Extracted 
|---| ---| ---|
|https://www.the-good-ai.com/examples| AI-generated | Approximately 100 AI-generated essays on 10 different topics. |
|www.speedypaper.com/| Human | INSERT BLURB |
|www.studyfy.com| Human | INSERT BLUB |
|www.k12.thoughtfullearning.com/| Human | INSERT BLUB  |

### Transformation


- beautiful soup: get human-written text from wherever website we want
- hugging face to generate more AI text perhaps?
- OR, beautiful soup to scrape AI text if we can find a dedicated place with AI text
- OR, if there's somehow a SQL server we can connect to with human/AI writing we can use that instead. get data w/ SQL query.

Transformation:
- do similar data wrangling to the first time around, to add the text to the pipeline
- transform so its suitable for uploading to SQL or NoSQL.
- if create a flask app, transform/organize so usable for flask

Load
- create SQL or NoSQL database with 1) the writing, 2) the processed features
- if create a flask app, provide it there.


