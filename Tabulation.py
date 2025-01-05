import shap
import lime
import lime.lime_tabular
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import os


REPORT_FILENAME = "prediction_report.txt"
VISUALIZATIONS_DIR = "visualizations"
os.makedirs(VISUALIZATIONS_DIR, exist_ok=True)

np.random.seed(42)
n_samples = 1000
n_features = 5
feature_names = ['PaymentHistory', 'Income', 'CreditUtilization', 'SocialMediaSentiment', 'DebtToIncomeRatio']

X = pd.DataFrame(np.random.rand(n_samples, n_features), columns=feature_names)
y = (X['PaymentHistory'] + X['Income'] * 0.5 - X['CreditUtilization'] * 0.3 + X['SocialMediaSentiment'] * 0.2 > 1).astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy * 100:.2f}%")

explainer = shap.Explainer(model, X_train)
shap_values = explainer(X_test)

try:
    shap.summary_plot(shap_values.values, X_test, feature_names=feature_names, show=False)
    plt.savefig(os.path.join(VISUALIZATIONS_DIR, "shap_summary_plot.png"))
    plt.close()
    print("SHAP summary plot saved.")
except Exception as e:
    print(f"Error saving SHAP summary plot: {e}")

for feature in feature_names:
    try:
        shap.dependence_plot(feature, shap_values.values, X_test, feature_names=feature_names, show=False)
        plt.savefig(os.path.join(VISUALIZATIONS_DIR, f"shap_dependence_{feature}.png"))
        plt.close()
        print(f"SHAP dependence plot for {feature} saved.")
    except Exception as e:
        print(f"Error saving SHAP dependence plot for {feature}: {e}")

lime_explainer = lime.lime_tabular.LimeTabularExplainer(
    training_data=np.array(X_train),
    feature_names=feature_names,
    class_names=['LowRisk', 'HighRisk'],
    mode='classification'
)

def generate_report(
    model: RandomForestClassifier, 
    instance: pd.Series, 
    shap_values: shap.Explanation, 
    feature_names: list, 
    i: int
) -> str:
    """
    Generate a textual report explaining a single instance prediction.

    Args:
        model: Trained model.
        instance: Single test instance (pd.Series).
        shap_values: SHAP values for the test set.
        feature_names: List of feature names.
        i: Index of the instance in the test set.

    Returns:
        A formatted string report.
    """
    shap_instance_values = shap_values.values[i]
    prediction = model.predict(instance.to_numpy().reshape(1, -1))[0]
    report = f"Risk Prediction Explanation for Instance {i}:\n\n"
    report += f"Model Prediction: {'High Risk' if prediction == 1 else 'Low Risk'}\n\n"
    report += "Key Factors Contributing to the Decision:\n"
    for feature, value, shap_value in zip(feature_names, instance, shap_instance_values):
        report += f"- {feature}: {value:.2f} (Contribution to risk score: {shap_value:.2f})\n"
    return report

with open(REPORT_FILENAME, "w") as f:
    for i in range(min(5, len(X_test))):  # Limit to top 5 instances for brevity
        instance = X_test.iloc[i]
        try:
            lime_exp = lime_explainer.explain_instance(instance.to_numpy(), model.predict_proba)
            lime_exp.save_to_file(os.path.join(VISUALIZATIONS_DIR, f"lime_explanation_{i}.html"))
            report = generate_report(model, instance, shap_values, feature_names, i)
            f.write(report + "\n\n---\n\n")
            print(f"LIME explanation and report for instance {i} saved.")
        except Exception as e:
            print(f"Error processing instance {i}: {e}")

print(f"Reports saved to {REPORT_FILENAME}")
print(f"Visualizations saved to {VISUALIZATIONS_DIR}")
