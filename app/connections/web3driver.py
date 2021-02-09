from web3 import Web3


def get_web3_session(endpoint):
    session = Web3(Web3.WebsocketProvider(endpoint))
    return session