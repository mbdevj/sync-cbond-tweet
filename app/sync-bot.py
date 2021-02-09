#!/usr/bin/python3

import time
import os
import platform
from utilities import event_signatures
from utilities import parameters_handler
from utilities import event_processor
from connections import web3driver

ETHEREUM_CONTRACT = parameters_handler.get_eth_contract()
w3 = web3driver.get_web3_session(parameters_handler.get_eth_endpoint())
checksum_address = w3.toChecksumAddress(ETHEREUM_CONTRACT)
operating_system = platform.system()
os.environ['TZ'] = 'EST+05EDT,M4.1.0,M10.5.0'
time.tzset()


def poll_blockchain(event_filter, poll_interval, is_test, send_tweet):
    if not is_test:
        while True:
            if operating_system == 'Windows':
                message = "Polling for events on " + ETHEREUM_CONTRACT
            else:
                message = time.strftime('%X %x %Z') + " - Polling for events on " + ETHEREUM_CONTRACT
            print(message)
            for event in event_filter.get_all_entries():
                block_id = parameters_handler.get_block_id(event)
                print("Processing transactionHash: " + str(block_id.hex()))
                if send_tweet:
                    event_processor.process_create_event_and_tweet(event)
            time.sleep(poll_interval)
    else:
        if operating_system == 'Windows':
            message = "Polling for events on " + ETHEREUM_CONTRACT
        else:
            message = time.strftime('%X %x %Z') + " - Polling for events on " + ETHEREUM_CONTRACT
        for event in event_filter.get_all_entries():
            print(message)
            block_id = parameters_handler.get_block_id(event)
            print("Processing transactionHash: " + str(block_id.hex()))
            if send_tweet:
                event_processor.process_create_event_and_tweet(event)
            time.sleep(poll_interval)


def main():
    is_test = False
    send_tweet = False
    event_signature = event_signatures.get_created_signature()
    # event_signature = event_signatures.get_transfer_signature()
    # event_signature = event_signatures.getMaturedSignature()
    if is_test:
        event_filter = w3.eth.filter({"address": checksum_address, 'fromBlock': 11774988, 'toBlock': 'latest', 'topics': [event_signature]})
    else:
        event_filter = w3.eth.filter({"address": checksum_address, 'fromBlock': 'latest', 'topics': [event_signature]})
    poll_blockchain(event_filter, 2, is_test, send_tweet)


if __name__ == '__main__':
    main()
