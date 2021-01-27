#!/usr/bin/python3

from flask import Flask, request
from ..Utilities import tweet

app = Flask(__name__)

@app.route('/api/v1/tweet', methods=["GET", "POST"])
def create_tweet():
    first_ticker = str(request.args["first-ticker"])
    first_qty = str(request.args["first-qty"])
    second_ticker = str(request.args["second-ticker"])
    second_qty = str(request.args["second-qty"])
    duration = str(request.args["duration"])
    apr = str(request.args["apr"])
    image_path = str(request.args["image-path"])

    tweet_text = "New " + duration + " day $SYNC #CryptoBond created using " \
    + first_qty + " $" + first_ticker + " and " + second_qty + " $" + second_ticker \
    + ", yielding an APR of " + apr + "%! Create yours now at https://syncbond.com." 

    try:
        tweet.update_status_with_media(tweet_text, image_path)
        message = "Successfully tweeted."
    except Exception as e:
        message = "Failed to tweet."
        print(e)

    return message

app.run(debug=False)
