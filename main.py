import plotly.graph_objects as go
from datetime import datetime, timedelta
import pandas as pd
import streamlit as st
import yfinance as yf
import pandas as pd


# import custom modules
from fetch_data import fetch_data
from candlestick import fetch_all_data, plot_candlestick
from price_trends import get_btc_trend, get_wif_trend, get_bnb_trend, get_eth_trend
from crypto_trends import get_price_trend


crypto_list = [
        'BTC-USD', 'ETH-USD', 'XRP-USD', 'LTC-USD', 'BCH-USD', 'ADA-USD', 'DOT-USD',
        'BNB-USD', 'LINK-USD', 'XLM-USD', 'DOGE-USD', 'UNI-USD', 'AAVE-USD', 'ATOM-USD',
        'AVAX-USD', 'PEPE24478-USD', 'SOL-USD', 'CHR-USD', 'ALGO-USD', 'FTT-USD', 'VET-USD',
        'USDT-USD', 'TRX-USD', 'ETC-USD', 'XMR-USD', 'EOS-USD', 'THETA-USD', 'NEO-USD',
        'DASH-USD', 'WIF-USD'
    ]

data = fetch_data()
all_data_df = fetch_all_data()

st.title('SoliGence Crypto Platform')

tab1, tab2 = st.tabs(["Live Prices","Forecast"])

# ====================
#TAB 1: LIVE PRICES
# ====================

with tab1:
    st.header('Live Crypto Prices')

    selected_symbol = st.selectbox("Select a Cryptocurrency", crypto_list, key='price_chart_generator')
    fig_trend = get_price_trend(all_data_df, selected_symbol)
    st.plotly_chart(fig_trend, use_container_width=True, key='trend_lines')
    st.subheader("Candlestick Chart")
    fig_candlestick = plot_candlestick(all_data_df, selected_symbol)
    st.plotly_chart(fig_candlestick, use_container_width=True, key='candlestick_chart')

# ===================
# TAB 2: FORECAST
# ===================

with tab2:
    selected_symbol = st.selectbox("Select a Cryptocurrency", crypto_list, key='forecast_selection')
    # Read the HTML file for BTC Prophet Forecast
    with open('forecast_chart.html', 'r', encoding='utf-8') as f:
        btc_html = f.read()
    # Read the HTML file for BNB Prophet Forecast
    with open('bnbforecast.html', 'r', encoding='utf-8') as f:
        bnb_html = f.read()
        # Read the HTML file for BNB Prophet Forecast
    with open('wif_forecast.html', 'r', encoding='utf-8') as f:
        wif_html = f.read()


    if selected_symbol == 'BTC-USD':
        # Display btc_forecast in Streamlit
        st.components.v1.html(btc_html, height=500, scrolling=True)
    elif selected_symbol == 'BNB-USD':
        # Display bnb forecast in Streamlit
        st.components.v1.html(bnb_html, height=500, scrolling=True)
    elif selected_symbol == 'WIF-USD':
        # Display wif forecast in Streamlit
        st.components.v1.html(wif_html, height=500, scrolling=True)
    else: 
        st.info("Price trend chart not available for this coin.")
