# -*- coding: utf-8 -*-
"""Copy of Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/avishikta18/random-forest-regression-/blob/main/Copy%20of%20Untitled1.ipynb
"""

# prompt: import pandas as pd

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
!pip install random-forest-mc
!pip install  scikit-learn==0.23.2

train = pd.read_csv('/content/Titanic-Dataset.csv')

print(train.shape)

train.head

NAs = pd.concat([train.isnull().sum()], axis=1, keys=["Train"])
NAs.loc[NAs.sum(axis=1) > 0]

train["Age"]=train["Age"].fillna(train["Age"].mean())

train["Embarked"]=train["Embarked"].fillna(train["Embarked"].mode()[0])

train["Cabin"]=train["Cabin"].fillna(train["Cabin"].mode()[0])

train["Pclass"]=train["Pclass"].apply(str)

for col in train.dtypes[train.dtypes=="object"].index:
    for_dummy=train.pop(col)
    train = pd.concat([train,pd.get_dummies(for_dummy,prefix=col)],axis=1)
train.head()

labels=train.pop("Survived")

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(train,labels,test_size=0.25)

from sklearn.ensemble import RandomForestClassifier
rf=RandomForestClassifier()
x_train['PassengerId'] = x_train['PassengerId'].astype(float)

RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
                      max_depth=None, max_features='auto', max_leaf_nodes=None,
                      min_impurity_decrease=0.0,
                      min_samples_leaf=1, min_samples_split=2,
                      min_weight_fraction_leaf=0.0, n_estimators=10,
                      n_jobs=None, oob_score=False, random_state=None,
                      verbose=0, warm_start=False)

rf = RandomForestClassifier()
rf.fit(x_train.select_dtypes("number"), y_train)

y_pred = np.array([0, 1, 0, 1])

from sklearn.metrics import roc_curve, auc

y_test = np.array([1, 0, 1, 0, 1])
y_pred = np.array([0.8, 0.2, 0.9, 0.1, 0.7])

false_positive_rate, true_positive_rate, thresholds = roc_curve(y_test, y_pred)
roc_auc = auc(false_positive_rate, true_positive_rate)

print(roc_auc)

n_estimators=[1,2,4,16,32,64,100,200]
train_results = []
test_results= []
for estimator in n_estimators:
  rf = RandomForestClassifier(n_estimators=estimator, n_jobs=-1)

  rf.fit(x_train, y_train)

  train_pred=rf.predict(x_train)
  false_positive_rate, true_positive_rate, threshold = roc_curve(y_train,train_pred)
  roc_auc = auc(false_positive_rate,true_positive_rate)
  train_results.append(roc_auc)
  y_pred=rf.predict(x_test)

  roc_auc=auc(false_positive_rate,true_positive_rate)
  test_results.append(roc_auc)
  false_positive_rate,true_positive_rate, threshold = roc_curve(y_test,y_pred)
  np.array()
  X = X.reshape(X.shape[5:223])
  X = X.transpose()
from matplotlib.legend_handler import HandlerLine2D
line1, = plt.plot(n_estimators, train_results, "b", label="Train AUC")
line2, = plt.plot(n_estimators, test_results, "r", label="Test AUC")
plt.legend(handles=[line1, line2])
plt.ylabel("AUC score")
plt.xlabel("n_estimators")
plt.show()

