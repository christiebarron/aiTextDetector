from flask import Flask, render_template, request
import text_features  # This is the file containing the feature extraction code

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        input_text = request.form['input_text']
        processed_text = text_features.text_preprocessing(input_text)
        results = {
            'sentence_complexity': text_features.sentence_complexity(input_text),
            'vocabulary_richness': text_features.vocabulary_richness(processed_text),
            'grammatical_errors': text_features.grammatical_errors(input_text),
            'ngrams': text_features.ngram_analysis(processed_text, 3),
            'stylistic_patterns': text_features.stylistic_patterns(processed_text),
        }
        return render_template('index.html', results=results)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
