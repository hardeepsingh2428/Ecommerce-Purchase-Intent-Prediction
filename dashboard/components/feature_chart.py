import streamlit as st
from pathlib import Path

# ======================================================
# PROJECT PATHS
# ======================================================

BASE_DIR = Path(__file__).resolve().parents[2]
DOCS_DIR = BASE_DIR / "docs"


# ======================================================
# FEATURE CHART COMPONENT
# ======================================================

def render_feature_chart():

    st.header("🔍 Model Explainability (SHAP & LIME)")

    st.markdown("""
    These visualizations explain how the Random Forest model makes predictions.

    **SHAP (SHapley Additive exPlanations)** explains global and local feature importance.

    **LIME (Local Interpretable Model-Agnostic Explanations)** explains individual predictions.
    """)

    # ==================================================
    # SHAP CHARTS
    # ==================================================

    tab1, tab2 = st.tabs(
        [
            "📊 SHAP Summary Plot",
            "📈 SHAP Feature Importance"
        ]
    )

    with tab1:

        summary_path = DOCS_DIR / "shap_summary_plot.png"

        if summary_path.exists():

            st.image(
                str(summary_path),
                use_container_width=True,
                caption=(
                    "Each point represents one visitor session. "
                    "Red indicates higher feature values and blue indicates lower values."
                )
            )

        else:

            st.warning(
                f"SHAP summary plot not found:\n\n{summary_path}"
            )

    with tab2:

        bar_path = DOCS_DIR / "shap_feature_importance_bar.png"

        if bar_path.exists():

            st.image(
                str(bar_path),
                use_container_width=True,
                caption="Average impact of each feature on model predictions."
            )

        else:

            st.warning(
                f"SHAP feature importance plot not found:\n\n{bar_path}"
            )

    st.divider()

    # ==================================================
    # SHAP LOCAL EXPLANATION
    # ==================================================

    st.subheader("📍 SHAP Local Explanation")

    local_path = DOCS_DIR / "shap_local_explanation_sample0.png"

    if local_path.exists():

        st.image(
            str(local_path),
            use_container_width=True,
            caption="Explanation of an individual customer prediction using SHAP."
        )

    else:

        st.warning(
            f"SHAP local explanation image not found:\n\n{local_path}"
        )

    st.divider()

    # ==================================================
    # LIME LOCAL EXPLANATION
    # ==================================================

    st.subheader("🟢 LIME Local Explanation")

    lime_path = DOCS_DIR / "lime_local_explanation_sample0.html"

    if lime_path.exists():

        with open(lime_path, "r", encoding="utf-8") as f:
            html = f.read()

        st.components.v1.html(
            html,
            height=700,
            scrolling=True
        )

    else:

        st.warning(
            f"LIME explanation HTML not found:\n\n{lime_path}"
        )

    st.divider()
    