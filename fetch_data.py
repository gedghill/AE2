def fetch_data():
    #import plotly.graph_objects as go
    from datetime import datetime, timedelta
    import pandas as pd
    import yfinance as yf
    #from price_trends import get_btc_trend

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
    #Convert downloaded data to csv format
    df.to_csv(r'All_Data.csv',index=True, header = True)
    df = df.drop(['High', 'Low', 'Open', 'Volume'], axis=1)

    #Drop level of data frame to change axis
    df = df.droplevel('Price', axis=1) #remove comment on this line when re-running
    df.to_csv(r'Close_Data.csv', index=True, header=True)

    data = pd.read_csv('Close_Data.csv', sep=',', encoding='utf-8', index_col=0, parse_dates=True)
    return data