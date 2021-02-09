from web3 import Web3


def get_created_signature():
    event_signature = Web3.sha3(text="Created(address,uint256,uint256,uint256,uint256,uint256)").hex()
    return event_signature


def get_transfer_signature():
    event_signature = Web3.sha3(text="Transfer(address,address,uint256)").hex()
    return event_signature


def get_matured_signature():
    pass