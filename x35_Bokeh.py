
import streamlit as st
import pandas as pd
from bokeh.plotting import figure


def run_app_upload():
	st.title('SF Trees')
	st.write('This app analyses trees in San Francisco using'
	' a dataset kindly provided by SF DPW')
	st.subheader('Bokeh Chart')


	trees_df = pd.read_csv('./files/trees.csv')
	scatterplot = figure(title = 'Bokeh Scatterplot')
	scatterplot.scatter(trees_df['dbh'], trees_df['site_order'])
	st.bokeh_chart(scatterplot)
	scatterplot.xaxis.axis_label = "dbh"
 
	scatterplot = figure(title = 'Bokeh Scatterplot')
	scatterplot.scatter(trees_df['dbh'], trees_df['site_order'])
	scatterplot.yaxis.axis_label = "site_order"
	scatterplot.xaxis.axis_label = "dbh"
	st.bokeh_chart(scatterplot)



