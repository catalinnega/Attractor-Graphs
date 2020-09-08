import plotly.graph_objs as go
import rossler.rossler_settings as settings
import dash_settings

def data_gen():
    time = 0.01
    x, y, z = 0.01, 0, 0
    X, Y, Z = [], [], []
    for i in range(settings.TIME_LEN):
        dx = (-y - z) * time
        dy = (x + settings.a * y) * time
        dz = (settings.b + z * (x - settings.c)) * time
        
        x = x + dx
        y = y + dy
        z = z + dz

        X.append(x)
        Y.append(y)
        Z.append(z)
        yield X, Y, Z

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
            x, y, z = next(g)

    prev_num_input = num_iters
    x, y, z = next(g)
    fig = go.Figure(data = [go.Scatter3d(
        x = x,
        y = y,
        z = z,
        mode = 'markers',
        marker = dict(
            size = 2,
            color = z,
            colorscale = 'Viridis',
            opacity = 0.9
        ),
        line = dict(
            color = 'darkblue',
            width = 2)
    )])

    camera = dict(
        up=dict(x = 0, y = 0, z = 1),
        center=dict(x = 0, y = 0, z = 0),
        eye=dict(x = 0.5, y = 1.25, z = 1.25)
    )
    fig.update_layout(
        margin=dict(l = 0, r = 0, b = 0, t = 0),
        plot_bgcolor = dash_settings.app_colors['background'],
        paper_bgcolor = dash_settings.app_colors['background'],
        height = 900,
        uirevision='same',
        scene_camera = camera)
    return fig