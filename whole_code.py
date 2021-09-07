#!/usr/bin/env python
# coding: utf-8

# In[88]:


import numpy as np
import pandas as pd
import json
import requests
# import sys
# import io


# ## set the http-headers

# In[89]:


ua="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36" 
headers={"User-Agent":ua} #environment setting


# 

# In[90]:


reviews=[]
scores=[]
scoresd={}
def get_review_content(baseurl,start,end):
    
    for i in range(start,end,10):
        url=baseurl + "&start={}".format(i)
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
    return 'crawling finished'


# In[91]:


burl="https://www.yelp.com/biz/FH978pIP1TLRuPAH-MbWIQ/review_feed?rl=en&q=&sort_by=rating_asc"
burl2="https://www.yelp.com/biz/EGS6y6WsPkNs8PZ2X6bHOA/review_feed?rl=en&q=&sort_by=relevance_desc"
get_review_content(burl2,0,1000)


# In[92]:


# # take a look on example data
example_index=0
print("review: {}".format(reviews[example_index]))
print("score: {}".format(scores[example_index]))

print(scoresd) # see how the score distributed


# In[108]:


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

# vectorizer = CountVectorizer(max_df=0.8,min_df=0.15)
vectorizer = TfidfVectorizer(max_df=0.8,min_df=0.15)

vectorizer.fit(reviews)
X=vectorizer.transform(reviews)#result in sparse matrix


# In[94]:


y=[] # if score less or equal to 3, we will assign it to 0 which mean bad review,otherwise we will assign it to 1 which means good review
for i in range(len(scores)):
    if(scores[i]<=3):
        y.append(0)

    else:
        y.append(1)


# In[95]:


print(X.todense()[0])
print('----')
print(X[0])
print(X.shape)
print(reviews[0])
print(len(reviews))
print(len(reviews[0]))
print(vectorizer.get_feature_names())
print(len(y))


# In[96]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X.todense(),y,test_size=0.21,random_state=42) #split the data to train set and test set
print(X_train.shape)
print(X_test.shape)
print(y_test)


# In[97]:


from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

model.fit(X_train, y_train)
print("training done.")


# In[98]:


y_pred = model.predict(X_test)
print(y_pred)


# In[99]:


from sklearn.metrics import classification_report

r = classification_report(y_test,y_pred)
print(r)


# In[100]:


from sklearn import svm
from sklearn.preprocessing import StandardScaler


#regularization
sc = StandardScaler()

xtrain = sc.fit_transform(X_train)
xtest = sc.transform(X_test)


# In[101]:


model = svm.SVC()
model.fit(xtrain, y_train)
y_pred = model.predict(xtest)
print(y_pred)
r = classification_report(y_test,y_pred)
print(r)


# In[102]:


from sklearn import tree
tr = tree.DecisionTreeClassifier()
tr.fit(X_train, y_train)
print("training done.")


# In[103]:


tree_predict = tr.predict(X_test)
print(tree_predict)
rc = classification_report(y_test,tree_predict)
print(rc)


# In[104]:


from sklearn.ensemble import GradientBoostingClassifier
gdb = GradientBoostingClassifier() #取长补短
gdb.fit(X_train, y_train)
print("training done.")


# In[105]:


gdb_pred = gdb.predict(X_test)
gdb_report = classification_report(y_test,gdb_pred)
print(gdb_report)


# In[106]:


import lightgbm as lgb
rng = lgb.LGBMClassifier()
rng.fit(X_train, y_train)
print('training done')


# In[107]:


rng_pred = rng.predict(X_test)
rng_report = classification_report(y_test,rng_pred)
print(rng_report)


# In[ ]:




