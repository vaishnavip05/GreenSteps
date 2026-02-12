import streamlit as st

from modules.scoring import scoring_ui, add_score
from modules.rewards import rewards_ui, add_points

# ✅ games
from games.storytelling import storytelling_ui
from games.pet_growth import pet_ui
from games.trash_sorting import trash_sorting_ui


def kids_dashboard():
    st.title("👶 Kids Zone")
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
    storytelling_ui()

    st.divider()

    # ---------------- PET SYSTEM ----------------
    st.subheader("🐾 Your Eco Pet")
    pet_ui()

    st.divider()

    # ---------------- TRASH GAME ----------------
    st.subheader("♻ Trash Sorting")
    trash_sorting_ui()
