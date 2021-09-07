#!/usr/bin/env python
# coding: utf-8

def data_cleaning(scores):
    y=[] # if score less or equal to 3, we will assign it to 0 which mean bad review,otherwise we will assign it to 1 which means good review
    for i in range(len(scores)):
        if(scores[i]<=3):
            y.append(0)

        else:
            y.append(1)
    return y




