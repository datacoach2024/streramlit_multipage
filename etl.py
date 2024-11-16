import duckdb
import pandas as pd



def load_tips_data():
    with duckdb.connect('my.db') as duck:
        tips = duck.query("select * from tips").to_df()
    
    return tips

