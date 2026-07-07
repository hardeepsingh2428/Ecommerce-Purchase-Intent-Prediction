import streamlit as st
import pandas as pd


def render_analytics(history):

    st.header("📈 Prediction Analytics")

    if len(history) == 0:
        st.info("No predictions yet. Make a prediction above to see analytics here.")
        return

    df = pd.DataFrame(history)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Purchase Probability Distribution")
        if "Probability" in df.columns:
            st.bar_chart(df["Probability"])
        else:
            st.info("Probability data not available.")

    with col2:
        st.subheader("Prediction Outcomes")
        label_col = next(
            (c for c in ["Prediction", "Prediction Label", "prediction_label"] if c in df.columns),
            None
        )
        if label_col:
            st.bar_chart(df[label_col].value_counts())
        else:
            st.info("Prediction outcome column not found.")

    st.subheader("Response Time Trend")
    if "Response Time (s)" in df.columns:
        st.line_chart(df["Response Time (s)"])
    else:
        st.info("Response time data not available.")

    st.divider()
    