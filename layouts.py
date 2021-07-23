import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from datetime import date

features = ['feature1','feature2','feature3','feature4','feature5','feature6','feature7','feature8','feature9',
            'feature10','feature11','feature12','feature13','feature14','feature15','feature16','feature17']
predictors = [{"label": i, "value": i} for i in features]
manufactures = ["Производство №1"]
plant = ["Установка №1"]
models = ["Потребление топлива"]

main_dash = html.Div([
        dbc.Row(
            [
                dbc.Col(html.H4(children='Main Dashboard:',style={'text-decoration': 'underline'}), width=1.5),
                dbc.Col(
                    dcc.Dropdown(id='manufacture-drop', multi=False, options=[{"label": i, "value": i} for i in manufactures],
                                 style={'color': '#212121', 'background-color': '#212121'}), width=2),
                dbc.Col(
                    dcc.Dropdown(id='plant-drop', multi=False, options=[{"label": i, "value": i} for i in plant],
                                 style={'color': '#212121', 'background-color': '#212121'}), width=1),
                dbc.Col(
                    dcc.Dropdown(id='main-drop', multi=False, options=[{"label": i, "value": i} for i in models],
                                 style={'color': '#212121', 'background-color': '#212121'}), width=3),
            ], style={'padding': '20px'}),
        dbc.Row(
            [
            dbc.Col(dcc.Graph(id='main-graph', figure={'layout': {'height': 250}}), width=10),
            dbc.Col(dcc.Graph(id='mape-graph', figure={'layout': {'height': 250}}), width=2)
            ]
        )
])

feature_dash = html.Div([
        dbc.Row(
            [
            dbc.Col(
                [
                    dbc.Row(html.H4(children='Features graph:',style={'text-decoration': 'underline'}), style={'padding': '20px'}),
                    dcc.Graph(id='features-graph', figure={'layout': {'height': 200}})
                ],
                width=10),
            dbc.Col(
                [
                    dbc.Row(html.H4(children='Model features:',style={'text-decoration': 'underline'}), style={'padding': '20px'}),
                    dcc.Checklist(id='features-drop', value=[], labelStyle={'display': 'block'},
                                  options=[{"label": f"\t{i}", "value": i} for i in features],
                                  style={"overflow-y": "scroll", 'font-size': '16px', "maxHeight": "200px"})
                ],
                width=2,
            )
            ]
        )
])

factor_dash = html.Div([
        dbc.Row(html.H4(children='Factor analysis:',style={'text-decoration': 'underline'}), style={'padding': '20px'}),
        dbc.Col(
            dcc.Graph(id='factor-graph',
                      figure={'layout': {'height': 220}}),
            width=12
        )
])