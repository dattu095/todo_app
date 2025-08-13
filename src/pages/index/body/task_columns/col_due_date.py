from datetime import date

import streamlit as st


def render_due_date(delta):
    if delta < 0:
        st.markdown(
            "<span style='color:red; font-weight:bold;'>Past Due</span>",
            unsafe_allow_html=True,
        )
    elif delta == 0:
        st.markdown(
            "<span style='color:orange; font-weight:bold;'>Due Today</span>",
            unsafe_allow_html=True,
        )
    elif delta < 31:
        st.markdown(
            f"<span style='color:green;'>{delta} days left</span>",
            unsafe_allow_html=True,
        )
    elif delta < 365:
        months = delta // 30
        st.markdown(
            f"<span style='color:green;'>{months} months left</span>",
            unsafe_allow_html=True,
        )
    else:
        years = delta // 365
        st.markdown(
            f"<span style='color:green;'>{years} years left</span>",
            unsafe_allow_html=True,
        )


def col_due_date(index, task):
    due = task.due_date

    today = date.today()
    delta = (due - today).days

    render_due_date(delta)
