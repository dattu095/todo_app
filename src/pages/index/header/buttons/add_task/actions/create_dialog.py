import streamlit as st

from .create_task import create_task


@st.dialog(title="Create New Task")
def new_task_form():
    with st.form("New Task"):
        title = st.text_input(label="Title", placeholder="Give task title")
        description = st.text_area(
            label="Description", placeholder="Give task description"
        )
        due_date = st.date_input(label="Due Date", format="DD-MM-YYYY")
        priority_level = st.select_slider(
            label="Priority Level", options=["Low", "Moderate", "High"]
        )

        if st.form_submit_button(label="Create Task"):
            create_task(
                title=title,
                description=description,
                due_data=due_date,
                priority=priority_level,
            )
            st.rerun()
