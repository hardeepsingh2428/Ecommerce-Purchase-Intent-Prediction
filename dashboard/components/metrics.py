import streamlit as st


def render_metrics(api_online, prediction_count):

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Model",
            "Random Forest"
        )

    with c2:
        st.metric(
            "Features",
            "17"
        )

    with c3:
        if api_online:
            st.metric(
                "API",
                "🟢 Online"
            )
        else:
            st.metric(
                "API",
                "🔴 Offline"
            )

    with c4:
        st.metric(
            "Predictions",
            prediction_count
        )