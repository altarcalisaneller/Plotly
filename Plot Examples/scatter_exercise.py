#######
# Objective: Create a scatterplot of 1000 random data points.
# x-axis values should come from a normal distribution using
# np.random.randn(1000)
# y-axis values should come from a uniform distribution over [0,1) using
# np.random.rand(1000)
######

import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np

random_x = np.random.randn(1000) # normal distribution
random_y = np.random.rand(1000)  # uniform distribution

data = [go.Scatter(x = random_x, y = random_y, mode = 'markers')]

layout = go.Layout(title = 'Random Data Scatterplot',xaxis = dict(title = 'Normal distribution'), yaxis = dict(title = 'Uniform distribution'), hovermode ='closest')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='solution1.html')
