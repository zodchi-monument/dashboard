from plotly import graph_objects as go
from plotly import express as px
from datetime import datetime
import pandas as pd
import numpy as np
from itertools import cycle
import random
import base64
import io
from utils import MAPE

fact_df, plan_df = pd.read_csv("data/fact.csv"), pd.read_csv("data/plan.csv")


def pars_uploaded_file(content, name: str, type: str):
    global fact_df, plan_df
    if content:
        content_type, content_string = content.split(',')
        decoded = base64.b64decode(content_string)

        a = lambda x: pd.read_csv(io.StringIO(x.decode('utf-8')))
        if type == "fact":
            fact_df = a(decoded)
        else:
            plan_df = a(decoded)
        return [name]
    else:
        return ['Drag and Drop your FACT-data csv file']


def main_graph(model):
    global fact_df, plan_df

    timeline = [datetime.strptime(i, '%d.%m.%Y %H:%M:%S') for i in fact_df["date"].values]

    fact_data = list(fact_df["y_consumption"].values)
    fact_trace = go.Scatter(x=timeline, y=fact_data,
                            line=dict(color=px.colors.qualitative.Prism[0], width=2, shape='hv'),
                            name='Фактическое по прибору')

    load_data = list(fact_df["load"].values)
    load_trace = go.Scatter(x=timeline, y=load_data,
                            line=dict(color='grey', width=1, shape='hv'),
                            name='Загрузка установки')

    plan_data = list(plan_df["y_consumption"].values)
    plan_trace = go.Scatter(x=timeline, y=plan_data,
                            line=dict(color=px.colors.qualitative.Prism[1], width=2, dash='dot', shape='hv'),
                            name='Фактическое по модели')

    fig = go.Figure(layout=go.Layout(paper_bgcolor='rgba(0,0,0,0.1)',plot_bgcolor='rgba(0,0,0,0)', height=300))
    for i in [fact_trace, plan_trace, load_trace]:
        fig.add_trace(i)
    fig.update_xaxes(showgrid=False, zeroline=False,)
    fig.update_yaxes(showgrid=False, zeroline=False)
    fig.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
                      font_color="white", height=240,
                      margin=dict(l=20, r=20, t=20, b=20),)
    return fig


def mape_graph(model):
    mean_plan, mean_fact = round(np.mean(plan_df["y_consumption"]),3), round(np.mean(fact_df["y_consumption"]),3)
    delta = round(mean_plan-mean_fact, 3)

    pie_dict = dict(hole=.8, domain={'x': [0.1, 0.9], 'y': [0.1, 0.9]},)
    if delta > 0:
        fact_pie = go.Pie(labels=["План"], values=[mean_plan], hole=.85,)
        small_pie = go.Pie(labels=["", "Факт", "Дельта"], values=[0, mean_fact, delta], **pie_dict)
    else:
        fact_pie = go.Pie(labels=["Факт"], values=[mean_fact], hole=.85,)
        small_pie = go.Pie(labels=["", "План", "Дельта"], values=[0, mean_plan, abs(delta)], **pie_dict )

    fig = go.Figure(layout=go.Layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=300))
    fig.add_trace(fact_pie)
    fig.add_trace(small_pie)
    fig.update_traces(textinfo='none', marker=dict(colors=[px.colors.qualitative.Prism[i] for i in [0, 1, 3]]))

    fig.update_layout(showlegend=False,font_color="white",margin=dict(l=20, r=20, t=20, b=20), height=240,)

    fig.add_annotation(dict(font=dict(color=px.colors.qualitative.Prism[0], size=14),
                            x=0.5, y=0.6, showarrow=False, text=f"Факт: {mean_fact}",))
    fig.add_annotation(dict(font=dict(color=px.colors.qualitative.Prism[1], size=14),
                            x=0.5, y=0.5, showarrow=False, text=f"План: {mean_plan}", ))
    fig.add_annotation(dict(font=dict(color=px.colors.qualitative.Prism[3], size=14),
                            x=0.5, y=0.4, showarrow=False, text=f"Дельта: {abs(delta)}", ))
    return fig


def feature_graph(tags):
    palette = cycle(px.colors.qualitative.Prism)

    timeline = [datetime.strptime(i, '%d.%m.%Y %H:%M:%S') for i in fact_df["date"].values]

    fig = go.Figure(layout=go.Layout(paper_bgcolor='rgba(0,0,0,0.1)', plot_bgcolor='rgba(0,0,0,0)', height=200))
    for t in tags:
        p = dict(marker_color=next(palette), x=timeline )
        trace = go.Scatter(y=list(fact_df[t].squeeze().values),
                           line=dict(width=1, shape='hv'), name=t, **p)
        fig.add_trace(trace)
        trace = go.Scatter(y=list(plan_df[t].squeeze().values), legendrank=1001,  name=f"plan",
                           line=dict(width=1, shape='hv', dash='dot'), **p)
        fig.add_trace(trace)

    fig.update_xaxes(showgrid=False, zeroline=False)
    fig.update_yaxes(showgrid=False, zeroline=False)
    fig.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
                      font_color="white", height=260,
                      margin=dict(l=20, r=20, t=20, b=20))
    return fig


controlledf = ["Pressure:P111",  "Consumption:F4", "Consumption:F5", "Temperature:T11", "Temperature:T12",
               "Temperature:T13", "Temperature:T14", "Temperature:T15", "Consumption:F1", "Consumption:F2",
               "Pressure:P112", "Pressure:P113", "Pressure:P114", "Pressure:P115", "Consumption:F3",]
manipulated = ["Meteo:T1 [°C]", "Meteo:T2 [°C]", "Meteo:P [mm Hg]", "Meteo:V1 [m/sec]", "Meteo:V2 [m/sec]",
               "Meteo:NV:Avarage"]

def factor_graph(tags):
    measure = ["absolute"] + ["relative" for _ in controlledf] + ["absolute"] + ["relative" for _ in manipulated] + ["absolute"]
    x = ["Plan"] + controlledf + ["Normal"] + manipulated + ["Model"]
    y = [2] + [random.random()-0.5 for _ in controlledf] + [5] + [random.random()-0.5 for _ in manipulated] + [7]
    trace = go.Waterfall(measure=measure, x=x, y=y,
                         increasing={"marker": {"color": px.colors.qualitative.Prism[0]}},
                         decreasing={"marker": {"color": px.colors.qualitative.Prism[1]}},
                         totals ={"marker": {"color": px.colors.qualitative.Prism[3]}},)

    fig = go.Figure(layout=go.Layout(paper_bgcolor='rgba(0,0,0,0.1)',plot_bgcolor='rgba(0,0,0,0)', height=200))
    fig.add_trace(trace)

    fig.update_xaxes(showgrid=False, zeroline=False)
    fig.update_yaxes(showgrid=False, zeroline=False)
    fig.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
                      font_color="white",
                      margin=dict(l=20, r=20, t=20, b=20))
    return fig