import plotly.graph_objects as go
import plotly.express as px
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
from eda_charts import get_scatter, get_histogram, get_volume_chart, get_time_decomp
from correlation import get_corr_matrix, get_selected_corr, get_top_4_positive, get_top_4_negative, get_kmeans_tables



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

tab1, tab2, tab3, tab4 = st.tabs(["Live Prices","Exploratory Data Analysis","Clustering and Correlation", "Forecast"])

# ====================
#TAB 1: LIVE PRICES
# ====================

with tab1:
    st.header('Live Crypto Prices')

    # Display line chart based on selected coin
    selected_symbol = st.selectbox("Select a Cryptocurrency", crypto_list, key='price_chart_generator')
    fig_trend = get_price_trend(all_data_df, selected_symbol)
    st.plotly_chart(fig_trend, use_container_width=True, key='trend_lines')

    # Display candlestick chart based on selected coin
    st.subheader("Candlestick Chart")
    fig_candlestick = plot_candlestick(all_data_df, selected_symbol)
    st.plotly_chart(fig_candlestick, use_container_width=True, key='candlestick_chart')

    # Display data table for selected coin
    st.subheader("Data Table")
    
    symbol_columns = all_data_df.filter(like=selected_symbol)
    filtered_df = pd.concat([all_data_df['Date'], symbol_columns], axis=1)
    st.dataframe(filtered_df, height=400)

    # Display news articles
    articles = [
    {"title": "Bitcoin breaks through $95k amidst ongoing rally", "url": "https://crypto.news/bitcoin-breaks-through-95k-amidst-ongoing-rally/", "summary": "Bitcoin has surpassed the $95,000 as it continues to climb higher.", "date":"Published: April 30th, 2025 01:43 PM GMT+1"},
    {"title": "Ethereum price can crash to $1,000 in 2025: Polymarket", "url": "https://crypto.news/ethereum-price-can-crash-to-1000-in-2025-polymarket/", "summary": "Ethereum price has stalled below 2,000USD this week, and some signals indicate a potential drop to $1,000 before it reaches $4,000.","date":"Published April 29th, 2025 05:32 PM GMT+1"},
    {"title": "BNB Chain posts strong Q1 performance despite 15% market cap dip: Messari", "url": "https://crypto.news/bnb-chain-posts-strong-q1-performance-despite-15-market-cap-dip-messari/", "summary": "BNB Chain delivered a standout Q1 performance in revenue and on-chain metrics, even as its market cap dipped almost 15%.","date":"Published April 30th, 2025 at 09:56 AM GMT+1"}
]

    st.markdown("### Crypto News Highlights")

    for article in articles:
        st.markdown(f"**[{article['title']}]({article['url']})**")
        st.markdown(f"*{article['summary']}*\n")
        st.markdown(f"*{article['date']}*\n")



# ==================
# TAB 2: EDA
# ==================

with tab2:
    eda_list = [
        'Summary Statistics',
        'Close Price Histogram',
        'Correlation Scatter Plots',
        'Trading Volume Distribution',
        'Time Series Decomposition'
    ]
    st.header('Exploratory Data Analysis')

    eda_option = st.selectbox('Select an EDA option:',eda_list,key='eda_selection')

    if eda_option == 'Summary Statistics':
        st.subheader('Select a cryptocurrency to view its summary statistics')
        summary_crypto = st.selectbox('Choose a crypto', crypto_list, key='summary_selection')
        summary_features = [f'Close_{summary_crypto}', f'High_{summary_crypto}',f'Low_{summary_crypto}',f'Open_{summary_crypto}',f'Volume_{summary_crypto}']
        summary_df = all_data_df[summary_features].describe()
        st.dataframe(summary_df)

    elif eda_option == 'Close Price Histogram':
        st.subheader('Select a cryptocurrency to view its close price histogram')
        histogram_crypto = st.selectbox('Choose a crypto:', crypto_list, key='histogram_selection')
        histogram_fig = get_histogram(all_data_df, histogram_crypto)
        st.plotly_chart(histogram_fig, use_container_width=True, key='close_price_histogram')

    elif eda_option == 'Correlation Scatter Plots':
        st.subheader('Select two cryptocurrencies to view a scatter plot of their close prices:')
        crypto_1 = st.selectbox('Select first crypto:', crypto_list,key='crypto_selection_1')
        crypto_2 = st.selectbox('Select second crypto:', crypto_list,index=1, key='crypto_selection_2')
        scatter_fig = get_scatter(all_data_df, crypto_1, crypto_2)
        st.plotly_chart(scatter_fig, use_container_width=True, key='correlation_scatter_plot')

    elif eda_option == 'Trading Volume Distribution':
        st.subheader('Select a cryptocurrency to view its trading volume distribution over time')
        volume_crypto = st.selectbox('Choose a crypto:',crypto_list, key='volume_chart')
        volume_fig = get_volume_chart(all_data_df,volume_crypto)
        st.plotly_chart(volume_fig, use_container_width=True, key='volume_over_time')
    elif eda_option == 'Time Series Decomposition':
        st.subheader('Select a cryptocurrency to view its time series decomposition chart')
        time_decomp = st.selectbox('Choose crypto:', crypto_list,key='time_decomp_select')
        decomp_fig = get_time_decomp(all_data_df,time_decomp)
        st.pyplot(decomp_fig,use_container_width=True)



# ===================
# TAB 3: CLUSTERING AND CORRELATION
# ===================


with tab3:
    st.header('Results of K-Means Clustering and Correlation Analysis')
    # Display selectbox so user can see top 4 positive correlated coins to chosen coin
    st.text('Choose a cryptocurrency to see its top 4 positive correlated coins.')
    corr_crypto = st.selectbox('Choose crypto:',chosen_crypto_list, key='corr_tables')
    top_positive = get_top_4_positive(data,corr_crypto)
    st.dataframe(top_positive, width=300)
    # Display selectbox so user can see top 4 negative correlated coins to chosen coin
    st.text('Choose a cryptocurrency to see its top 4 negative correlated coins.')
    corr_crypto_neg = st.selectbox('Choose crypto:',chosen_crypto_list, key='corr_tables_negative')
    top_negative = get_top_4_negative(data, corr_crypto_neg)
    st.dataframe(top_negative, width=300)


    st.subheader('Correlation Matrix for all 30 Coins')
    corr_fig = get_corr_matrix(data)
    st.plotly_chart(corr_fig, use_container_width=True, key='corr_chart')
    
    # Unpack all kmeans results
    chosen_coins_df, all_clusters_df, clusters_fig = get_kmeans_tables(data)
    
    # Display k-means table with PCA results and cluster labels
    st.subheader('2D PCA and K-Means Clustering Result')
    st.dataframe(all_clusters_df)
    # Display selected coins from each cluster
    st.subheader('Randomly chosen coins from each cluster:')
    st.dataframe(chosen_coins_df)
    # Display plotly chart with clusters
    st.subheader('Clustered coins:')
    st.plotly_chart(clusters_fig, use_container_width=True, key='clusters_figure')



# ===================
# TAB 3: FORECAST
# ===================

with tab4:
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
        st.info("Forecast chart not available for this coin.")
