import plotly.graph_objs as go
import henon.henon_settings as settings
import dash_settings
import plotly.express as px

def data_gen():
    x, y = 0.01, 0
    X, Y = [], []
    for i in range(settings.TIME_LEN):
        prev_x = x
        x = 1 - settings.a * (prev_x ** 2) + y
        y = settings.b * prev_x

        X.append(x)
        Y.append(y)
        yield X, Y

g = None
init_flag = False
prev_num_iters = -1

def get_graph(num_iters):
    global init_flag
    global prev_num_iters
    global g

    if(num_iters != prev_num_iters):
        g = data_gen()
        for _ in range(num_iters):
            x, y = next(g)

    prev_num_input = num_iters
    x, y = next(g)
    fig = go.Figure(data = [go.Scatter(
        x = x,
        y = y,
        mode = 'markers',
        marker = dict(
            size = 2,
            color = y,
            colorscale = 'Viridis',
            opacity = 0.9
        ),
        line = dict(
            color = 'darkblue',
            width = 2)
    )])

    fig.update_layout(
        plot_bgcolor = dash_settings.app_colors['background'],
        paper_bgcolor = dash_settings.app_colors['background'],
        height = 900,
        uirevision='same',
        )
    return fig