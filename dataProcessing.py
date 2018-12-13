#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 18:10:05 2018
@author: arnav04
"""

import numpy as np
import textblob
from textblob import TextBlob
import csv
import re

#file loading 
filer = open('tweetsData.csv', 'r')
reader=csv.reader(filer)
filew = open('Sentiment.csv', 'a')
writerFinal = csv.writer(filew)
filem = open('modifiedtweetsData.csv', 'a')
writer = csv.writer(filem)

#creating numpy array for the tweet data
data=np.array([])
for row in reader:
    data=np.append(data,row,axis=0)
    
#editing the data using regex
for i in range(data.shape[0]):
    data[i]=re.sub(r'^[^:]*:','',data[i])
    data[i]=re.sub(r'http\S+','',data[i])
    data[i]=re.sub(r'\\n','',data[i])
    data[i]=re.sub(r'\\x..','',data[i])
    data[i]=re.sub(r'\W',' ',data[i])
    writer.writerow(data[i])
    
#sentiment analysis on each tweet
for i in range(data.shape[0]):
    blob = TextBlob(data[i])
    writerFinal.writerow([blob.sentiment.polarity])
