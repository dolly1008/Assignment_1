# -*- coding: utf-8 -*-
"""2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xH0VzLP_LMnicCbMmtggfhC4QqjmHZUS
"""



import pandas as pd
import numpy as np
from scipy.stats import mode
import zipfile
from sklearn.impute import KNNImputer

# Path to the zip file
zip_path = '/content/HousePrice India.csv.zip'

# Unzipping the file
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall('/content')

# Assuming the extracted file is named 'House Price India.csv'
csv_path = '/content/HousePrice India.csv'

# Reading data from the CSV file
df = pd.read_csv(csv_path)

# Display original DataFrame with missing values
print("Original DataFrame:")
print(df.head())

# Selecting the column for imputation
house_prices = df[['Price']]

# Initializing KNN Imputer
imputer = KNNImputer(n_neighbors=5)

# Applying KNN imputation
df['HousePrice_KNN'] = imputer.fit_transform(house_prices)

# Display DataFrame after KNN imputation
print("\nDataFrame after KNN Imputation:")
print(df.head())

