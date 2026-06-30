import streamlit as st

def show_metrics():
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Activos monitoreados", "7")
    col2.metric("Alarmas activas", "3")
    col3.metric("Disponibilidad", "99.2 %")
    col4.metric("OT abiertas", "12")