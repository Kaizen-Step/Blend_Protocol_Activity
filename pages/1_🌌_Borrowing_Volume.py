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
st.set_page_config(page_title='Borrowing Volume - Blend Protocol On-Chain Activity',
                   page_icon=':bar_chart:💸', layout='wide')
st.title('💸 Borrowing Volume')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache_data()
def get_data(query):
    if query == 'Loan_offer':
        return pd.read_csv('Data/Old/Loan_Offer20.csv')
    elif query == 'Amount':
        return pd.read_csv('Data/Old/Loan_Offer20.csv')
    elif query == 'Azuki':
        return pd.read_csv('Data/Collections/Azuki.csv')
    elif query == 'Degods':
        return pd.read_csv('Data/Collections/Degods.csv')
    elif query == 'Milady':
        return pd.read_csv('Data/Collections/Milady.csv')
    elif query == 'Wrapped_Cryptopunks':
        return pd.read_csv('Data/Collections/Wrapped_Cryptopunks.csv')
    return None


Loan_offer = get_data('Loan_offer')
Amount = get_data('Amount')
Azuki = get_data('Azuki')
Degods = get_data('Degods')
Milady = get_data('Milady')
Wrapped_Cryptopunks = get_data('Wrapped_Cryptopunks')

############################
df = Loan_offer
df1 = Amount
# df2 = df.groupby(['time', 'collection_address'])['evt_tx_hash'].count()
df2 = df.groupby(['time', 'collection_address'])[
    'evt_tx_hash'].count().reset_index()
df2.columns = ['date', 'collection_Name', 'Number_of_transactions']

df3 = df1.groupby(['time', 'collection_address'])[
    'loanAmount'].count().reset_index()
df3.columns = ['date', 'collection_Name', 'Loan_Amount_ETH']
############################################
df11 = Azuki
df112 = df11.groupby(['time', 'collection_address'])[
    'evt_tx_hash'].count().reset_index()
df112.columns = ['date', 'collection_Name', 'Number_of_transactions']

df113 = df11.groupby(['time', 'collection_address'])[
    'loanAmount'].count().reset_index()
df113.columns = ['date', 'collection_Name', 'Loan_Amount_ETH']

##################################
df12 = Degods

df122 = df12.groupby(['time', 'collection_address'])[
    'evt_tx_hash'].count().reset_index()
df122.columns = ['date', 'collection_Name', 'Number_of_transactions']

df123 = df12.groupby(['time', 'collection_address'])[
    'loanAmount'].count().reset_index()
df123.columns = ['date', 'collection_Name', 'Loan_Amount_ETH']
########################################
df13 = Milady

df132 = df13.groupby(['time', 'collection_address'])[
    'evt_tx_hash'].count().reset_index()
df132.columns = ['date', 'collection_Name', 'Number_of_transactions']

df133 = df13.groupby(['time', 'collection_address'])[
    'loanAmount'].count().reset_index()
df133.columns = ['date', 'collection_Name', 'Loan_Amount_ETH']
###############################################
df14 = Wrapped_Cryptopunks

df142 = df14.groupby(['time', 'collection_address'])[
    'evt_tx_hash'].count().reset_index()
df142.columns = ['date', 'collection_Name', 'Number_of_transactions']

df143 = df14.groupby(['time', 'collection_address'])[
    'loanAmount'].count().reset_index()
df143.columns = ['date', 'collection_Name', 'Loan_Amount_ETH']
#################################################################################################
st.write(""" ### ETH Borrowing Volume ##  """)

st.write("""
If you're looking to buy non-fungible tokens (NFTs) on the Blur platform using Blend portocol, you may want to consider borrowing Ethereum (ETH) to do so. 
By borrowing ETH on Blur, you can get the funds you need to buy the NFTs you want without having to sell other cryptocurrencies or dip into your savings. Plus, borrowing ETH can be a more cost-effective way to access liquidity than selling other NFTs, especially if you believe that the value of those NFTs will appreciate over time.
To borrow ETH on Blur, you'll need to have some collateral to put up.    
Collateral is a NFT that you own that you pledge as security for the loan. In the case of borrowing ETH to buy NFTs. Once you've put up your collateral, you can borrow ETH at a competitive interest rate and use it to purchase NFTs on the Blur platform .You can then pay back the loan at your own pace, depending on the loan terms you choose. In this section we dipe dive on ETH volume borrow using Blend portocol on blur platform.

  """)


st.info(""" ##### In This User Growth Section you can find: ####

* Daily Number of BNPL (Borrowed) NFT on Blur Platform
* Volume of Borrowed Transactions  
* ETH Volume Borrowed In each NFT Collection




""")


#################################################################################################

