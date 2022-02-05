import csv
from statistics import correlation
import numpy as np
import pandas as pd
import plotly.express as px

def getDataSource(dataPath):
    marks_in_percentage=[]
    days_present=[]
    with open(dataPath) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            marks_in_percentage.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))
    return {"x":marks_in_percentage,"y":days_present}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("correlation between marks in percentage and days present = \n--->",correlation[0,1])

def setUp():
    dataPath="Student Marks vs Days Present.csv"
    dataSource=getDataSource(dataPath)
    findCorrelation(dataSource)

def graphplot():
    df=pd.read_csv("cups of coffee vs hours of sleep.csv")
    fig=px.bar(df,x="week",y="Coffee in ml",color="sleep in hours",title="COFFEE INTAKE AND SLEEP TAKEN")
    fig.show()

setUp()
