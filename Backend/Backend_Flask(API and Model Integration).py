from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
import logging
import os

app = Flask(__name__)
CORS(app)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if not os.path.exists('credit_model.pkl'):
    logging.error("Model file not found!")
    exit(1)

try:
    model = joblib.load('credit_model.pkl')
    logging.info("Model loaded successfully.")
except FileNotFoundError:
    logging.error("Error: Could not find the model file.")
    exit(1)

@app.route('/predict', methods=['POST'])
def predict():
    try:       
        data = request.get_json()

        required_features = ['feature1', 'feature2', 'feature3']  # Replace with actual feature names
        if not all(feature in data for feature in required_features):
            return jsonify({'error': 'Missing required features'}), 400

        if not isinstance(data['feature1'], (int, float)):
            return jsonify({'error': 'Feature1 must be a number'}), 400

        features = pd.DataFrame([data])

        risk_score = model.predict(features)[0]
        probabilities = model.predict_proba(features)[0]

        return jsonify({
            'risk_score': risk_score,
            'probabilities': {
                'low': probabilities[0],
                'medium': probabilities[1],
                'high': probabilities[2]
            }
        })

    except ValueError as e:
        logging.error(f"ValueError: {e}")
        return jsonify({'error': 'Invalid input data'}), 400
    except Exception as e:
        logging.exception("An unexpected error occurred.")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
