# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from PIL import Image


# Global Variables
theme_plotly = None  # None or streamlit
week_days = ['Monday', 'Tuesday', 'Wednesday',
             'Thursday', 'Friday', 'Saturday', 'Sunday']

# Layout
st.set_page_config(page_title='Aknowledgement - Blend Protocol On-Chain Activity',
                   page_icon=':bar_chart:', layout='wide')
st.title('🪔 References')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# SQL Codes
st.write(""" ## Acknowledgement ## """)

st.write("""
We are grateful to all who helped us develop this project specially [**Mr. Ali Taslimi**](https://twitter.com/AliTslm) with comprehensive streamlit open source project [Cross chain Monitoring](https://github.com/alitslm/cross_chain_monitoring) that provides streamlit functions and tools.
And also ****Dune**** and  ****Flipside**** with massive database and last but not least ****MetricsDao**** that is the reason behind this project.


""")

st.text(" \n")
st.text(" \n")

# Sources
st.write(""" ## Sources ## """)

st.write("""
Here are the reference numbers for all of the sources used in this project:
  


""")

st.write("""
 1.https://nftnow.com/features/what-blurs-blend-protocol-means-for-nfts/     
                2.https://milkroad.com/news/blur-lending-blend   
        3.https://www.paradigm.xyz/2023/05/blend     
        4.[Image Source]https://twitter.com/blur_io   
        5.https://www.youtube.com/channel/UCOaX0Vu-dWB7bNjFMnbBo2A  
    

""")
