# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#Aqui llamo al estilo de bootstrap
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server

graduados = pd.read_csv('dataset/graduados_acacias.csv')
print(graduados.columns)

fig= px.bar(graduados,x="ESTRATO 2",y="INSTITUCIÓN EDUCATIVA")

app.layout = html.Div(children=[
    html.H1(children='Bienvenido a mi Dash experimental'),

    html.Div(children='''
        Estudiantes graduados en la ciudad de Acacias-Meta desde 2013 - 2019.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)