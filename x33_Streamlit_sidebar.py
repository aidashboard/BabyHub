
import streamlit as st
import pandas as pd

def run_app_upload():
	st.title('SF Trees')
	st.write('This app analyses trees in San Francisco using'
				' a dataset kindly provided by SF DPW. The '
					'histogram below is filtered by tree owner.')
	trees_df = pd.read_csv('./files/trees.csv')
	owners = st.sidebar.multiselect(
	'Tree Owner Filter', trees_df['caretaker'].unique())
	if owners:
		trees_df = trees_df[trees_df['caretaker'].isin(owners)]
		df_dbh_grouped = pd.DataFrame(trees_df.groupby(['dbh']).count()['tree_id'])
		df_dbh_grouped.columns = ['tree_count']
		st.line_chart(df_dbh_grouped)
  
	st.write(trees_df)
