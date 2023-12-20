import pandas as pd
df_copy=pd.read_csv('heart.csv')

df_copy.target=df_copy.target.map({1:'Yes', 0:'No'})
df_copy.sex= df_copy.sex.map({1:'Male',0:'Female'})
df_copy.cp= df_copy.cp.map({0:'Normal',1:'Atypical Angina',2:'Non Anginal Pain', 3:'Asymptotic'})
df_copy.head()

import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('heart.csv')
x= df.drop(['target'], axis=1)
y = df['target']

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3,random_state=40)
model = LogisticRegression()
model.fit(X_train,y_train)

prediction= model.predict(X_test)
from sklearn.metrics import confusion_matrix

confusion_mtx=confusion_matrix(y_test,prediction)
confusion_mtx

import numpy as np

v = np.array([[63,1,3,145,233,1,0,150,0,2.3,0,0,1]])
print(model.predict(v))