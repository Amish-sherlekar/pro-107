import pandas as pd
import plotly.graph_objects as go
df = pd.read_csv("data.csv")

studentdf=df.loc[df['student_id']=="TRL_987"]
r = studentdf.groupby("level")["attempt"].mean()

print(r)

fig=go.Figure(go.Bar(
    x=r,
    y=['Level 1','Level 2','Level 3','Level 4'],
    orientation='h'
))
fig.show()