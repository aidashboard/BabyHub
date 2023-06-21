import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

def convert_df(df):
       return df.to_csv(index=False).encode('utf-8')

def run_app_upload():
    #Read Avocado Dataset
    df = px.data.gapminder().query("year == 2007")
    csv = convert_df(df)

    st.download_button(
    "Download dataset",
    csv,
    "file.csv",
    "text/csv",
    key='download-csv'
    )

    st.header("Choropleth Maps")

    # Implementing Pie Plot
    fig = px.choropleth(df, locations="iso_alpha",
                    color="lifeExp", # lifeExp is a column of gapminder
                    hover_name="country", # column to add to hover information
                    color_continuous_scale=px.colors.sequential.Plasma)

    st.plotly_chart(fig)
    st.write(df)
#     st.write(df)
    


    
