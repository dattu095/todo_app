import streamlit as st

from .add_task.button import render_add_task


def render_buttons():
    buttons = [render_add_task]

    with st.container(
        key="header_buttons",
        height='stretch',
        horizontal=True,
        horizontal_alignment="right",
        vertical_alignment="bottom",
    ):
        for button in buttons:
            button()
