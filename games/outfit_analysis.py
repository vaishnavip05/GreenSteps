import streamlit as st
from modules.scoring import add_score


# --------------------------------------------------
# SAMPLE DATABASE
# later can be replaced with CSV or AI model
# --------------------------------------------------
OUTFIT_DATA = {
    "Fast Fashion T-Shirt": {
        "impact": "High water usage & waste generation.",
        "better": "Try thrifted or sustainably made clothing."
    },
    "Reusable Cotton Shirt": {
        "impact": "Lower environmental impact.",
        "better": "Great choice! Maintain it for long use."
    },
    "Polyester Jacket": {
        "impact": "Microplastic pollution risk.",
        "better": "Consider natural fiber alternatives."
    },
    "Second-Hand Clothes": {
        "impact": "Extends product life, very eco-friendly.",
        "better": "Excellent sustainable decision!"
    }
}


# --------------------------------------------------
# MAIN UI
# --------------------------------------------------
def outfit_analysis_ui():
    st.subheader("👕 Outfit Impact Analyzer")

    item = st.selectbox(
        "Select what you are wearing today:",
        list(OUTFIT_DATA.keys())
    )

    if st.button("Analyze"):
        result = OUTFIT_DATA[item]

        st.write("### 🌍 Environmental Impact")
        st.info(result["impact"])

        st.write("### ✅ Better Suggestion")
        st.success(result["better"])

        add_score(10)
        st.write("⭐ +10 points for checking your impact!")
