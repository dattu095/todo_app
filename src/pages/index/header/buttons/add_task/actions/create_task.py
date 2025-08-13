import streamlit as st

from utils.task import Task


def create_task(title, description, due_data, priority):
    new_task = Task(
        title=title,
        description=description,
        due_date=due_data,
        priority=priority
    )

    st.session_state.tasks.append(new_task)
