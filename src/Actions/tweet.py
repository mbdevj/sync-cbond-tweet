#!/usr/bin/python3

import tweepy
from configparser import RawConfigParser

properties_file = '../resources/application.properties'

config = RawConfigParser()
config.read(properties_file)

CONSUMER_KEY = config.get('TwitterApiSection', 'twitter.consumer.key')
CONSUMER_SECRET = config.get('TwitterApiSection', 'twitter.consumer.secret')
ACCESS_KEY = config.get('TwitterApiSection', 'twitter.access.key')
ACCESS_SECRET = config.get('TwitterApiSection', 'twitter.access.secret')


def update_status_with_media(tweet_text, image_path):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    api.update_with_media(image_path, tweet_text)
