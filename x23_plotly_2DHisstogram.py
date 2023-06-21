import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

def convert_df(df):
       return df.to_csv(index=False).encode('utf-8')

def run_app_upload():
    #Read Avocado Dataset
    df = px.data.tips()
    csv = convert_df(df)

    st.download_button(
    "Download dataset",
    csv,
    "file.csv",
    "text/csv",
    key='download-csv'
    )

    st.header("2D Hisstogram")

    # Implementing Pie Plot
    fig = px.density_heatmap(df, x="total_bill", y="tip", marginal_x="histogram", marginal_y="histogram")

    st.plotly_chart(fig)
#     st.write(df)
    st.write(df)
    


    
