import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv("data/mpg.csv")

data = [go.Histogram(x=df["mpg"], xbins=dict(start=0, end=50, size=1),texttemplate="%{y}")]
# start and end parameters set the range of histogram values on x axis..
# texttemplate="%{y}" shows the values in bars according to y axis. You can try texttemplate="%{y}, %{x}" or texttemplate="%{x}" as alternatives.
# size sets the "bin" size.
layout = go.Layout(title="Histogram Plot")

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)
