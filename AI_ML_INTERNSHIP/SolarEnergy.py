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

y = data['Radiation']
print(y.head())

predictors = ['Temperature', 'Pressure', 'Humidity', 'WindDirection(Degrees)', 'Speed']
target = ["Radiation"]
x = data[predictors].values
y = data[target].values
print(x)
print(y)


# Splitting the dataset

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size =0.30, random_state=0)
print(x_train, x_test, y_train, y_test)

# Scalling the numerical variable 
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

print(x_train, x_test)

# Training the model
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train, y_train)

print("Traning Score:", model.score(x_train, y_train))

# Training the randomforestRegressor model
from sklearn.ensemble import RandomForestRegressor
rf_model = RandomForestRegressor()
rf_model.fit(x_train, y_train)

print("Training Score:", rf_model.score(x_train, y_train))

# Testing on Real Time Data
temp = float(input("Enter the temp ="))
pressur = float(input("Enter the pressure  ="))
hum = float(input("Enter the Humidity="))
direction = float(input("Enter the direction ="))
speed = float(input("Enter the speed ="))

test_sample = [[temp, pressur, hum, direction, speed]]
test_sample = scaler.transform(test_sample)
result = rf_model.predict(test_sample)
print("Predicted Radiation= ", result)