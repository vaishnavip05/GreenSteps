import streamlit as st
import random
from modules.scoring import add_score


# --------------------------------------------------
# TRASH ITEMS DATABASE
# --------------------------------------------------
TRASH_ITEMS = {
    "Plastic Bottle": "Plastic",
    "Newspaper": "Paper",
    "Banana Peel": "Organic",
    "Glass Jar": "Glass",
    "Cardboard Box": "Paper",
    "Food Waste": "Organic"
}

BINS = ["Plastic", "Paper", "Organic", "Glass"]


# --------------------------------------------------
# INIT GAME STATE
# --------------------------------------------------
def init_game():
    if "current_item" not in st.session_state:
        st.session_state.current_item = random.choice(list(TRASH_ITEMS.keys()))


# --------------------------------------------------
# NEW ITEM
# --------------------------------------------------
def next_item():
    st.session_state.current_item = random.choice(list(TRASH_ITEMS.keys()))


# --------------------------------------------------
# MAIN UI
# --------------------------------------------------
def trash_sorting_ui():
    init_game()

    st.subheader("♻ Trash Sorting Game")

    item = st.session_state.current_item
    correct_bin = TRASH_ITEMS[item]

    st.write(f"### 🗑 Where should this go?")
    st.info(item)

    choice = st.radio("Choose a bin:", BINS)

    if st.button("Submit Answer"):
        if choice == correct_bin:
            st.success("Correct! Great job 🌟")
            add_score(10)
            st.write("⭐ +10 points")
        else:
            st.error(f"Oops! It belongs in **{correct_bin}** bin.")

        next_item()
        st.rerun()
