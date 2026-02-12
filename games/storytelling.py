import streamlit as st
from modules.scoring import add_score


# --------------------------------------------------
# SAMPLE STORY BANK
# --------------------------------------------------
STORIES = {
    "The Talking Tree": 
    "One day, a little child met a tree who could talk. "
    "The tree said, 'Save water and protect nature, and I will give you fresh air forever.' "
    "The child promised to care for the Earth.",

    "Captain Recycle":
    "Captain Recycle traveled across cities teaching people "
    "how to separate waste. Soon the streets became clean "
    "and everyone became eco heroes.",

    "The Last Drop":
    "A village almost ran out of water. A young girl taught "
    "everyone to save water. Together they protected every drop."
}


# --------------------------------------------------
# MAIN UI
# --------------------------------------------------
def storytelling_ui():
    st.subheader("📖 AI Eco Storytime")

    story_title = st.selectbox("Choose a story:", list(STORIES.keys()))

    if st.button("Tell me the story"):
        st.write("### ✨ कहानी / Story")
        st.info(STORIES[story_title])

        add_score(5)
        st.success("Great listening! +5 points 🌟")
