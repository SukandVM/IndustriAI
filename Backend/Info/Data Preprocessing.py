import json
import requests

def preprocess_data(data):
    """
    Preprocess incoming data before sending it to the /predict endpoint.

    Args:
        data (dict): Raw input data.

    Returns:
        dict: Preprocessed data.
    """
    required_keys = ["feature1", "feature2", "feature3"]
    for key in required_keys:
        if key not in data:
            raise ValueError(f"Missing required key: {key}")

    for key, value in data.items():
        if value is None:
            if isinstance(value, (int, float)):
                data[key] = 0
            elif isinstance(value, str):
                data[key] = ""

    numerical_keys = ["feature1", "feature2"]
    for key in numerical_keys:
        if key in data and isinstance(data[key], (int, float)):
            data[key] = (data[key] - 10) / 2  

    categorical_keys = ["feature3"]
    for key in categorical_keys:
        if key in data:
            data[key] = data[key].lower().strip()  

    return data

def send_to_predict_endpoint(preprocessed_data, endpoint_url):
    """
    Send preprocessed data to the /predict endpoint.

    Args:
        preprocessed_data (dict): Preprocessed data.
        endpoint_url (str): URL of the /predict endpoint.

    Returns:
        dict: Response from the /predict endpoint.
    """
    response = requests.post(endpoint_url, json=preprocessed_data)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

if __name__ == "__main__":
    raw_data = {
        "feature1": 25,
        "feature2": None,
        "feature3": " Category A "
    }

    try:
        preprocessed_data = preprocess_data(raw_data)
        print("Preprocessed Data:", preprocessed_data)

        endpoint_url = "http://example.com/predict"
        prediction = send_to_predict_endpoint(preprocessed_data, endpoint_url)
        print("Prediction Response:", prediction)

    except Exception as e:
        print("Error:", str(e))
