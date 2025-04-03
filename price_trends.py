def get_btc_trend(data):
    import plotly.graph_objects as go
    # PLOT BTC TREND
    BTC_trend = go.Figure()

    BTC_trend.add_trace(go.Scatter(
        x=data.index,
        y=data.loc[:,'BTC-USD'],
        name='BTC-USD',
        line=dict(color='#766CDB', width=2)
    ))

    # Update layout
    BTC_trend.update_layout(
        title=dict(
            text='Bitcoin Price Trend',
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
        height=600,
        margin=dict(l=50, r=50, b=50, t=80)  # Adjusted margins
    )
    return BTC_trend

def get_wif_trend(data):
    import plotly.graph_objects as go
    # PLOT BTC TREND
    WIF_trend = go.Figure()

    WIF_trend.add_trace(go.Scatter(
        x=data.index,
        y=data.loc[:,'WIF-USD'],
        name='WIF-USD',
        line=dict(color='#766CDB', width=2)
    ))

    # Update layout
    WIF_trend.update_layout(
        title=dict(
            text='Dogwifhat Price Trend',
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
        height=600,
        margin=dict(l=50, r=50, b=50, t=80)  # Adjusted margins
    )
    return WIF_trend