#######
# Objective: Using the file 2010YumaAZ.csv, develop a Line Chart
# that plots seven days worth of temperature data on one graph.
# You can use a for loop to assign each day to its own trace.
######

import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv("data/2010YumaAZ.csv")

days = pd.unique(pd.Series(df["DAY"]))

df.set_index("DAY",inplace=True)

data = [go.Scatter(x=df.loc[i]["LST_TIME"], y = df.loc[i]["T_HR_AVG"], mode="lines", name=i) for i in days]
layout = go.Layout(title="Temparatures")
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
