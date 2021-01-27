#!/usr/bin/python3

from flask import Flask, request
from src.Scenarios import bond_created

app = Flask(__name__)


@app.route('/api/v1/tweet-crypto-bond-created', methods=["GET", "POST"])
def tweet_crypto_bond_created():
    return bond_created.tweet()


app.run(debug=True)
