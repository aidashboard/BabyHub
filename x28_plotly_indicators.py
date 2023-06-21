import streamlit as st
import plotly.graph_objects as go
import pandas as pd


def convert_df(df):
       return df.to_csv(index=False).encode('utf-8')

def run_app_upload():
    #Read Avocado Dataset

    st.header("Indicators")
    fig = go.Figure()

    fig.add_trace(go.Indicator(
        value = 200,
        delta = {'reference': 160},
        gauge = {
            'axis': {'visible': False}},
        domain = {'row': 0, 'column': 0}))

    fig.add_trace(go.Indicator(
        value = 120,
        gauge = {
            'shape': "bullet",
            'axis' : {'visible': False}},
        domain = {'x': [0.05, 0.5], 'y': [0.15, 0.35]}))

    fig.add_trace(go.Indicator(
        mode = "number+delta",
        value = 300,
        domain = {'row': 0, 'column': 1}))

    fig.add_trace(go.Indicator(
        mode = "delta",
        value = 40,
        domain = {'row': 1, 'column': 1}))
    
    

    fig.update_layout(
        grid = {'rows': 2, 'columns': 2, 'pattern': "independent"},
        template = {'data' : {'indicator': [{
            'title': {'text': "Speed"},
            'mode' : "number+delta+gauge",
            'delta' : {'reference': 90}}]
                            }})
    
    st.plotly_chart(fig)

    fig2 = go.Figure(go.Indicator(
    mode = "number+delta",
    value = 492,
    delta = {"reference": 512, "valueformat": ".0f"},
    title = {"text": "Users online"},
    domain = {'y': [0, 1], 'x': [0.25, 0.75]}))

    fig2.add_trace(go.Scatter(
        y = [325, 324, 405, 400, 424, 404, 417, 432, 419, 394, 410, 426, 413, 419, 404, 408, 401, 377, 368, 361, 356, 359, 375, 397, 394, 418, 437, 450, 430, 442, 424, 443, 420, 418, 423, 423, 426, 440, 437, 436, 447, 460, 478, 472, 450, 456, 436, 418, 429, 412, 429, 442, 464, 447, 434, 457, 474, 480, 499, 497, 480, 502, 512, 492]))

    fig2.update_layout(xaxis = {'range': [0, 62]})
    st.plotly_chart(fig2)

    fig3 = go.Figure(go.Indicator(
    mode = "number+delta",
    value = 400,
    number = {'prefix': "$"},
    delta = {'position': "top", 'reference': 320},
    domain = {'x': [0, 1], 'y': [0, 1]}))

    fig3.update_layout(paper_bgcolor = "lightgray")

    st.plotly_chart(fig3)

    fig4 = go.Figure()

    fig4.add_trace(go.Indicator(
        mode = "number+delta",
        value = 200,
        domain = {'x': [0, 0.5], 'y': [0, 0.5]},
        delta = {'reference': 400, 'relative': True, 'position' : "top"}))

    fig4.add_trace(go.Indicator(
        mode = "number+delta",
        value = 350,
        delta = {'reference': 400, 'relative': True},
        domain = {'x': [0, 0.5], 'y': [0.5, 1]}))

    fig4.add_trace(go.Indicator(
        mode = "number+delta",
        value = 450,
        title = {"text": "Accounts<br><span style='font-size:0.8em;color:gray'>Subtitle</span><br><span style='font-size:0.8em;color:gray'>Subsubtitle</span>"},
        delta = {'reference': 400, 'relative': True},
        domain = {'x': [0.6, 1], 'y': [0, 1]}))

    st.plotly_chart(fig4)

#     st.write(df)
    


    
