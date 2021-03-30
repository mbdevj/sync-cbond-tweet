from web3 import Web3


def get_token_created_event_signature():
    event_signature = Web3.sha3(text="Created(address,uint256,uint256,uint256,uint256,uint256)").hex()
    return event_signature


def get_token_transferred_event_signature():
    event_signature = Web3.sha3(text="Transfer(address,address,uint256)").hex()
    return event_signature


def get_token_matured_signature():
    event_signature = Web3.sha3(text="Matured(address,uint256,uint256,uint256)").hex()
    return event_signature