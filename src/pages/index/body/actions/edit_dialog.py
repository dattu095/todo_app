import streamlit as st


@st.dialog(title="Edit Task")
def edit_task_form(task):
    with st.form("New Task"):
        title = st.text_input(label="Title", value=task.title)
        description = st.text_area(label="Description", value=task.description)
        due_date = st.date_input(
            label="Due Date", value=task.due_date, format="DD-MM-YYYY"
        )
        priority_level = st.select_slider(
            label="Priority Level",
            options=["Low", "Moderate", "High"],
            value=task.priority,
        )

        if st.form_submit_button(label="Edit Task"):
            task.title = title
            task.description = description
            task.due_date = due_date
            task.priority = priority_level

            st.rerun()
