import json
from web3 import Web3, HTTPProvider
import os
import ethereum

w3 = Web3(HTTPProvider("https://mainnet.infura.io/v3/337d7f32be2f4356bc28b30d5917312b"))

with open(os.getcwd() + "/resources/abi/cbond.abi") as f:
    cbond_abi = json.load(f)

cbond_address = w3.toChecksumAddress('0xc6c11f32d3ccc3beaac68793bc3bfbe82838ca9f')
event_signature = w3.sha3(text="Transfer(address,address,uint256)").hex()
event = w3.eth.getLogs({
    "fromBlock": 11800354,
    "address": cbond_address,
    "topics": [event_signature]
})


ethereum.handle_event(event)