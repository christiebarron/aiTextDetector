from flask import Flask, jsonify, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/dashboard')
def dashboard():
    return render_template('index.html')

@app.route('/data', methods=['GET'])
def get_data():
    # Read the Excel file into a DataFrame
    df = pd.read_excel('/Users/paramdeepsinghbirdi/Downloads/selected_essays.xlsx')

    # Select the desired columns from the DataFrame
    selected_columns = [
        'essay_id_sql',
        'essay_set',
        'rare_word_count',
        'stop_word_count',
        'avg_word_length',
        'avg_sentence_length',
        'sentiment_polarity',
        'flesch_kincaid_grade_level',
        'TTR'
    ]
    data = df[selected_columns].to_dict(orient='records')

    # Return the JSON response
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True)
