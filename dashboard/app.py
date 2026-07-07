import streamlit as st
import requests

from components.sidebar import render_sidebar
from components.metrics import render_metrics
from components.predictor_form import render_prediction_form
from components.prediction_result import render_prediction_result
from components.history_table import render_history
from components.analytics import render_analytics
from components.feature_chart import render_feature_chart
from components.footer import render_footer

from utils.api import check_api_status, predict_purchase
from utils.session import (
    initialize_session,
    add_prediction,
    get_history
)

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Ecommerce Purchase Intent Predictor",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

.main{
    padding-top:1rem;
}

.block-container{
    padding-top:2rem;
}

div[data-testid="metric-container"]{
    border-radius:12px;
    border:1px solid #dddddd;
    padding:15px;
    background:#fafafa;
}

.stButton>button{
    width:100%;
    height:55px;
    border-radius:12px;
    font-size:18px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# INITIALIZE
# =====================================================

initialize_session()

api_online = check_api_status()

# =====================================================
# SIDEBAR
# =====================================================

render_sidebar(
    st.session_state.prediction_count
)

# =====================================================
# HEADER
# =====================================================

st.title("🛒 Ecommerce Purchase Intent Prediction")

st.markdown("""
### Machine Learning Powered Customer Purchase Prediction

Predict whether an online visitor is likely to complete a purchase based on browsing behaviour.
""")

st.divider()

# =====================================================
# DASHBOARD METRICS
# =====================================================

render_metrics(
    api_online,
    st.session_state.prediction_count
)

st.divider()

# =====================================================
# PREDICTOR FORM
# =====================================================

predict_button, payload = render_prediction_form()

# =====================================================
# MAKE PREDICTION
# =====================================================

if predict_button:

    try:

        result, response_time = predict_purchase(payload)

        probability = result["purchase_probability"]

        confidence = max(
            probability,
            1 - probability
        )

        add_prediction(
            result["prediction_label"],
            round(probability, 4),
            round(confidence, 4),
            response_time
        )

        render_prediction_result(
            result,
            probability,
            confidence,
            response_time
        )

    except requests.exceptions.ConnectionError:

        st.error("Cannot connect to FastAPI server.")

    except requests.exceptions.HTTPError as e:

        st.error(f"HTTP Error: {e}")

    except Exception as e:

        st.error(f"Unexpected Error: {e}")

# =====================================================
# HISTORY
# =====================================================

history = get_history()

render_history(history)

# =====================================================
# ANALYTICS
# =====================================================

render_analytics(history)

# =====================================================
# MODEL EXPLAINABILITY (SHAP)
# =====================================================

render_feature_chart()

# =====================================================
# PROJECT INFORMATION
# =====================================================

st.header("📘 Project Information")

left, right = st.columns(2)

with left:

    st.subheader("📌 Project Overview")

    st.markdown("""

This project predicts whether an online visitor will complete a purchase.

The application demonstrates a complete Machine Learning workflow:

- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Model Training
- Hyperparameter Tuning
- Model Explainability using SHAP
- Experiment Tracking with MLflow
- REST API using FastAPI
- Interactive Dashboard using Streamlit

""")

with right:

    st.subheader("🛠 Technology Stack")

    st.markdown("""

### Languages

- Python

### Machine Learning

- Scikit-Learn
- Random Forest
- Logistic Regression
- Decision Tree

### Explainability

- SHAP
- LIME

### Backend

- FastAPI

### Frontend

- Streamlit

### Tracking

- MLflow

""")

st.divider()

# =====================================================
# DASHBOARD SUMMARY
# =====================================================

st.header("📊 Dashboard Summary")

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Predictions Made",
        st.session_state.prediction_count
    )

with col2:

    if history:

        avg_prob = sum(
            item["Probability"]
            for item in history
        ) / len(history)

        st.metric(
            "Average Purchase Probability",
            f"{avg_prob:.2%}"
        )

    else:

        st.metric(
            "Average Purchase Probability",
            "0%"
        )

with col3:

    if history:

        avg_time = sum(
            item["Response Time (s)"]
            for item in history
        ) / len(history)

        st.metric(
            "Average API Response",
            f"{avg_time:.3f}s"
        )

    else:

        st.metric(
            "Average API Response",
            "0.000 s"
        )

st.divider()

# =====================================================
# FOOTER
# =====================================================

render_footer()