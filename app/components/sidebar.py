import streamlit as st

def show_sidebar():
    st.sidebar.image("assets/logo.png", width=160)
    st.sidebar.markdown("### Estado de Integraciones")
    st.sidebar.success("SCADA: Simulado")
    st.sidebar.success("SAP PM: Simulado")
    st.sidebar.success("OPC UA: Preparado")
    st.sidebar.success("MCP: Roadmap")

    st.sidebar.markdown("---")
    st.sidebar.caption("CuarkX v0.1")