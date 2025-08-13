import streamlit as st

from .task_columns import (col_delete, col_description, col_due_date, col_edit,
                           col_index, col_mark_done, col_priority, col_status,
                           col_title)


def render_buttons(index, task):
    with st.container(
        horizontal=True,
        width="stretch",
        horizontal_alignment="right"
    ):
        col_mark_done(index, task)
        col_edit(index, task)
        col_delete(index, task)


def show_task(index, task):
    columns_config = [
        (0.7, col_index),
        (1.5, col_title),
        (4, col_description),
        (2.5, col_due_date),
        (1.5, col_priority),
        (1.5, col_status),
        (3.6, render_buttons),
    ]
    with st.container():
        widths, funcs = zip(*columns_config)
        cols = st.columns(widths)

        for col, func in zip(cols, funcs):
            with col:
                func(index, task)


def render_tasks_header():
    header_config = [
        (0.7, "Sl_no."),
        (1.5, "Title"),
        (4, "Description"),
        (2.5, "Due"),
        (1.5, "Priority"),
        (1.5, "Status"),
        (3.6, ""),
    ]

    with st.container():
        widths, headers = zip(*header_config)
        cols = st.columns(widths)

        for col, header in zip(cols, headers):
            with col:
                st.markdown(
                    f"<span style='font-weight:bold;'>{header}</span>",
                    unsafe_allow_html=True,
                )


def render_tasks():
    tasks = st.session_state.tasks
    if tasks == []:
        st.write("No Available Tasks")
        return

    for i, task in enumerate(tasks):
        show_task(i + 1, task)
