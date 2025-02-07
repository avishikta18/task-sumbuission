# -*- coding: utf-8 -*-
"""Copy of Welcome To Colaboratory

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1efnVR5qclAVsEM0oMnQJgisNsnjZLVug

<div class="markdown-google-sans">
  <h1>Welcome to Colab!</h1>
</div>

<!-- TODO(b/319266067) remove temporary advert after a few weeks. -->
<div class="markdown-google-sans">
  <h2>(New) Try the Gemini API</h2>
  <ul>
  <li><a href="https://colab.research.google.com/github/googlecolab/colabtools/blob/main/notebooks/Talk_to_Gemini_with_Google%27s_Speech_to_Text_API.ipynb?utm_medium=link&utm_campaign=gemini">Talk to Gemini with the Speech-to-Text API</a></li>
  <li><a href="https://colab.research.google.com/github/googlecolab/colabtools/blob/main/notebooks/Learning_with_Gemini_and_ChatGPT.ipynb?utm_medium=link&utm_campaign=gemini">Compare Gemini with ChatGPT</a></li>  
  <li><a href="https://colab.google/notebooks/?utm_medium=link&utm_campaign=gemini">More notebooks</a></li>
  </ul>
</div>
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
!pip install scikit-learn

insurance_dataset = pd.read_csv('/content/insurance.csv')

insurance_dataset .head()

insurance_dataset.shape

insurance_dataset.info()

insurance_dataset.isnull().sum()

insurance_dataset.describe()

sns.set()
plt.figure(figsize=(6,6))
sns.distplot(insurance_dataset['age'])
plt.title('Age Distribution')
plt.show()

plt.figure(figsize=(6,6))
sns.countplot(x='sex',data=insurance_dataset)
plt.title('Sex Distribution')
plt.show()

insurance_dataset['sex'].value_counts()



plt.figure(figsize=(6,6))
sns.distplot(insurance_dataset['bmi'])
plt.title('BMI Distribution')
plt.show()

plt.figure(figsize=(6,6))
sns.countplot(x='children',data=insurance_dataset)
plt.title('Children')
plt.show()

insurance_dataset['children'].value_counts()

plt.figure(figsize=(6,6))
sns.countplot(x='smoker',data=insurance_dataset)
plt.title('smoker')
plt.show()

insurance_dataset['smoker'].value_counts()

plt.figure(figsize=(6,6))
sns.countplot(x='region',data=insurance_dataset)
plt.title('region')
plt.show()

insurance_dataset['region'].value_counts()

plt.figure(figsize=(6,6))
sns.distplot(insurance_dataset['charges'])
plt.title('Charges Distribution')
plt.show()

insurance_dataset.replace({'sex':{'male':0,'female':1}},inplace=True)
insurance_dataset.replace({'smoker':{'yes':0,'no':1}},inplace =True)
insurance_dataset.replace({'region':{'southeast':0,'southwest':1,'northeast':2,'northwest':3}},inplace=True)

X = insurance_dataset.drop(columns='charges',axis=1)
Y = insurance_dataset['charges']

print(X)

print(Y)

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=2)

print(X.shape,X_train.shape,X_test.shape)

regressor = LinearRegression()

regressor.fit(X_train,Y_train)

training_data_prediction=regressor.predict(X_train)

r2_train = metrics.r2_score(Y_train,training_data_prediction)
print('R squared value : ',r2_train)

test_data_prediction=regressor.predict(X_test)

r2_test = metrics.r2_score(Y_test,test_data_prediction)
print('R squared value : ',r2_test)

input_data = [31,1,25.74,0,1,0]

input_data_as_numpy_array = np.asarray(input_data)
input_data_reshaped = np.asarray(input_data).reshape(-1, 1)

regressor = LinearRegression()

regressor.fit(input_data_reshaped,input_data)
prediction = regressor.predict(input_data_reshaped)

print(prediction)

print('the insurance cost is USD',prediction[0])