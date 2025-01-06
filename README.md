# IndustriAI
Commit Title:
Completed Part 1: Data Collection and Integration

Commit Description:
In this commit, we collected and integrated data from three different sources:

    Social Media Sentiment: Collected data on customer sentiments based on their posts.
    Utility Payments: Integrated customer payment history for utilities.
    Geolocation Data: Included location stability scores based on customer city.

The datasets were cleaned by handling missing values and removing duplicates. These datasets were then merged into one final dataset and saved as final_merged_data.csv for further use.

Commit Title:
Part 2: Approach
The task given to us was to enable credit risk analysis using alternative sources of data.
Specifics of this data were already provided above.
Apart from Social Media Sentiment ,the other two fields require a pre - existing prediction model based on traditional data.
To give an example , Geolocation Data assigns stability scores based on customer city. For this we need to collect the credit score data for that particular city.
We have used this particular Kaggle Dataset
(https://www.kaggle.com/datasets/parisrohan/credit-score-classification?select=train.csv )

In order to resolve missing data problems, kindly use the preprocessed data present in the repository.

Commit Title:
Part 3: Explainability and Transparency
The goal is to ensure the model's predictions are explainable and transparent for lenders by using tools like SHAP and LIME to identify key factors influencing risk scores, such as payment history and social media sentiment. Visualizations like bar charts for feature importance and SHAP summary plots will be created to highlight top contributors. Additionally, clear and simple reports will be generated to explain model decisions, providing examples such as, "On-time utility payments added +20% to this person's low-risk score." Deliverables include explainable predictions, feature importance visualizations, and user-friendly decision reports for lenders.

Links :
Geolocation Model:
https://www.kaggle.com/code/sukandwyrm/notebookf1148cf6d2
Flask Backend:
https://www.kaggle.com/code/sukandwyrm/notebook971748f37d

Round 2:
Expanding on explainability:
As stated before ,One of our goals is to make sure that users gain a clear perspective on the data obtained. Now our work will focus on integrating the ML backend with our Flask frontend. The outputs of all 3 ML algorithms will be accessible and a separate page will display a graph based on user data collected from them.
And so, we hope to locally host and deploy a website that implements all these features.

This page is a demo of what a Real - Time system can achieve. For demonstration purposes we have taken datasets from Kaggle , Google and generated our own.
   The model predicts this person is low risk (likely to repay the loan).
        Explanation:
            Social Media Sentiment: Positive posts (+10%).
            Utility Payments: Consistent on-time payments (+20%).
            Location Stability: Staying in one place (+15%).
After generating the predicted outputs from the the 3 Ml algorithms used , we focused on the positive weighted interactions and assigned a multiplier to them. To express in simple terms, this is the formula we used.[  

avg_score = (model1_output * model1_multiplier + model2_output * model2_multiplier + model3_output * model3_multiplier) / 3

[Contribution = Weight × Average Score from Model Outputs:]
    
total_score = avg_score + sentiment_contribution + utility_contribution + location_contribution.

Using the data generated from this a graph was plotted.

In order to make our site simpler to interact with , we opted for a more traditional approach. The results are stored to be viewd at the viewer's convenience.
These results can be viewd from the website we built using flask. Temporarily its local - hosted .
