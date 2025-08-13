import streamlit as st


def col_title(index, task):
    st.markdown(
        f"<span style='font-weight:bold;'>{task.title}</span>",
        unsafe_allow_html=True
    )
