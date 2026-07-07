import streamlit as st
import pandas as pd


def render_history(history):

    if len(history) == 0:

        return

    st.header("📜 Prediction History")

    history_df = pd.DataFrame(history)

    st.dataframe(
        history_df,
        use_container_width=True
    )

    csv = history_df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        "📥 Download Prediction History",
        data=csv,
        file_name="prediction_history.csv",
        mime="text/csv",
        use_container_width=True
    )

    st.divider()
    