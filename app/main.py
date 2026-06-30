import streamlit as st

st.set_page_config(
    page_title="CuarkX Platform",
    page_icon="⚙️",
    layout="wide"
)

st.title("⚙️ CuarkX Platform")

st.subheader("Industrial AI | Predictive Maintenance | Observability")

st.markdown("---")

st.success("Proyecto inicial configurado correctamente.")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Activos monitoreados", "0")

with col2:
    st.metric("Alertas", "0")

with col3:
    st.metric("Estado", "Inicializando")

st.markdown("---")

st.write("Bienvenido a CuarkX.")