import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

df = pd.read_csv('processed_sales.csv')
df['date'] = pd.to_datetime(df['date'])

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods Pink Morsel Sales Visualiser"),

    html.Div([
        html.Label("Filter by Region:", id='region-selector-label'),
        dcc.RadioItems(
            id='region-selector',
            options=[
                {'label': 'All', 'value': 'all'},
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
            ],
            value='all',
            labelClassName='radio-item',  
            inputClassName='radio-input'  
        ),
    ], id='region-selector'),

    dcc.Graph(id='sales-line-chart'),

    html.Div(
        "Sales before and after the price increase on 15th January 2021",
        className='footer-text'
    )
])


@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-selector', 'value')
)
def update_line_chart(selected_region):
    if selected_region == 'all':
        filtered_df = df.copy()
    else:
        filtered_df = df[df['region'].str.lower() == selected_region]

    daily_sales = filtered_df.groupby('date')['Sales'].sum().reset_index()
    daily_sales = daily_sales.sort_values('date')

    fig = px.line(
        daily_sales,
        x='date',
        y='Sales',
        title=f'Daily Sales of Pink Morsels ({selected_region.capitalize()})',
        labels={'date': 'Date', 'Sales': 'Total Sales (£)'}
    )

    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(color='#6a1b9a'),
        title_font=dict(size=20, family='Arial'),
        xaxis=dict(showgrid=True, gridcolor='lightgrey'),
        yaxis=dict(showgrid=True, gridcolor='lightgrey'),
    )

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
