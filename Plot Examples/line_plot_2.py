import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv("data/nst-est2017-alldata.csv")

df2 = df[df["DIVISION"] == "1"] # I filtered data which i will work on it.
df2.set_index("NAME",inplace=True) # the value of NAME columns set as index verideki NAME sutunundaki değerleri index değeri olarak ayarladım.

population_list = [i for i in df2.columns if i.startswith("POP")] # working on the columns startswith "POP"
df2 = df2[population_list] # set df with population list

data = [go.Scatter(x=df2.columns, y = df2.loc[i], mode="lines", name=i) for i in df2.index] # mode line is required for line plot.
pyo.plot(data)
