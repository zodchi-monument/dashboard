import dash
from dash.dependencies import Output, Input, State
from layouts import *
import dash_html_components as html
from callbacks import *

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

app.layout = html.Div([
    main_dash,
    feature_dash,
    factor_dash
], style={"maxWidth": "2050px"})

@app.callback(
    Output('main-graph', 'figure'),
    [Input('main-drop', 'value')])
def update_main_graph(tags):
    return main_graph(tags)

@app.callback(
    Output('mape-graph', 'figure'),
    [Input('main-drop', 'value')])
def update_mape_graph(tags):
    return mape_graph(tags)

@app.callback(
    Output('features-graph', 'figure'),
    [Input('features-drop', 'value')])
def update_feature_graph(tags):
    return feature_graph(tags)

@app.callback(
    Output('factor-graph', 'figure'),
    [Input('main-drop', 'value')])
def update_factor_graph(tags):
    return factor_graph(tags)

@app.callback(
    Output('upload-fact-data-title', 'children'),
    Input('upload-fact-data', 'contents'),
    State('upload-fact-data', 'filename'))
def update_fact_data(content, name):
    return pars_uploaded_file(content, name, 'fact')

@app.callback(
    Output('upload-plan-data-title', 'children'),
    Input('upload-plan-data', 'contents'),
    State('upload-plan-data', 'filename'))
def update_plan_data(content, name):
    return pars_uploaded_file(content, name, 'plan')


if __name__ == "__main__":
    app.run_server(debug=True)