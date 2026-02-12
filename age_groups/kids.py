import streamlit as st

from modules.scoring import scoring_ui, add_score
from modules.rewards import rewards_ui, add_points


def kids_dashboard():
    st.title("👶 Kids Zone")

    # ---------------- USER INFO ----------------
    st.write(f"Welcome, **{st.session_state.user}**")
    st.write("Awareness Level:", st.session_state.user_level)

    st.divider()

    # ---------------- PROGRESS ----------------
    scoring_ui()
    rewards_ui()

    st.divider()

    # ---------------- DAILY TASK ----------------
    st.subheader("🎯 Today's Fun Mission")
    st.info("Put waste into the correct dustbin.")

    if st.button("I Did It!"):
        add_score(10)
        add_points(10)
        st.success("Amazing job! +10 points 🌟")
        st.balloons()
        st.rerun()

    st.divider()

    # ---------------- STORY MODE ----------------
    st.subheader("📖 AI Storytelling")
    st.write("Listen to eco stories and learn good habits.")
    st.warning("Story feature coming soon.")

    st.divider()

    # ---------------- PET SYSTEM ----------------
    st.subheader("🐾 Your Eco Pet")
    st.write("Complete missions to help your pet grow.")
    st.warning("Pet growth feature coming soon.")
