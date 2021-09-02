import csv
import plotly.express as px
import pandas as pd

df = pd.read_csv("data.csv")

print(df.groupby("level")["attempt"].mean())

fig = px.scatter(x = df.groupby("level")["attempt"].mean(),
                 y = ['Level 1', 'Level 2', 'Level 3', 'Level 4'])

fig.show()