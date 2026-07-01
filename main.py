import streamlit as st

from app.components.header import show_header
from app.components.sidebar import show_sidebar
from app.components.metrics import show_metrics
from app.components.charts import show_asset_health_chart

st.set_page_config(
    page_title="CuarkX Platform",
    page_icon="assets/favicon.png",   # <-- Nuevo favicon
    layout="wide",
    initial_sidebar_state="expanded"
)

show_sidebar()
show_header()

st.divider()

show_metrics()

st.divider()

show_asset_health_chart()