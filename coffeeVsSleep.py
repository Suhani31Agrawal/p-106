import csv
from statistics import correlation
import numpy as np

def getDataSource(dataPath):
    coffee=[]
    sleep=[]
    with open(dataPath) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))
    return {"x":coffee,"y":sleep}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("correlation between coffee intake and sleep taken = \n--->",correlation[0,1])

def setUp():
    dataPath="cups of coffee vs hours of sleep.csv"
    dataSource=getDataSource(dataPath)
    findCorrelation(dataSource)

setUp()
