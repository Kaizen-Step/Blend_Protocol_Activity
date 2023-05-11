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
st.set_page_config(page_title=' User Activity - Blend Protocol On-Chain Activity',
                   page_icon=':bar_chart:🔥', layout='wide')
st.title(' 🔥 User Activity')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Data Sources


# Data Sources
@st.cache_data()
def get_data(query):
    if query == 'Loan_offer':
        return pd.read_csv('Data/Old/Loan_Offer20.csv')
    elif query == 'Amount':
        return pd.read_csv('Data/Old/Loan_Offer22.csv')
    elif query == 'Lender':
        return pd.read_csv('Data/Old/Loan_Offer20.csv')
    elif query == 'Azuki':
        return pd.read_csv('Data/Collections/Azuki.csv')
    elif query == 'Degods':
        return pd.read_csv('Data/Collections/Degods.csv')
    elif query == 'Milady':
        return pd.read_csv('Data/Collections/Milady.csv')
    elif query == 'Wrapped_Cryptopunks':
        return pd.read_csv('Data/Collections/Wrapped_Cryptopunks.csv')
    elif query == 'Heat_Map':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/18e20510-9905-4a1f-84e6-28860a9a410b/data/latest')
    return None


Loan_offer = get_data('Loan_offer')
Amount = get_data('Amount')
Lender = get_data('Lender')
Azuki = get_data('Azuki')
Degods = get_data('Degods')
Milady = get_data('Milady')
Wrapped_Cryptopunks = get_data('Wrapped_Cryptopunks')
Heat_Map = get_data('Heat_Map')

df = Loan_offer
df1 = Amount
df11 = Lender
df22 = Heat_Map
# # df2 = df.groupby(['time', 'collection_address'])['evt_tx_hash'].count()
# df2 = df.groupby(['borrower', 'collection_address'])[
#     'loanAmount'].sort_values(ascending=False).reset_index()
# df2.columns = ['borrower', 'Loan_Amount_ETH']

df3 = df.groupby(['time', 'collection_address'])[
    'borrower'].nunique().reset_index()
df3.columns = ['date', 'collection_Name', 'Number_of_borrower']


df31 = df11.groupby(['time', 'collection_address'])[
    'lender'].nunique().reset_index()
df31.columns = ['date', 'collection_Name', 'Number_of_Lender']

#################################################################################################
st.write(""" ### Blend User Growth ##  """)

st.write("""
Blur is a blockchain-based platform for non-fungible tokens (NFTs) that allows users to mint, sell, and trade digital assets. One of the key challenges for any NFT platform is user growth, as the value of the platform depends heavily on the number of active users and the activity level of those users.
To address this challenge, Blur has developed a protocol called "Blend" that is designed to incentivize and reward users for contributing to the growth of the platform. The protocol works by rewarding users with tokens for actions such as referring new users, participating in platform activities, and engaging with other members of the community.
By incentivizing users to invite others and participate in platform activities, Blend User Growth aims to create a virtuous cycle of user engagement and growth, ultimately driving the long-term success of the platform. As more users join and engage with the platform, the value of the NFTs and the overall ecosystem is expected to increase, benefiting all participants.
  """)


st.info(""" ##### In This User Growth Section you can find: ####

* Outstanding Borrower & Incentivized Bidding Negative Impact 
* Lender Activity
* Distinct Active User Pattern After Blend Launched



""")


#################################################################################################

st.write(""" ## Outstanding Borrower & Incentivized Bidding Negative Impact 
""")

st.write(""" The number of unique users decreased, and many people who are enthusiastic about this are playing with The Lending on Blur. However, many others are saying, "I don't really understand what's going on there; I'm going to take a little while before I figure it out and get involved, and then eventually we'll probably get back involved," but I believe that this chart reflects this. The second thing to keep in mind while looking at these figures is that virtually every purchase made through Leverage on Blur comes from the same wallet, making it appear that the number of unique users is declining a little bit more than it actually is.     
I re-added those to the graph, but the number of unique users was still significantly lower. We seem to be in a slightly more bullish atmosphere. The guys that had the lending, you know, on their collections, azuki and punks, and who then boarded Apes in expectation were the ones who knew what was going on. Doodles and moon birds are both down at least seven percent. It was a little bit quieter on those projects because not many in the mid-cap index received incentive loans, and most of them saw incentive bidding decrease from 2x to 1x.
Incentivized bidding, which was expected to have a positive impact on prices, led to a negative impact over a three-month period. One of the main reasons was a shift in supply from long-term holders to flippers, who needed to get their money back quickly. This caused a perception of oversupply and kept real buyers away, leading to a decline in prices. Moreover, momentum assets like NFTs can experience a price drop when the ball starts rolling.  
""")
# Daily Numner of Distinct Borrower
fig = px.bar(df3, x='date', y="Number_of_borrower", color="collection_Name",
             title='Daily Numner of Distinct Borrower')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Distinct Number of Borrower')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

st.table(df1.head(10))


st.write(""" ## Active User Pattern After Blend Launched
""")

st.write(""" 
The complex process of airdrop farming and earning blur left many average users out of the market, as they saw some pump and dumps and could not understand what was going on. Therefore, they opted to wait for things to be over. This contributed to the negativity that followed.   
The question is whether the NFT market will experience a similar trend in the future, where prices will skyrocket and then plummet. There are some similarities and differences to consider.       
One similarity is the speculative nature of the market. People are buying NFTs not necessarily for their inherent value, but for the potential resale value. This can lead to a bubble that eventually bursts. Another similarity is the possibility of market manipulation. Just as some people were artificially inflating CryptoPunks prices, others could do the same with NFTs.     
On the other hand, there are also some differences to consider. One is the wider range of NFTs available. While CryptoPunks were limited to a specific set of characters, NFTs can represent anything from digital art to sports highlights. This could lead to a more diverse and stable market. Another difference is the increasing acceptance of NFTs by mainstream institutions. As more museums and galleries display NFT art, it may become more widely accepted as a legitimate form of art and investment.    
Only time will tell what the future holds for the NFT market, but it's important to be aware of both the similarities and differences to avoid being caught off guard by potential market fluctuations.   

""")

# Daily Numner of Distinct Borrower
fig = px.bar(df31, x='date', y="Number_of_Lender", color="collection_Name",
             title='Daily Numner of Distinct Lender')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Distinct Number of Borrower')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
###################################################################


c1, c2 = st.columns(2)

with c2:
    # User per minute on hour of day (UTC)
    fig = px.density_heatmap(df22, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="User per minute on hour of day (UTC)",
                             histfunc='avg', title="User per minute on hour of day (UTC)".title(), nbinsx=24)
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
        'dtick': 1}, coloraxis_colorbar=dict(title="User per minute on hour of day (UTC)"))
    fig.update_yaxes(categoryorder='array')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


with c1:

    # User per minute on hour of day (UTC)
    fig = px.density_heatmap(df22, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="transactions per minute on hour of day (UTC)",
                             histfunc='avg', title="Borrow Transaction per minute on hour of day (UTC)".title(), nbinsx=24)
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
        'dtick': 1}, coloraxis_colorbar=dict(title="Borrow Transaction per minute on hour of day (UTC)"))
    fig.update_yaxes(categoryorder='array')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


#####################################################
