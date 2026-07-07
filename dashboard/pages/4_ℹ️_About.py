import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About This Project")

st.markdown("""
# 🛒 Ecommerce Purchase Intent Prediction Platform

An end-to-end Machine Learning application that predicts whether an online customer is likely to complete a purchase based on browsing behavior.
""")

st.divider()

col1, col2 = st.columns(2)

with col1:

    st.subheader("🎯 Project Objective")

    st.write("""
The objective of this project is to help businesses identify high-intent customers in real time.

This enables marketing teams to:

- Increase conversions
- Improve customer targeting
- Reduce marketing costs
- Personalize customer experiences
""")

with col2:

    st.subheader("🛠 Technology Stack")

    st.write("""
- Python
- Streamlit
- FastAPI
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- Requests
""")

st.divider()

st.subheader("📂 Project Workflow")

st.markdown("""
1. Data Collection
2. Data Cleaning
3. Feature Engineering
4. Model Training
5. Model Evaluation
6. FastAPI Deployment
7. Streamlit Dashboard
8. Real-Time Predictions
""")

st.divider()

st.subheader("🚀 Key Features")

st.markdown("""
✅ Real-time Purchase Prediction

✅ Random Forest Machine Learning Model

✅ FastAPI REST API

✅ Interactive Streamlit Dashboard

✅ Prediction History

✅ CSV Export

✅ Feature Importance Visualization

✅ Multi-Page Application
""")

st.divider()

st.subheader("👨‍💻 Developer")

st.success("Developed by Hardeep Singh")

st.caption("Data Analytics | Data Science | Machine Learning")