import streamlit as st

from .actions.create_dialog import new_task_form


def render_add_task():
    st.button("Add Task", icon=":material/add:", on_click=new_task_form)
