import streamlit as st

st.set_page_config(
    page_title="Predict Purchase",
    page_icon="🔮",
    layout="wide"
)

st.title("🔮 Purchase Predictor")

st.markdown("""
Use this page to predict whether a customer is likely to complete a purchase.

This page will use the same prediction form and model as the main dashboard.
""")

st.info(
    "🚧 This page is under development. In the next step, we'll move the prediction form here."
)