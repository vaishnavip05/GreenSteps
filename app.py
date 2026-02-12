import streamlit as st

# modules
from modules.auth import login_page
from modules.survey_engine import run_survey
from modules.profile_engine import build_profile

# age dashboards
from age_groups.kids import kids_dashboard
from age_groups.youth import youth_dashboard
from age_groups.adults import adults_dashboard
from age_groups.elders import elders_dashboard


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(page_title="GreenSteps", layout="wide")


# --------------------------------------------------
# SESSION STATE INIT
# --------------------------------------------------
if "user" not in st.session_state:
    st.session_state.user = None

if "age_group" not in st.session_state:
    st.session_state.age_group = None

if "profile_built" not in st.session_state:
    st.session_state.profile_built = False


# --------------------------------------------------
# TITLE
# --------------------------------------------------
st.title("🌱 GreenSteps")
st.write("Small steps today. Greener planet tomorrow.")


# --------------------------------------------------
# LOGIN
# --------------------------------------------------
if not st.session_state.user:
    login_page()
    st.stop()


# --------------------------------------------------
# AGE SELECTION
# --------------------------------------------------
if not st.session_state.age_group:
    st.subheader("Select your age group")

    c1, c2, c3, c4 = st.columns(4)

    if c1.button("👶 5–12"):
        st.session_state.age_group = "kids"
        st.rerun()

    if c2.button("🎓 13–22"):
        st.session_state.age_group = "youth"
        st.rerun()

    if c3.button("👨‍💼 23–40"):
        st.session_state.age_group = "adults"
        st.rerun()

    if c4.button("👵 40+"):
        st.session_state.age_group = "elders"
        st.rerun()

    st.stop()


# --------------------------------------------------
# SURVEY
# --------------------------------------------------
if not st.session_state.profile_built:
    answers = run_survey(st.session_state.age_group)

    if answers:
        build_profile(answers)
        st.session_state.profile_built = True
        st.rerun()

    st.stop()


# --------------------------------------------------
# ROUTE TO DASHBOARD
# --------------------------------------------------
age = st.session_state.age_group

if age == "kids":
    kids_dashboard()

elif age == "youth":
    youth_dashboard()

elif age == "adults":
    adults_dashboard()

elif age == "elders":
    elders_dashboard()
