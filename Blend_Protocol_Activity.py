# Libraries
import streamlit as st
from PIL import Image

# Layout
st.set_page_config(page_title='Blend Protocol On-Chain Activity',
                   page_icon=':bar_chart:📈', layout='wide')
st.title(' Blend Protocol On-Chain Activity')
st.text(" \n")
# Content
c1, c2, c3 = st.columns(3)


with c1:
    st.text(" \n")
    st.text(" \n")
    st.image(Image.open('Images/blend7.jpg'))

with c2:
    st.text(" \n")
    st.text(" \n")
    st.image(Image.open('Images/blend3.png'))
with c3:
    st.text(" \n")
    st.text(" \n")
    st.image(Image.open('Images/blend7.jpg'))


st.write("""
### What Blur’s Blend Protocol Means for NFTs ###
nce again, the NFT marketplace and aggregator Blur has shaken up the NFT space. On May 1, the company announced the launch of Blend, a peer-to-peer lending protocol built alongside Web3 investment firm Paradigm. Blur claims the new protocol will help unlock liquidity for NFTs and help grow the market overall.
In the first 24 hours of its release, Blend became the number one lending protocol both by volume and users on the Ethereum blockchain.
Unsurprisingly, the launch has been met with praise, criticism, and everything in between. Blur is no stranger to controversy, but its latest move is its most contentious and influential to date. Here’s what you need to know about how Blend could affect the NFT ecosystem, what people are saying about it, and why it matters.     
Blend powers two new product offerings from Blur. The first allows people to use their NFTs as collateral to access ETH liquidity. The second is the buy-now-pay-later function, which lets users gain access to expensive blue-chip NFTs for a small down payment. Currently, Blur users can only use Blend on three NFT collections, including Azuki, CryptoPunks, and Milady Maker. However, the platform said it will add more collections in the near future.   
What sets Blend apart from other lending protocols like NFTfi is that Blend loans are set at fixed rates and have no expiration date, accruing interest until the loan is repaid. Blend automatically “rolls a borrowing position for as long as some lender is willing to lend that amount against the collateral,” and on-chain transactions are only required if someone decides to exit the position or if there is a change in interest rate.  
Borrowers can repay their loan at any time. If a borrower fails to pay the full amount at the expiration time, lenders can initiate a Dutch auction refinancing option (whenever they want). New lenders can then overtake the loan at an interest rate that appeals to them. If there are no interested bidders on the loan, the original lender then gets ownership of the collateralized NFT.  
And because Blur is offering rewards to users who offer loans, lenders are incentivized to offer favorable terms.[[1]](https://nftnow.com/features/what-blurs-blend-protocol-means-for-nfts/) """)

st.write(""" ### How do Blend Loans Work
Theoretically speaking, Blend loans are “fixed rate” and have “no expiry.” They are made on a peer-peer basis without the need for intermediary oracles to set collateralization ratios. Practically speaking, they are best classified as being “variable rate” and “variable expiry.” Lenders on Blend can, at any time, exit their leading positions by initiating a Dutch auction.   
Typical (competitive) auctions conclude when the highest bidder is discovered. In these auctions, bidding starts at a low price and remains open until the highest bidder is found.
Dutch auctions conclude when the first bidder is discovered. In these auctions, bidding typically starts at an unattractive price (in the instance of Blend, a low APY for lenders) and gradually moves to a more attractive price until the first bidder is found.
In the case of Blend, once a lender initiates an auction process, the borrower has 30 hours to repay all of the outstanding principal and interest on their loans.
If the borrower does not repay the loan within that given time, the loan goes off to auction, where another lender can step in and refinance the loan. The auction starts at a 0% APY and ends at a 1,000% APY. If the borrower cannot repay their loan and no new lender is willing to refinance it, the NFT collateral is transferred to the lender.
This auction mechanism is the key defining feature of Blend and creates unique opportunities for both borrowers and lenders.
[[2]](https://milkroad.com/news/blur-lending-blend  ) """)

c1, c2, c3 = st.columns(3)

with c1:
    st.image(Image.open('Images/blend8.jpg'))

with c2:
    st.image(Image.open('Images/blend5.jpeg'))

with c3:
    st.image(Image.open('Images/blend6.jpg'))

st.write("""
## Methodology ##   
We go in-depth on Blend protocol transactions in this dashboard.  we begin searching for Blend transactions using the contract address '0x29469395eaf6f95920e59f858042f0e28d98a20b' On the Flipside . This contract has 13 unique functions, and every one of them does certain tasks, some of which are not regarded as lending transactions. Due to the various structure of log saving, it is almost impossible to divide each function and combine the results in a single table.   
We discovered that there is unfortunately no decoded value for the LoanOfferTaken function in flipside tables by comparing the Etherscan result with flipside data, thus we went looking for a different data source. We discovered that the Blend transaction values are contained in a single table in Dune's 'blur_ethereum.Blend_evt_LoanOfferTaken'. We generated our queries using the Pandas tool after extracting the Dune source table. In the first component of this dashboard, we look into the ETH borrowed over the course of the last ten days starting on May 1 and attempt to divide the results by collections as requested in the chart description.      
The activity of lenders and borrowers as well as daily and hourly NFT borrowing patterns are examined in the second section. After that, we assess how Blend's introduction has affected other platforms and the NFT market as a whole.  
""")
st.warning(""" Due to Blur's official announcement of three available collections—Azuki, Milady, and Cryptopunk—there were five lending transactions on the first day Blend commenced trading NFT in the Boner collection. These 5 transactions were omitted from the data set and they were considered as system checks transactions.    """)


st.text(" \n")
st.write("""   
#### Sources ####  """)
st.write("""    1.https://nftnow.com/features/what-blurs-blend-protocol-means-for-nfts/     
                2.https://milkroad.com/news/blur-lending-blend   
        3.https://www.paradigm.xyz/2023/05/blend     
        4.[Image Source]https://twitter.com/blur_io
            """)


st.text(" \n")
c1, c2 = st.columns(2)
with c1:
    st.info(
        '**Twitter:  [Ludwig.1989](https://twitter.com/Ludwig_1989)**', icon="🕊️")
    st.info(
        '**Data Set (1):  [Dune-Blend LoanOfferTaken](https://dune.com/queries/2456014?category=decoded_project&namespace=blur&blockchains=ethereum&contract=Blend&abi=Seize)**', icon="🧠")

with c2:
    st.info(
        '**Project Github:  [Blend Portocol Activity](https://github.com/Kaizen-Step/NCAA_Basketball)**', icon="💻")
    st.info(
        '**Data Set (2):  [Flipside](https://barttorvik.com/trank.php#)**', icon="🧠")
