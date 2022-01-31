import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)
x_values = np.linspace(0,1,100)
y_values = np.random.randn(100) # generate 100 values which has normal distribution.

trace0 = go.Scatter(x=x_values, y=y_values+5, mode="markers", name="markers") # to avoid crashing the graphs each others, you can add/minus a number for y value.
trace1 = go.Scatter(x=x_values, y=y_values, mode="lines", name="my lines") # name sets the lines name.
trace2 = go.Scatter(x=x_values, y=y_values-5, mode="markers+lines", name="my favorite")

data = [trace0, trace1,trace2] # To show 3 graphs together, they are covered in a array.
layout = go.Layout(title="Line Charts")
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
