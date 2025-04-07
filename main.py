import plotly.graph_objects as go
from datetime import datetime, timedelta
import pandas as pd
import streamlit as st
import yfinance as yf
from price_trends import get_btc_trend, get_wif_trend, get_bnb_trend, get_eth_trend
from fetch_data import fetch_data

data = fetch_data()
fig = get_btc_trend(data)
wif = get_wif_trend(data)
bnb = get_bnb_trend(data)
eth = get_eth_trend(data)
# Streamlit
st.write("""BTC-USD Close Price Trend""")
st.plotly_chart(fig, theme='streamlit', use_container_width=True)  # Set to True
st.write("""WIF-USD Close Price Trend""")
st.plotly_chart(wif, theme='streamlit', use_container_width=True)
st.write("""BNB-USD Close Price Trend""")
st.plotly_chart(bnb, theme='streamlit', use_container_width=True)
st.write("""ETH-USD Close Price Trend""")
st.plotly_chart(eth, theme='streamlit', use_container_width=True)