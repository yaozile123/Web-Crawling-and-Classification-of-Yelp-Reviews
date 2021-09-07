#!/usr/bin/env python
# coding: utf-8

#import the packages we need for web crawler
import numpy as np
import pandas as pd
import json
import requests

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
            text=text.replace("&#39;","_").replace("<br>","") 
            
            reviews.append(text)
            scores.append(score)
            if(score not in scoresd):
                scoresd[score]=0
            scoresd[score]+=1
    return
    
'''
Here is the sample of review from yelp
"review: Great!  I love this place.  I found it by chance last fall while in NYC on a street photography trip.  Very friendly staff, tasty food at reasonable prices, good beers selection too.   I went back 3 times that week and would have gone again had my visit not come to an end.  There_s a beer garden-like court yard area and when the weather is good, like when I was there, they have all the doors open so a nice breeze was passing through the main eating area; sort of felt like a pleasant little greenhouse.  I_m no NYC expert but this place felt like a little oasis.",
      "score: 4",
      "total number of scores:{4: 104, 3: 633, 2: 286, 5: 22, 1: 130}"

'''




