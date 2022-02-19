import csv

import numpy as np
def getDataSource(data_path):
    week = []
    Coffe_in_ml = []
    sleep_in_hours = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            week.append(float(row["Week"]))
            Coffe_in_ml.append(float(row["Coffe in ml"]))
            sleep_in_hours.append(float(row["\tSleep time in week hours"]))

    return{"x" :week, "y": Coffe_in_ml, "z": sleep_in_hours}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"], datasource["z"])
    print("correlation between week, Coffe in ml and Sleep time in week hours : \n--->", correlation[0,1,2])

def setup():
    data_path = "coffe.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()