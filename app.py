import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objs as go
import dash_daq as daq
import dash_bootstrap_components as dbc


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server


df = px.data.iris()
fig= px.scatter(df,x="sepal_width",y="sepal_length")
grafica_1= dcc.Graph(figure=fig)


fig2 = go.Figure(data=[go.Scatter(x=[1,2,3,4],y=[1,2,3,4])])
grafica_2=dcc.Graph(figure=fig2)


grafica_3=dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )



indicador_1=daq.Knob(

            size=400,
            max=10,
            color={"ranges":{"green":[0,5],"yellow":[5,9],"red":[9,10]}}


)


body = html.Div(
    [
        
        dbc.Row(
            [
                dbc.Col(grafica_1),
                dbc.Col(grafica_2),
                dbc.Col(grafica_3),
            ]
        ),
        dbc.Row(dbc.Col(indicador_1),),
    ]
)



app.layout=html.Div([ 
body
])

if __name__ == '__main__':
    app.run_server(debug=True)