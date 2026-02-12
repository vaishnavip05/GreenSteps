import streamlit as st


def login_page():
    st.subheader("🔐 Login to GreenSteps")

    username = st.text_input("Enter your name")

    if st.button("Login"):
        if username.strip() == "":
            st.warning("Please enter your name.")
        else:
            st.session_state.user = username
            st.success(f"Welcome, {username}! 🌱")
            st.rerun()
