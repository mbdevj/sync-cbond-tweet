#!/usr/bin/python3

import time
import os
import platform
import logging
from utilities import event_signatures
from utilities import parameters_handler
from utilities import event_processor
from connections import web3driver

logging.basicConfig(filename=os.getcwd() + "/app/application.log",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)

logging.getLogger()

ETHEREUM_CONTRACT = parameters_handler.get_eth_contract()

try:
    w3 = web3driver.get_web3_session(parameters_handler.get_eth_endpoint())
    checksum_address = w3.toChecksumAddress(ETHEREUM_CONTRACT)
except Exception as e:
    logging.error(e)

operating_system = platform.system()


def poll_blockchain(event_filter, poll_interval, is_test, process_events):
    if not is_test:
        while True:
            if operating_system == 'Windows':
                message = "Polling for events on " + ETHEREUM_CONTRACT
            else:
                os.environ['TZ'] = 'EST+05EDT,M4.1.0,M10.5.0'
                time.tzset()
                message = time.strftime('%X %x %Z') + " - Polling for events on " + ETHEREUM_CONTRACT
            logging.info(message)
            for event in event_filter.get_all_entries():
                block_id = parameters_handler.get_block_id(event)
                logging.info("Processing transactionHash: " + str(block_id.hex()))
                try:
                    if process_events:
                        event_processor.process_create_event_and_tweet(event)
                except Exception as e:
                    logging.error(e)

            time.sleep(poll_interval)
    else:
        if operating_system == 'Windows':
            message = "Polling for events on " + ETHEREUM_CONTRACT
        else:
            os.environ['TZ'] = 'EST+05EDT,M4.1.0,M10.5.0'
            time.tzset()
            message = time.strftime('%X %x %Z') + " - Polling for events on " + ETHEREUM_CONTRACT
        for event in event_filter.get_all_entries():
            logging.info(message)
            block_id = parameters_handler.get_block_id(event)
            logging.info("Processing transactionHash: " + str(block_id.hex()))
            if process_events:
                event_processor.process_create_event_and_tweet(event)
            time.sleep(poll_interval)


def main():
    is_test = True
    process_events = True
    while True:
        try:
            event_signature = event_signatures.get_token_created_event_signature()
            # event_signature = event_signatures.get_token_transferred_event_signature()
            # event_signature = event_signatures.get_token_matured_signature()
            if is_test:
                event_filter = w3.eth.filter({"address": checksum_address, 'fromBlock': 11774988, 'toBlock': 'latest',
                                              'topics': [event_signature]})
            else:
                event_filter = w3.eth.filter({"address": checksum_address, 'fromBlock': 'latest',
                                              'topics': [event_signature]})
            try:
                poll_blockchain(event_filter, 2, is_test, process_events)
            except Exception as e:
                logging.error(e)
        except Exception as e:
            logging.error(e)
            time.sleep(30)
            continue


if __name__ == '__main__':
    main()
