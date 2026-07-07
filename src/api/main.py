from fastapi import FastAPI

from src.api.schemas import SessionInput, PredictionOutput
from src.api.predictor import predict_purchase

app = FastAPI(
    title="Ecommerce Purchase Intent Prediction API",
    description="Predict whether an online visitor will make a purchase.",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "API is running successfully!"
    }


@app.post("/predict", response_model=PredictionOutput)
def predict(data: SessionInput):

    result = predict_purchase(data.model_dump())

    return result
