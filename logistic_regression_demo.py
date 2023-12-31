# -*- coding: utf-8 -*-
"""LogRDemo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zTYx3HkMB0ffFUUoyahlV__-fbARrufS
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
from matplotlib import pyplot as plt
# %matplotlib inline
from sklearn import linear_model
from google.colab import files
uploaded = files.upload()

df = pd.read_csv("insdata.csv")
df.head()

plt.scatter(df.age,df.bought_insurance,marker='+',color='red')

newmv_dfx = df.drop(df.columns[[1]],axis = 1)
newmv_dfx

newmv_dfy = df.drop(df.columns[[0]],axis = 1)
newmv_dfy

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(df[['age']],df.bought_insurance,train_size=0.8)

newmv_dfx_train, newmv_dfx_test, newmv_dfy_train, newmv_dfy_test = train_test_split(newmv_dfx, newmv_dfy, test_size=0.2, random_state=0)

X_train

X_test

y_train

y_test

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

model.fit(X_train,y_train)

model.fit(newmv_dfx_train,newmv_dfy_train)

y_predicted = model.predict(X_test)

y_predicted

model.predict_proba(X_test)

Y_predicted = model.predict(newmv_dfx_test)

Y_predicted

K= newmv_dfx_test.values

K

model.predict_proba(K)

model.predict_proba(newmv_dfx_test)

X_test['Predicted bought_insurance']=y_predicted
X_test

newmv_dfx_test['Predicted bought_insurance']=Y_predicted

newmv_dfx_test

X_test['Actual bought_insurance']=y_test
X_test

newmv_dfx_test['Actual bought_insurance']=newmv_dfy_test

newmv_dfx_test

model.predict([[5]])

model.predict([[95]])

model.coef_

model.intercept_

import math
def sigmoid(x):
  return 1 / (1 + math.exp(-x))

def prediction_function(age):
    z = 0.11 * age - 4.61 # 0.11216016 ~ 0.11 and -4.60960684 ~ -4.61
    y = sigmoid(z)
    return y

age = 35
prediction_function(age)

age = 43
prediction_function(age)