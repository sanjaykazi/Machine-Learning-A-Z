# -*- coding: utf-8 -*-
"""Multiple_Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P0K7_JL6VHEnxv6dL6IgLnylN2b6gN10

#Multiple Regression

need to apply one hot encoding as there is 3 categorical data is state category feature.

## Importing the libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""## Importing the dataset"""

dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

print(X)

"""##Encoding categorical dataset
###Using One Hot Encoding
"""

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [3])], remainder='passthrough')
X = np.array(ct.fit_transform(X))

"""## Splitting the dataset into the Training set and Test set"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

"""##Training the Multiple Linear Model on the Training Set"""

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)

"""##Predicting the test set results
### Ploting vectors of real text values and then predicted test values
"""

y_pred = regressor.predict(X_test)

np.set_printoptions(precision=2)
print(np.concatenate((y_pred.reshape(len(y_pred),1),y_test.reshape(len(y_test),1)),axis=1))

"""MAKING A SINGLE PREDICTION"""

print(regressor.predict([[1,0,0, 160000, 130000, 300000]]))

"""##Gettingt the final multiple regression equations with the values of coeffircients."""

print(regressor.coef_)
print(regressor.intercept_)

