# -*- coding: utf-8 -*-
"""4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FgtVklVN0vMTrR2n9GuwIgSHTi8nUPEv
"""

import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
import zipfile

# Path to the zip file
zip_path = '/content/HousePrice India.csv.zip'

# Unzipping the file
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall('/content')

# Assuming the extracted file is named 'HousePrice India.csv'
csv_path = '/content/HousePrice India.csv'

# Reading data from the CSV file
df = pd.read_csv(csv_path)

# Display original DataFrame with missing values
print("Original DataFrame:")
print(df.head())

# Selecting the column for imputation
house_prices = df[['Price']]

# Separate rows with and without missing values
# NOTE: No missing values in this dataset, so creating an artificial example
df_missing = house_prices.sample(n=10)  # Select 10 random rows for demonstration
df_complete = house_prices.drop(df_missing.index)  # Remove those rows from the complete set

# Split complete data into training and testing sets
X_train, X_test = train_test_split(df_complete, test_size=0.2, random_state=0)

# Scaling the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Define the neural network model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train_scaled.shape[1],)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mse')

# Train the model
model.fit(X_train_scaled, X_train, epochs=50, batch_size=32, validation_split=0.2)

# Impute missing values (now using the artificially created df_missing)
X_missing_scaled = scaler.transform(df_missing)
# ... rest of your code for imputation

# Impute missing values
X_missing_scaled = scaler.transform(df_missing)
df['HousePrice_DL'] = house_prices.copy()
df.loc[df_missing.index, 'HousePrice_DL'] = model.predict(X_missing_scaled)

# Display DataFrame after deep learning imputation
print("\nDataFrame after Deep Learning Imputation:")
print(df.head())

