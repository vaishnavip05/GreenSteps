import streamlit as st
import pandas as pd
from modules.scoring import add_score


def photo_alternative_ui():
    st.subheader("📷 AI Eco Alternative Finder")

    uploaded = st.file_uploader("Upload your item photo", type=["jpg", "png"])

    if uploaded:
        st.image(uploaded, caption="Uploaded Image", use_column_width=True)

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

        if st.button("Find Better Option"):
            # ✅ corrected path
            df = pd.read_csv("products/eco_alternatives.csv")

            match = df[df["item"] == item_name]

            if not match.empty:
                alt = match.iloc[0]["alternative"]
                benefit = match.iloc[0]["benefit"]

                st.success(f"✅ Try: {alt}")
                st.info(f"🌍 Benefit: {benefit}")

                add_score(15)
                st.write("⭐ +15 points for choosing better!")
            else:
                st.warning("No suggestion found yet.")
