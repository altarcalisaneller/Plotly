import plotly.offline as pyo
import plotly.graph_objs as go
from plotly import subplots
import pandas as pd

# multiple heatmaps with subplots

df1 = pd.read_csv("data/2010SitkaAK.csv")
df2 = pd.read_csv("data/2010SantaBarbaraCA.csv")
df3 = pd.read_csv("data/2010YumaAZ.csv")

trace1 = go.Heatmap(x=df1["DAY"], y=df1["LST_TIME"], z=df1["T_HR_AVG"], colorscale="JET", zmin=5, zmax=40)
# you should give zmin and zmax value. Because the scale should be common for 3 figure. Otherwise, the numbers are shown as nested.
trace2 = go.Heatmap(x=df2["DAY"], y=df2["LST_TIME"], z=df2["T_HR_AVG"], colorscale="JET",zmin=5, zmax=40)
trace3 = go.Heatmap(x=df3["DAY"], y=df3["LST_TIME"], z=df3["T_HR_AVG"], colorscale="JET",zmin=5, zmax=40)

fig = subplots.make_subplots(rows=1, cols=3, shared_yaxes=True, subplot_titles=["SitkaAK","SantaBarbaraCA","YumaAZ"])
# row=1 means, all figures should be on 1 row.
# cols=3 means, all figures should be shown on fig seperately (as 3 columns)
# shared_yaxes=True means y values of all traces are same. So, only one y axis is shown. If you set False, y values for each trace is shown seperately.

fig.append_trace(trace1,1,1) # the first number represents the number of row. the second is column number.
fig.append_trace(trace2,1,2)
fig.append_trace(trace3,1,3)

fig["layout"].update(title="Temps for 3 cities") # set the main fig title

pyo.plot(fig)
