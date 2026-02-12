import streamlit as st

from modules.scoring import scoring_ui, add_score
from modules.rewards import rewards_ui, add_points, increase_streak

# ✅ enable features
from games.photo_alternative import photo_alternative_ui
from games.outfit_analysis import outfit_analysis_ui


def youth_dashboard():
    st.title("🎓 Youth Zone")
    # ---------------- HOME BUTTON ----------------
    if st.button("🏠 Home"):
        st.session_state.page = "home"
        st.rerun()
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
    photo_alternative_ui()

    st.divider()

    # ---------------- OUTFIT / PRODUCT ANALYSIS ----------------
    st.subheader("👕 Smart Alternative Suggestions")
    outfit_analysis_ui()
