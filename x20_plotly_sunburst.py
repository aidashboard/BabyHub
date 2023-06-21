import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

def convert_df(df):
       return df.to_csv(index=False).encode('utf-8')

def run_app_upload():
    #Read Avocado Dataset
    df = px.data.gapminder().query("year == 2007")
    csv = convert_df(df)
    
    xx = pd.DataFrame(data=df)

    st.download_button(
    "Download dataset",
    csv,
    "file.csv",
    "text/csv",
    key='download-csv'
    )

    st.header("Sunburst Chart")

    # Implementing Pie Plot
    fig = px.sunburst(df, path=['continent', 'country'], values='pop',
                  color='lifeExp', hover_data=['iso_alpha'],
                  color_continuous_scale='RdBu',
                  color_continuous_midpoint=np.average(df['lifeExp'], weights=df['pop']))

    st.plotly_chart(fig)
    st.write(df)
    st.write(xx)
    


    




# import streamlit as st
# import pandas as pd

# data = px.data.gapminder().query("year == 2007")
# df = pd.DataFrame(data=data)
# st.write(df)