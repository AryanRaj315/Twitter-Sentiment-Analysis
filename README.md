This is a part of the Sentiment analysis project under the Winter of Code of IIT(ISM) Dhanbad.

The project aims at getting data from twitter API using tweepy library of python with #MeToo and then implementing sentiment analysis on the data collected

*dataExtraction
The tweets data is collected using tweepy which support for geocode by which tweets from a particular area can be extracted.
Also Tweets with any search query can be extracted.
The number of tweets to be extracted can be provided by the user.
The language of tweets can also be modified with ISO 639-1 code.

*dataProcessing
The tweet data is collected in csv file which is then converted into a numpy array with every element of the array corresponding to a single tweet.Every tweet is then modified and scrapped using regex and a final modified tweet data csv file is created.

*textblobAnalysis
Finally textblob is used for sentiment analysis of the tweets and a csv file is created with entries between -1 and +1 where -1 indicates negative and +1 positive opinion

*vaderAnalysis
Vader uses NLTK lexicons and does analysis giving positive ,negative ,neutral and compound score.

*tweetsdata.JPG-Raw tweets data samples collected from twitter

*modifiedtweetsdata.JPG-Used REGEX for scrapping the data with only the key words

*Sentiments.JPG-Has four coloumns pos,neut,neg and compound giving scores from -1 to +1 for each tweet
