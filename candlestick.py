# Create a function that returns a candlestick chart for any of the 30 crypto coins
import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import plotly.graph_objects as go
from plotly.offline import iplot

def fetch_all_data():
    # Fetch Data
    crypto_list = [
            'BTC-USD', 'ETH-USD', 'XRP-USD', 'LTC-USD', 'BCH-USD', 'ADA-USD', 'DOT-USD',
            'BNB-USD', 'LINK-USD', 'XLM-USD', 'DOGE-USD', 'UNI-USD', 'AAVE-USD', 'ATOM-USD',
            'AVAX-USD', 'PEPE24478-USD', 'SOL-USD', 'CHR-USD', 'ALGO-USD', 'FTT-USD', 'VET-USD',
            'USDT-USD', 'TRX-USD', 'ETC-USD', 'XMR-USD', 'EOS-USD', 'THETA-USD', 'NEO-USD',
            'DASH-USD', 'WIF-USD'
        ]
    def download_data(cryptos, duration):
        end_date = datetime.now()
        start_date = end_date - timedelta(days=int(duration-1))

        #initialize empty data frame
        data=pd.DataFrame()

        data = yf.download(cryptos, start=start_date, end=end_date)
        return data

    df = download_data(crypto_list, 365) 

    #Prepare dataset
    # 1. Flatten the MultiIndex columns
    df.columns = ['_'.join(col).strip() for col in df.columns.values]

    # 2. Reset index if date is part of the index and move it to a column
    if isinstance(df.index, pd.DatetimeIndex) or df.index.name == 'Date':
        df = df.reset_index()

    # 3. Convert 'Date' column to datetime if not already
    df['Date'] = pd.to_datetime(df['Date'])

    # 4. Sort by date if needed
    df = df.sort_values(by='Date')
    return df

#Define function for creating candlestick charts
def plot_candlestick(all_data_df: pd.DataFrame, symbol: str):
    fig = go.Figure(data=[go.Candlestick(
        x=all_data_df['Date'],
        open=all_data_df[f'Open_{symbol}'],
        high=all_data_df[f'High_{symbol}'],
        low=all_data_df[f'Low_{symbol}'],
        close=all_data_df[f'Close_{symbol}'],
        increasing_line_color='green',
        decreasing_line_color='red'
    )])
    fig.update_layout(
        xaxis_title='Date',
        yaxis_title='Price (USD)',
    )
    fig.update_layout(
        title=dict(
            text=f'{symbol} Candlestick Chart',
            font=dict(size=20, color='#222222'),
            x=0.5,
            y=0.95
        )
    )
    return fig
