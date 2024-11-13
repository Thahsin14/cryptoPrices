if __name__ == '__main__':
    import dash, requests
    from dash import dcc, html
    import plotly.graph_objs as go
    import plotly.express as px

    base_url = "https://api.sandbox.gemini.com/v2/candles/btcusd/1m"
    response = requests.get(base_url)
    btc_data = response.json()
    
    changes = [item[1] for item in btc_data]
    indexes = list(range(1, len(changes) + 1))

    app = dash.Dash(__name__)

    app.layout = html.Div([
        dcc.Graph(
            id='changes-line-chart',
            figure={
                'data': [
                    go.Scatter(
                        x=indexes,
                        y=changes,
                        mode='lines+markers',
                        name='Cena'
                    )
                ],
                'layout': go.Layout(
                    title='BTC/USD current price = ' + str(btc_data[0][1]) + ' USD (1min candle)',
                    xaxis={'autorange': 'reversed'},
                    yaxis={'title': 'Price (USD)'},
                )
            }
        )
    ])

    app.run_server(debug=True)