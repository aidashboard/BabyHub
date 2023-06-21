import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

fig = make_subplots(
    rows=2, cols=2,
    specs=[[{'type': 'volume'}, {'type': 'volume'}],
           [{'type': 'volume'}, {'type': 'volume'}]])


def convert_df(df):
       return df.to_csv(index=False).encode('utf-8')

def run_app_upload():
    #Read Avocado Dataset

    st.header("Opacity scale of volume plots")

    # Implementing Pie Plot
    X, Y, Z = np.mgrid[-8:8:30j, -8:8:30j, -8:8:30j]
    values =    np.sin(X*Y*Z) / (X*Y*Z)


    fig.add_trace(go.Volume(
        opacityscale="uniform",
        ), row=1, col=1)
    fig.add_trace(go.Volume(
        opacityscale="extremes",
        ), row=1, col=2)
    fig.add_trace(go.Volume(
        opacityscale="min",
        ), row=2, col=1)
    fig.add_trace(go.Volume(
        opacityscale="max",
        ), row=2, col=2)
    fig.update_traces(x=X.flatten(), y=Y.flatten(), z=Z.flatten(), value=values.flatten(),
        isomin=0.15, isomax=0.9, opacity=0.1, surface_count=15)
    
    st.plotly_chart(fig)
#     st.write(df)
    


    
