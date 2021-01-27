#!/usr/bin/python

import tweepy

CONSUMER_KEY = "XXXXXXXX"
CONSUMER_SECRET = "XXXXXXXX"
ACCESS_KEY = "XXXXXXXX"
ACCESS_SECRET = "XXXXXXXX"

def update_status_with_media(tweet_text, image_path):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

    api.update_with_media(image_path, tweet_text)
