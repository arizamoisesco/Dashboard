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
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

fig= px.bar(graduados,x="ESTRATO 2",y="INSTITUCIÓN EDUCATIVA")

#Modificación del diseño del layout
fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(children='Bienvenido a mi Dash experimental',
    style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    html.Div(children='''
        Estudiantes graduados en la ciudad de Acacias-Meta desde 2013 - 2019.
    ''',
    style={
        'textAlign': 'center'
    }),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)