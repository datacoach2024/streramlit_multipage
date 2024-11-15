import plotly
import pandas as pd
import duckdb

tips = plotly.data.tips()

with duckdb.connect("my.db") as duck:
    try:
        duck.query("create table tips as select * from tips")
    except:
        print('unsuccessful')
