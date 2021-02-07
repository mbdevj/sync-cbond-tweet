import time
import os
import sys
import requests
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

w3 = Web3(HTTPProvider(ETHEREUM_ENDPOINT))
checksum_address = w3.toChecksumAddress(ETHEREUM_CONTRACT)


def handle_event(event):
    block_id = (event['transactionHash'])
    print(event)
    print("Processing transactionHash: " + str(block_id.hex()))
    token_id = int((event['topics'][3]).hex(), 16)
    bond_image = str(token_id) + ".png"
    token_image = "https://img.syncbond.com/bond/" + bond_image
    print("link to cbond image: " + token_image)

    request = requests.get(token_image, stream=True)
    if request.status_code == 200:
        bond_image = "images/" + bond_image
        with open(bond_image, 'wb') as image:
            for chunk in request:
                image.write(chunk)
    print("Send tweet after all variables taken")
    # UNCOMMENT BELOW LINE WHEN WE HAVE ALL THE VARIABLES NEEDED FOR TWEETING
    # twitter.update_status_with_media("This is a test tweet", bond_image)


def log_loop(event_filter, poll_interval, is_test):
    os.environ['TZ'] = 'EST+05EDT,M4.1.0,M10.5.0'
    time.tzset()
    message = time.strftime('%X %x %Z') + " - Polling for events on " + ETHEREUM_CONTRACT
    if not is_test:
        while True:
            print(message)
            for event in event_filter.get_all_entries():
                handle_event(event)
            time.sleep(poll_interval)
    else:
        print(message)
        for event in event_filter.get_all_entries():
            handle_event(event)
        time.sleep(poll_interval)



def main():
    is_test = True
    event_signature = w3.sha3(text="Transfer(address,address,uint256)").hex()
    if is_test:
        event_filter = w3.eth.filter({"address": checksum_address, 'fromBlock': 11774988, 'toBlock': 'latest', 'topics': [event_signature]})
    else:
        event_filter = w3.eth.filter({"address": checksum_address, 'fromBlock': 'latest', 'topics': [event_signature]})
    log_loop(event_filter, 2, is_test)


if __name__ == '__main__':
    main()