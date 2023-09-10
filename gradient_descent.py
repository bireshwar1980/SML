# -*- coding: utf-8 -*-
"""Gradient Descent.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eZlq_IAZE9MuCVPtL7MQ4wNx71RJhGD9
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
X = np.array([1,2,3,4,5])
Y = np.array([5,7,9,11,13])
plt.scatter(X, Y)
plt.show()

m = 0
c = 0

L = 0.001  # The learning Rate
epochs = 1000  # The number of iterations to perform gradient descent

n = float(len(X)) # Number of elements in X

# Performing Gradient Descent
for i in range(epochs):
    Y_pred = m*X + c  # The current predicted value of Y
    cost=(1/n) * sum([val**2 for val in(Y - Y_pred)])
    D_m = (-2/n) * sum(X * (Y - Y_pred))  # Derivative wrt m
    D_c = (-2/n) * sum(Y - Y_pred)  # Derivative wrt c
    m = m - L * D_m  # Update m
    c = c - L * D_c  # Update c
    print("m {},c {},cost {}, epochs {}".format(m,c,cost,i))
    plt.plot(X,Y_pred,color='green')

print (m, c)
plt.plot(X,Y_pred,color='red')
