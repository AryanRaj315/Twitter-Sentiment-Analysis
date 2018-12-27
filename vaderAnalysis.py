#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 19:58:32 2018

@author: arnav04
"""
import csv
from nltk.sentiment.vader import SentimentIntensityAnalyzer as sent
sid=sent()
filew = open('SentimentsVader.csv', 'a')
writerFinal = csv.writer(filew)
#li=['neg','pos','neu','compound']
#sentiment analysis on each tweet
for i in range(data.shape[0]):
    text=data[i]
    snt = sid.polarity_scores(text)
    writerFinal.writerow((snt['neg'],snt['neu'],snt['pos'],snt['compound']))