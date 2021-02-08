from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract
import json
import os

w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/abf746348603424d830dd8c9f55b08c7"))

# Total value of LPT
# First Token
# Second Token
# Total value of bonded SYNC
# APR
# Duration

with open(os.getcwd() + "/resources/abi/cbond.abi") as f:
    cbond_abi = json.load(f)

cbond_address = w3.toChecksumAddress('0xc6c11f32d3ccc3beaac68793bc3bfbe82838ca9f')
cbond_contract = w3.eth.contract(address=cbond_address, abi=cbond_abi)
cbond_concise = ConciseContract(cbond_contract)


def get_lpt_value():
    # print('total cbonds:', cbond_concise.totalCBONDS())
    print('total sync locked:', cbond_concise.totalSYNCLocked(804))
    # print(cbond_contract.all_functions())


def get_first_token():
    pass


def get_second_token():
    pass


def get_total_value_of_bonded_sync():
    pass


def get_apr():
    pass


def get_duration():
    pass

get_lpt_value()
