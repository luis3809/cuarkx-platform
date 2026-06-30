import streamlit as st

def show_header():
    col1, col2 = st.columns([1, 4])

    with col1:
        st.image("assets/logo.png", width=180)

    with col2:
        st.title("CuarkX Platform")
        st.caption("Industrial AI | Predictive Maintenance | Observability | Edge AI")