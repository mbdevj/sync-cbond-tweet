import time
import os
import sys
import platform
from app.utilities import event_handler
from app.utilities import event_signatures
from app.utilities import blockchain_handler
from app.utilities import image_handler
from app.connections import twitter
from web3 import Web3, HTTPProvider
from configparser import RawConfigParser

properties_file = os.getcwd() + "/resources/application.properties"
config = RawConfigParser()
config.read(properties_file, encoding=None)

try:
    ETHEREUM_CONTRACT = config.get("EthereumProperties", "ethereum.contract")
    ETHEREUM_ENDPOINT = config.get("EthereumProperties", "ethereum.provider")
except Exception as e:
    print('Could not read configuration file')
    print(e)
    sys.exit(1)


w3 = Web3(HTTPProvider(ETHEREUM_ENDPOINT))
checksum_address = w3.toChecksumAddress(ETHEREUM_CONTRACT)


def poll_blockchain(event_filter, poll_interval, is_test):
    operating_system = platform.system()
    if operating_system == 'Windows':
        message = "Polling for events on " + ETHEREUM_CONTRACT
    else:
        os.environ['TZ'] = 'EST+05EDT,M4.1.0,M10.5.0'
        time.tzset()
        message = time.strftime('%X %x %Z') + " - Polling for events on " + ETHEREUM_CONTRACT
    if not is_test:
        while True:
            print(message)
            for event in event_filter.get_all_entries():
                token_id = event_handler.handle_create_event(event)
                image = image_handler.get_bond_image(token_id)
                twitter.update_status_with_media("Message here :)", image)
            time.sleep(poll_interval)
    else:
        print("TEST: " + message)
        for event in event_filter.get_all_entries():
            block_id = (event['transactionHash'])
            print("Processing transactionHash: " + str(block_id.hex()))
            token_id = event_handler.handle_create_event(event)
            # print(token_id)
            data = ([event['data'][26:66]])
            lpt_contract = "0x" + str((data[0]))
            lpt_pair = str(blockchain_handler.get_lpt_pair(lpt_contract))
            lpt_value = str(blockchain_handler.get_lpt_value(token_id))
            duration = str(blockchain_handler.get_duration(token_id))
            total_value_of_bonded_sync = str(blockchain_handler.get_total_value_of_bonded_sync(token_id))
            apr = str(blockchain_handler.get_apr(token_id))
            image = image_handler.get_bond_image(token_id)
            tweet_text = "New " + duration + " day #CryptoBond created with " + total_value_of_bonded_sync \
                         + " $SYNC and " + lpt_value + " " + lpt_pair + ", yielding an APR of " + apr \
                         + "%! Create yours now at https://syncbond.com!"
            twitter.update_status_with_media(tweet_text, image)
            time.sleep(poll_interval)


def main():
    is_test = False
    event_signature = event_signatures.get_created_signature()
    # event_signature = event_signatures.get_transfer_signature()
    # event_signature = event_signatures.getMaturedSignature()
    if is_test:
        event_filter = w3.eth.filter({"address": checksum_address, 'fromBlock': 11774988, 'toBlock': 'latest', 'topics': [event_signature]})
    else:
        event_filter = w3.eth.filter({"address": checksum_address, 'fromBlock': 'latest', 'topics': [event_signature]})
    poll_blockchain(event_filter, 2, is_test)


if __name__ == '__main__':
    main()