from app.utilities import event_handler
from app.utilities import blockchain_handler
from app.utilities import image_handler
from configparser import RawConfigParser
import os


def load_application_properties(property_section, property_name):
    properties_file = os.getcwd() + "/app/resources/application.properties"
    # print(properties_file)
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


def get_total_value_usd(token_id):
    total_value_usd = str(blockchain_handler.get_total_value_usd(token_id))
    return total_value_usd


def get_duration(token_id):
    duration = str(blockchain_handler.get_duration(token_id))
    return duration


def get_total_value_of_bonded_sync(token_id):
    total_value_of_bonded_sync = str(blockchain_handler.get_total_value_of_bonded_sync(token_id))
    return total_value_of_bonded_sync


def get_interest_upon_maturity(token_id):
    interest_upon_maturity = str(blockchain_handler.get_interest_upon_maturity(token_id))
    return interest_upon_maturity


def get_image(token_id):
    image = image_handler.get_bond_image(token_id)
    return image


def get_tweet_text(lpt_pair, token_id, total_value_usd, interest_upon_maturity, duration):
    tweet_text = lpt_pair + " #CryptoBond no. " + str(token_id) + " created with " + total_value_usd \
                 + ", yielding " + str(interest_upon_maturity) + "% upon maturity in " + duration + "! \n \n" \
                 + "Create your $SYNC CryptoBond now at https://syncbond.com, follow us on Twitter @SYNCTOKEN and join " \
                 "our community at https://t.me/SYNC_NETWORK! \n \n" + "https://view.syncbond.com/?id="\
                 + str(token_id)
    return tweet_text


