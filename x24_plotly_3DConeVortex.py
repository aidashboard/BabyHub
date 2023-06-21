import streamlit as st
import plotly.graph_objects as go
import pandas as pd


def convert_df(df):
       return df.to_csv(index=False).encode('utf-8')

def run_app_upload():
    #Read Avocado Dataset
    df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/vortex.csv")
    csv = convert_df(df)

    st.download_button(
    "Download dataset",
    csv,
    "file.csv",
    "text/csv",
    key='download-csv'
    )

    st.header("3D Cone Vortex")

    # Implementing Pie Plot
    fig = go.Figure(data = go.Cone(
                    x=df['x'],
                    y=df['y'],
                    z=df['z'],
                    u=df['u'],
                    v=df['v'],
                    w=df['w'],
                    colorscale='Blues',
                    sizemode="absolute",
                    sizeref=40))
    fig.update_layout(scene=dict(aspectratio=dict(x=1, y=1, z=0.8),
                             camera_eye=dict(x=1.2, y=1.2, z=0.6)))
    st.plotly_chart(fig)
    st.write(df)
    


    
