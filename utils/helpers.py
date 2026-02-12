import streamlit as st


def reset_user_progress():
    """Clear session for fresh start."""
    keys = list(st.session_state.keys())
    for k in keys:
        del st.session_state[k]


def greet_user():
    if "user" in st.session_state:
        st.write(f"Welcome, **{st.session_state.user}** 🌱")
