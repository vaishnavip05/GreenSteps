
import streamlit as st

from modules.scoring import scoring_ui, add_score
from modules.rewards import rewards_ui, add_points, increase_streak


def youth_dashboard():
    st.title("🎓 Youth Zone")

    # ---------------- USER INFO ----------------
    st.write(f"Welcome, **{st.session_state.user}**")
    st.write("Awareness Level:", st.session_state.user_level)

    st.divider()

    # ---------------- PROGRESS ----------------
    scoring_ui()
    rewards_ui()

    st.divider()

    # ---------------- DAILY CHALLENGE ----------------
    st.subheader("🔥 Today's Challenge")
    st.info("Avoid single-use plastic today.")

    if st.button("Challenge Completed"):
        add_score(15)
        add_points(15)
        increase_streak()
        st.success("Great consistency! +15 points 🚀")
        st.rerun()

    st.divider()

    # ---------------- PHOTO PROOF ----------------
    st.subheader("📷 Upload Action Proof")
    st.write("Upload a photo of your eco-friendly action.")
    st.warning("Upload & AI verification coming soon.")

    st.divider()

    # ---------------- OUTFIT / PRODUCT ANALYSIS ----------------
    st.subheader("👕 Smart Alternative Suggestions")
    st.write("AI will suggest greener choices.")
    st.warning("Analysis feature coming soon.")
