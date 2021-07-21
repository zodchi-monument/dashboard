import dash
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
    dash.dependencies.Output('main-graph', 'figure'),
    [dash.dependencies.Input('main-drop', 'value')])
def update_main_graph(tags):
    return main_graph(tags)

@app.callback(
    dash.dependencies.Output('mape-graph', 'figure'),
    [dash.dependencies.Input('main-drop', 'value')])
def update_main_graph(tags):
    return mape_graph(tags)

@app.callback(
    dash.dependencies.Output('features-graph','figure'),
    [dash.dependencies.Input('features-drop', 'value')])
def update_main_graph(tags):
    return feature_graph(tags)

@app.callback(
    dash.dependencies.Output('factor-graph','figure'),
    [dash.dependencies.Input('main-drop', 'value')])
def update_main_graph(tags):
    return factor_graph(tags)

if __name__ == "__main__":
    app.run_server(debug=True)