import streamlit as st


# --------------------------------------------------
# SAMPLE QUESTIONS (temporary)
# later we will load from JSON
# --------------------------------------------------
QUESTION_BANK = {
    "kids": [
        "Do you switch off lights?",
        "Do you use a water bottle?",
    ],
    "youth": [
        "How do you usually travel?",
        "Do you avoid plastic?",
    ],
    "adults": [
        "Do you track electricity bills?",
        "Are you open to home upgrades?",
    ],
    "elders": [
        "Would you like to guide younger people?",
        "Do you practice reuse habits?",
    ],
}


# --------------------------------------------------
# MAIN FUNCTION
# --------------------------------------------------
def run_survey(age_group):
    st.subheader("📝 Quick Survey")

    questions = QUESTION_BANK.get(age_group, [])
    answers = {}

    for q in questions:
        answers[q] = st.radio(q, ["Yes", "Sometimes", "No"], key=q)

    if st.button("Submit Survey"):
        return answers

    return None
