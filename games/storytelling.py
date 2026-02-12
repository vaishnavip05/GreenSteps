import streamlit as st
from modules.scoring import add_score
from gtts import gTTS
import tempfile


# --------------------------------------------------
# SAMPLE STORY BANK
# --------------------------------------------------
STORIES = {
    "The Talking Tree":
    "One day, a little child met a tree who could talk. "
    "The tree said, save water and protect nature, "
    "and I will give you fresh air forever.",

    "Captain Recycle":
    "Captain Recycle traveled across cities teaching people "
    "how to separate waste. Soon the streets became clean.",

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
        text = STORIES[story_title]

        # show text
        st.write("Story")
        st.info(text)

        # ---------------- TEXT TO SPEECH ----------------
        tts = gTTS(text)
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        tts.save(temp_file.name)

        # play audio
        st.audio(temp_file.name, format="audio/mp3")

        add_score(5)
        st.success("Great listening! +5 points 🌟")
