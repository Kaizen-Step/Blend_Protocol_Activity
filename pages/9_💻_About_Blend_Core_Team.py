# Libraries
import streamlit as st
from PIL import Image

# Layout
st.set_page_config(page_title='Blend Protocol On-Chain Activity',
                   page_icon=':bar_chart:📈', layout='wide')
st.title(' About Blend Core Team 📑 ')


c1, c2 = st.columns(2)


with c1:
    st.info(""" 
    Built in collaboration with 
    Dan Robinson  [[Linkedin]](https://www.linkedin.com/checkpoint/challenge/AgFYDcoznEV-qAAAAYgB0mcwhiZV55EJErDjRnS0-fEcVHwtWEbbdWm17cpK3zoha30Blgt5_AlBHKYTWy446LueiV2EtQ?ut=18WDtNqIcybqM1)  [[Twitter]](https://twitter.com/danrobinson)
    is one of the inventors of Uniswap V3, the leading DEX for fungible tokens. Dan Robinson is a General Partner and the Head of Research at Paradigm, focused on crypto investments and research into open-source protocols.    
    Previously, Dan was a protocol researcher at Interstellar. Before Interstellar, Dan practiced as a litigation attorney at Paul, Weiss, Rifkind, Wharton & Garrison LLP. He earned a J.D. from Harvard Law School and an A.B. from Harvard University.    
    Dan two recent writing which one of them become the whitepaper of Blend portocol:
    * [Blend: Perpetual Lending With NFT Collateral](https://www.paradigm.xyz/2023/05/blend)  ,     [Base Layer Neutrality](https://www.paradigm.xyz/2022/09/base-layer-neutrality) 
    
    Dan Robinson was envolved in a lot of project recently  Amber (Crypto finance firm) ,Blowfish (Blowfish makes it easy to identify & stop fraud before it happens) are among them, you can see the rest at [Portfolio](https://www.paradigm.xyz/portfolio).   
    @transmissions11 [[Twitter]](https://twitter.com/transmissions11) is a researcher at Paradigm and a top contributor to Seaport. He made great contributions to the gas optimizations of Blend.


    """)


with c2:
    st.image(Image.open('Images/Dan.jpg'))


c1, c2 = st.columns(2)


with c1:
    st.image(Image.open('Images/para3.png'))


with c2:

    st.info("""    ##### Paradigm
    Paradigm is a research-driven technology investment firm invest in, build, and contribute to companies and protocols they often get involved at the earliest stages and continue to support portfolio companies over time. they take hands-on approach to help projects reach their full potential, from the technical (mechanism design, security, engineering) to the operational (recruiting, go-to-market, legal and regulatory strategy).     
    The crypto investment firm Paradigm disclosed that its assets under management have ballooned to \$13.2 billion.   
    That’s up 343% from /$2.98 billion in Paradigm’s financial filing from December 2020.     
    Traditionally, the value of venture capital firms’ holdings have been kept secret and are not subject to financial disclosures.    
    But in a recent shift, venture capital firms — eager to invest in crypto tokens and other assets — have begun to file as registered investment advisors. To maintain that designation, firms are required to reveal the total amount of assets under management across their holdings. """)
