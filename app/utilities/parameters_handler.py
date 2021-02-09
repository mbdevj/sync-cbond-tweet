from app.utilities import event_handler
from app.utilities import blockchain_handler
from app.utilities import image_handler
from configparser import RawConfigParser
import os


def load_application_properties(property_section, property_name):
    properties_file = os.getcwd() + "/app/resources/application.properties"
    config = RawConfigParser()
    config.read(properties_file, encoding=None)
    value = config.get(property_section, property_name)
    return value


def get_eth_contract():
    property_section = "EthereumProperties"
    property_name = "ethereum.contract"
    value = load_application_properties(property_section, property_name)
    return value


def get_eth_endpoint():
    property_section = "EthereumProperties"
    property_name = "ethereum.endpoint"
    value = load_application_properties(property_section, property_name)
    return value


def get_is_test():
    pass


def get_send_tweet():
    pass


def get_block_id(event):
    block_id = (event['transactionHash'])
    return block_id


def get_token_id(event):
    token_id = event_handler.handle_create_event(event)
    # print(token_id)
    return token_id

def get_lpt_pair(event):
    data = ([event['data'][26:66]])
    lpt_contract = "0x" + str((data[0]))
    lpt_pair = str(blockchain_handler.get_lpt_pair(lpt_contract))
    return lpt_pair


def get_lpt_value(token_id):
    lpt_value = str(blockchain_handler.get_lpt_value(token_id))
    return lpt_value


def get_duration(token_id):
    duration = str(blockchain_handler.get_duration(token_id))
    return duration


def get_total_value_of_bonded_sync(token_id):
    total_value_of_bonded_sync = str(blockchain_handler.get_total_value_of_bonded_sync(token_id))
    return total_value_of_bonded_sync


def get_apr(token_id):
    apr = str(blockchain_handler.get_apr(token_id))
    return apr


def get_image(token_id):
    image = image_handler.get_bond_image(token_id)
    return image


def get_tweet_text(token_id, duration, total_value_of_bonded_sync, lpt_value, lpt_pair, apr):
    tweet_text = "New " + duration + " day #CryptoBond created with " + total_value_of_bonded_sync \
                 + " $SYNC and " + lpt_value + " " + lpt_pair + ", yielding an APR of " + apr \
                 + "%! Create yours now at https://syncbond.com!"
    return tweet_text


