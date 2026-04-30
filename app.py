import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

df = pd.read_csv('formatted_data.csv')
df['date'] = pd.to_datetime(df['date'])

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser", style={'textAlign': 'center'}),
    html.Label("Select Region:"),
    dcc.Dropdown(
        id='region-dropdown',
        options=[
            {'label': 'All', 'value': 'all'},
            {'label': 'North', 'value': 'north'},
            {'label': 'East', 'value': 'east'},
            {'label': 'South', 'value': 'south'},
            {'label': 'West', 'value': 'west'}
        ],
        value='all',
        clearable=False
    ),
    dcc.Graph(id='sales-line-chart')
])

@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-dropdown', 'value')
)
def update_chart(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]
    daily_sales = filtered_df.groupby('date')['sales'].sum().reset_index()
    fig = px.line(daily_sales, x='date', y='sales',
                  title=f'Pink Morsel Sales Over Time ({selected_region.capitalize() if selected_region != "all" else "All Regions"})',
                  labels={'sales': 'Total Sales ($)', 'date': 'Date'})
    return fig

if __name__ == '__main__':
    app.run(debug=True)