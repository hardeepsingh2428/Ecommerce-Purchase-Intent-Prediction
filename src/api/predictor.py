import json
import joblib
import pandas as pd
from pathlib import Path

# Project root
BASE_DIR = Path(__file__).resolve().parents[2]

# Models directory
MODELS_DIR = BASE_DIR / "models"

# Load model
model = joblib.load(MODELS_DIR / "best_random_forest.pkl")

# Load label encoders
label_encoders = joblib.load(MODELS_DIR / "label_encoders.pkl")

# Load feature order
with open(MODELS_DIR / "feature_columns.json", "r") as f:
    feature_columns = json.load(f)


def predict_purchase(data: dict):

    df = pd.DataFrame([data])

    # Encode categorical columns
    for col, encoder in label_encoders.items():
        df[col] = encoder.transform(df[col])

    # Match training feature order
    df = df[feature_columns]

    prediction = int(model.predict(df)[0])

    probability = float(model.predict_proba(df)[0][1])

    return {
        "prediction": prediction,
        "prediction_label": "Purchase" if prediction == 1 else "No Purchase",
        "purchase_probability": probability,
    }