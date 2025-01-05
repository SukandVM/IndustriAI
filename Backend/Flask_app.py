from flask import Flask, request, jsonify
import pandas as pd
from preprocessing import preprocess_data

app = Flask(__name__)

@app.route('/preprocess', methods=['POST'])
def preprocess():
    try:
        file = request.files['file']
        file_path = 'uploaded_data.csv'  

        file.save(file_path)

        processed_data = preprocess_data(file_path)

        processed_data_json = processed_data.to_json(orient='records')

        return jsonify(processed_data_json)

    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
