import streamlit as st


# --------------------------------------------------
# INIT DONATION STORAGE
# --------------------------------------------------
def init_donations():
    if "donations" not in st.session_state:
        st.session_state.donations = {
            "Trees": 0,
            "Water": 0,
            "Recycling": 0
        }


# --------------------------------------------------
# ADD DONATION
# --------------------------------------------------
def donate(cause, amount):
    st.session_state.donations[cause] += amount


# --------------------------------------------------
# UI FOR DONATIONS
# --------------------------------------------------
def donation_ui():
    init_donations()

    st.subheader("❤️ Support a Cause")

    cause = st.selectbox(
        "Choose where you want to contribute:",
        ["Trees", "Water", "Recycling"]
    )

    amount = st.slider("Contribution Amount", 1, 100, 10)

    if st.button("Donate"):
        donate(cause, amount)
        st.success(f"Thank you for supporting {cause}! 🌱")
        st.rerun()

    st.divider()

    # ---------------- SHOW TOTALS ----------------
    st.subheader("🌍 Community Contributions")

    for c, value in st.session_state.donations.items():
        st.write(f"{c}: {value} points")
