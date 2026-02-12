import streamlit as st


def build_profile(answers):
    """
    Convert survey answers into a simple user profile.
    Later we can make this smarter with AI logic.
    """

    # Save raw answers
    st.session_state.survey_answers = answers

    # ---------------- Score ----------------
    score = 0
    for ans in answers.values():
        if ans == "Yes":
            score += 2
        elif ans == "Sometimes":
            score += 1

    st.session_state.awareness_score = score

    # ---------------- Level ----------------
    total_questions = len(answers)

    if total_questions == 0:
        level = "Beginner"
    elif score >= total_questions * 1.5:
        level = "Advanced"
    elif score >= total_questions:
        level = "Intermediate"
    else:
        level = "Beginner"

    st.session_state.user_level = level
