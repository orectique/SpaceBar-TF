import dash
import dash_core_components as dcc
from dash_core_components.Markdown import Markdown
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


import pandas as pd
import random

app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}], external_stylesheets=[dbc.themes.SUPERHERO])
app.title = 'SpaceBar'
server = app.server


########################################################

app.layout = html.Div([

    html.Div([
        dcc.Graph(id='indicator-graphic')
        
    ], style = {'width' : '60%', 'float': 'left', 'display': 'inline-block'}),
    
    
    html.Div([
        dcc.Upload(
        id='upload-image',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select File')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=False
    ),
        
        
        
    ], style = {'width' : '40%', 'float': 'right', 'display': 'inline-block'})

  
])

########################################################

@app.callback(

)
def style_transfer():
    return

if __name__ == '__main__':
    app.run_server(debug=True)
