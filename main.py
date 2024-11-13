if __name__ == '__main__':
    import dash, requests
    from dash import dcc, html
    import plotly.graph_objs as go
    from datetime import datetime
    
    app = dash.Dash(__name__)

    base_url = "https://api.gemini.com/v2/candles/btcusd/15m"
    response = requests.get(base_url)
    btc_data = response.json()
    
    timestamps = [entry[0] for entry in btc_data]
    opens = [entry[1] for entry in btc_data]
    highs = [entry[2] for entry in btc_data]
    lows = [entry[3] for entry in btc_data]
    closes = [entry[4] for entry in btc_data]
    
    dates = [datetime.utcfromtimestamp(ts/1000) for ts in timestamps]

    fig = go.Figure(data=go.Candlestick(
        x=dates,
        open=opens,
        high=highs,
        low=lows,
        close=closes
    ))
    
    fig.update_layout(
        title="BTC/USD Candlestick Chart, current price: " + str(closes[0]) +" USD, candle every 15 minutes",
        xaxis_title="Date",
        yaxis_title="Price (USD)"
    )

    app.layout = html.Div([
        dcc.Graph(
            id='candlestick-chart',
            figure=fig
        )
    ])

    app.run_server(debug=True)