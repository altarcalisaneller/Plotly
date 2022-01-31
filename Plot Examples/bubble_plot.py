import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv("data/mpg.csv")

df['horsepower'] = pd.to_numeric(df['horsepower'], errors='coerce') # convert the string to number

# By setting errors=’coerce’, you’ll transform the non-numeric values into NaN.

data = [go.Scatter(x=df["horsepower"], y=df["mpg"], text=df["name"], mode="markers", marker=dict(size=df["cylinders"], showscale=True, color=df["cylinders"]))]

# text parameter sets the text for hover.
# color parameter sets different colors for values.
# if showscale is True, shows the legend on graph.
# marker size sets the size of each bubble according to values.

layout= go.Layout(title="Bubble Chart", hovermode="closest") #hovermode closest gets the text of the closest bubble according to mouse location.

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
