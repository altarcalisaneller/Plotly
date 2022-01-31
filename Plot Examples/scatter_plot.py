#######
# Objective: Create a scatterplot of 1000 random data points.
# x-axis values should come from a normal distribution using
# np.random.randn(100)
# y-axis values should come from a uniform distribution over [0,1) using
# np.random.rand(100)
######

import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

data = [go.Scatter(x=random_x, y = random_y,  mode="markers", marker=dict(size=12, color="antiquewhite", symbol="octagon", line={"width":2}) )]

# mode should be set to markers.
# set the marker features as color, shape, witdh (frame border) and size.

layout = go.Layout(title="Hello first plot", xaxis={"title": "my x axis"}, yaxis=dict(title="my y axis"), hovermode="closest")

# title= graph title, xaxis=x the name given x axis, hovermode gives information of the point which is closest (closest is default value) to mouse location.
# note that x and y axis defination syntax are different but both of them works.comman usage as dict().

fig = go.Figure(data=data, layout=layout) # create a fig object
pyo.plot(fig,filename="scatter.html") # it creates also a file as scatter.html.
