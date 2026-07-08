# 🛒 Ecommerce Purchase Intent Prediction

> End-to-End Machine Learning Project for predicting customer purchase intent using Explainable AI, FastAPI, Streamlit, and MLflow.

## 📌 Project Overview

This project predicts whether an online customer session will result in a purchase using Machine Learning.

The application combines a Random Forest Classifier with a FastAPI backend and an interactive Streamlit dashboard to deliver real-time purchase predictions along with model explainability using SHAP and LIME.

---

# 🚀 Features

- Real-time purchase prediction
- FastAPI REST API
- Interactive Streamlit Dashboard
- Prediction history
- Analytics dashboard
- Model performance comparison
- SHAP Feature Importance
- SHAP Local Explanation
- MLflow Experiment Tracking
- Download prediction history
- Production-ready project structure

---

# 🛠 Tech Stack

## Programming Language

- Python

## Machine Learning

- Scikit-learn
- Random Forest Classifier

## Data Analysis

- Pandas
- NumPy

## Visualization

- Matplotlib
- Plotly
- SHAP
- LIME

## Backend

- FastAPI
- Uvicorn

## Frontend

- Streamlit

## Experiment Tracking

- MLflow

---

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green?logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?logo=streamlit)
![MLflow](https://img.shields.io/badge/MLflow-Experiment%20Tracking-blue)
![SHAP](https://img.shields.io/badge/SHAP-Explainable%20AI-purple)
![License](https://img.shields.io/badge/License-MIT-yellow)

# 📊 Model Performance

| Metric | Score |
|---------|---------|
| Accuracy | 93.17% |
| Precision | 81.23% |
| Recall | 73.47% |
| F1 Score | 77.16% |
| ROC-AUC | 96.91% |

---

# 📁 Project Structure

```
dashboard/
data/
docs/
images/
mlruns/
models/
notebooks/
reports/
src/
requirements.txt
README.md
```

---

# ⚙ Installation

Clone the repository

```bash
git clone <repository-url>
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Run FastAPI

```bash
uvicorn src.api.main:app --reload
```

---

# ▶ Run Streamlit Dashboard

```bash
streamlit run dashboard/app.py
```

---

# 📈 Dashboard Features

- Purchase Prediction
- API Status
- Prediction History
- Analytics Dashboard
- Model Performance
- SHAP Explainability
- LIME Local Explanation

---

# 🧠 Explainable AI

This project includes:

- SHAP Summary Plot
- SHAP Feature Importance
- LIME Local Explanation

These techniques help explain why the model predicts a purchase.

---

# 📊 MLflow

The project uses MLflow for:

- Experiment Tracking
- Parameter Logging
- Metric Logging
- Model Artifact Storage

---

# 📌 Future Improvements

- Docker Support
- Cloud Deployment
- User Authentication
- Batch Prediction API
- CI/CD Pipeline

---

# 👨‍💻 Author

**Hardeep Singh**

Aspiring Data Analyst | Machine Learning Enthusiast

---

⭐ If you like this project, consider giving it a star.
