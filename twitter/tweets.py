# MIT Licensed
# Copyright 2014 REM <rami.developer@gmail.com>.

import tweepy
from pymongo import MongoClient
import utility
import sys
import datetime
import os
import subprocess

proc = subprocess.Popen(['cd octave && octave -q predict.m "Aggressive growth strategy for #Uber http://t.co/Bre8zukWRB by @semilshah | Boom! Exciting. http://t.co/OCtW9WBmLh"'], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
print "program output:", out
exit()

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
  
#auth = tweepy.OAuthHandler('', '')
#auth.set_access_token('', '')
auth = tweepy.OAuthHandler('WTAkclxY6ROtIHxOIv5yfD0Jd', 'FG3O5xhkB40SS5VOHSPkUVJLK2chnHo8qAZKFuA42k7sJAEPx0')
auth.set_access_token('12969442-25I4FUpAsPFrDEVhFpd3dM0YTrKMQmfp4jf2hXVAU', 'a63TefhlMDPlQK4aOUJME7DLZqYThxm3EFcCnm8HYjYsd')

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