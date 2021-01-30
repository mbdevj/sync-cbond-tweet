#!/usr/bin/python3

from flask import request
import locale
from app.external_apis import twitter
from app.external_apis import coingecko
from babel.numbers import format_currency


def tweet():
    first_ticker = str(request.args["first-ticker"]).upper()
    first_qty = str(request.args["first-qty"])
    second_ticker = str(request.args["second-ticker"]).upper()
    second_qty = str(request.args["second-qty"])
    duration = str(request.args["duration"])
    apr = str(request.args["apr"])
    image_path = str(request.args["image-path"])

    if first_ticker == "ETH":
        first_long_name = "ethereum"
    elif first_ticker == "SYNC":
        first_long_name = "sync-network"

    if second_ticker == "ETH":
        second_long_name = "ethereum"
    elif second_ticker == "SYNC":
        second_long_name = "sync-network"

    first_total = format_currency(coingecko.get_price(first_long_name, "usd") * float(first_qty), 'USD', locale='en_US')
    second_total = format_currency(coingecko.get_price(second_long_name, "usd") * float(second_qty), 'USD', locale='en_US')

    tweet_text = "New " + duration + " day $SYNC #CryptoBond created with " \
                 + first_total + " $" + first_ticker + " and " + second_total + " $" + second_ticker \
                 + ", yielding an APR of " + apr + "%! Create yours now at https://syncbond.com!"

    try:
        twitter.update_status_with_media(tweet_text, image_path)
        message = "Successfully tweeted."
    except Exception as e:
        message = "Failed to tweet."
        print(e)

    return message