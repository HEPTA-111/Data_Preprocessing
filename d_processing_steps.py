# Import necessary libraries
import pandas as pd                 # Importing pandas for data manipulation
import numpy as np                  # Importing numpy for numerical operations
import seaborn as sns               # Importing seaborn for data visualization
import matplotlib.pyplot as plt     # Importing matplotlib for plotting

# Load the dataset
df = pd.read_csv('Data/diabetes.csv')  # Reading the dataset from a CSV file

# Display the first few rows of the dataset
print(df.head())

# Display information about the dataset including data types and missing values
print(df.info())

# Check for missing values in the dataset
print(df.isnull().sum())

# Descriptive statistics of the dataset
print(df.describe())

# Visualize outliers using box plots
fig, axs = plt.subplots(9, 1, dpi=95, figsize=(7, 17))  # Create subplots
i = 0
for col in df.columns:
    axs[i].boxplot(df[col], vert=False)  # Create a box plot for each column
    axs[i].set_ylabel(col)               # Set y-label
    i += 1
plt.show()

# Drop outliers for the 'Insulin' column
q1, q3 = np.percentile(df['Insulin'], [25, 75])         # Identify quartiles
iqr = q3 - q1                                           # Calculate interquartile range
lower_bound = q1 - (1.5 * iqr)                          # Calculate lower bound
upper_bound = q3 + (1.5 * iqr)                          # Calculate upper bound
clean_data = df[(df['Insulin'] >= lower_bound)          # Drop outliers
                & (df['Insulin'] <= upper_bound)]

# Similar procedure for other columns to drop outliers

# Visualize correlation between features using heatmap
corr = df.corr()
plt.figure(dpi=130)
sns.heatmap(df.corr(), annot=True, fmt='.2f')  # Create heatmap with correlation values
plt.show()
