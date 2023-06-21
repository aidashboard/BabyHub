import streamlit as st
import pandas as pd
import numpy as np
def run_app_upload():
    st.title('Line')

    # Defining dataframe with its values 
    df = pd.DataFrame(
        np.random.randn(40, 4),
        columns=["C1", "C2", "C3", "C4"])

    # Bar Chart 
    st.line_chart(df)
    st.write(df)
