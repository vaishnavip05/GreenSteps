import streamlit as st


def section_header(title):
    st.markdown(f"## {title}")


def info_card(text):
    st.info(text)


def success_card(text):
    st.success(text)


def divider():
    st.divider()
