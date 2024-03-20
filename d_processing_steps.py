# importing libraries

import pandas as pd
import scipy
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('Data/diabetes.csv')
print(df.head())

#check the data informtion
print(df.info())

#check the null values 
print(df.isnull().sum())

#describe the data 
print(df.describe())

#check outliners
# Box Plots
fig, axs = plt.subplots(9,1,dpi=95, figsize=(7,17))
i = 0
for col in df.columns:
	axs[i].boxplot(df[col], vert=False)
	axs[i].set_ylabel(col)
	i+=1
plt.show()
