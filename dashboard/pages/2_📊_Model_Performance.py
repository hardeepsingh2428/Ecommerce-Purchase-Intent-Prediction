import streamlit as st
import pandas as pd
from pathlib import Path
st.set_page_config(
    page_title="Model Performance",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Model Performance")

st.markdown("""
This page summarizes the performance of the Random Forest model used for purchase prediction.
""")

st.divider()
BASE_DIR = Path(__file__).resolve().parents[2]

comparison = pd.read_csv(
    BASE_DIR / "reports" / "model_comparison.csv",
    index_col=0
)

rf = comparison.loc["Random Forest"]

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Accuracy", f"{rf['accuracy']:.2%}")

with col2:
    st.metric("Precision", f"{rf['precision']:.2%}")

with col3:
    st.metric("Recall", f"{rf['recall']:.2%}")

with col4:
    st.metric("F1 Score", f"{rf['f1_score']:.2%}")

with col5:
    st.metric("ROC-AUC", f"{rf['roc_auc']:.2%}")
st.divider()
st.subheader("📊 Model Comparison")

st.dataframe(
    comparison.style.format("{:.2%}"),
    use_container_width=True
)

st.divider()

st.subheader("Confusion Matrix")

confusion_matrix = pd.DataFrame(
    [
        [865, 52],
        [49, 267]
    ],
    columns=["Predicted No", "Predicted Yes"],
    index=["Actual No", "Actual Yes"]
)

st.dataframe(confusion_matrix, use_container_width=True)

st.divider()

st.subheader("Model Evaluation Summary")

st.markdown("""
### Random Forest Classifier

**Strengths**

- High overall accuracy
- Handles non-linear relationships effectively
- Robust against overfitting
- Fast prediction time
- Works well with mixed feature types

**Limitations**

- Less interpretable than simple models
- Larger model size
- Requires feature importance analysis for explainability
""")

st.success("✅ Model performance meets production-ready standards for demonstration purposes.")