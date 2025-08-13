import streamlit as st

from .buttons import render_buttons
from .title import render_title


def render_header():
    st.set_page_config(page_title="To-Do", layout="wide")

    with st.container(key="header"):
        title_col, buttons_col = st.columns(2)

        with title_col:
            render_title()
        with buttons_col:
            render_buttons()


__all__ = [render_header]
