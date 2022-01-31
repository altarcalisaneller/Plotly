#######
# Objective: Create a histogram that plots the 'length' field
# from the Abalone dataset (../data/abalone.csv).
# Set the range from 0 to 1, with a bin size of 0.02
######

import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv("data/abalone.csv")

data = [go.Histogram(x=df["length"], xbins=dict(start=0, end=1, size=0.02))]

layout = go.Layout(title="Histogram Plot")

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)
