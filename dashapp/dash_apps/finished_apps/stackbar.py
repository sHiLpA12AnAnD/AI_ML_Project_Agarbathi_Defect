
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from django_plotly_dash import DjangoDash

app = DjangoDash()

app.layout = html.Div([
    html.H2('Agarbathi dashboard Sample charts using Dash!!')
])



app = DjangoDash('stackbar')


df = pd.read_csv('E:/AB Plastomech Pvt Ltd/Responsive Dashboard/charts/agarbathi.csv')


fig = px.bar(df,
             x="Agarbathi Classification",
             y=["Top Defect (T)","Bottom Defect (B)","No Tip Defect (N)","Middle Defect (M)","No Defect (G)"],
             title='Agarbathi Defects based on classification',
             color_discrete_sequence=["rgb(237,100,90)","rgb(127,60,141)","#DD4477","#2ED9FF","rgb(166,216,84)"])

app.layout = html.Div( children=[

    # html.H1(children='Agarbathi Dashboard'),
    #
    # html.Div(children='''
    #    Sample Pie chart for Agarbathi Defect Detection
    # '''),

    dcc.Graph(
        id='example-graph',
        figure=fig,
    )
])
