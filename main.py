import streamlit as st
import pandas as pd
import numpy as np




def main_page():
    from x01_bar_chart import run_app_upload
    run_app_upload()

def Line():
    from x02_line_chart import run_app_upload
    run_app_upload()


def Area():
    from x03_area_chart import run_app_upload
    run_app_upload()

def x04_maps():
    from x04_maps import run_app_upload
    run_app_upload()

def x05_graphviz_dot():
    from x05_graphviz_dot import run_app_upload
    run_app_upload()

def x06_graphviz():
    from x06_graphviz import run_app_upload
    run_app_upload()

def x07_seaborn_count():
    from x07_seaborn_count import run_app_upload
    run_app_upload()

def x08_seaborn_violin():
    from x08_seaborn_violin import run_app_upload
    run_app_upload()

def x09_seaborn_strip():
    from x09_seaborn_strip import run_app_upload
    run_app_upload()

def x10_altair_box():
    from x10_altair_box import run_app_upload
    run_app_upload()

def x11_altair_area():
    from x11_altair_area import run_app_upload
    run_app_upload()

def x12_altair_heatmap():
    from x12_altair_heatmap import run_app_upload
    run_app_upload()

def x13_plotly_pie():
    from x13_plotly_pie import run_app_upload
    run_app_upload()

def x14_plotly_donut():
    from x14_plotly_donut import run_app_upload
    run_app_upload()

def x15_plotly_scatter():
    from x15_plotly_scatter import run_app_upload
    run_app_upload()

def x16_plotly_line():
    from x16_plotly_line import run_app_upload
    run_app_upload()

def x17_plotly_bar():
    from x17_plotly_bar import run_app_upload
    run_app_upload()

def x18_plotly_bar_horizontal():
    from x18_plotly_bar_horizontal import run_app_upload
    run_app_upload()

def x19_plotly_subplots():
    from x19_plotly_subplots import run_app_upload
    run_app_upload()

def x20_plotly_sunburst():
    from x20_plotly_sunburst import run_app_upload
    run_app_upload()

def x21_plotly_mapoftree():
    from x21_plotly_mapoftree import run_app_upload
    run_app_upload()

def x22_plotly_choropleth():
    from x22_plotly_choropleth import run_app_upload
    run_app_upload()

def x23_plotly_2DHisstogram():
    from x23_plotly_2DHisstogram import run_app_upload
    run_app_upload()

def x24_plotly_3DConeVortex():
    from x24_plotly_3DConeVortex import run_app_upload
    run_app_upload()

def x25_plotly_3DPositionSegments():
    from x25_plotly_3DPositionSegments import run_app_upload
    run_app_upload()

def x26_plotly_3Dscaleofvolume():
    from x26_plotly_3Dscaleofvolume import run_app_upload
    run_app_upload()

def x27_plotly_3DSurfacePlotWithContours():
    from x27_plotly_3DSurfacePlotWithContours import run_app_upload
    run_app_upload()

def x28_plotly_indicators():
    from x28_plotly_indicators import run_app_upload
    run_app_upload()

def x29_plotly_ScatterplotMatrix():
    from x29_plotly_ScatterplotMatrix import run_app_upload
    run_app_upload()

def x30_plotly_DistributionPlots():
    from x30_plotly_DistributionPlots import run_app_upload
    run_app_upload()

def x31_plotly_DensityPlots():
    from x31_plotly_DensityPlots import run_app_upload
    run_app_upload()
def x32_Image_Classification():
    from x32_Image_Classification import run_app_upload
    run_app_upload()
    
def x33_Streamlit_sidebar():
    from x33_Streamlit_sidebar import run_app_upload
    run_app_upload()   
def x34_Altair():
    from x34_Altair import run_app_upload
    run_app_upload()   
    
def x35_Bokeh():
    from x35_Bokeh import run_app_upload
    run_app_upload() 
    
page_names_to_funcs = {
    "Bar": main_page,
    "Line": Line,
    "Area": Area,
    "Maps": x04_maps,
    "Graphviz dot": x05_graphviz_dot,
    "Graphviz": x06_graphviz,
    "Seaborn count": x07_seaborn_count,
    "Seaborn violin": x08_seaborn_violin,
    "Seaborn strip": x09_seaborn_strip,
    "Altair box": x10_altair_box,
    "Altair area": x11_altair_area,
    "Altair heatmap": x12_altair_heatmap,
    "Plotly pie": x13_plotly_pie,
    "Plotly donut": x14_plotly_donut,
    "Plotly scatter": x15_plotly_scatter,
    "Plotly line": x16_plotly_line,
    "Plotly bar": x17_plotly_bar,
    "Plotly bar horizontal": x18_plotly_bar_horizontal,
    "Plotly subplots": x19_plotly_subplots,
    "Plotly Sunburst": x20_plotly_sunburst,
    "Plotly Map of Tree": x21_plotly_mapoftree,
    "Plotly Choropleth": x22_plotly_choropleth,
    "Plotly 2DHisstogram": x23_plotly_2DHisstogram,
    "3D Cone Vortex": x24_plotly_3DConeVortex,
    "3D Position and Segments": x25_plotly_3DPositionSegments,
    "3D Opacity scale of volume plots": x26_plotly_3Dscaleofvolume,
    "3D Surface Plot With Contours": x27_plotly_3DSurfacePlotWithContours,
    "Plotly Indicators": x28_plotly_indicators,
    "Scatterplot Matrix": x29_plotly_ScatterplotMatrix,
    "Distribution Plots": x30_plotly_DistributionPlots,
    "Density Plots": x31_plotly_DensityPlots,
    "Image-Classification": x32_Image_Classification,
    "Streamlit sidebar": x33_Streamlit_sidebar,
    "Altair": x34_Altair,
    "Bokeh": x35_Bokeh,
    
    
 

}

# selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
# page_names_to_funcs[selected_page]()

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        (page_names_to_funcs.keys())
    )
page_names_to_funcs[add_radio]()