import streamlit as st
import plotly.express as px


def convert_df(df):
       return df.to_csv(index=False).encode('utf-8')

def run_app_upload():
    #Read Avocado Dataset
    df = df = px.data.tips()
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
    fig = px.ecdf(df, x="total_bill")

    st.plotly_chart(fig)
#     st.write(df)
    st.header("show multiple variables")
    fig2 = px.ecdf(df, x=["total_bill", "tip"])
    st.plotly_chart(fig2)
    

    st.header("Markers and/or Lines")
    fig3 = px.ecdf(df, x="total_bill", color="sex", markers=True, lines=False)
    st.plotly_chart(fig3)

    st.header("Marginal Plots")
    fig4 = px.ecdf(df, x="total_bill", color="sex", markers=True, lines=False, marginal="histogram")
    st.plotly_chart(fig4)

    st.header("Facets")
    fig5 = px.ecdf(df, x="total_bill", color="sex", facet_row="time", facet_col="day")
    st.plotly_chart(fig5)
    st.write(df)
    