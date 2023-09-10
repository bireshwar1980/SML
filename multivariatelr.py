# -*- coding: utf-8 -*-
"""MultivariateLR.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oXeoxCq1_OlkCnkmDwsgNiufJZkqDGBU
"""

import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
from google.colab import files

uploaded = files.upload()
df1 = pd.read_csv('homepricesMV.csv')
df1

df1.bedrooms.median()

df1.bedrooms = df1.bedrooms.fillna(df1.bedrooms.median())
df1

reg1 = linear_model.LinearRegression()
reg1.fit(df1.drop('price',axis='columns'),df1.price)

reg1.coef_

reg1.intercept_

from warnings import filterwarnings
filterwarnings(action='ignore')
reg1.predict([[3000, 3, 40]])

112.06244194*3000 + 23388.88007794*3 + -3231.71790863*40 + 221323.00186540384

reg1.predict([[2500, 4, 5]])

from google.colab import files

uploaded = files.upload()

df2 = pd.read_csv("MVT.csv")
df2.head(3)

pp = reg1.predict(df2)
pp

df2['prices']=pp
df2

from google.colab import drive
drive.mount('/content/drive')

df2.to_csv('/content/drive/My Drive/mvprediction.csv', index=True)