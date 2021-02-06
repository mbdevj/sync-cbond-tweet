#!/usr/bin/python3

import tweepy
import sys
from configparser import RawConfigParser
import os

properties_file = os.getcwd() + "/resources/application.properties"

config = RawConfigParser()
config.read(properties_file, encoding=None)


try:
    CONSUMER_KEY = config.get("TwitterProperties", "twitter.consumer.key")
    CONSUMER_SECRET = config.get("TwitterProperties", "twitter.consumer.secret")
    ACCESS_KEY = config.get("TwitterProperties", "twitter.access.key")
    ACCESS_SECRET = config.get("TwitterProperties", "twitter.access.secret")
except Exception as e:
    print('could not read configuration file')
    print(e)
    sys.exit(1)


def update_status_with_media(tweet_text, image_path):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    api.update_with_media(image_path, tweet_text)
