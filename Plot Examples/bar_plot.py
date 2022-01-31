import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv("data/2018WinterOlympics.csv")

trace0 = go.Bar(x = df["NOC"], y = df["Gold"], name="Gold", marker_color="gold")
trace1 = go.Bar(x = df["NOC"], y = df["Silver"], name="Silver", marker_color="silver")
trace2 = go.Bar(x = df["NOC"], y = df["Bronze"], name="Bronze", marker_color="brown")

data = [trace0, trace1, trace2]
layout = go.Layout(title="Medals", barmode="group") # stack parameters might be used for barmode. Various parameters are avaliable. Check documentation.
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
