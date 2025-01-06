from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Folder paths for static files
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'static')

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Home Page</title>
            <style>
                /* Global Reset */
                * {
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                }

                /* Body Styling */
                body {
                    font-family: 'Roboto', sans-serif;
                    background: linear-gradient(135deg, #1a1c2c, #2e324b);
                    color: #f4f4f4;
                    line-height: 1.8;
                    padding-bottom: 50px;
                }

                /* Header */
                header {
                    background: linear-gradient(135deg, #252837, #090920);
                    color: #fad20c;
                    padding: 2rem 1rem;
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    font-family: 'Helvetica', sans-serif;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
                }

                /* Round Logo with Light Yellow Shadow */
                header img {
                    width: 100px; /* Set the logo size */
                    height: 100px;
                    border-radius: 50%; /* Make the image round */
                    margin-right: 20px; /* Add some space on the right */
                    box-shadow: 0 0 15px 5px rgba(244, 181, 22, 0.6); /* Light yellow shadow */
                }

                header h1 {
                    font-family: 'Arial', sans-serif;
                    font-size: 3rem;
                    text-transform: uppercase;
                    background: linear-gradient(135deg, #fad20c, #f9c936, #f7b731);
                    -webkit-background-clip: text;
                    color: transparent;
                    text-shadow: 3px 3px 0 rgba(244, 181, 22, 0.8), 4px 4px 5px rgba(143, 72, 72, 0.7);
                    margin-left: 20px; /* Added some left margin for better spacing */
                }

                /* Section Styling */
                section {
                    padding: 3rem;
                    max-width: 1000px;
                    margin: 2rem auto;
                    background-color: rgba(255, 255, 255, 0.05);
                    border-radius: 12px;
                    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.1);
                    backdrop-filter: blur(10px);
                }

                section h2 {
                    font-size: 2.5rem;
                    color: #fad20c;
                    text-transform: uppercase;
                    background: linear-gradient(135deg, #fad20c, #f9c936);
                    -webkit-background-clip: text;
                    color: transparent;
                    margin-bottom: 20px;
                }

                section p {
                    color: #f4f4f4;
                    font-size: 1.1rem;
                    margin-bottom: 15px;
                }

                /* Sticky footer bar */
                .sticky-bar {
                    position: fixed;
                    bottom: 0;
                    width: 100%;
                    background-color: #252837;
                    color: #fad20c;
                    padding: 10px 20px;
                    text-align: center;
                    box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.3);
                }

                .sticky-bar a {
                    color: #fad20c;
                    font-size: 1.2rem;
                    text-decoration: none;
                    margin-left: 15px;
                }

                /* Buttons */
                .button-container {
                    display: flex;
                    justify-content: space-between;
                    gap: 20px;
                    margin-right: 20px;
                    margin-top: 20px;
                    width: 30%;
                }

                .button {
                    display: inline-block;
                    padding: 12px 25px;
                    font-size: 18px;
                    color: #252837; /* Darker text for contrast */
                    background-color: #fad20c; /* Matching yellow color */
                    text-decoration: none;
                    border-radius: 8px;
                    border: none;
                    cursor: pointer;
                    transition: all 0.3s ease;
                    box-shadow: 0 4px 10px rgba(244, 181, 22, 0.6);
                }

                .button:hover {
                    background-color: #f9c936; /* Slightly lighter yellow */
                    box-shadow: 0 6px 12px rgba(249, 201, 54, 0.8);
                }

                /* Image Styling */
                img {
                    width: 100%;
                    max-width: 400px;
                    border-radius: 8px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
                }
            </style>
        </head>
        <body>
            <header>
                <img src="/static/eidos.jpg" alt="Eidos Logo">
                <h1>EIDOS</h1>
                <div class="button-container">
                    <button class="button" onclick="window.location.href='/data-storage'">Go to Data Storage</button>
                    <button class="button" onclick="window.location.href='/graph'">Go to Graph</button>
                </div>
            </header>

            <section>
                <h2>Introduction</h2>
                <p>
                    Credlysis focuses on revolutionizing credit risk analysis by incorporating alternative data sources, such as social media sentiment, utility payment history, and geolocation stability scores. By leveraging these non-traditional data points, the project aims to provide financial institutions with more accurate, comprehensive, and transparent credit risk predictions.
                </p>

                <h2>Objective</h2>
                <p>
                    The primary objective of Credlysis is to:
                    <ul>
                        <li>Integrate alternative data sources to enhance credit risk analysis.</li>
                        <li>Build a predictive model combining traditional and alternative data for more accurate risk assessments.</li>
                        <li>Ensure transparency and explainability of predictions through clear visualizations and reports.</li>
                        <li>Deploy a user-friendly platform to facilitate easy access to risk prediction insights for lenders.</li>
                    </ul>
                </p>

                <h2>Approach</h2>
                <p>
                    Credlysis follows a phased approach:
                    <ul>
                        <li>Data Collection: Gathered and cleaned three key datasets:
                            <ul>
                                <li>Social media sentiment data</li>
                                <li>Utility payment history</li>
                                <li>Geolocation stability scores</li>
                            </ul>
                        </li>
                        <li>Data Integration: The datasets were merged into a comprehensive dataset for model training and analysis.</li>
                    </ul>
                </p>

                <h2>Solution</h2>
                <p>
                    The solution consists of:
                    <ul>
                        <li>Credit Risk Prediction Model: A machine learning model developed using integrated data sources, including geolocation-based credit scores from external datasets like Kaggle.</li>
                        <li>Model Explainability: Implemented tools like SHAP and LIME to ensure that the model's predictions are understandable, with visualizations showing feature importance.</li>
                        <li>Future Enhancements: A Flask-based web application has been developed to host the model, providing an interactive platform for users to view risk predictions and insights. What you see now is a very rudimentary but functional model.</li>
                    </ul>
                </p>
            </section>

            <!-- Sticky footer with GitHub link -->
            <div class="sticky-bar">
                <i><span>Check out the code on GitHub<a href="https://github.com/SukandVM/IndustriAI" target="_blank">.</a></span></i>
            </div>
        </body>
    </html>
    '''

@app.route('/data-storage')
def data_storage():
    return '''
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Data Storage</title>
            <style>
                /* Body Styling */
                body {
                    font-family: 'Roboto', sans-serif;
                    background: linear-gradient(135deg, #1a1c2c, #2e324b);
                    color: #f4f4f4;
                    line-height: 1.8;
                    padding-bottom: 50px;
                }

                /* Section Styling */
                section {
                    padding: 3rem;
                    max-width: 1000px;
                    margin: 2rem auto;
                    background-color: rgba(255, 255, 255, 0.05);
                    border-radius: 12px;
                    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.1);
                    backdrop-filter: blur(10px);
                }

                section h1 {
                    font-size: 2.8rem;
                    color: #fad20c;
                    margin-bottom: 20px;
                    text-shadow: 3px 3px 0 rgba(244, 181, 22, 0.8), 4px 4px 5px rgba(143, 72, 72, 0.7);
                }

                section a {
                    color: #fad20c;
                    font-size: 1.2rem;
                    text-decoration: none;
                    margin: 10px 0;
                    display: block;
                }

                .button-container {
                    text-align: left;
                    margin-top: 30px;
                }

                .button {
                    display: inline-block;
                    padding: 12px 25px;
                    font-size: 18px;
                    color: #252837; /* Darker text for contrast */
                    background-color: #fad20c; /* Matching yellow color */
                    text-decoration: none;
                    border-radius: 8px;
                    border: none;
                    cursor: pointer;
                    transition: all 0.3s ease;
                    box-shadow: 0 4px 10px rgba(244, 181, 22, 0.6);
                }

                .button:hover {
                    background-color: #f9c936; /* Slightly lighter yellow */
                    box-shadow: 0 6px 12px rgba(249, 201, 54, 0.8);
                }

                /* Image Styling */
                img {
                    width: 100%;
                    max-width: 400px;
                    border-radius: 8px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
                }
            </style>
        </head>
        <body>
            <section>
                <h1>Data Storage</h1>
                <div>
                    <h2>Utility Payments</h2>
                    <img src="/static/Utility.png" alt="Utility Payments">
                    <a href ="/static/Fin_output.txt" download>Utility Payments-> click here to download</a>
                </div>
                <div>
                    <h2>Locator Stability</h2>
                    <img src="/static/MO.png" alt="Locator Stability">
                    <a href ="/static/MLOutput.txt" download>Locator Stability-> click here to download</a>
                </div>
                <div>
                    <h2>Social Media Sentiment</h2>
                    <img src="/static/Sociall.png" alt="Social Media Sentiment">
                    <a href ="/static/Socialout_put.txt" download>Social Media Sentiment-> click here to download</a>
                </div>

                <!-- Button to return to home page -->
                <div class="button-container">
                    <button class="button" onclick="window.location.href='/'">Go Back</button>
                </div>
            </section>
        </body>
    </html>
    '''
@app.route('/graph')
def graph():
    return '''
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Graph</title>
            <style>
                /* Body Styling */
                body {
                    font-family: 'Roboto', sans-serif;
                    background: linear-gradient(135deg, #1a1c2c, #2e324b);
                    color: #f4f4f4;
                    line-height: 1.8;
                    padding-bottom: 50px;
                }

                /* Section Styling */
                section {
                    padding: 3rem;
                    max-width: 1000px;
                    margin: 2rem auto;
                    background-color: rgba(255, 255, 255, 0.05);
                    border-radius: 12px;
                    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.1);
                    backdrop-filter: blur(10px);
                }

                section h1 {
                    font-size: 2.8rem;
                    color: #fad20c;
                    margin-bottom: 20px;
                    text-shadow: 3px 3px 0 rgba(244, 181, 22, 0.8), 4px 4px 5px rgba(143, 72, 72, 0.7);
                }

                .image-container {
                    text-align: center;
                    margin-top: 20px;
                }

                img {
                    max-width: 100%;
                    border-radius: 10px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
                }

                .button-container {
                    text-align: left;
                    margin-top: 30px;
                }

                .button {
                    display: inline-block;
                    padding: 12px 25px;
                    font-size: 18px;
                    color: #252837; /* Darker text for contrast */
                    background-color: #fad20c; /* Matching yellow color */
                    text-decoration: none;
                    border-radius: 8px;
                    border: none;
                    cursor: pointer;
                    transition: all 0.3s ease;
                    box-shadow: 0 4px 10px rgba(244, 181, 22, 0.6);
                }

                .button:hover {
                    background-color: #f9c936; /* Slightly lighter yellow */
                    box-shadow: 0 6px 12px rgba(249, 201, 54, 0.8);
                }
            </style>
        </head>
        <body>
            <section>
                <h1>Graph</h1>
                <div class="image-container">
                    <img src="/static/graph.jpg" alt="Graph Image">
                </div>
                <div class="button-container">
                    <a href="/" class="button">Go to Home</a>
                </div>
            </section>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
