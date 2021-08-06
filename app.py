import dash
from dash.dependencies import Output, Input, State
from layouts import *
from callbacks import *

objects_dict = {}
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

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

@app.callback(
    Output('agg-drop', 'options'),
    Input('plant-drop', 'value'))
def update_plant_dropdown(plant_name):
    ls = objects_dict.get(plant_name)
    ls = [{"label": i, "value": i} for i in ls] if ls else []
    return ls

@app.callback(
    Output('main-drop', 'options'),
    Input('plant-drop', 'value'),
    Input('agg-drop', 'value'))
def update_agg_dropdown(plant_name, agg_name):
    ls = objects_dict.get(plant_name)
    ls = ls.get(agg_name) if ls else None
    ls = [{"label": i, "value": i} for i in ls] if ls else []
    return ls