from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract
import json

w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/337d7f32be2f4356bc28b30d5917312b"))

print('connected to web3?',w3.isConnected())

with open("../resources/abi/sync.abi") as f:
    abi = json.load(f)['abi']

sync_checksum_add = w3.toChecksumAddress('0xb6ff96b8a8d214544ca0dbc9b33f7ad6503efd32')
sync_contract = w3.eth.contract(address=sync_checksum_add, abi=abi)
sync_concise = ConciseContract(sync_contract)

with open("../resources/abi/cbond.abi") as f:
    cbond_abi = json.load(f)

cbond_address = w3.toChecksumAddress('0xc6c11f32d3ccc3beaac68793bc3bfbe82838ca9f')
cbond_contract = w3.eth.contract(address=cbond_address, abi=cbond_abi)
cbond_concise = ConciseContract(cbond_contract)

cbond_contract.all_functions()

print('total cbonds:', cbond_concise.totalCBONDS())
print('SYNC total supply:', sync_concise.totalSupply() / (10**18))
print('total sync locked:', cbond_concise.totalSYNCLocked() / (10**18))