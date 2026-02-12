import streamlit as st


# --------------------------------------------------
# INIT REWARD STORAGE
# --------------------------------------------------
def init_rewards():
    if "points" not in st.session_state:
        st.session_state.points = 0

    if "streak" not in st.session_state:
        st.session_state.streak = 0


# --------------------------------------------------
# ADD POINTS
# --------------------------------------------------
def add_points(value):
    st.session_state.points += value


# --------------------------------------------------
# INCREASE STREAK
# --------------------------------------------------
def increase_streak():
    st.session_state.streak += 1


# --------------------------------------------------
# RESET STREAK
# --------------------------------------------------
def reset_streak():
    st.session_state.streak = 0


# --------------------------------------------------
# SHOW REWARD DASHBOARD
# --------------------------------------------------
def rewards_ui():
    init_rewards()

    st.subheader("🏆 Your Rewards")

    c1, c2 = st.columns(2)

    c1.metric("⭐ Points", st.session_state.points)
    c2.metric("🔥 Streak", st.session_state.streak)
