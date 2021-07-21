import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from datetime import date

features = ['Meteo:T1', 'Meteo:NV:Average', 'Meteo:SV', 'Meteo:VV', 'Meteo:AD',"AVT10:QI932", "AVT10:PI3_30-33_avr",
            "AVT10:FC_39-42_sum", "AVT10:TI60_3-6_avr", "AVT10:TI806","AVT10:P11_out_T_weighted_sum", "AVT10:QI933",
            "AVT10:PI3_34-37_avr", "AVT10:FC_43-46_sum","AVT10:TI60_7-10_avr", "AVT10:TI806",
            "AVT10:P12_out_T_weighted_sum","AVT10:QI934","AVT10:PI3_38-41_avr", "AVT10:FC_47-50_sum", "AVT10:TI806",
            "AVT10:TI6_11-14_avr","AVT10:P13_out_T_weighted_sum", "AVT10:QI936", "AVT10:PI3_48-49_avr",
            "AVT10:FC_30-33_sum","AVT10:TI5_27-28_avr","AVT10:P101_out_T_weighted_sum", "AVT10:TI518", "AVT10:QI937",
            "AVT10:PI3_46-47_avr", "AVT10:FC_84-87_sum", "AVT10:TI7_50-51_avr", "AVT10:TI690",
            "AVT10:P102_out_T_weighted_sum","AVT10:QI935", "AVT10:PI3_42-45_avr", "AVT10:FC1_12-17_sum",
            "AVT10:TI7_11-14_avr", "AVT10:P3_out_T_weighted_sum","AVT10:TI567", "AVT10:TI826", "AVT10:TI739",
            "AVT10:TI736"]
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