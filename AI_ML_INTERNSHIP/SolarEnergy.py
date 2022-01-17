import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# loading data det
data = pd.read_csv("D:\AI_ML_INERNSHIP\Project_SolarEnergy\dataset\SolarPrediction.csv")
print(data.head())

# data Analysis
print(data.info())
print(data.describe())

# extracting input and output variables
x = data.drop(['Data', 'Time', 'TimeSunSet', 'Radiation'], axis=1)
print(x.head())

y= data['Radiation']
print(y.head())

predictors = ['Temperature','Pressure','Humidity','WindDirection(Degrees)','Speed']
target = ["Radiation"]
x= data[predictors].values
y= data[target].values
print(x)
print(y)

