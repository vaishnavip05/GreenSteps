import streamlit as st


# --------------------------------------------------
# INIT SCORE STORAGE
# --------------------------------------------------
def init_scoring():
    if "total_points" not in st.session_state:
        st.session_state.total_points = 0


# --------------------------------------------------
# ADD SCORE
# --------------------------------------------------
def add_score(points):
    init_scoring()
    st.session_state.total_points += points


# --------------------------------------------------
# GET TOTAL
# --------------------------------------------------
def get_score():
    init_scoring()
    return st.session_state.total_points


# --------------------------------------------------
# LEVEL CALCULATION BASED ON POINTS
# --------------------------------------------------
def get_level_from_points():
    points = get_score()

    if points >= 200:
        return "Expert"
    elif points >= 100:
        return "Advanced"
    elif points >= 50:
        return "Intermediate"
    else:
        return "Beginner"


# --------------------------------------------------
# PROGRESS TOWARD NEXT LEVEL
# --------------------------------------------------
def get_progress():
    points = get_score()

    if points < 50:
        return points / 50
    elif points < 100:
        return (points - 50) / 50
    elif points < 200:
        return (points - 100) / 100
    else:
        return 1.0


# --------------------------------------------------
# SHOW SCORE PANEL
# --------------------------------------------------
def scoring_ui():
    init_scoring()

    st.subheader("📈 Progress")

    st.metric("⭐ Total Points", get_score())
    st.write("Level:", get_level_from_points())
    st.progress(get_progress())
