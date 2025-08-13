import streamlit as st

from ..actions.edit_dialog import edit_task_form


def col_edit(index, task):
    st.button(
        "",
        icon=":material/edit:",
        key=f"edit_{index}",
        on_click=edit_task_form,
        args=[task],
    )
