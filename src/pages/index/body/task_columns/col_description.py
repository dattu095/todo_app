import streamlit as st


def col_description(index, task):
    st.markdown(
        f"""
        <div style="
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            max-width: 100%;
        ">
            {task.description}
        </div>
        """,
        unsafe_allow_html=True
    )
