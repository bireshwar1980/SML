# -*- coding: utf-8 -*-
"""LRMV.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HcRC48S8pXHBLShNUN6MImuMcbm53wgc
"""

import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
from google.colab import files
uploaded = files.upload()

mvdf = pd.read_csv('homepricesmv1.csv')
mvdf

mvdf.bedrooms.median()

mvdf.bedrooms = mvdf.bedrooms.fillna(mvdf.bedrooms.median())
mvdf

newmv_dfx = mvdf.drop('price',axis='columns')
newmv_dfx

newmv_dfy = mvdf.drop(mvdf.columns[[0,1, 2]],axis = 1)
newmv_dfy

from sklearn.model_selection import train_test_split

newmv_dfx_train, newmv_dfx_test, newmv_dfy_train, newmv_dfy_test = train_test_split(newmv_dfx, newmv_dfy, test_size=0.2, random_state=0)

newmv_dfx_train

newmv_dfx_test

newmv_dfy_train

newmv_dfy_test

reg2 = linear_model.LinearRegression()
reg2.fit(newmv_dfx_train,newmv_dfy_train)

reg2.coef_

reg2.intercept_

y_pred = reg2.predict(newmv_dfx_test)

y_pred

newmv_dfx_test['Predicted price']=y_pred
newmv_dfx_test

newmv_dfx_test['Actual price']=newmv_dfy_test
newmv_dfx_test

data_actual = newmv_dfx_test.drop(newmv_dfx_test.columns[[0,1, 2,3]],axis = 1)
data_actual

data_predict = newmv_dfx_test.drop(newmv_dfx_test.columns[[0,1, 2,4]],axis = 1)
data_predict

from google.colab import drive
drive.mount('/content/drive')

#area_df.to_csv("prediction.csv")

newmv_dfx_test.to_csv('/content/drive/My Drive/mvprediction.csv', index=False)

from google.colab import files

uploaded = files.upload()
homeprices_df = pd.read_csv("homepricesMVF1.csv")
homeprices_df.head(3)

mvp = reg2.predict(homeprices_df)
mvp

homeprices_df['prices']=mvp
homeprices_df

homeprices_df.to_csv('/content/drive/My Drive/mypredictionmv.csv', index=True)

from sklearn.metrics import r2_score
score = r2_score(data_actual, data_predict)
print("The accuracy of our model is {}%".format(round(score, 2) *100))

from sklearn.metrics import mean_absolute_error
mae_score = mean_absolute_error(data_actual, data_predict)
print("The Mean Absolute Error of our Model is {}".format(round(mae_score, 2)))

from sklearn.metrics import mean_squared_error
import numpy as np
rmae_score = mean_squared_error((data_actual, data_predict))
print("The Mean Absolute Error of our Model is {}".format(round(rmae_score, 2)))

plt.scatter(data_actual, data_predict);
plt.xlabel('Actual');
plt.ylabel('Predicted');

import seaborn as sns

sns.regplot(x=data_actual,y=data_predict,ci=None,color ='red');