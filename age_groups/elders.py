import streamlit as st
from modules.community import community_ui
from modules.scoring import scoring_ui


def elders_dashboard():
    st.title("👵 Elders Community")
    # ---------------- HOME BUTTON ----------------
    if st.button("🏠 Home"):
        st.session_state.age_group = None
        st.session_state.profile_built = False
        st.rerun()

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

    # ---------------- MONEY DONATION ----------------
    st.subheader("🤝 Support a Cause")

    cause = st.selectbox(
        "Choose where you want to contribute:",
        ["Recycling", "Trees", "Money"]
    )

    amount = st.number_input("Enter donation amount (₹)", min_value=0)

    if st.button("Donate Now"):
        if amount > 0:
            st.success(f"🙏 Thank you for donating ₹{amount} towards {cause}!")
            st.balloons()
        else:
            st.warning("Please enter a valid amount.")
