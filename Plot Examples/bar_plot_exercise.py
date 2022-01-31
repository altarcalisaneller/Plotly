#######
# Objective: Create a stacked bar chart from
# the file ../data/mocksurvey.csv. Note that questions appear in
# the index (and should be used for the x-axis), while responses
# appear as column labels.  Extra Credit: make a horizontal bar chart!
######

import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv("data/mocksurvey.csv", index_col=0) # it is a pandasSeries and has no column name. So the first column is set as index.

data = [go.Bar(x = df.index , y = df[i], name=i) for i in df.columns]
layout = go.Layout(title="Mock Survey Results", barmode="stack")
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)


# horizantal form

# data = [go.Bar(x = df[i] , y = df.index, name=i, orientation="h") for i in df.columns]
# layout = go.Layout(title="Mock Survey Results", barmode="stack")
# fig = go.Figure(data=data, layout=layout)
# pyo.plot(fig)
