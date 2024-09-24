# Zero Variance

# Python Libraries (Packages)
import pandas as pd

# Read data into Python
Z_data = pd.read_csv(r"F:\Liser Time\360digitmg\2.EDA\Data Sets\InClass_DataPreprocessing_datasets\Z_dataset.csv")
Z_data

Z_data.dtypes

print(Z_data['square.length'].var())
print(Z_data['square.breadth'].var())
print(Z_data['rec.Length'].var())
print(Z_data['rec.breadth'].var())

