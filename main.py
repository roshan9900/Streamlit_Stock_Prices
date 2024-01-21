import streamlit as st
import pandas as pd
import yfinance as yf
import warnings
import datetime
warnings.filterwarnings('ignore')

st.header('Stock Price App')

ticker_name = st.text_input('Enter any stock ticker', 'goog', key='placeholder')
stock_data = yf.Ticker(ticker_name)
col1, col2 = st.columns(2)
with col1:
    st.header('Enter a start date')
    start_date = st.date_input('Enter Start Date', datetime.date(2010, 1, 1))
with col2:
    st.header('Enter a end date')
    end_date = st.date_input('Enter End Date')

stock_data = stock_data.history(period='1d', start=start_date, end=end_date)
st.header(f'Stock Analysis Of {ticker_name}')
st.dataframe(stock_data)

# col3, col4  = st.columns(2)
# with col3:
st.header('Volume Chart')
st.line_chart(stock_data['Volume'])
# with col4:
st.header('Price Chart')
st.line_chart(stock_data['Close'])
st.header('High')
st.line_chart(stock_data['High'])