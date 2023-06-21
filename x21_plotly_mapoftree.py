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

    st.header("Treemap Chart")

    # Implementing Pie Plot
    fig = px.treemap(df, path=[px.Constant("world"), 'continent', 'country'], values='pop',
                  color='lifeExp', hover_data=['iso_alpha'],
                  color_continuous_scale='RdBu',
                  color_continuous_midpoint=np.average(df['lifeExp'], weights=df['pop']))
    fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))

    st.plotly_chart(fig)
    st.write(df)
#     st.write(df)
    


    
