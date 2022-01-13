import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# loading data det
data = pd.read_csv("D:\AI_ML_INERNSHIP\Project_SolarEnergy\dataset\SolarPrediction.csv")
print(data.head())

# data Analysis
print(data.info())
print(data.describe())


