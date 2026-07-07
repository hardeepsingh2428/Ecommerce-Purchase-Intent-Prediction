import streamlit as st
import requests


def render_sidebar(prediction_count):

    with st.sidebar:

        st.title("🛒 Purchase Predictor")

        st.markdown("---")

        st.subheader("Project Information")

        st.write("**Model:** Random Forest")
        st.write("**Features:** 17")
        st.write("**Frontend:** Streamlit")
        st.write("**Backend:** FastAPI")

        st.markdown("---")

        try:
            requests.get("http://127.0.0.1:8000/")
            st.success("🟢 API Online")
        except Exception:
            st.error("🔴 API Offline")

        st.markdown("---")

        st.subheader("Statistics")

        st.metric(
            "Predictions Made",
            prediction_count
        )

        st.metric(
            "Features",
            17
        )

        st.markdown("---")

        st.info(
            "Enterprise Machine Learning Dashboard"
        )

        st.caption("Developed by Hardeep Singh")
        print("sidebar.py loaded")