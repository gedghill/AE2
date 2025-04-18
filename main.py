import plotly.graph_objects as go
from datetime import datetime, timedelta
import pandas as pd
import streamlit as st
import yfinance as yf
from price_trends import get_btc_trend
from fetch_data import fetch_data
data = fetch_data()
fig = get_btc_trend(data)
# Streamlit
st.write("""#BTC-USD Price Trend""")
st.plotly_chart(fig, theme='streamlit', use_container_width=True)  # Set to True