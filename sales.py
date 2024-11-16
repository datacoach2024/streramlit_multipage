import streamlit as st
import etl
import plotly.express as px


st.title("Sales Report")

tips = etl.load_tips_data()

fig = px.scatter(
    data_frame = tips,
    x = 'tip',
    y = 'total_bill'
)

st.plotly_chart(fig)