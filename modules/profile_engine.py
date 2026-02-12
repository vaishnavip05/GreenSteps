import streamlit as st


def build_profile(answers):
    """
    Convert survey answers into a simple user profile.
    Later we can make this smarter with AI logic.
    """

    # Save raw answers
    st.session_state.survey_answers = answers

    # --------------------------------------------------
    # Basic awareness score (temporary logic)
    # --------------------------------------------------
    score = 0

    for ans in answers.values():
        if ans == "Yes":
            score += 2
        elif ans == "Sometimes":
            score += 1
        else:
            score += 0

    st.session_state.awareness_score = score

    # --------------------------------------------------
    # Simple level mapping
    # --------------------------------------------------
    if score >= len(answers) * 2 * 0.7:
        level = "Advanced"
    elif score >= len(answers):
        level = "Intermediate"
    else:
        level = "Beginner"

    st.session_state.user_level = level
