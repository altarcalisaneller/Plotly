#######
# Objective: Create a bubble chart that compares three other features
# from the mpg.csv dataset. Fields include: 'mpg', 'cylinders', 'displacement'
# 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name'
######

import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv("data/mpg.csv")

data = [go.Scatter(x=df["displacement"], y=df["acceleration"], text=df["name"], mode="markers")]

layout= go.Layout(title="My Bubble Solution", hovermode="closest")

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
