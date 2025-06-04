import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load processed data from the CSV you created earlier
df = pd.read_csv('processed_sales.csv')

# Convert date column to datetime for sorting and plotting
df['date'] = pd.to_datetime(df['date'])

# Aggregate sales by date (sum sales for each date)
daily_sales = df.groupby('date')['Sales'].sum().reset_index()

# Sort by date just to be sure
daily_sales = daily_sales.sort_values('date')

# Create Dash app
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Soul Foods Pink Morsel Sales Visualiser'),

    dcc.Graph(
        id='sales-line-chart',
        figure=px.line(
            daily_sales,
            x='date',
            y='Sales',
            title='Daily Sales of Pink Morsels',
            labels={'date': 'Date', 'Sales': 'Total Sales (£)'}
        )
    ),

    html.Div(children='''
        Sales before and after the price increase on 15th January 2021
    ''')
])

if __name__ == '__main__':
    app.run_server(debug=True)
