from web3.auto import w3
import asyncio
import logging
import os
import time
import platform
from utilities import parameters_handler
from utilities import event_signatures
from utilities import event_processor
from connections import web3driver


logging.basicConfig(filename=os.getcwd() + "/app/application.log",
                    filemode='a',
                    format='%(asctime)s, %(levelname)s %(message)s',
                    datefmt='%D %H:%M:%S',
                    level=logging.INFO)

logging.getLogger()

ETHEREUM_ENDPOINT = parameters_handler.get_eth_endpoint()
ETHEREUM_CONTRACT = parameters_handler.get_eth_contract()

try:
    w3 = web3driver.get_web3_session(ETHEREUM_ENDPOINT)
    checksum_address = w3.toChecksumAddress(ETHEREUM_CONTRACT)
except Exception as e:
    print(e)
    logging.error(e)

operating_system = platform.system()


def handle_event(event, event_type):
    if event_type == "created":
        event_processor.process_create_event_and_tweet(event)
    elif event_type == "matured":
        event_processor.process_mature_event_and_tweet(event)


async def created_worker(event_filter, poll_interval, event_type):
    for event in event_filter.get_all_entries():
        try:
            message = "Polling for " + event_type + " bonds: " + str(event_filter) + " on " + ETHEREUM_CONTRACT
            logging.info(message)
            print(message)
            block_id = parameters_handler.get_block_id(event)
            logging.info("Processing transactionHash: " + str(block_id.hex()))
            print("Processing transactionHash: " + str(block_id.hex()))
            handle_event(event, event_type)
            await asyncio.sleep(poll_interval)
        except asyncio.CancelledError as e:
            print("Break it out")
            logging.error(e)
            raise e # Raise a proper error


async def matured_worker(event_filter, poll_interval, event_type):
    for event in event_filter.get_all_entries():
        try:
            message = "Polling for " + event_type + " bonds: " + str(event_filter) + " on " + ETHEREUM_CONTRACT
            logging.info(message)
            print(message)
            block_id = parameters_handler.get_block_id(event)
            logging.info("Processing transactionHash: " + str(block_id.hex()))
            print("Processing transactionHash: " + str(block_id.hex()))
            handle_event(event, event_type)
            await asyncio.sleep(poll_interval)
        except asyncio.CancelledError as e:
            logging.error(e)
            print("Break it out")
            raise e # Raise a proper error


created_event_signature = event_signatures.get_token_created_event_signature()
# created_event_filter = w3.eth.filter({"address": checksum_address, 'topics': [created_event_signature]})
matured_event_signature = event_signatures.get_token_matured_signature()
# matured_event_filter = w3.eth.filter({"address": checksum_address, 'topics': [matured_event_signature]})

created_event_filter = w3.eth.filter({"address": checksum_address, 'fromBlock': 11868999, 'toBlock': 'latest',
                                      'topics': [created_event_signature]})
matured_event_filter = w3.eth.filter({"address": checksum_address, 'fromBlock': 11868999, 'toBlock': 'latest',
                                      'topics': [matured_event_signature]})
loop = asyncio.get_event_loop()
while True:
    asyncio.ensure_future(created_worker(created_event_filter, 4, "created"))
    asyncio.ensure_future(matured_worker(matured_event_filter, 4, "matured"))
    loop.run_forever()
