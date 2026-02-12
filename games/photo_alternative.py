import streamlit as st
import pandas as pd
from modules.scoring import add_score


# --------------------------------------------------
# FAKE AI DETECTION (demo purpose)
# --------------------------------------------------
def detect_item_from_image():
    """
    For hackathon demo.
    Later replace with real AI model.
    """
    return "Plastic water bottle"


# --------------------------------------------------
# MAIN UI
# --------------------------------------------------
def photo_alternative_ui():
    st.subheader("📷 AI Eco Alternative Finder")

    uploaded = st.file_uploader("Upload your item photo", type=["jpg", "png"])

    if uploaded:
        st.image(uploaded, caption="Uploaded Image", use_column_width=True)

        if st.button("Analyze with AI"):
            # 🤖 AI detection
            item_name = detect_item_from_image()

            st.write(f"### 🤖 AI detected: **{item_name}**")

            df = pd.read_csv("products/eco_alternatives.csv")
            match = df[df["item"] == item_name]

            if not match.empty:
                alt = match.iloc[0]["alternative"]
                benefit = match.iloc[0]["benefit"]

                st.success(f"✅ Better choice: {alt}")
                st.info(f"🌍 Benefit: {benefit}")

                add_score(15)
                st.write("⭐ +15 points for improving your choice!")
            else:
                st.warning("No suggestion found yet.")
