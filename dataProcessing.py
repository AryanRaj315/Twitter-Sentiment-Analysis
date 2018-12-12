#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 18:10:05 2018

@author: arnav04
"""

import numpy as np
import textblob
from textblob import TextBlob
import matplotlib.pyplot as plt
import csv

data=np.zeros(1)
file = open('tweetsData.csv', 'r')
reader=csv.reader(file)
for row in reader:
    data=np.append(data,row,axis=0)
print(data)

for i in range(data.shape[0]):
    blob = TextBlob(data[i])
    print(blob.sentiment)