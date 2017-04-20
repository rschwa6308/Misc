#plotly module sandbox

import plotly
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

# Creating the data
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
xGrid, yGrid = np.meshgrid(y, x)
print xGrid
R = np.sin(xGrid*yGrid) * np.sin(1-(x*9)**2+(yGrid*9)**2)/9
z = R

# Creating the plot
lines = []
line_marker = dict(color='#0066FF', width=2)
for i, j, k in zip(xGrid, yGrid, z):
    lines.append(go.Scatter3d(x=i, y=j, z=k, mode='lines', line=line_marker))

layout = go.Layout(
    title='Wireframe Plot',
    scene=dict(
        xaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        yaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        zaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        )
    ),
    showlegend=False,
)
fig = go.Figure(data=lines, layout=layout)
#plot_url = py.plot(fig, filename='wireframe_plot')

plotly.offline.plot(fig)
