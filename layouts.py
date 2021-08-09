import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


def get_layout(objects_dict):

    controlledf = ["Pressure:P111",  "Consumption:F4", "Consumption:F5", "Temperature:T11", "Temperature:T12",
                   "Temperature:T13", "Temperature:T14", "Temperature:T15", "Consumption:F1", "Consumption:F2",
                   "Pressure:P112", "Pressure:P113", "Pressure:P114", "Pressure:P115", "Consumption:F3",]
    manipulated = ["Meteo:T1 [°C]", "Meteo:T2 [°C]", "Meteo:P [mm Hg]", "Meteo:V1 [m/sec]", "Meteo:V2 [m/sec]",
                   "Meteo:NV:Avarage"]
    features = controlledf + manipulated


    main_dash = \
        html.Div([
            dbc.Row(
                [
                    dbc.Col(
                        dcc.Upload(id='upload-fact-data',
                           children=html.Div(['Drag and Drop your FACT-data csv file'], id='upload-fact-data-title'),
                           style={'width': '98%', 'height': '40px', 'lineHeight': '40px', 'borderWidth': '1px',
                                  'borderStyle': 'dashed', 'borderRadius': '5px', 'textAlign': 'center', 'margin': '10px'}
                           ),
                        width=6
                    ),
                    dbc.Col(
                        dcc.Upload(id='upload-plan-data',
                           children=html.Div(['Drag and Drop your PLAN-data csv file'], id='upload-plan-data-title'),
                           style={'width': '98%', 'height': '40px', 'lineHeight': '40px', 'borderWidth': '1px',
                                  'borderStyle': 'dashed', 'borderRadius': '5px', 'textAlign': 'center', 'margin': '10px'}
                           ),
                        width=6
                    )
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(html.H4(children='Main Dashboard:', style={'text-decoration': 'underline'}), width=2),
                    dbc.Col(
                        dcc.Dropdown(id='plant-drop', multi=False,
                                     options=[{"label": i, "value": i} for i in objects_dict.keys()],
                                     style={'color': '#212121', 'background-color': '#212121'}), width=2),
                    dbc.Col(
                        dcc.Dropdown(id='agg-drop', multi=False, options=[],
                                     style={'color': '#212121', 'background-color': '#212121'}), width=1),
                    dbc.Col(
                        dcc.Dropdown(id='main-drop', multi=False, options=[],
                                     style={'color': '#212121', 'background-color': '#212121'}), width=3),
                    dbc.Col(
                        dcc.Slider(min=1, max=4, marks={1:"Hour", 2:"Day", 3:"Month", 4:"Year"}, value=1), width=4),

                ], style={'padding': '20px'}),
            dbc.Row(
                [
                dbc.Col(dcc.Graph(id='main-graph', figure={'layout': {'height': 240}}), width=10),
                dbc.Col(dcc.Graph(id='mape-graph', figure={'layout': {'height': 240}}), width=2)
                ]
            )
    ])

    feature_dash = html.Div([
            dbc.Row(
                [
                dbc.Col(
                    [
                        dbc.Row(html.H4(children='Features graph:',style={'text-decoration': 'underline'}), style={'padding': '20px'}),
                        dcc.Graph(id='features-graph', figure={'layout': {'height': 260}})
                    ],
                    width=10),
                dbc.Col(
                    [
                        dbc.Row(html.H4(children='Model features:', style={'text-decoration': 'underline'}), style={'padding': '20px'}),
                        dcc.Checklist(id='features-drop', value=[], labelStyle={'display': 'block'},
                                      options=[{"label": f"*Choose the model*", "value": 0}],
                                      style={"overflow-y": "scroll", 'font-size': '16px', "maxHeight": "260px"})
                    ],
                    width=2,
                )
                ]
            )
    ])

    factor_dash = html.Div([
            dbc.Row(html.H4(children='Factor analysis:', style={'text-decoration': 'underline'}), style={'padding': '20px'}),
            dbc.Col(
                dcc.Graph(id='factor-graph',
                          figure={'layout': {'height': 220}}),
                width=12
            )
    ])
    return html.Div([main_dash, feature_dash, factor_dash], style={"maxWidth": "2050px"})