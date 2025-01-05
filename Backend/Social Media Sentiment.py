import pandas as pd
import re
import spacy
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import StratifiedKFold

nlp = spacy.load("en_core_web_sm")

df = pd.read_csv('/kaggle/input/credit-social-media/credit_social_media_posts.csv')

df['Sentiment'] = df['Hashtags'].apply(lambda x: 'positive' if 'Success' in x or 'Freedom' in x 
                                       else ('negative' if 'Debt' in x or 'Pitfalls' in x else 'neutral'))


X = df['Post Content']  
y = df['Sentiment']     

le = LabelEncoder()
y_encoded = le.fit_transform(y)

def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)  
    text = re.sub(r'\d+', '', text)  
    text = re.sub(r'[^\w\s]', '', text)  
    return text

X_cleaned = X.apply(clean_text)

def lemmatize_text(text):
    doc = nlp(text)
    return " ".join([token.lemma_ for token in doc])

X_lemmatized = X_cleaned.apply(lemmatize_text)

X_train, X_test, y_train, y_test = train_test_split(X_lemmatized, y_encoded, test_size=0.2, random_state=42)

pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(ngram_range=(1, 2), max_features=5000, stop_words='english')),
    ('clf', RandomForestClassifier(random_state=42))
])

param_grid = {
    'tfidf__max_df': [0.75, 0.85],
    'clf__n_estimators': [100, 200],
    'clf__max_depth': [10, 20, None],
    'clf__min_samples_split': [2, 5]
}

grid_search = GridSearchCV(pipeline, param_grid, cv=StratifiedKFold(n_splits=5), scoring='accuracy', verbose=1)

grid_search.fit(X_train, y_train)

print(f"Best Parameters: {grid_search.best_params_}")

y_pred = grid_search.predict(X_test)

print(f"Unique classes in the test set: {set(y_test)}")
print(f"Unique classes in the prediction: {set(y_pred)}")

report = classification_report(y_test, y_pred, target_names=le.classes_, labels=range(len(le.classes_)))

print("\nClassification Summary (Percentage - Wise):")
print("----------------------------------------------------")

for line in report.split('\n')[2:-3]:
    parts = line.split()
    class_name = parts[0]
    precision = float(parts[1])
    recall = float(parts[2])
    f1_score = float(parts[3])
    
    print(f"Class: {class_name.capitalize()}")
    print(f"  - Precision: {precision*100:.2f}% (How often the model was correct when it said {class_name})")
    print(f"  - Recall: {recall*100:.2f}% (How good the model is at identifying all {class_name} posts)")
    print(f"  - F1-Score: {f1_score*100:.2f}% (A balance of precision and recall for {class_name})")
    print(f"  - Support: {int(parts[4])} posts were actually labeled as {class_name}")
    print("----------------------------------------------------")

average_precision = float(parts[1])
average_recall = float(parts[2])
average_f1_score = float(parts[3])

print(f"\nOverall Performance:")
print(f"  - Average Precision: {average_precision*100:.2f}% (Overall accuracy when the model makes positive predictions)")
print(f"  - Average Recall: {average_recall*100:.2f}% (Overall ability of the model to identify the correct posts)")
print(f"  - Average F1-Score: {average_f1_score*100:.2f}% (Overall balance of precision and recall)")
print(f"  - Accuracy: {grid_search.best_score_*100:.2f}% (How often the model got the correct sentiment overall)")
