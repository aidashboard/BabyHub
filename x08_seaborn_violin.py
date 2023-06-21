# Import python libraries
import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

def convert_df(df):
       return df.to_csv(index=False).encode('utf-8')

def run_app_upload():
    

    st.title('Seaborn Violin')
    # Data Set
    df = pd.read_csv("./files/avocado.csv")

    # Defining Violin Graph
    fig = plt.figure(figsize=(10, 5))
    sns.violinplot(x = "year", y="AveragePrice", data = df)
    st.pyplot(fig)

    st.title('Violin Plot')
    
    df2 = px.data.tips()
    csv = convert_df(df2)

    st.download_button(
    "Download dataset",
    csv,
    "file.csv",
    "text/csv",
    key='download-csv'
    )


    fig = px.violin(df2, y="total_bill")
    st.plotly_chart(fig)

    fig2 = px.violin(df2, y="tip", x="smoker", color="sex", box=True, points="all",
          hover_data=df2.columns)
    
    st.plotly_chart(fig2)

    st.title('Multiple Traces')
    df3 = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/violin_data.csv")

    fig3 = go.Figure()

    days = ['Thur', 'Fri', 'Sat', 'Sun']

    for day in days:
        fig3.add_trace(go.Violin(x=df3['day'][df3['day'] == day],
                                y=df3['total_bill'][df3['day'] == day],
                                name=day,
                                box_visible=True,
                                meanline_visible=True))
    st.plotly_chart(fig3)




    st.header("Advanced Violin Plot")
    df4 = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/violin_data.csv")

    pointpos_male = [-0.9,-1.1,-0.6,-0.3]
    pointpos_female = [0.45,0.55,1,0.4]
    show_legend = [True,False,False,False]

    fig4 = go.Figure()

    for i in range(0,len(pd.unique(df4['day']))):
        fig4.add_trace(go.Violin(x=df4['day'][(df4['sex'] == 'Male') &
                                            (df4['day'] == pd.unique(df4['day'])[i])],
                                y=df4['total_bill'][(df4['sex'] == 'Male')&
                                                (df4['day'] == pd.unique(df4['day'])[i])],
                                legendgroup='M', scalegroup='M', name='M',
                                side='negative',
                                pointpos=pointpos_male[i], # where to position points
                                line_color='lightseagreen',
                                showlegend=show_legend[i])
                )
        fig4.add_trace(go.Violin(x=df4['day'][(df4['sex'] == 'Female') &
                                            (df4['day'] == pd.unique(df4['day'])[i])],
                                y=df4['total_bill'][(df4['sex'] == 'Female')&
                                                (df4['day'] == pd.unique(df4['day'])[i])],
                                legendgroup='F', scalegroup='F', name='F',
                                side='positive',
                                pointpos=pointpos_female[i],
                                line_color='mediumpurple',
                                showlegend=show_legend[i])
                )

    # update characteristics shared by all traces
    fig4.update_traces(meanline_visible=True,
                    points='all', # show all points
                    jitter=0.05,  # add some jitter on points for better visibility
                    scalemode='count') #scale violin plot area with total count
    fig4.update_layout(
        title_text="Total bill distribution<br><i>scaled by number of bills per gender",
        violingap=0, violingroupgap=0, violinmode='overlay')
    
    st.plotly_chart(fig4)


    from plotly.colors import n_colors
    import numpy as np

    np.random.seed(1)

    st.header("Ridgeline plot")

    # 12 sets of normal distributed random data, with increasing mean and standard deviation
    data = (np.linspace(1, 2, 12)[:, np.newaxis] * np.random.randn(12, 200) +
                (np.arange(12) + 2 * np.random.random(12))[:, np.newaxis])

    colors = n_colors('rgb(5, 200, 200)', 'rgb(200, 10, 10)', 12, colortype='rgb')

    fig5 = go.Figure()
    for data_line, color in zip(data, colors):
        fig5.add_trace(go.Violin(x=data_line, line_color=color))

    fig5.update_traces(orientation='h', side='positive', width=3, points=False)
    fig5.update_layout(xaxis_showgrid=False, xaxis_zeroline=False)

    st.plotly_chart(fig5)
    st.write(df)
    st.write(df3)

