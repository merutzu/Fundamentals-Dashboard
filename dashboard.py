import streamlit as st
import requests
import config, json
import configuration
from iex import IEXStock
from datetime import datetime, timedelta


symbol = st.sidebar.text_input("Symbol", value="TSLA")

stock = IEXStock(configuration.IEX_API_TOKEN, symbol)

screen = st.sidebar.selectbox("view", ('Overview', 'Fundamentals', 'News', 'Daily Quote'))

st.title(screen)


if screen == 'Overview':
    logo = stock.get_logo()
    company_info = stock.get_company_info()
    
    col1, col2 = st.columns([1, 4])
    
    with col1:
        st.image(logo['url'])
         
    with col2:
        st.subheader(company_info['companyName'])
        st.subheader('Description')
        st.write(company_info['description'])
        st.subheader('Industry')
        st.write(company_info['industry'])
        st.header('CEO')
        st.write(company_info['CEO'])
        

if screen == 'Fundamentals':
    logo = stock.get_logo()
    st.image(logo['url'])
    
    
    stats = stock.get_stats()
    
    #st.header('Ratios')
    
    col1, col2 = st.columns(2)
    #st.write(stats)   
    with col2:
        st.subheader('Market Cap')
        st.write(stats['marketcap'])
        st.subheader('P/E')
        st.write(stats['peRatio'])
        st.subheader('Beta')
        st.write(stats['beta'])        
        st.subheader('YTD change %')
        st.write(stats['ytdChangePercent'])
        st.subheader('Max change %')
        st.write(stats['maxChangePercent'])
        st.subheader('Week 52 High Split Adjust Only')
        st.write(stats['week52highSplitAdjustOnly'])
        st.subheader('Week 52 Low Split Adjust Only')
        st.write(stats['week52lowSplitAdjustOnly'])
        
        
        
    with col1:        
        st.subheader('Company')
        st.write(stats['companyName'])
        st.subheader('Employees')
        st.write(stats['employees'])
        #st.header("Dividends") 
        st.subheader('Dividend Yield')
        st.write(stats['dividendYield'])
        st.subheader('Next Dividend Date')
        st.write(stats['nextDividendDate'])
        st.subheader('Ex Divided Date')
        st.write(stats['exDividendDate'])
        st.subheader('Next Earnings Date')
        st.write(stats['nextEarningsDate'])
        st.subheader('SharesOutstanding')
        st.write(stats['sharesOutstanding'])
        st.subheader('TTMEPS')
        st.write(stats['ttmEPS'])

        
        
        
    
     
        
        
        
if screen == 'News':
    news = stock.get_company_news()
    
    
    for article in news:
        st.subheader(article['headline'])
        dt = datetime.utcfromtimestamp(article['datetime']/1000).isoformat()
        st.write(f"Posted by {article['source']} at {dt}")
        st.write(article['url'])
        st.write(article['summary'])
        st.image(article['image'])

        
if screen == 'Daily Quote':
    st.subheader("Latest Updates")
    institutional_ownership = stock.get_institutional_ownership()
    inst = institutional_ownership
    
    col1, col2 = st.columns(2)
    
          
    with col1:
        st.subheader('Company')
        st.write(inst['companyName'])
        st.subheader('Ticker Symbol')
        st.write(inst['symbol'])     
        st.subheader('Primary Exchange')
        st.write(inst['primaryExchange'])
        st.subheader('Currency')
        st.write(inst['currency'])
        st.subheader('Calculation Price')
        st.write(inst['calculationPrice'])
        st.subheader('Latest Time')
        st.write(inst['latestTime'])
        st.subheader('High Source')
        st.write(inst['highSource'])
        st.subheader('Low Source')
        st.write(inst['lowSource'])
        st.subheader('Open Source')
        st.write(inst['openSource'])
        st.subheader('Close Source')
        st.write(inst['closeSource'])
        
        
    with col2:
        st.subheader('Open')
        st.write(inst['open'])
        st.subheader('Open Time')
        st.write(inst['openTime'])        
        st.subheader('High')
        st.write(inst['high'])
        st.subheader('High Time')
        st.write(inst['highTime'])
        st.subheader('Low')
        st.write(inst['lowTime'])
        st.subheader('Latest Price')
        st.write(inst['latestPrice'])
        st.subheader('Latest Update')
        st.write(inst['latestUpdate'])
        st.subheader('Latest Volume')
        st.write(inst['latestVolume'])
        st.subheader('IEX Real Time Price')
        st.write(inst['iexRealtimePrice'])
        st.subheader('IEX Real Time Size')
        st.write(inst['iexRealtimeSize'])
        
        

    
       
      
    #st.write(inst)
    
#     for institution in institutional_ownership:
#         st.write(institution['date'])
#         st.write(institution['entityProperName'])
#         st.write(institution['reportedHolding'])
    
    
    
    

        

    
    
    
