#!/usr/bin/python3

from flask import Flask, request
from utilities import sync_bond_tweet

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
    try:
        sync_bond_tweet.tweet(first_ticker, first_qty, second_ticker, second_qty, duration, apr, image_path)
        message = "Successfully tweeted."
    except Exception as e:
        message = "Failed to tweet."
        print(e)

    return message

app.run(debug=False)