st.write(""" ## Daily Number of BNPL (Borrowed) NFT on Blur Platform
""")

st.write(""" we believe the chart depicts the fact that while many people who are enthusiastic about this are jumping in and playing with The Lending on Blur, many others are saying, "I don't really know what's going on there; I'm going to take a little while before I figure it out and then get involved, and then eventually we'll probably get back involved." The second thing to keep in mind while looking at these figures is that virtually every purchase made through Leverage on Blur comes from the same wallet, Some Twitter users are saying that lending and NFTs are a bad combination. Still, we believe that the innovative lending solutions that companies like Blur are offering will drive the NFT market to new heights. 

""")
# Employment Rate In the Unite State Before and After War
fig = px.bar(df2, x='date', y="Number_of_transactions", color="collection_Name",
             title='Daily Numner of Borrowed Transactions')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Number of Transactions')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Employment Rate In the Unite State Before and After War
fig = px.area(df3, x='date', y="Loan_Amount_ETH", color="collection_Name",
              title='Daily Amont of Loan Borrowed [ETH]')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Loan Amount [ETH]')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

#####################################################
st.write(""" ## ETH Volume Borrowed In each NFT Collection
""")

st.write("""  The NFT market experienced a rapid rise in prices due to the new liquidity brought in by token buying, which allowed airdrop farmers to bid up NFT prices. However, this resulted in one of the sharpest downturns in NFT history, which lasted for three months.Incentivized bidding, which was expected to have a positive impact on prices, led to a negative impact over a three-month period. One of the main reasons was a shift in supply from long-term holders to flippers, who needed to get their money back quickly. This caused a perception of oversupply and kept real buyers away, leading to a decline in prices. Moreover, momentum assets like NFTs can experience a price drop when the ball starts rolling.In terms of notable sales, we saw a few demgods sales, but everything did less than 10 ETH. The volume of sales was relatively low. We also saw some wraped crypto prunck sell for 51 ETH, and Milady range for 6 ETH, and Azuki most expesive NFT sold for 16 ETH.

""")

st.text(" \n")
st.text(" \n")
c1, c2 = st.columns(2)

with c1:
    st.text(" \n")
    st.text(" \n")
    st.text(" \n")
    st.text(" \n")
    st.write(" ### Please Choose NFT Collection as collateral to better understand the impact of the protocol ")
    st.text(" \n")
    Collection = st.selectbox('NFT Collection', options=[
        'Azuki', 'Wrapped Cryptopunks', 'Degods', 'Milady'])

with c2:

    if Collection == 'Azuki':
        st.image(Image.open('Images/Azuki1.png'))

    elif Collection == 'Degods':
        st.image(Image.open('Images/Demigod3.jpg'))

    elif Collection == 'Milady':
        st.image(Image.open('Images/Milady2.jpg'))

    elif Collection == 'Wrapped Cryptopunks':
        st.image(Image.open('Images/cryptop22.jpg'))

##########################################################################


if Collection == 'Azuki':
    fig = px.bar(df112, x='date', y="Number_of_transactions", color="date",
                 title='Daily Numner of Borrowed Transactions')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Number of Transactions')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Employment Rate In the Unite State Before and After War
    fig = px.area(df113, x='date', y="Loan_Amount_ETH", color="collection_Name",
                  title='Daily Amont of Loan Borrowed [ETH]')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Loan Amount [ETH]')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

elif Collection == 'Degods':
    fig = px.bar(df122, x='date', y="Number_of_transactions", color="date",
                 title='Daily Numner of Borrowed Transactions')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Number of Transactions')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Employment Rate In the Unite State Before and After War
    fig = px.area(df123, x='date', y="Loan_Amount_ETH", color="collection_Name",
                  title='Daily Amont of Loan Borrowed [ETH]')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Loan Amount [ETH]')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
elif Collection == 'Milady':
    fig = px.bar(df132, x='date', y="Number_of_transactions", color="date",
                 title='Daily Numner of Borrowed Transactions')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Number of Transactions')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Employment Rate In the Unite State Before and After War
    fig = px.area(df133, x='date', y="Loan_Amount_ETH", color="collection_Name",
                  title='Daily Amont of Loan Borrowed [ETH]')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Loan Amount [ETH]')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
elif Collection == 'Wrapped Cryptopunks':
    fig = px.bar(df142, x='date', y="Number_of_transactions", color="date",
                 title='Daily Numner of Borrowed Transactions')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Number of Transactions')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Employment Rate In the Unite State Before and After War
    fig = px.area(df143, x='date', y="Loan_Amount_ETH", color="collection_Name",
                  title='Daily Amont of Loan Borrowed [ETH]')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Loan Amount [ETH]')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
