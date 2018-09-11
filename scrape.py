#Importing dependencies
import tweepy
import csv
import pandas as pd
import numpy as np
import os

#Credentials and Auth
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

#Terms to be searched. 
filename = "words.csv"
terms = []
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    terms = [term for row in list(csvreader) for term in row]

#Defining labelling logic.
def labelTweet(tweet):
    return np.random.randint(2)

#Scrape result from terms
clear = lambda: os.system('clear')
from time import sleep
#from IPython.display import clear_output

tweets = {}
filename = "tweets.csv"
f = csv.writer(open(filename, "a"))
count = 0
for term in terms:
    for tweet in tweepy.Cursor(api.search, q=term, count=100, lang="en").items():
        if tweet.text not in tweets:
            count = count + 1
            tweets[tweet.text] = labelTweet(tweet.text)
            f.writerow(['''"''' + tweet.text + '''"''', labelTweet(tweet.text)])
            print (term + " " + str(count))
            sleep(1)
            clear()
            #clear_output(wait = True)

