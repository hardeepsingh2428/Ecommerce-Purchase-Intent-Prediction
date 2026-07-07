import streamlit as st


def render_prediction_form():

    st.header("📋 Customer Session Details")

    left, right = st.columns(2)

    with left:

        administrative = st.number_input(
            "Administrative",
            min_value=0,
            value=1
        )

        administrative_duration = st.number_input(
            "Administrative Duration",
            min_value=0.0,
            value=14.65
        )

        informational = st.number_input(
            "Informational",
            min_value=0,
            value=0
        )

        informational_duration = st.number_input(
            "Informational Duration",
            min_value=0.0,
            value=0.0
        )

        product_related = st.number_input(
            "Product Related",
            min_value=0,
            value=19
        )

        product_related_duration = st.number_input(
            "Product Related Duration",
            min_value=0.0,
            value=283.88
        )

        bounce_rates = st.number_input(
            "Bounce Rates",
            min_value=0.0,
            max_value=1.0,
            value=0.008
        )

    with right:

        exit_rates = st.number_input(
            "Exit Rates",
            min_value=0.0,
            max_value=1.0,
            value=0.042
        )

        page_values = st.number_input(
            "Page Values",
            min_value=0.0,
            value=68.58
        )

        special_day = st.number_input(
            "Special Day",
            min_value=0.0,
            max_value=1.0,
            value=0.0
        )

        month = st.selectbox(
            "Month",
            [
                "Feb",
                "Mar",
                "May",
                "June",
                "Jul",
                "Aug",
                "Sep",
                "Oct",
                "Nov",
                "Dec"
            ]
        )

        operating_system = st.number_input(
            "Operating System",
            min_value=1,
            value=1
        )

        browser = st.number_input(
            "Browser",
            min_value=1,
            value=2
        )

        region = st.number_input(
            "Region",
            min_value=1,
            value=1
        )

        traffic_type = st.number_input(
            "Traffic Type",
            min_value=1,
            value=1
        )

    visitor_type = st.selectbox(
        "Visitor Type",
        [
            "Returning_Visitor",
            "New_Visitor",
            "Other"
        ]
    )

    weekend = st.checkbox("Weekend")

    payload = {

        "Administrative": administrative,
        "Administrative_Duration": administrative_duration,
        "Informational": informational,
        "Informational_Duration": informational_duration,
        "ProductRelated": product_related,
        "ProductRelated_Duration": product_related_duration,
        "BounceRates": bounce_rates,
        "ExitRates": exit_rates,
        "PageValues": page_values,
        "SpecialDay": special_day,
        "Month": month,
        "OperatingSystems": operating_system,
        "Browser": browser,
        "Region": region,
        "TrafficType": traffic_type,
        "VisitorType": visitor_type,
        "Weekend": weekend

    }

    predict_button = st.button(
        "🚀 Predict Purchase",
        use_container_width=True
    )

    return predict_button, payload