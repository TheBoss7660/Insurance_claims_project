import pandas as pd
import numpy as np
import plotly.express as px
from dash import dcc, html
from dash.dependencies import Input, Output
from database import create_db_engine
from sqlalchemy import create engine

# connect to database
engine =  create_engine('postgresql://postgres:bosire@localhost:5432/insurance_db')

# Load data from database
query = "SELECT * FROM insurance_claims"
df = pd.read_sql(query, engine)

# Initialize dash app
app = dash.Dash(__name__)

fig= px.bar(df, x='claim_status', y='claim_amount', color='claim_status', barmode='group')
#App layout
app.layout = html.Div([
    html.H1("Insurance Claims Dashboard"),
    dcc.Dropdown(
        id='claim-type-dropdown',
        options=[{'label': claim_type, 'value': claim_type} for claim_type in df['claim_type'].unique()],
        value=df['claim_type'].unique()[0]
    ),
    dcc.Graph(id='claims-graph')
])

# Callback to update graph based on dropdown selection
@app.callback(
    Output('claims-graph', 'figure'),
    [Input('claim-type-dropdown', 'value')]
)
def update_graph(selected_claim_type):
    filtered_df = df[df['claim_type'] == selected_claim_type]
    fig = px.bar(filtered_df, x='claim_status', y='claim_amount', color='claim_status', barmode='group')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)