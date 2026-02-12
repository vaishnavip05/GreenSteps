import streamlit as st
import pandas as pd
from modules.scoring import add_score


def photo_alternative_ui():
    st.subheader("📷 AI Eco Alternative Finder")

    # ---------------- UPLOAD ----------------
    uploaded = st.file_uploader("Upload your item photo (optional)", type=["jpg", "png", "jpeg"])

    if uploaded:
        st.image(uploaded, caption="Uploaded Image", use_column_width=True)

    # ---------------- ITEM SELECTION (ALWAYS VISIBLE) ----------------
    st.write("### What item is this?")
    item_name = st.selectbox(
        "Select closest match:",
        [
            "Plastic water bottle",
            "Plastic bag",
            "Fast fashion shirt",
            "Disposable cup",
            "Paper napkins",
            "Battery lights"
        ]
    )

    # ---------------- FIND OPTION ----------------
    if st.button("Find Better Option"):
        df = pd.read_csv("products/eco_alternatives.csv")

        match = df[df["item"] == item_name]

        if not match.empty:
            alt = match.iloc[0]["alternative"]
            benefit = match.iloc[0]["benefit"]

            st.success(f"✅ Better choice: {alt}")
            st.info(f"🌍 Benefit: {benefit}")

            add_score(15)
            st.write("⭐ +15 points for choosing better!")
        else:
            st.warning("No suggestion found yet.")
