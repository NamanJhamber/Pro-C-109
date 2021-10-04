import random
import plotly.express as px
import plotly.figure_factory as ff
import csv
import pandas as pd

df=pd.read_csv("data2.csv")

fig=ff.create_distplot([df['Mobile Brand'].tolist()],['Weight'],show_hist=False)
fig.show()
