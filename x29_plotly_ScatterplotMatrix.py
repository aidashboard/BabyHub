import streamlit as st
import plotly.express as px


def convert_df(df):
       return df.to_csv(index=False).encode('utf-8')

def run_app_upload():
    #Read Avocado Dataset
    df = df = px.data.iris()
    csv = convert_df(df)

    st.download_button(
    "Download dataset",
    csv,
    "file.csv",
    "text/csv",
    key='download-csv'
    )

    st.header("Scatterplot Matrix")

    # Implementing Pie Plot
    fig = px.scatter_matrix(df)

    st.plotly_chart(fig)
#     st.write(df)

    fig2 = px.scatter_matrix(df,
    dimensions=["sepal_length", "sepal_width", "petal_length", "petal_width"],
    color="species")
    st.plotly_chart(fig2)
    st.write(df)
    
