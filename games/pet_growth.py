import streamlit as st


# --------------------------------------------------
# INIT PET
# --------------------------------------------------
def init_pet():
    if "pet_level" not in st.session_state:
        st.session_state.pet_level = 1


# --------------------------------------------------
# LEVEL UP PET
# --------------------------------------------------
def grow_pet():
    st.session_state.pet_level += 1


# --------------------------------------------------
# PET STAGE TEXT
# --------------------------------------------------
def get_pet_stage(level):
    if level < 3:
        return "🥚 Egg"
    elif level < 6:
        return "🐣 Baby"
    elif level < 10:
        return "🐥 Growing"
    else:
        return "🦜 Eco Hero"


# --------------------------------------------------
# MAIN UI
# --------------------------------------------------
def pet_ui():
    init_pet()

    st.subheader("🐾 Your Eco Pet")

    level = st.session_state.pet_level
    stage = get_pet_stage(level)

    st.write(f"Stage: **{stage}**")
    st.write(f"Level: **{level}**")

    st.progress(min(level / 10, 1.0))

    if st.button("Feed Pet 🌱"):
        grow_pet()
        st.success("Your pet is happy and growing!")
        st.balloons()
        st.rerun()
