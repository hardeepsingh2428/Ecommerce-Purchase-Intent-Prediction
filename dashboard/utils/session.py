import streamlit as st


def initialize_session():

    if "history" not in st.session_state:
        st.session_state.history = []

    if "prediction_count" not in st.session_state:
        st.session_state.prediction_count = 0


def add_prediction(prediction, probability, confidence, response_time):

    st.session_state.prediction_count += 1

    st.session_state.history.append({
        "Prediction": prediction,
        "Probability": probability,
        "Confidence": confidence,
        "Response Time (s)": response_time
    })


def get_history():
    return st.session_state.history