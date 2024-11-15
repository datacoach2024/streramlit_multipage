import streamlit as st
import backend
import plotly.express as px


st.title("Sales Report")

tips = backend.load_tips_data()

fig = px.scatter(
    data_frame = tips,
    x = 'tip',
    y = 'total_bill'
)

st.plotly_chart(fig)