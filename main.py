import plotly.graph_objects as go
from datetime import datetime, timedelta
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
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
chosen_crypto_list = ['BTC-USD', 'ETH-USD', 'BNB-USD','WIF-USD']

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
    st.subheader("Data Table")
    # Display filtered table
    symbol_columns = all_data_df.filter(like=selected_symbol)
    filtered_df = pd.concat([all_data_df['Date'], symbol_columns], axis=1)
    st.dataframe(filtered_df, height=400)

# ===================
# TAB 2: FORECAST
# ===================

with tab2:
    selected_symbol = st.selectbox("Select a Cryptocurrency", chosen_crypto_list, key='forecast_selection')
    # Define options
    options = [30, 7, 1]

    # Create a slider with only those options
    selected_days = st.select_slider(
        'Select forecast duration (days):',
        options=options,
        value=30  # default selection
    )   
    # Read the HTML file for BNB Prophet Forecast
    with open('bnbforecast.html', 'r', encoding='utf-8') as f:
        bnb_html = f.read()
        # Read the HTML file for BNB Prophet Forecast
    with open('wif_forecast.html', 'r', encoding='utf-8') as f:
        wif_html = f.read()


    if selected_symbol == 'BTC-USD':
        # Map the selection to file names
        file_map = {
            1: "btc_LSTM_1.html",
            7: "btc_LSTM_7.html",
            30: "btc_LSTM_30.html"
        }
        # Load and display the corresponding HTML file
        html_file = file_map[selected_days]

        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        # Display BTC forecast with day range slider
        components.html(html_content, height=600, scrolling=True)  
        
    elif selected_symbol == 'BNB-USD':
        # Map the selection to file names
        file_map = {
            1: "BNB_EXP_1.html",
            7: "BNB_Prophet_7.html",
            30: "BNB_Prophet_30.html"
        }
        # Load and display the corresponding HTML file
        html_file = file_map[selected_days]

        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        # Display BTC forecast with day range slider
        components.html(html_content, height=600, scrolling=True) 
        # Display bnb forecast in Streamlit
        #st.components.v1.html(bnb_html, height=500, scrolling=True)
    elif selected_symbol == 'WIF-USD':
         # Map the selection to file names
        file_map = {
            1: "WIF_ARIMA_1.html",
            7: "WIF_ARIMA_7.html",
            30: "WIF_ARIMA_30.html"
        }
        # Load and display the corresponding HTML file
        html_file = file_map[selected_days]

        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        # Display BTC forecast with day range slider
        components.html(html_content, height=600, scrolling=True) 
        # Display wif forecast in Streamlit
        #st.components.v1.html(wif_html, height=500, scrolling=True)
    elif selected_symbol == 'ETH-USD':
        # Map the selection to file names
        file_map = {
            1: "ETH_EXP_1.html",
            7: "ETH_EXP_7.html",
            30: "ETH_EXP_30.html"
        }
        # Load and display the corresponding HTML file
        html_file = file_map[selected_days]

        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        # Display BTC forecast with day range slider
        components.html(html_content, height=600, scrolling=True) 
    else: 
        st.info("Price trend chart not available for this coin.")
