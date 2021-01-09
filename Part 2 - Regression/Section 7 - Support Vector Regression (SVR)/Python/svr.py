# -*- coding: utf-8 -*-
"""SVR.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_EFcjTK9z68iO7zjAlSmp3NZYLbKSMTw

#Support Vector Regression [SVR]

## Importing the libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""## Importing the dataset"""

dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

print(X)

print(y)

y = y.reshape(len(y),1)

"""#Feature Scaling"""

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)

print(X)

print(y)

"""#Training the SVR model on the whole dataset"""

from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(X,y )

"""#Predict a new value
###we need to inverse feature scaling else we'll be getting 0.01150915 as a result which is not correct
"""

sc_y.inverse_transform(regressor.predict(sc_X.transform([[6.5]])))

"""#Visualising the SVR results """

import matplotlib.pyplot as plt
plt.scatter(sc_X.inverse_transform(X),sc_y.inverse_transform(y),color='g')
plt.plot(sc_X.inverse_transform(X),sc_y.inverse_transform(regressor.predict(X)))
plt.title('Truth or Bluff(SVR)')
plt.xlabel('Position Label')
plt.ylabel('Salary')
plt.show()

"""#Visualising the results of the SVR model (for higher resolution and smoother curve)"""

x_grid = np.arange(min(sc_X.inverse_transform(X)),max(sc_X.inverse_transform(X)), 0.1)
x_grid = x_grid.reshape((len(x_grid),1))
plt.scatter(sc_X.inverse_transform(X),sc_y.inverse_transform(y),color='g')
plt.plot(x_grid, sc_y.inverse_transform(regressor.predict(sc_X.transform(x_grid))))
plt.title('Truth or Bluff(SVR)')
plt.xlabel('Position Label')
plt.ylabel('Salary')
plt.show()

