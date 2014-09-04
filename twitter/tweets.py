# MIT Licensed
# Copyright 2014 REM <rami.developer@gmail.com>.

import tweepy
from pymongo import MongoClient
import utility
import sys
import datetime
import subprocess

client = MongoClient('localhost', 27017)
db = client.uberly
clt = db.tweets

def save_tweet(tweet):
  try:
    clt.insert(tweet)
    return True
  except:
    print "Unexpected error: ", sys.exc_info()[0]
    return False

def print_tweets(tweets):
  for tweet in tweets:
    print '[' + str(tweet.created_at) + ']: <' + tweet.text + '>\n'

def print_tweet(tweet):
  print '[' + str(tweet.created_at) + ']: <' + tweet.text + '>\n'
  
auth = tweepy.OAuthHandler('', '')
auth.set_access_token('', '')

#api = tweepy.API(auth, proxy="127.0.0.1:8888")
api =  tweepy.API(auth)

query = '#uber'
count = 10
i = 1
added = 0
for status in tweepy.Cursor(api.search, q=query, count=count, lang='en').items():
  if i>1: break
  #print_tweet(status)
  tweet = {}
  tweet['text'] = status.text
  tweet['id'] = status.id
  tweet['created_at'] = status.created_at
  tweet['added'] = datetime.datetime.now()
  tweet['class'] = -1
  tweet['screenname'] = status.user.screen_name
  if save_tweet(tweet):
    added += 1 
  print '[', i, ']'
  utility.dump(tweet)
  i += 1
  #os.system('cd octave && octave predict.m "' + status.text.replace('"','\\"') + '"');

  proc = subprocess.Popen(['cd octave && octave -q predict.m "' + status.text.replace('"','\\"') + '"'], stdout=subprocess.PIPE, shell=True)
  (out, err) = proc.communicate()
  print "program output:", out
  
print 'Total added: ', added