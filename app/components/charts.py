import pandas as pd
import plotly.express as px
import streamlit as st

def show_asset_health_chart():
    data = pd.DataFrame({
        "Activo": ["M-101", "M-102", "P-201", "UPS-01", "TR-01"],
        "Salud": [92, 87, 74, 96, 81]
    })

    fig = px.bar(
        data,
        x="Activo",
        y="Salud",
        title="Índice de salud de activos",
        text="Salud"
    )

    fig.update_layout(yaxis_range=[0, 100])
    st.plotly_chart(fig, use_container_width=True)