from web3 import Web3
from web3 import exceptions


def get_web3_session(endpoint):
    try:
        session = Web3(Web3.WebsocketProvider(endpoint))
    except exceptions.InfuraKeyNotFound as e:
        print(e)
        exit(1)
    return session