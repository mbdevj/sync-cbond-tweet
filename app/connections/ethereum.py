import time
import os
import sys
import twitter
import json
import requests
import web3.datastructures as wd
from web3 import Web3, HTTPProvider
from configparser import RawConfigParser

properties_file = os.getcwd() + "/resources/application.properties"
config = RawConfigParser()
config.read(properties_file, encoding=None)

try:
    ETHEREUM_CONTRACT = config.get("EthereumProperties", "ethereum.contract")
    ETHEREUM_ENDPOINT = config.get("EthereumProperties", "ethereum.provider")
except Exception as e:
    print('could not read configuration file')
    print(e)
    sys.exit(1)

# Instantiate connection to Ethereum Mainnet
w3 = Web3(HTTPProvider(ETHEREUM_ENDPOINT))
# Set contract to be used for filtering
checksum_address = w3.toChecksumAddress(ETHEREUM_CONTRACT)


def handle_event(event):
    print(event)
    dicts = json.loads(Web3.toJSON(event))
    print(dicts)
    token_id = str(int(dicts[0]['topics'][3], 16))
    print(token_id)
    bond_image = token_id + ".png"
    token_image = "https://img.syncbond.com/bond/" + bond_image
    print("link to cbond image: " + token_image)

    request = requests.get(token_image, stream=True)
    if request.status_code == 200:
        bond_image = "images/" + bond_image
        with open(bond_image, 'wb') as image:
            for chunk in request:
                image.write(chunk)
    twitter.update_status_with_media("This is a test tweet", bond_image)


def log_loop(event_filter, poll_interval):
    while True:
        os.environ['TZ'] = 'EST+05EDT,M4.1.0,M10.5.0'
        time.tzset()
        print(time.strftime('%X %x %Z') + " - Polling for events on " + ETHEREUM_CONTRACT)
        for event in event_filter.get_new_entries():
            # print(event)
            # print(w3.eth.(event))
            # exit(0)
            # w3.eth.getLogs(event)
            handle_event(event)
        time.sleep(poll_interval)


def main():
    event_filter = w3.eth.filter({"address": checksum_address})
    log_loop(event_filter, 2)


if __name__ == '__main__':
    main()