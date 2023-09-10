# -*- coding: utf-8 -*-
"""LRDEMO.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16udqA8HnhpIyw9fi9HL1leQ04FbHZup-
"""

import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
from google.colab import files

uploaded = files.upload()

df = pd.read_csv('homeprices1.csv')
df

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
plt.xlabel('area')
plt.ylabel('price')
plt.scatter(df.area,df.price,color='red',marker='+')

new_dfx = df.drop('price',axis='columns')
new_dfx

new_dfy = df.drop('area',axis='columns')
new_dfy

from sklearn.model_selection import train_test_split

new_dfx_train, new_dfx_test, new_dfy_train, new_dfy_test = train_test_split(new_dfx, new_dfy, test_size=0.2, random_state=0)

new_dfx_train

new_dfx_train.shape

new_dfy_train

new_dfy_train.shape

new_dfx_test.shape

new_dfy_test.shape

new_dfy_test

new_dfx_test

from sklearn.linear_model import LinearRegression

reg = LinearRegression()

reg.fit(new_dfx_train, new_dfy_train)

reg.coef_

reg.intercept_

y_pred = reg.predict(new_dfx_test)

y_pred

new_dfx_test['Predicted price']=y_pred
new_dfx_test

new_dfx_test['Actual price']=new_dfy_test
new_dfx_test

from google.colab import drive
drive.mount('/content/drive')

#area_df.to_csv("prediction.csv")

new_dfx_test.to_csv('/content/drive/My Drive/mydata1.csv', index=True)
new_dfx_test.to_csv('/content/drive/My Drive/prediction.csv', index=False)

from google.colab import files

uploaded = files.upload()
area_df = pd.read_csv("areas1.csv")
area_df.head(3)

p = reg.predict(area_df)
p

area_df['prices']=p
area_df

area_df.to_csv('/content/drive/My Drive/myprediction.csv', index=True)

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
X = np.array(new_dfx_train)
Y = np.array(new_dfy_train)
plt.scatter(X, Y)
plt.show()

m = 0
c = 0

L = 0.0001  # The learning Rate
epochs = 1000  # The number of iterations to perform gradient descent

n = float(len(X)) # Number of elements in X

# Performing Gradient Descent
for i in range(epochs):
    Y_pred = m*X + c  # The current predicted value of Y
    D_m = (-2/n) * sum(X * (Y - Y_pred))  # Derivative wrt m
    D_c = (-2/n) * sum(Y - Y_pred)  # Derivative wrt c
    m = m - L * D_m  # Update m
    c = c - L * D_c  # Update c
    plt.plot(X,Y_pred,color='green')

print (m, c)
plt.plot(X,Y_pred,color='red')