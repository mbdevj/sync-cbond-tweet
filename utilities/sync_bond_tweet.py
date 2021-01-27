#!/usr/bin/python

import sys, getopt
import tweepy

CONSUMER_KEY = "XXXXXXXX"
CONSUMER_SECRET = "XXXXXXXX"
ACCESS_KEY = "XXXXXXXX"
ACCESS_SECRET = "XXXXXXXX"

def tweet(first_ticker, first_qty, second_ticker, second_qty, duration, apr, image_path):
    first_ticker = first_ticker.upper()
    second_ticker = second_ticker.upper()

    tweet_text = "New " + duration + " day $SYNC #CryptoBond created using " \
    + first_qty + " $" + first_ticker + " and " + second_qty + " $" + second_ticker \
    + ", yielding an APR of " + apr + "%! Create yours now at https://syncbond.com." 

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

    api.update_with_media(image_path, tweet_text)
