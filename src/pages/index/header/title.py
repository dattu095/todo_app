import streamlit as st


def render_title():
    with st.container(
        key="title",
        height="stretch",
    ):
        st.title("To Do List")
