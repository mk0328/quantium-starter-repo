import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

# Load the data
df = pd.read_csv('formatted_data.csv')
df['date'] = pd.to_datetime(df['date'])

# Initialize the app
app = dash.Dash(__name__)

# Define the layout with inline CSS for styling
app.layout = html.Div([
    # Main container with background and font
    html.Div([
        html.H1("🍬 Pink Morsel Sales Visualiser",
                style={'textAlign': 'center',
                       'color': '#2c3e50',
                       'fontFamily': 'Arial, sans-serif',
                       'marginTop': '20px'}),
        
        html.Hr(),
        
        # Radio button section
        html.Div([
            html.Label("Select Region:", style={'fontSize': '18px', 'fontWeight': 'bold'}),
            dcc.RadioItems(
                id='region-radio',
                options=[
                    {'label': '🌍 All', 'value': 'all'},
                    {'label': '⬆️ North', 'value': 'north'},
                    {'label': '➡️ East', 'value': 'east'},
                    {'label': '⬇️ South', 'value': 'south'},
                    {'label': '⬅️ West', 'value': 'west'}
                ],
                value='all',
                labelStyle={'display': 'inline-block', 'marginRight': '20px', 'fontSize': '16px'}
            )
        ], style={'textAlign': 'center', 'marginBottom': '30px'}),
        
        # Graph
        dcc.Graph(id='sales-line-chart')
        
    ], style={
        'width': '90%',
        'maxWidth': '1200px',
        'margin': '0 auto',
        'padding': '20px',
        'backgroundColor': '#f9f9f9',
        'borderRadius': '15px',
        'boxShadow': '0px 4px 12px rgba(0,0,0,0.1)'
    })
])

# Callback to update chart based on selected region
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-radio', 'value')
)
def update_chart(selected_region):
    if selected_region == 'all':
        filtered_df = df
        title = "Pink Morsel Sales Over Time (All Regions)"
    else:
        filtered_df = df[df['region'] == selected_region]
        title = f"Pink Morsel Sales Over Time ({selected_region.capitalize()} Region)"
    
    # Group by date to get total sales per day
    daily_sales = filtered_df.groupby('date')['sales'].sum().reset_index()
    
    # Create line chart
    fig = px.line(daily_sales, x='date', y='sales',
                  title=title,
                  labels={'sales': 'Total Sales ($)', 'date': 'Date'})
    
    # Improve chart appearance
    fig.update_layout(
        plot_bgcolor='white',
        title_font_size=20,
        title_font_family="Arial",
        xaxis_title_font_size=14,
        yaxis_title_font_size=14,
        hovermode='x unified'
    )
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
    
    return fig

if __name__ == '__main__':
    app.run(debug=True)