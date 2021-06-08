import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from django_plotly_dash import DjangoDash

app = DjangoDash()

app.layout = html.Div([
    html.H2('Agarbathi dashboard Sample charts using Dash!!')
])

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('piechart', external_stylesheets=external_stylesheets)


df = pd.read_csv('E:/AB Plastomech Pvt Ltd/Responsive Dashboard/charts/agarbathipie.csv')


fig = px.pie(df,
             values='Counts',
             names='Defects',
             title='Agarbathi Defects based on type',
             color_discrete_sequence=["rgb(166,216,84)","rgb(127,60,141)","#DD4477","#2ED9FF","rgb(237,100,90)"])

fig.update_traces (textposition='inside',
                  textinfo='percent',
                  marker=dict(line=dict(color='white',width=1)),
                  pull=[0,0,0.1,0,0],
                  rotation=90)
# fig.show()
app.layout = html.Div(children=[
    # html.H1(children='Agarbathi Dashboard'),
    #
    # html.Div(children='''
    #    Sample Pie chart for Agarbathi Defect Detection
    # '''),

    dcc.Graph(
        id='pie',
        figure=fig
    )
])


