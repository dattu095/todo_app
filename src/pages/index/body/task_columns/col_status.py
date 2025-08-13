import streamlit as st


def col_status(index, task):
    if task.completed:
        st.markdown(
            "<span style='color:green; font-weight:bold;'>Completed</span>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            "<span style='color:red; font-weight:bold;'>Pending</span>",
            unsafe_allow_html=True
        )
