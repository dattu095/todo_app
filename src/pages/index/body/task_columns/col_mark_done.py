import streamlit as st


def col_mark_done(index, task):
    if not task.completed:
        if st.button("", icon=":material/check:", key=f"done_{index}"):
            task.markdone()
            st.rerun()
