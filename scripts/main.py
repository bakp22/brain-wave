#: this script will help load and preprocess the EEG data

#: python data analysis library
import pandas as pd
import matplotlib.pyplot as plt

#: filepath for EEG data
file = "../data/data.csv"

#: reading the dataset
read_file = pd.read_csv(file)

#: displays the first few rows of the dataset
print(read_file.head())

print("---------------------------------------------------------")

print(read_file.describe())

print("---------------------------------------------------------")

print(read_file.info())

#: makes the read file a plot 
read_file.plot()

#: display plot 
plt.show()