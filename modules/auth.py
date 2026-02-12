import streamlit as st
import json
import os


USER_FILE = "data/users.json"


# --------------------------------------------------
# LOAD USERS
# --------------------------------------------------
def load_users():
    if not os.path.exists(USER_FILE):
        return {}
    with open(USER_FILE, "r") as f:
        return json.load(f)


# --------------------------------------------------
# SAVE USERS
# --------------------------------------------------
def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f)


# --------------------------------------------------
# LOGIN PAGE
# --------------------------------------------------
def login_page():
    st.subheader("🔐 Login to GreenSteps")

    mode = st.radio("Choose:", ["Sign In", "Sign Up"])

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    users = load_users()

    # ---------------- SIGN UP ----------------
    if mode == "Sign Up":
        if st.button("Create Account"):
            if username in users:
                st.error("User already exists.")
            elif username.strip() == "" or password.strip() == "":
                st.warning("Enter username and password.")
            else:
                users[username] = password
                save_users(users)
                st.success("Account created! Please sign in.")

    # ---------------- SIGN IN ----------------
    else:
        if st.button("Login"):
            if username in users and users[username] == password:
                st.session_state.user = username
                st.success("Login successful 🌱")
                st.rerun()
            else:
                st.error("Invalid username or password.")
