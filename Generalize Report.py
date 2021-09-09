#!/usr/bin/env python
# coding: utf-8

from sklearn.metrics import classification_report
def generalize_report(y_test,y_pred):
    r = classification_report(y_test,y_pred)
    print(r)



