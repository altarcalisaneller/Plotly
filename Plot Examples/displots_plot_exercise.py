
#######
# Objective: Using the iris dataset, develop a Distplot
# that compares the petal lengths of each class.
# File: '../data/iris.csv'
# Fields: 'sepal_length','sepal_width','petal_length','petal_width','class'
# Classes: 'Iris-setosa','Iris-versicolor','Iris-virginica'
######

import plotly.offline as pyo
import plotly.figure_factory as ff
import pandas as pd
import scipy

df = pd.read_csv("data/iris.csv")

data1= df[df["class"]=="Iris-setosa"]["petal_length"]
data2= df[df["class"]=="Iris-versicolor"]["petal_length"]
data3= df[df["class"]=="Iris-virginica"]["petal_length"]

hist_data = [data1,data2,data3]
group_labels = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]

fig = ff.create_distplot(hist_data, group_labels)

pyo.plot(fig)
