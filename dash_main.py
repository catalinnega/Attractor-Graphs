import dash
from dash.dependencies import Output, Input, State
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
import plotly
from plotly.subplots import make_subplots
from time import time

import numpy as np

import dash_settings
import global_settings as gs

app = dash.Dash(__name__)
app.layout = html.Div(
    [
        html.Div(
        [
        html.H1('Attractors', style={'color':"#CECECE"}),
        # dcc.RadioItems(
        #     id = 'radio-item',
        #     options=[
        #         {'label': 'run update', 'value': 'on'},
        #         {'label': 'stop update', 'value': 'off'},
        #     ],
        #     value = 'on',
        #     labelStyle = {'display': 'block'},
        #     style = {'color': 'white'}
        # ),
        dcc.Dropdown(
                id='dropdown_input',
                options = [
                    {"label" : "Lorenz Attractor", "value" : "LOR"},
                    {"label" : "Rossler Attractor", "value" : "ROS"},
                    {"label" : "Henon Map", "value" : "HEN"}
                          ],
                placeholder="Select an indicator here",
                style={'backgroundColor': 'White', 'width' : 250},
                value="LOR"
            ),
        daq.NumericInput(
            id = 'numeric-input',
            value = dash_settings.DEFAULT_NUM_ITERS_INIT,
            min = 0,
            max = 100000,
            label = 'No. of iterations',
            labelPosition = 'top',
            size = 150,
            style = {'color': 'white', 'width': 250}
        ),
        dcc.Graph(id='app_main', config=dict(editable=True)),
        dcc.Interval(
            id = 'graph-update',
            interval = 900,
            n_intervals = dash_settings.DEFAULT_NUM_ITERS_INIT
        ),
        ], style = {'backgroundColor': dash_settings.app_colors['background'], 'margin-top':'-20px', 'margin-left':'-10px', 'margin-right':'-10px'}
        ),
    ], style = {'backgroundColor': dash_settings.app_colors['background'], 'margin-top':'-20px', 'margin-left':'-0px', 'margin-right':'-0px'},
)

@app.callback(Output('app_main', 'figure'),
              [Input('graph-update', 'n_intervals'), Input('dropdown_input', 'value')],
              #[State('app_main', 'hoverData')],
              #[State('radio-item', 'value')],
              [State('numeric-input', 'value')],
              #[State('app_main', 'figure')]
              )
def update_graph(n_intervals, dropdown_id, num_iters):
    fig = None
    if(dropdown_id in gs.graph_fns):
        fn = gs.graph_fns[dropdown_id]['fn']
        #args = gs.graph_fns[dropdown_id]['kwargs']
        fig = fn(num_iters)
    return fig

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8120 ,debug=True)