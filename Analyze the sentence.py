#!/usr/bin/env python
# coding: utf-8

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer


vectorizer = CountVectorizer(max_df=0.8,min_df=0.15) #choose the vectorizer you want
#vectorizer = TfidfVectorizer(max_df=0.8,min_df=0.15) #de-annotation if you wanna use tf-idf
def analyze_sentence(vectorizer, reviews):
    vectorizer.fit(reviews)
    X = vectorizer.transform(reviews).todense()
    rerurn X



