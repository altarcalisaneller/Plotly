#######
# Objective: Make a DataFrame using the Abalone dataset (../data/abalone.csv).
# Take two independent random samples of different sizes from the 'rings' field.
# HINT: np.random.choice(df['rings'],10,replace=False) takes 10 random values
# Use box plots to show that the samples do derive from the same population.
######

import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import numpy as np

df = pd.read_csv("data/abalone.csv")

A = np.random.choice(df["rings"], 10)
B = np.random.choice(df["rings"], 10)

data = [go.Box(y=A, name="A",boxpoints="outliers"), go.Box(y=B, name="B",boxpoints="outliers")] # if you give "x" instead of "y" as parameters, the graphs are created horizantal.
layout = go.Layout(title="Comparison two random samples")
fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)
