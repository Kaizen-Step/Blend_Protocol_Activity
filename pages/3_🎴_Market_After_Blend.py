# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from PIL import Image

# Theme
theme_plotly = None  # None or streamlit

# Layout
st.set_page_config(page_title='Collection After Blend - Blend Protocol On-Chain Activity',
                   page_icon=':bar_chart:📈', layout='wide')
st.title('🎴 NFT Market After Blend')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache_data()
def get_data(query):
    if query == 'Platforms_overall':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/a10804ce-3df0-4b42-8c9e-e7172cb981e5/data/latest')
    elif query == 'Platforms_Blur':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/722d1e1f-cfb9-4ddf-8a27-530f2df02dd3/data/latest')
    return None


Platforms_overall = get_data('Platforms_overall')
Platforms_Blur = get_data('Platforms_Blur')

df = Platforms_overall
df2 = Platforms_Blur


#################################################################################################
st.write(""" ### Blend Impact on NFT Market ##  """)

st.write("""
Blur is a cutting-edge platform that is having a significant impact on the rapidly growing NFT market. NFTs have become increasingly popular in recent years, particularly in the art world. Blur is a platform that allows artists and creators to mint, sell, and trade NFTs in a seamless and user-friendly way. In this part we'll concentrate on blur and Blend, a recently introduced loan approach impact on NFT makrket. 
""")


st.info(""" ##### In This Blend impact on NFT market Section you can find: ####

* Market Over view [2 Month Period]
* Blend Impact on Blur Platform  [2 Month Period]





""")


#################################################################################################

st.write(""" ## Market Over view  [2 Month Period]
""")

st.write(""" Let's start with a market overview. Market overview volumes are up just a small bit now that we can see Here is when we got incentivized. Bidding volumes went up something like 10 times, but we only saw a significant increase on May 1, and it's good to mention that the lending that went on to blur was only on three projects. If you look at the USD volume, you know the top three players were those three.
projects wrap crypto punks Azuki's Milady and then a couple other projects that people may be anticipating will get lending on Blur sooner than later, but market share largely with Blur went from about 70 to 75 percent.    

""")
# Employment Rate In the Unite State Before and After War
fig = px.bar(df, x="DATE", y="VOLUME_USD", color="PLATFORMS",
             title='Daily Numner of Active Users Before and After Shanghai Update')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Number of Users')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

#####################################################
# Employment Rate In the Unite State Before and After War
fig = px.bar(df, x="DATE", y="VOLUME_USD", color="STATUES",
             title='Daily Numner of Active Users Before and After Shanghai Update')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Number of Users')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


##########################################################################
st.write(""" ## Blend Impact on Blur Platform  [2 Month Period]
""")

st.write(""" 
Unique users were down, and a lot of people who are really excited about this are jumping in and playing with The Lending on Blur, but a lot of people are saying, I don't really know what's going on there; I'm going to take a little while before I figure it out and then get involved, and then eventually we'll probably get back involved," but I think that this chart reflects this. The other thing to know when we see these charts is that all the buys that happen from the Leverage wallet and basically every buy on Leverage on Blur is from the same wallet, so it may seem like unique users are down a little bit more than they are. I added those back onto this chart, and we still saw unique users down a fair bit. The large-cap index was up about 2.5 percent. Always pumped to get that move higher. It feels like we have a bit more of a bullish environment. In terms of what was up, it was the guys that had the lending, you know, on their collections, azuki and punks, and then boarded Apes in anticipation. Moon birds and doodles are both down seven or more percent. Not that many projects in the mid-cap index got incentivized lending, and we also saw incentivized bidding go from 2x to 1x on most of these projects, so it was a little bit quieter on those projects.

""")
# Employment Rate In the Unite State Before and After War
fig = px.area(df2, x="DATE", y="VOLUME_USD", color="PLATFORMS",
              title='Daily Numner of Active Users Before and After Shanghai Update')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Number of Users')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

#####################################################
# Employment Rate In the Unite State Before and After War
fig = px.line(df2, x="DATE", y="VOLUME_USD", color="STATUES",
              title='Daily Numner of Active Users Before and After Shanghai Update')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Number of Users')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
