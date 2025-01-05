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
We have used a Kaggle Dataset
(https://www.kaggle.com/datasets/parisrohan/credit-score-classification?select=train.csv )
