import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv("data/2010SantaBarbaraCA.csv")

data = [go.Heatmap(x=df["DAY"], y=df["LST_TIME"], z=df["T_HR_AVG"], colorscale="JET")]
# z is about figures while others are categorical variables.
# colorscale is an optional parameter. JET is a common colorscale.
layout = go.Layout(title="City Degree")

fig = go.Figure(data=data,layout=layout)
pyo.plot(fig)
