This is a part of the Sentiment analysis project under the Winter of Code of IIT(ISM) Dhanbad.

The project aims at getting data from twitter API using tweepy library of python with #MeToo and then implementing sentiment analysis on the data collected

*dataExtraction
The tweets data is collected using tweepy which support for geocode by which tweets from a particular area can be extracted.
Also Tweets with any search query can be extracted.
The number of tweets to be extracted can be provided by the user.
The language of tweets can also be modified with ISO 639-1 code.


*dataProcessing
Every tweet collected is analysed using textblob library
