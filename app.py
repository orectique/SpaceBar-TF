import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from styleTransfer import make_image

app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}], external_stylesheets=[dbc.themes.SUPERHERO])
app.title = 'SpaceBar'
server = app.server


########################################################

app.layout = html.Div([    
    
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
        
        html.Div(id='output-image'),
        
    ], style = {'width' : '40%', 'display': 'inline-block'})

  
])

########################################################

@app.callback(
Output('output-image', 'children'),
Input('upload-image', 'contents')
)
def style_transfer(upload_image):
    image = make_image(upload_image)
    return image

if __name__ == '__main__':
    app.run_server(debug=True)
