import altair as alt
import streamlit as st
import pandas as pd

import plotly.graph_objects as go
import plotly.express as px


def run_app_upload():

    st.title('Altair Box')
    #Read albany Dataset
    df = pd.read_csv("./files/albany.csv")

    # Box Plot
    box_plot = alt.Chart(df).mark_boxplot().encode(
        x = "Date",
        y = "Large Bags"
    )

    st.altair_chart(box_plot)


    st.title('Grouped Horizontal Box Plot')
    
    y = ['day 1', 'day 1', 'day 1', 'day 1', 'day 1', 'day 1',
     'day 2', 'day 2', 'day 2', 'day 2', 'day 2', 'day 2']

    fig = go.Figure()
    fig.add_trace(go.Box(
        x=[0.2, 0.2, 0.6, 1.0, 0.5, 0.4, 0.2, 0.7, 0.9, 0.1, 0.5, 0.3],
        y=y,
        name='kale',
        marker_color='#3D9970'
    ))
    fig.add_trace(go.Box(
        x=[0.6, 0.7, 0.3, 0.6, 0.0, 0.5, 0.7, 0.9, 0.5, 0.8, 0.7, 0.2],
        y=y,
        name='radishes',
        marker_color='#FF4136'
    ))
    fig.add_trace(go.Box(
        x=[0.1, 0.3, 0.1, 0.9, 0.6, 0.6, 0.9, 1.0, 0.3, 0.6, 0.8, 0.5],
        y=y,
        name='carrots',
        marker_color='#FF851B'
    ))

    fig.update_layout(
        xaxis=dict(title='normalized moisture', zeroline=False),
        boxmode='group'
    )

    fig.update_traces(orientation='h') # horizontal box plots
    st.plotly_chart(fig)

    st.title('Box Plots')
    df = px.data.tips()

    fig1 = px.box(df, x="day", y="total_bill", color="smoker")
    fig1.update_traces(quartilemethod="exclusive") # or "inclusive", or "linear" by default
    st.plotly_chart(fig1)

    fig2 = px.box(df, x="time", y="total_bill", points="all")
    st.plotly_chart(fig2)

    fig3 = px.box(df, x="day", y="total_bill", color="smoker")
    fig3.update_traces(quartilemethod="exclusive") # or "inclusive", or "linear" by default
    st.plotly_chart(fig3)

    fig4 = px.box(df, x="time", y="total_bill", color="smoker",
             notched=True, # used notched shape
             title="Box plot of total bill",
             hover_data=["day"] # add day column to hover data
            )
    st.plotly_chart(fig4)
    st.write(df)