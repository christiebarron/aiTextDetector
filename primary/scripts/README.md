## Script Explanation

These scripts form a pipeline and are intended to be run in a consecutive order.

- 1: scripts using APIs to generate AI text
    - 1a: a script using OpenAI's API to generate AI text
    - 1b: a script using HuggingFace's API to generate AI text

- 2: scripts scraping human and AI essays from the internet
    - 2a: a script scraping AI text from https://www.the-good-ai.com/examples
    - 2b: a script scraping human text from www.speedypaper.com/
    - 2c: a script scraping human text from www.studyfy.com
    - 2d: a script scraping human text from www.k12.thoughtfullearning.com/

- 3: scripts used to read, merge and prepreprocess text.

- 4: scripts used to extract features from the text.

- 5: scripts used to conduct exploratory data analysis and data visualization of the extracted features.

- 6: a script used to transform data for project 2.

- 7: scripts related to the databases on Render
    - 7a: the SQL script depicting the table schema.
    - 7b: the SQL script used to run queries
