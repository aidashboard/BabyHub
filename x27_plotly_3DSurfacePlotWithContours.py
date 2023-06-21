import streamlit as st
import plotly.graph_objects as go
import pandas as pd


def convert_df(df):
       return df.to_csv(index=False).encode('utf-8')

def run_app_upload():
    #Read Avocado Dataset
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')
    csv = convert_df(df)

    st.download_button(
    "Download dataset",
    csv,
    "file.csv",
    "text/csv",
    key='download-csv'
    )

    st.header("Surface Plot With Contours")

    # Implementing Pie Plot
    fig = go.Figure(data=[go.Surface(z=df.values)])
    fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                  highlightcolor="limegreen", project_z=True))

    fig.update_layout(title='Mt Bruno Elevation', autosize=False,
                    scene_camera_eye=dict(x=1.87, y=0.88, z=-0.64),
                    width=500, height=500,
                    margin=dict(l=65, r=50, b=65, t=90)
    )
    st.plotly_chart(fig)
#     st.write(df)
    


    
