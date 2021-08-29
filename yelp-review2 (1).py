#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import json
import requests
import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
ua="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
headers={"User-Agent":ua}

reviews=[]
scores=[]
scoresd={}
def get_review_content(baseurl,start,end):
    
    for i in range(start,end,10):
        url=baseurl + "&start={}".format(i)
        #print(url)

        resp = requests.get(url,headers=headers)
        jsnStr=json.loads(resp.text)
        if(len(jsnStr['reviews'])==0):
            print("no more comments, stopping")
            break
        for review in jsnStr['reviews']:
            text=review['comment']['text']
            score=review["rating"]
            #print(json.dumps(review,indent=2))
            text=text.replace("&#39;","_").replace("<br>","")
            
            reviews.append(text)
            scores.append(score)
            if(score not in scoresd):
                scoresd[score]=0
            scoresd[score]+=1
    return



# In[2]:


burl="https://www.yelp.com/biz/FH978pIP1TLRuPAH-MbWIQ/review_feed?rl=en&q=&sort_by=rating_asc"
burl2="https://www.yelp.com/biz/EGS6y6WsPkNs8PZ2X6bHOA/review_feed?rl=en&q=&sort_by=relevance_desc"
get_review_content(burl2,400,900)


# # take a look on example data

# In[3]:


example_index=0
print("review: {}".format(reviews[example_index]))
print("score: {}".format(scores[example_index]))

print(scoresd)


# In[4]:


#scikit-learn

#bag of words


#this is a document
#this is another document

#this=0, is=1, a=2, another=3, document=4
#[1,1,1,0,1]
#[1,1,0,1,1]


# In[21]:


from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(max_df=0.8,min_df=0.15)

vectorizer.fit(reviews)
X=vectorizer.transform(reviews)#result in sparse matrix

y=[]
for i in range(len(scores)):
    if(scores[i]<=3):
        y.append(0)

    else:
        y.append(1)

# print(X)
print(X.todense())
print(X.shape)
print(vectorizer.get_feature_names())
print(len(y))


# # In[22]:
#
#
# #80% train, 20% test
# #60% train, 20% validate, 20% test
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X.todense(),y,test_size=0.21,random_state=42)
print(X_train.shape)
print(X_test.shape)
print(y_test)
#
#
# # In[23]:
#
#
# #accuracy, precision, recall, F-score
#
# # true positive  / total
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

model.fit(X_train, y_train)
print("training done.")

y_pred = model.predict(X_test)
print(y_pred)
# #baseline
#
#
# # In[24]:
#
#
# #True Positive  TP
# #False Positive FP
# #True Negative  TN
# #False Negative FN
#
# P= TP/(TP+FP) Recall = TP/(TP+FN)
# #F = 2* (precision * recall)/  (precision + recall)
#
from sklearn.metrics import classification_report

r = classification_report(y_test,y_pred)
print(r)


# In[25]:


from sklearn import svm
from sklearn.preprocessing import StandardScaler


#regularization
sc = StandardScaler()

xtrain = sc.fit_transform(X_train)
xtest = sc.transform(X_test)

model = svm.SVC()
model.fit(xtrain, y_train)
y_pred = model.predict(xtest)
print(y_pred)
r = classification_report(y_test,y_pred)
print(r)
#
#
# # In[ ]:
#
#
# #Gradient Boosting Tree
# #TF-IDF
# #lightGBM

