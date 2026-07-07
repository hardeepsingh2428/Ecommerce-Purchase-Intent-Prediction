import streamlit as st


def render_prediction_result(result, probability, confidence, response_time):

    st.success("Prediction Complete!")

    st.caption(
        f"Prediction completed in {response_time:.3f} seconds"
    )

    st.subheader("🎯 Prediction Result")

    col1, col2, col3 = st.columns(3)

    with col1:

        if result["prediction"] == 1:

            st.success("🛒 PURCHASE")

        else:

            st.error("❌ NO PURCHASE")

    with col2:

        st.metric(
            "Purchase Probability",
            f"{probability:.2%}"
        )

    with col3:

        st.metric(
            "Model Confidence",
            f"{confidence:.2%}"
        )

    st.progress(float(probability))

    if probability >= 0.75:

        st.success(
            "🟢 High likelihood of purchase."
        )

    elif probability >= 0.50:

        st.info(
            "🟡 Moderate likelihood of purchase."
        )

    else:

        st.warning(
            "🔴 Low likelihood of purchase."
        )

    st.divider()
    