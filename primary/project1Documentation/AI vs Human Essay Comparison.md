# AI vs Human Essay Comparison

This project aims to compare AI-generated and human-written essays by analyzing various linguistic features, including lexical, syntactic, stylistic, and semantic. The program extracts these features from both sets of essays, compares them, and stores the results in an Excel file.

## Features Analyzed

1. Lexical Features
   - Total word count
   - Average word length
   - Average sentence length
   - Type-token ratio (TTR)
   - Stop word count
   - Punctuation count

2. Syntactic Features
   - Average parse tree depth
   - Parse tree depth variation

3. Stylistic Features
   - Use of passive voice
   - Readability scores (Flesch Reading Ease and Flesch-Kincaid Grade Level)

4. Semantic Features
   - Sentiment analysis scores (polarity and subjectivity)

Summary:
Total Word Count: Total number of words in the essay. A higher value indicates a longer essay.

Average Word Length: Average length of words in the essay. A higher value indicates longer words, which may make the essay harder to read.

Average Sentence Length: Average number of words per sentence in the essay. A higher value indicates longer sentences, which may make the essay harder to read.

Type-Token Ratio: Ratio of unique words to total words in the essay. A higher value indicates more diverse vocabulary in the essay.

Stop Word Count: Number of stop words (common words such as "the", "and", "in", etc.) in the essay. A higher value may indicate less meaningful or informative text.

Avg Parse Tree Depth: The average depth of the parse tree (a tree structure that represents the grammatical structure of the sentence) for all sentences in the essay. A higher value indicates more complex sentence structures.

Parse Tree Depth Variation: The variation in parse tree depth for all sentences in the essay. A higher value indicates more varied sentence structures.

Punctuation Count: Number of punctuation marks (such as periods, commas, etc.) in the essay. A higher value indicates more complex sentence structures or more frequent use of lists or enumerations.

Passive Sentences: Number of passive voice sentences in the essay. A higher value may indicate less direct and more complex writing style.

Flesch Reading Ease: A measure of how easy it is to read the essay based on the average sentence length and average number of syllables per word. A higher value indicates an easier-to-read essay.

SMOG Index: A measure of the complexity of the essay based on the number of polysyllabic words and the number of sentences. A higher value indicates a more complex essay.

Sentiment Polarity: A measure of the overall emotional tone of the essay, where a higher value indicates a more positive tone and a lower value indicates a more negative tone.

Sentiment Subjectivity: A measure of the degree of personal opinion and emotion in the essay, where a higher value indicates a more subjective and emotional tone.

## Dependencies

- Python 3.6+
- pandas
- nltk
- textblob
- textstat
- spacy (with the en_core_web_sm model)
- openpyxl

## How to Run the Code

1. Install the required Python packages using pip:

```bash
pip install pandas nltk textblob textstat spacy openpyxl

2. Download the necessary spaCy model:
bash
Copy code
python -m spacy download en_core_web_sm

3. Run the Python script (replace script.py with the actual name of your script):
bash
Copy code
python script.py

4. The program will process the essays, calculate the features, and store the results in an Excel file named feature_comparison.xlsx.

Notes
The code assumes that AI-generated essays are stored in a file named aiGenerated.xlsx and human-written essays are stored in a file named training_set_rel3.xlsx.
You may need to modify the file paths and the number of essays to process according to your dataset.
