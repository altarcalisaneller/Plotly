#######
# Objective: Using the "flights" dataset available
# from the data folder as flights.csv
# create a heatmap with the following parameters:
# x-axis="year"
# y-axis="month"
# z-axis(color)="passengers"
######

import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv("data/flights.csv")

data = [go.Heatmap(x=df["year"], y=df["month"], z=df["passengers"], colorscale="JET")]

layout = go.Layout(title="Flights")

fig = go.Figure(data=data,layout=layout)
pyo.plot(fig)
