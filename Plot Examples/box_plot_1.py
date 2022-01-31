import plotly.offline as pyo
import plotly.graph_objs as go

y = [1,14,14,15,16,18,18,19,19,20,20,23,24,26,27,27,28,29,33,54]

data = [go.Box(y=y, boxpoints="all", pointpos=1.5, name="example")] # pointpos set the points on the left or right of graph. the value is avaliable between -2 ile 2.
# boxpoints shows the values on graph if you prefer. "outliers" argument only shows the outliers figures.
# name means the name of the graph what you want.
pyo.plot(data)
