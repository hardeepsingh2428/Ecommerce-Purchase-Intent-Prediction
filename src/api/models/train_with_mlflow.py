import pandas as pd
import numpy as np
import joblib
import json
import mlflow
import mlflow.sklearn

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)

# =====================================================
# LOAD DATA (same processed data from Phase 4)
# =====================================================

train = pd.read_csv("data/processed/train.csv")
test = pd.read_csv("data/processed/test.csv")

X_train = train.drop("Converted", axis=1)
y_train = train["Converted"]

X_test = test.drop("Converted", axis=1)
y_test = test["Converted"]

# =====================================================
# MLFLOW SETUP
# =====================================================

mlflow.set_tracking_uri("sqlite:///mlflow.db") # stores runs locally in a folder called mlruns/
mlflow.set_experiment("purchase_intent_prediction")


def evaluate_and_log(model, name, params):
    """Fit a model, log its params/metrics/artifact to MLflow, return the fitted model."""

    with mlflow.start_run(run_name=name):

        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        probs = model.predict_proba(X_test)[:, 1]

        metrics = {
            "accuracy": accuracy_score(y_test, preds),
            "precision": precision_score(y_test, preds),
            "recall": recall_score(y_test, preds),
            "f1_score": f1_score(y_test, preds),
            "roc_auc": roc_auc_score(y_test, probs)
        }

        # Log hyperparameters
        mlflow.log_params(params)

        # Log evaluation metrics
        mlflow.log_metrics(metrics)

        # Log the trained model itself as an MLflow artifact
        mlflow.sklearn.log_model(model, artifact_path="model")

        print(f"\n{'='*40}\n{name}\n{'='*40}")
        for k, v in metrics.items():
            print(f"{k}: {v:.4f}")

        return model, metrics


# =====================================================
# RUN EXPERIMENTS FOR EACH MODEL
# =====================================================

results = {}

# 1. Logistic Regression
lr_params = {"max_iter": 1000}
lr = LogisticRegression(**lr_params)
_, results["Logistic Regression"] = evaluate_and_log(lr, "Logistic Regression", lr_params)

# 2. Decision Tree
dt_params = {"random_state": 42}
dt = DecisionTreeClassifier(**dt_params)
_, results["Decision Tree"] = evaluate_and_log(dt, "Decision Tree", dt_params)

# 3. Random Forest (your best model's params from Phase 6 optimization)
rf_params = {
    "n_estimators": 500,
    "max_depth": 10,
    "max_features": "log2",
    "min_samples_leaf": 4,
    "min_samples_split": 5,
    "random_state": 42
}
rf = RandomForestClassifier(**rf_params)
best_model, results["Random Forest"] = evaluate_and_log(rf, "Random Forest (Tuned)", rf_params)

# =====================================================
# SUMMARY TABLE
# =====================================================

results_df = pd.DataFrame(results).T
print("\n\nModel Comparison:\n")
print(results_df)

results_df.to_csv("reports/model_comparison.csv")
print("\nSaved comparison table to reports/model_comparison.csv")
print("\nRun 'mlflow ui' in your terminal to view the tracking dashboard.")
