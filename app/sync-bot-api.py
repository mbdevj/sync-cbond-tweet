#!/usr/bin/python3

from flask import Flask
from flask import render_template_string
from app.scenarios import bond_created
import os
from configparser import RawConfigParser


properties_file = os.getcwd() + "/resources/application.properties"
print(properties_file)
config = RawConfigParser()
config.read(properties_file, encoding=None)
debug_mode = config.get("FlaskSection", "flask.debug.mode")
print(debug_mode)

SYNC_BOND_API = '''
<html>\
    <body>\
        <strong><a href="http://0.0.0.0:5000/api/v1/tweet-crypto-bond-created?first-ticker=eth&first-qty=2\
        &second-ticker=sync&second-qty=109746&duration=90&apr=22&image-path=resources/bond.png">Sync Bond Created \
        API - Test\
        </a></strong>\
    </body>\
</html>
'''

app = Flask(__name__)


@app.route('/api/v1/tweet-crypto-bond-created', methods=["GET", "POST"])
def tweet_crypto_bond_created():
    app.logger.info("Processing request for 'tweet-crypto-bond-created'")
    return bond_created.tweet()


@app.route('/')
def home():
    return render_template_string(SYNC_BOND_API)


try:
    print(debug_mode)
    app.run(host='0.0.0.0', debug=False)
except Exception as e:
    print(e)
