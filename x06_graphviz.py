import streamlit as st
import graphviz as graphviz

def run_app_upload():
    st.title('Graphviz')

    # Create a graphlib graph object
    graph = graphviz.Digraph()
    graph.edge('Training Data', 'ML Algorithm')
    graph.edge('ML Algorithm', 'Model')
    graph.edge('Model', 'Result Forecasting')
    graph.edge('New Data', 'Model')
    st.graphviz_chart(graph)
    st.text("# Create a graphlib graph object")
    st.text("graph = graphviz.Digraph()")
    st.text(" graph.edge('Training Data', 'ML Algorithm')")
    st.text("graph.edge('ML Algorithm', 'Model')")
    st.text(" graph.edge('Model', 'Result Forecasting')")
    st.text("graph.edge('New Data', 'Model')")
