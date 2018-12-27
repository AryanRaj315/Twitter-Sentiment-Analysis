#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 20:14:09 2018

@author: arnav04
"""
import textblob
from textblob import TextBlob

filew = open('Sentimentstextblob.csv', 'a')
writerFinal = csv.writer(filew)

#sentiment analysis on each tweet
for i in range(data.shape[0]):
    blob = TextBlob(data[i])
    writerFinal.writerow([blob.sentiment.polarity])