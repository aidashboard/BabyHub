import streamlit as st
import graphviz as graphviz

def run_app_upload():
    st.title('GraphViz uses the DOT language')

    # Create a graphlib graph object
    st.graphviz_chart('''
        digraph {
            "Training Data" -> "ML Algorithm"
            "ML Algorithm" -> "Model"
            "Model" -> "Result Forecasting"
            "New Data" -> "Model"
        }
    ''')
       