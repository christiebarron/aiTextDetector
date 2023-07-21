# ReadMe 

## Introduction

This repository contains a project to 1) develop an application that will 
use a large language model to for automated text generation and 2) an 
application that identifies AI-generated written text. 

The results of this project will be used to develop a basic filter model as part of a larger NLP pipeline for the automated scoring of student essays.

## Project 3: Full-stack Data Visualization Web Application
Project 3 invovled developing a data visualization web application. 
Please refer to AIWebsite3 for the final version of project 3.

## Project 2: Extract, Transform and Load

Project 2 involved 1) data extraction through web scraping and data-generation with [Mockaroo](https://www.mockaroo.com/), 2) data transformation using Python, and 3) data loading using [QuickDBD](https://www.quickdatabasediagrams.com/) and [Render](https://render.com/) with subsequent SQL queries. 

Key folders/files for Project 2 include:

- [Project 2 Proposal](https://github.com/christiebarron/aiTextDetector/blob/main/projectPlanning/project2Proposal.md): the proposal for using ETL within this aiTextDetect project.

- [Project 2 Report](https://github.com/christiebarron/aiTextDetector/blob/main/projectPlanning/project2Report.md): the final report written upon completion of Project 2.

- [Project 2 Database Documentation](https://github.com/christiebarron/aiTextDetector/tree/main/primary/Project2DatabaseDocumentation): Documentation of the Render SQL database, including an entity relationship diagram.

- [Project 1 and 2 Scripts](https://github.com/christiebarron/aiTextDetector/tree/main/primary/scripts): python, jupyter notebook, and SQL syntax used to scrape and wrangle the data. 

- [rawData](https://github.com/christiebarron/aiTextDetector/tree/main/primary/rawData): Data scraped from the web or generated with Mockaroo.


## Repository Folder structure

- primary: contains all of the code and data we are using for the NLP pipeline. Refer to this to see all work completed for project 1 and project 2.

    - primary/scripts: contains all of the python and jupyter notebook scripts we used to create the NLP pipeline. 
    - primary/rawData: contains all of the original data (excel documents and text files) prior to processing. 
    - primary/cleanData: contains all of the processed data.
    - primary/output: contains all figures, tables, and other output from analyses.
    - primary/documentation: contains documentation for the NLP pipeline.
    
- projectPlanning: contains documents related to project management and planning. In particular, it has project proposals.
     
- archive: contains files that are no longer relevant. 

- templates: contains highly-performing and highly-rated example templates *not written by us* designed for 1) automated *scoring* of the ASAP student response data and 2) to identify machine-generated text using a different dataset. These files were just used for idea generation.

- textAnalyzerApp: contains preliminary code for creating an application that can process text and classify it as AI-generated or human-written.
