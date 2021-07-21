from plotly import graph_objects as go
from plotly import express as px
import datetime
import pandas as pd
import numpy as np
from itertools import cycle


def main_graph(model):
    date_now = datetime.datetime.now()
    date_start = date_now - datetime.timedelta(hours=72)
    date_end = date_now + datetime.timedelta(hours=71)
    timeline = [i for i in pd.date_range(start=date_start, end=date_end, freq='1H')]

    mock_data = list(np.random.random(72))
    mock_data = mock_data + [np.mean(mock_data)]*71
    fact_trace = go.Scatter(x=timeline, y=mock_data,
                            line=dict(color=px.colors.qualitative.Prism[0], width=2, shape='hv'),
                            name='Фактическое по прибору')

    mock_data = [i/4.0-0.25 for i in mock_data]
    load_trace = go.Scatter(x=timeline, y=mock_data,
                            line=dict(color='grey', width=1, shape='hv'),
                            name='Загрузка установки')

    mock_data = list(np.random.random(72))
    mock_data = mock_data + [np.mean(mock_data)] * 71
    plan_trace = go.Scatter(x=timeline, y=mock_data,
                            line=dict(color=px.colors.qualitative.Prism[1], width=2, dash='dot', shape='hv'),
                            name='Фактическое по модели')

    fig = go.Figure(layout=go.Layout(paper_bgcolor='rgba(0,0,0,0.1)',plot_bgcolor='rgba(0,0,0,0)', height=300))
    fig.add_trace(fact_trace)
    fig.add_trace(plan_trace)
    fig.add_trace(load_trace)
    fig.add_vline(date_now, line_color="white")

    fig.update_xaxes(showgrid=False, zeroline=False)
    fig.update_yaxes(showgrid=False, zeroline=False)
    fig.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
                      font_color="white",
                      margin=dict(l=20, r=20, t=20, b=20),)
    return fig

def mape_graph(model):
    fact_pie = go.Pie(labels=["План"], values=[1.2334], hole=.85,)
    small_pie = go.Pie(labels=["","Факт", "Дельта"], values=[0, 1.1234, 0.11], hole=.8,
                       domain={'x': [0.1, 0.9], 'y': [0.1, 0.9]},)

    fig = go.Figure(layout = go.Layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)', height=300))
    fig.add_trace(fact_pie)
    fig.add_trace(small_pie)
    fig.update_traces(textinfo='none', marker=dict(colors=[px.colors.qualitative.Prism[0],
                                                           px.colors.qualitative.Prism[1],
                                                           px.colors.qualitative.Prism[3]]))

    fig.update_layout(showlegend=False,
                      font_color="white",
                      margin=dict(l=20, r=20, t=20, b=20))

    fig.add_annotation(dict(font=dict(color=px.colors.qualitative.Prism[0], size=14),
                            x=0.5, y=0.6, showarrow=False, text="Факт: 27.2341",))
    fig.add_annotation(dict(font=dict(color=px.colors.qualitative.Prism[1], size=14),
                            x=0.5, y=0.5, showarrow=False, text="План: 26.3348", ))
    fig.add_annotation(dict(font=dict(color=px.colors.qualitative.Prism[3], size=14),
                            x=0.5, y=0.4, showarrow=False, text="MAPE: 1.9214%", ))
    return fig


def feature_graph(tags):
    palette = cycle(px.colors.qualitative.Prism)

    date_now = datetime.datetime.now()
    date_start = date_now - datetime.timedelta(hours=72)
    date_end = date_now + datetime.timedelta(hours=71)
    timeline = [i for i in pd.date_range(start=date_start, end=date_end, freq='1H')]

    fig = go.Figure(layout = go.Layout(paper_bgcolor='rgba(0,0,0,0.1)', plot_bgcolor='rgba(0,0,0,0)', height=200))
    for t in tags:
        mock_data = list(np.random.random(72))
        mock_data = mock_data + [np.mean(mock_data)] * 71
        trace = go.Scatter(x=timeline, y=mock_data,
                           line=dict(width=1, shape='hv'),
                           name=t, marker_color=next(palette))
        fig.add_trace(trace)

    fig.add_vline(date_now, line_color="white")
    fig.update_xaxes(showgrid=False, zeroline=False)
    fig.update_yaxes(showgrid=False, zeroline=False)
    fig.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
                      font_color="white",
                      margin=dict(l=20, r=20, t=20, b=20))
    return fig

def factor_graph(tags):
    trace = go.Waterfall(measure=["relative", "relative", "total", "relative", "relative", "relative", "relative", "total", "relative", "relative", "total", "relative", "relative", "total"],
                         x=["Sales", "Consulting", "Net revenue", "Purchases", "Test", "Test1", "Other expenses", "Profit before tax","Sales1", "Consulting1", "Net revenue1", "Purchases1", "Other expenses1", "Profit 1before tax"],
                         y=[60, 80, 0, -40 , 40, 50, -20, 0, 60, 80, 0, -40, -20, 0],
                         increasing={"marker": {"color": px.colors.qualitative.Prism[0]}},
                         decreasing={"marker": {"color": px.colors.qualitative.Prism[1]}},
                         totals ={"marker": {"color": px.colors.qualitative.Prism[3]}},)

    fig = go.Figure(layout = go.Layout(paper_bgcolor='rgba(0,0,0,0.1)',plot_bgcolor='rgba(0,0,0,0)', height=200))
    fig.add_trace(trace)

    fig.update_xaxes(showgrid=False, zeroline=False)
    fig.update_yaxes(showgrid=False, zeroline=False)
    fig.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
                      font_color="white",
                      margin=dict(l=20, r=20, t=20, b=20))
    return fig