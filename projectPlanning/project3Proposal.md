# Project 3 Proposal

We propose creating a full-stack data visualization web application using a combination of a Python Flask-power API, HTML/CSS, Javascript, and SQL.

This project will include three different dashboard pages. The first two involve a server that performs multiple manipulations on data in a database prior to visualization. The final is a dashboard page with multiple charts that update from the same data.

### 1. Text-input AI text detection

A text-input dashboard in which anyone can input written text and our app will provide a dashboard depicting the likelihood it was AI-generated.

- User-driven interaction: textbox with an event listener.

- Visualizations:
    - overall probability of whether it is AI-written.
    - low priority: scores on key features?

### 2. Text-input Writing scoring

A text-input feedback dashboard similar to a report card. Anyone can input human-written text and our app will provide a dashboard and feedback on the quality of the writing. 

- User-driven interaction: textbox with an event listener.

- Proposed visualizations: 
    - [Word Cloud with D3 cloud](https://github.com/jasondavies/d3-cloud) and associated [horizontal bar chart](https://d3-graph-gallery.com/graph/barplot_horizontal.html) of most common words.
    - performance on features compared to the average student (in ASAP dataset perhaps?)


### 3. Teacher (Summary) Dashboard
A teacher dashboard depicting the writing characteristics of 100 different students whose writing has already been analyzed. These interactive graphs will mirror our work in project 1. 

- User-driven interaction: drop down selecting different a) students and b) features.


- Proposed visualizations for all data together:
    - histogram or pointplot summarizing all 100 essays in single graph (across all modalities)
    - histogram or pointplot summarizing essay performance by prompt? (drop-down)
    - [Heatmaps](https://plotly.com/javascript/heatmaps/) of the relationships between features.


- Proposed visualizations for individual student scores:
    - Top and bottom 10 performers (writing score).
    - Top 10 essays potentially AI? (or alternatively, essays that are above cutoff?)



