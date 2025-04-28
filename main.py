import plotly.graph_objects as go
from datetime import datetime, timedelta
import pandas as pd
import streamlit as st
import yfinance as yf
from price_trends import get_btc_trend, get_wif_trend, get_bnb_trend, get_eth_trend
from arima_prophet import get_btc_prophet
from fetch_data import fetch_data
#from arima_prophet import get_btc_prophet
import pandas as pd
from pycaret.time_series import *


data = fetch_data()


fig = get_btc_trend(data)
wif = get_wif_trend(data)
bnb = get_bnb_trend(data)
eth = get_eth_trend(data)
#t.write("""BTC-USD Prophet Forecast""")
#t.plotly_chart(pro, theme='streamlit', use_container_width=True)
#igf = get_btc_prophet(data)


# Read the HTML file for BTC Prophet Forecast
with open('forecast_chart.html', 'r', encoding='utf-8') as f:
    btc_html = f.read()
# Read the HTML file for BNB Prophet Forecast
with open('bnbforecast.html', 'r', encoding='utf-8') as f:
    bnb_html = f.read()

# Display it in Streamlit
st.components.v1.html(btc_html, height=500, scrolling=True)
# Display it in Streamlit
st.components.v1.html(bnb_html, height=500, scrolling=True)

# Streamlit
st.write("""BTC-USD Close Price Trend""")
st.plotly_chart(fig, theme='streamlit', use_container_width=True)  # Set to True
st.write("""WIF-USD Close Price Trend""")
st.plotly_chart(wif, theme='streamlit', use_container_width=True)
st.write("""BNB-USD Close Price Trend""")
st.plotly_chart(bnb, theme='streamlit', use_container_width=True)
st.write("""ETH-USD Close Price Trend""")
st.plotly_chart(eth, theme='streamlit', use_container_width=True)
#t.plotly_chart(figf, theme='streamlit', use_container_width=True)

#btc = data[['BTC-USD']]
# Set up PyCaret environment
#s = setup(data=btc, 
          #target = 'BTC-USD',
          #transform_target='log',
          #fh=30,  # Forecast horizon
          #session_id=123,
          #fold_strategy='expanding',
          #seasonal_period='D',
          #fold_spans="adaptive",
          #numeric_imputation_target = 'drift')
#prophet = create_model('prophet', verbose = False)
#arima = create_model('arima', verbose=False)
#tuned_prophet = tune_model(prophet)
#tuned_arima = tune_model(arima)
# Predictions
#final_prophet = finalize_model(tuned_prophet)
#prophet_predictions = predict_model(final_prophet)
#Plo prophet model forecast
#btc_prophet = plot_model(final_prophet, plot='forecast', display_format='streamlit')
#final_arima = finalize_model(tuned_arima)
#arima_predictions = predict_model(final_arima)
#Plot arima model forecast
#btc_arima =plot_model(final_arima, plot='forecast', display_format='streamlit')
#st.plotly_chart(btc_arima)