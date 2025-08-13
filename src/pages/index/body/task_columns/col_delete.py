import streamlit as st


def col_delete(index, task):
    if st.button("", icon=":material/delete:", key=f"del_{index}"):
        st.session_state.tasks.pop(index - 1)
        st.rerun()
