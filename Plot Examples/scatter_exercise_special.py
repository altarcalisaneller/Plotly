import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
import os

df = pd.read_csv("data/expense.csv",sep=";",decimal=",") # verideki sayı TR formatında olduğu için decimal parametresiyle tanımasını sağladım.

df["Tarih"] =  pd.to_datetime(df["Tarih"], dayfirst=True) # g.a.y şeklindeki veriyi datetime formatına çevirdim.

data = [go.Scatter(x=df["Tarih"], y=df["Tutar"], text=df["Hareket metni"], mode="markers")]

layout= go.Layout(title=df["Hesap"][0]+" "+df["Hesap Adı"][0] , hovermode="closest") # grafik ismini hesap kodu ve ismi olarak ayarladım.

fig = go.Figure(data=data, layout=layout)
fig.update_xaxes(tickformat="%d.%m.%Y", rangeslider_visible=True)
# grafikte x eksenindeki tarih formatını ayarladım. Belirlemezsem ay/yıl şeklinde veriyor sadece.
# rangeslider_visible altta kaydırma çubuğu ile ayarlama imkanı sağlıyor.

if not os.path.exists("images"):
    os.mkdir("images") # images isimli bir klasör yoksa oluşturur
    #fig.write_image(f"images/{layout.title.text}.png") # first you should install "pip install -U kaleido". grafiği kaydettim.
    fig.write_html(f"images/{layout.title.text}.html") # Interactive HTML Export
else:
    #fig.write_image(f"images/{layout.title.text}.png")
    fig.write_html(f"images/{layout.title.text}.html")

pyo.plot(fig)
