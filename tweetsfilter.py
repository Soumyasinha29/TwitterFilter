

import tweepy
import csv
import pandas as pd
import sys
import datetime as dt

consumer_key= '****'
consumer_secret= '****'
access_token= '****'
access_token_secret= '****'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

# Search word/hashtag value 
search_words = ""

# search start date value. the search will start from this date to the current date.
StartDate = ""
EndDate = ""
search_loc = ""

# getting the search word/hashtag and date range from user
search_words = input("Enter the search words you want the tweets to be downloaded for: ")
StartDate = input("Enter the start date in this format yyyy-mm-dd: ")
EndDate = input("Enter the end date in this format yyyy-mm-dd: ")
search_loc = input("Enter the location you want the tweets to be from ")
limit = 1000

# Open/Create a file to append data
csvFile = open(search_words+'.csv', 'a')

#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q=search_words,count=50,lang="en",since=StartDate,till = EndDate, loc=search_loc,limit = limit,tweet_mode='extended').items():
    print (tweet.created_at, tweet.full_text)
    csvWriter.writerow([tweet.created_at, tweet.full_text.encode('utf-8')])


print ("Scraping finished and saved to "+search_words+".csv")
#sys.exit()search_words

