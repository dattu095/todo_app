import streamlit as st


def col_priority(index, task):
    priority = task.priority.upper()

    priority_color = {"LOW": "green", "MODERATE": "orange", "HIGH": "red"}

    st.markdown(
        f"""
            <span style='color:{priority_color[priority]}; font-weight:bold;'>
                {priority}
            </span>
        """,
        unsafe_allow_html=True,
    )
