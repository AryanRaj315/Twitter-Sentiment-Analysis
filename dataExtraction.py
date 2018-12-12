# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tweepy
import csv
 
#credentials
consumerKey = "gIUKz7MW2kbE7zNO97mq4yvi7"
consumerSecret = "rNV0kZQ8NzIiQkyUEMZzEM8bzatx1Iv9mKy5Ib9O30HFyZbdeA"
accessToken = "311381463-86fWlo6vntrEaDXKMROFTPeoxi6hnrodJiJ3SXUC"
accessTokenSecret = "qI6CvCeiP6BP2isgorfCgMoJojKKnR82U3pWMoZidww7e"

#Function to extract tweets
def get_tweets(no_of_tweets):
    
    #making the datafile
    file = open('tweetsData.csv', 'a')
    writer = csv.writer(file)
    
    #authorization using credentials
    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessTokenSecret)
    
    #Calling twitter API using tweepy
    api=tweepy.API(auth)
    
    #Searching the tweets
    MeTooTweets = tweepy.Cursor(api.search, q='MeToo',geocode="19.134876,72.893954,50km", tweet_mode='extended', lang='en').items(no_of_tweets)
    
    #Adding tweets to the datafile
    for tweet in MeTooTweets:
        writer.writerow([tweet.full_text])
    
