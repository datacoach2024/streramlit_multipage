import pandas as pd
import plotly
import plotly.express as px
import streamlit as st

# st.title('Main page')
st.logo('static/logo.png')


pages = [
    st.Page('about.py', title = 'About'),
    st.Page('sales.py', title = 'Sales Report'),
    st.Page('customers.py', title = 'Customers Report'),
    st.Page('products.py', title = 'Products Report')
]

pg = st.navigation(pages)
pg.run()

