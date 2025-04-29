# Create a function that returns a price trend chart with moving averages for any of the 30 crypto coins
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import plotly.graph_objects as go
from plotly.offline import iplot
from candlestick import fetch_all_data


def get_price_trend(all_data_df: pd.DataFrame, symbol:str):
    # PLOT BNB TREND
    price_trend = go.Figure()
    # Compute moving averages
    all_data_df['MA_50'] = all_data_df[f'Close_{symbol}'].rolling(window=50, min_periods=1).mean()
    all_data_df['MA_200'] = all_data_df[f'Close_{symbol}'].rolling(window=200,min_periods=1).mean()

    price_trend.add_trace(go.Scatter(
        x=all_data_df['Date'],
        y=all_data_df[f'Close_{symbol}'],
        name=f'{symbol}',
        line=dict(color='#766CDB', width=2)
    ))
    # 50-day Moving Average
    price_trend.add_trace(go.Scatter(
        x=all_data_df['Date'],
        y=all_data_df['MA_50'],
        name='50-Day MA',
        line=dict(color='orange', width=2, dash='dash')
    ))

    # 200-day Moving Average
    price_trend.add_trace(go.Scatter(
        x=all_data_df['Date'],
        y=all_data_df['MA_200'],
        name='200-Day MA',
        line=dict(color='green', width=2, dash='dot')
    ))
    # Update layout
    price_trend.update_layout(
        title=dict(
            text=f'{symbol} Price Trend',
            font=dict(size=20, color='#222222'),
            x=0.5,
            y=0.95
        ),
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=3, label="3m", step="month", stepmode="backward"),
                    dict(count=6, label="6m", step="month", stepmode="backward"),
                    dict(count=12, label="1y", step="month", stepmode="backward")
                ])
            ),
            rangeslider=dict(visible=True),
            type="date",
            title=dict(
                text='Date',
                font=dict(size=16, color='#000000')  # Black color for x-axis title
            ),
            tickfont=dict(size=14, color='#333333')
        ),
        yaxis=dict(
            title=dict(
                text='Price (USD)',
                font=dict(size=16, color='#000000')  # Black color for y-axis title
            ),
            tickfont=dict(size=14, color='#333333')
        ),
        plot_bgcolor='white',
        paper_bgcolor='white',
        hovermode='x unified',
        #width=1000,
        #height=600,
        #margin=dict(l=50, r=50, b=50, t=80)  # Adjusted margins
    )
    return price_trend



