#!/usr/bin/env python
# coding: utf-8

# In[ ]:
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.preprocessing import StandardScaler
from sklearn import tree
import lightgbm as lgb


model = LogisticRegression()#logistic regression
model = svm.SVC()#svm
model = tree.DecisionTreeClassifier()#decision_tree
model = lgb.LGBMClassifier() #lightGBM

def model_fitting(model, X, y, test_size):
    X_train,X_test,y_train,y_test = train_test_split(X.todense(),y,test_size=test_size,random_state=42) #split the data to train set and test set
    model.fit(X_train,y_train) #fit the model that you choose
    y_pred = model.predict(X_test) #predict
    print('training done')
    return y_pred
    