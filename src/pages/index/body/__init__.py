import streamlit as st

from .task_renderer import render_tasks, render_tasks_header


def render_body():
    if "tasks" not in st.session_state:
        st.session_state.tasks = []

    with st.container(border=False, key="tasks", height=600):
        render_tasks_header()
        st.divider()
        render_tasks()
