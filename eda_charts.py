import pandas as pd

# Function to create correlation scatter plots for selected coins
def get_scatter(all_data_df: pd.DataFrame, symbol_1:str, symbol_2:str):
    import plotly.express as px
    # Create column names for closing prices
    col1 = f'Close_{symbol_1}'
    col2 = f'Close_{symbol_2}'
    # Create a scatter plot with trendline
    fig = px.scatter(
        all_data_df,
        x=col2,
        y=col1,
        title=f"{symbol_1} vs {symbol_2} Closing Prices",
        labels={col1: f"{symbol_1} Close Price", col2: f"{symbol_2} Close Price"},
        trendline="ols"  # Ordinary Least Squares trendline
    )
    fig.data[0].marker.color = 'blue'      # Points
    fig.data[1].line.color = 'red'         # Trendline
    return fig

# Function to create close price histogram for selected coin
def get_histogram(all_data_df:pd.DataFrame,symbol:str):
    import plotly.express as px
    fig = px.histogram(
    all_data_df,
    x=f'Close_{symbol}',
    nbins=50,  # You can adjust the number of bins
    title='Histogram of BTC-USD Close Prices',
    labels={'Close_BTC-USD': 'BTC-USD Close Price'},
    color_discrete_sequence=['blue'],  # Set bin color
    )
    return fig 

def get_volume_chart(all_data_df:pd.DataFrame, symbol:str):
    import plotly.express as px
    fig = px.bar(
        all_data_df,
        x='Date',
        y=f'Volume_{symbol}',
        title=f'{symbol} Volume Over Time',
        labels={f'Volume_{symbol}': 'Volume', 'Date': 'Date'},
        color_discrete_sequence=['blue']  # Bar color
    )

    return fig