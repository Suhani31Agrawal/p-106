import pandas as pd
import plotly.express as px

df=pd.read_csv("cups of coffee vs hours of sleep.csv")
fig=px.bar(df,x="week",y="Coffee in ml",color="sleep in hours",title="COFFEE INTAKE AND SLEEP TAKEN")
fig.show()