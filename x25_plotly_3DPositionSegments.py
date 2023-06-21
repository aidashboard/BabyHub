import streamlit as st
import plotly.graph_objects as go
import pandas as pd


def convert_df(df):
       return df.to_csv(index=False).encode('utf-8')

def run_app_upload():
    #Read Avocado Dataset
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/streamtube-wind.csv').drop(['Unnamed: 0'],axis=1)
    csv = convert_df(df)

    st.download_button(
    "Download dataset",
    csv,
    "file.csv",
    "text/csv",
    key='download-csv'
    )

    st.header("Position and Segments")

    # Implementing Pie Plot
    fig = go.Figure(data=go.Streamtube(
                    x = df['x'],
                    y = df['y'],
                    z = df['z'],
                    u = df['u'],
                    v = df['v'],
                    w = df['w'],
                    starts = dict(
                        x = [80] * 16,
                        y = [20,30,40,50] * 4,
                        z = [0,0,0,0,5,5,5,5,10,10,10,10,15,15,15,15]
                    ),
        sizeref = 0.3,
        colorscale = 'Portland',
        showscale = False,
        maxdisplayed = 3000
    ))
    fig.update_layout(
        scene = dict(
            aspectratio = dict(
                x = 2,
                y = 1,
                z = 0.3
            )
        ),
        margin = dict(
            t = 20,
            b = 20,
            l = 20,
            r = 20
        )
    )
    st.plotly_chart(fig)
    st.write(df)
    


    
