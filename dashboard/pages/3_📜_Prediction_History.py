import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Prediction History",
    page_icon="📜",
    layout="wide"
)

st.title("📜 Prediction History")

st.markdown("""
View all predictions made during the current session.
""")

# Initialize session history if missing
if "history" not in st.session_state:
    st.session_state.history = []

history = st.session_state.history

if len(history) == 0:

    st.info("No predictions have been made yet.")

else:

    history_df = pd.DataFrame(history)

    st.subheader("Prediction Records")

    st.dataframe(
        history_df,
        use_container_width=True
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Predictions",
            len(history_df)
        )

    with col2:
        avg_prob = history_df["Probability"].mean()

        st.metric(
            "Average Probability",
            f"{avg_prob:.2%}"
        )

    with col3:
        avg_time = history_df["Response Time (s)"].mean()

        st.metric(
            "Average Response Time",
            f"{avg_time:.3f}s"
        )

    st.divider()

    csv = history_df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        "📥 Download Prediction History",
        csv,
        file_name="prediction_history.csv",
        mime="text/csv",
        use_container_width=True
    )