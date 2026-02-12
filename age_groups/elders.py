import streamlit as st

from modules.community import community_ui
from modules.donations import donation_ui
from modules.scoring import scoring_ui


def elders_dashboard():
    st.title("👵 Elders Community")

    # ---------------- USER INFO ----------------
    st.write(f"Welcome, **{st.session_state.user}**")
    st.write("Awareness Level:", st.session_state.user_level)

    st.divider()

    # ---------------- CONTRIBUTION IMPACT ----------------
    scoring_ui()

    st.divider()

    # ---------------- COMMUNITY SPACE ----------------
    community_ui()

    st.divider()

    # ---------------- DONATIONS ----------------
    donation_ui()
