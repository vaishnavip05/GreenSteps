import streamlit as st

from modules.donations import donation_ui
from modules.scoring import scoring_ui
from modules.rewards import rewards_ui


def adults_dashboard():
    st.title("👨‍💼 Adults Zone")

    # ---------------- USER INFO ----------------
    st.write(f"Welcome, **{st.session_state.user}**")
    st.write("Awareness Level:", st.session_state.user_level)

    st.divider()

    # ---------------- PROGRESS ----------------
    scoring_ui()
    rewards_ui()

    st.divider()

    # ---------------- DAILY SUGGESTION ----------------
    st.subheader("🏠 Smart Home Suggestion")

    st.info(
        "Switching to LED bulbs can reduce energy consumption "
        "and lower your electricity bill."
    )

    if st.button("I will try this"):
        from modules.scoring import add_score
        from modules.rewards import add_points

        add_score(10)
        add_points(10)
        st.success("Great decision! +10 points 🌱")
        st.rerun()

    st.divider()

    # ---------------- DECISION STUDIO PLACEHOLDER ----------------
    st.subheader("🧠 AI Decision Studio")
    st.write("Compare choices and see environmental impact.")
    st.warning("Coming soon in next build.")

    st.divider()

    # ---------------- DONATIONS ----------------
    donation_ui()
