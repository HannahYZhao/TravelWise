import streamlit as st
import plotly.graph_objects as go 

st.title("Wanderlust")

left_col, right_col = st.columns(2)

with left_col:
    st.subheader("Conversation")

with right_col:
    fig = go.Figure(go.Scattermapbox())
    fig.update_layout(
        mapbox=dict(
            accesstoken="pk.eyJ1IjoiaGFubmFoeXpoYW8iLCJhIjoiY2xwYzNvbHQyMGs4eTJrcW93MGdzajNhNCJ9.yrC6qNXzb0MdYB_y7UqTow",  # Replace with your Mapbox access token
            center=go.layout.mapbox.Center(
                lat=45,
                lon=-73
            ),
        ),
        margin=dict(l=0, r=0, t=0, b=0),
    )
    st.plotly_chart(fig)
