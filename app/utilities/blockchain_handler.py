from web3 import Web3
from web3.contract import ConciseContract
from configparser import RawConfigParser
from app.utilities import parameters_handler
from app.connections import web3driver
from urllib import parse
import os
import sys
import urllib.request, json
import locale


locale.setlocale(locale.LC_ALL,'en_US.UTF-8')

ETHEREUM_CONTRACT = parameters_handler.get_eth_contract()
w3 = web3driver.get_web3_session(parameters_handler.get_eth_endpoint())
properties_file = os.getcwd() + "/app/resources/application.properties"
config = RawConfigParser()
config.read(properties_file, encoding=None)

try:
    ETHEREUM_CONTRACT = config.get("EthereumProperties", "ethereum.contract")
    ETHEREUM_ENDPOINT = config.get("EthereumProperties", "ethereum.endpoint")
except Exception as e:
    print('Could not read configuration file')
    print(e)
    sys.exit(1)

w3 = Web3(Web3.WebsocketProvider(ETHEREUM_ENDPOINT))


with open(os.getcwd() + "/app/resources/abi/cbond.abi") as f:
    cbond_abi = json.load(f)


cbond_address = w3.toChecksumAddress(ETHEREUM_CONTRACT)
cbond_contract = w3.eth.contract(address=cbond_address, abi=cbond_abi)
cbond_concise = ConciseContract(cbond_contract)


def get_lpt_value(token_id):
    with urllib.request.urlopen("https://tokenomics.syncbond.com/currentMaturedValue?id=" + str(token_id)) as url:
        data = json.loads(url.read().decode())
        lpt_value = data['lpt_value_usd']
        # print(data['lpt_value_usd'])
        return lpt_value


def get_total_value_of_bonded_sync(token_id):
    with urllib.request.urlopen("https://tokenomics.syncbond.com/currentMaturedValue?id=" + str(token_id)) as url:
        data = json.loads(url.read().decode())
        total_value = data['sync_value_usd']
        return total_value


def get_lpt_pair(contract):
    pools =[
    ["0xfb2f545a9ad62f38fe600e24f75ecd790d30a7ba","SYNC","ETH", "0xb6ff96b8a8d214544ca0dbc9b33f7ad6503efd32", "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"],
    ["0xdfc14d2af169b0d36c4eff567ada9b2e0cae044f","ETH","AAVE", "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2", "0x7fc66500c84a76ad7e9c93437bfc5ac33e2ddae9"],
    ["0xa2107fa5b38d9bbd2c461d6edf11b11a50f6b974","ETH","LINK", "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2", "0x514910771af9ca656af840dff83e8264ecf986ca"],
    ["0xd90a1ba0cbaaaabfdc6c814cdf1611306a26e1f8","SWAP","ETH", "0xcc4304a31d09258b0029ea7fe63d032f52e44efe", "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"],
    ["0x37a0464f8f4c207b54821f3c799afd3d262aa944","DEXT","ETH", "0x26ce25148832c04f3d7f26f32478a9fe55197166", "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"],
    ["0x3041cbd36888becc7bbcbc0045e3b1f144466f5f","USDT","USDC", "0xdac17f958d2ee523a2206206994597c13d831ec7", "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"],
    ["0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc","USDC","ETH", "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48", "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"],
    ["0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852","USDT","ETH", "0xdac17f958d2ee523a2206206994597c13d831ec7", "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"],
    ["0xa478c2975ab1ea89e8196811f51a7b7ade33eb11","DAI","ETH", "0x6b175474e89094c44da98b954eedeac495271d0f", "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"],
    ["0xbb2b8038a1640196fbe3e38816f3e67cba72d940","WBTC","ETH", "0x2260fac5e5542a773aa44fbcfedf7c193bc2c599", "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"],
    ["0x004375dff511095cc5a197a54140a24efef3a416","WBTC","USDC", "0x2260fac5e5542a773aa44fbcfedf7c193bc2c599", "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"],
    ["0x816579230a4c61670eba15486c8357bf87ec307e","xBTC","ETH", "0xecbf566944250dde88322581024e611419715f7a", "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"],
    ["0x767055e2a9f15783b1ec5ef134a89acf3165332f","USDC","EURS", "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48", "0xdb25f211ab05b1c97d595516f45794528a807ad8"],
    ]
    for i in pools[:10]:
        if contract == i[0]:
            lpt_pair = "$" + i[1] + " - $" + i[2]
            return lpt_pair


def get_interest_upon_maturity(token_id):
    with urllib.request.urlopen("https://tokenomics.syncbond.com/currentMaturedValue?id=" + str(token_id)) as url:
        data = json.loads(url.read().decode())
        original_amount_sync = data['numeric']['original_amount_sync']
        mature_amount_sync = data['numeric']['mature_amount_sync']
        interest_upon_maturity = round((mature_amount_sync / original_amount_sync - 1) * 100, 2)
        # print(interest_upon_maturity)
        return interest_upon_maturity


def get_duration(token_id):
    URL = cbond_concise.tokenURI(token_id)
    data = dict(parse.parse_qsl(parse.urlsplit(URL).query))
    duration = int(int(data['termLength'])/86400)
    if duration == 30:
        duration = "1 month"
    if duration == 90:
        duration = "3 months"
    if duration == 180:
        duration = "6 months"
    if duration == 360:
        duration = "1 year"
    if duration == 720:
        duration = "2 years"
    if duration == 1080:
        duration = "3 years"
    return duration


def get_original_amount_sync(token_id):
    original_amount_sync = int(cbond_concise.syncAmountById(token_id) / (10 ** 18))
    return original_amount_sync


def get_sync_price_at_creation(token_id):
    sync_price_at_creation = cbond_concise.syncPriceById(token_id) / (10 ** 18) * 1400.22
    return sync_price_at_creation


def get_original_amount_ltoken(token_id):
    original_amount_ltoken = int(cbond_concise.lTokenAmountById(token_id) / (10 ** 18))
    return original_amount_ltoken


def get_ltoken_price_at_creation(token_id):
    ltoken_price_at_creation = cbond_concise.lTokenPriceById(token_id) / (10 ** 18) * 1400.22
    return ltoken_price_at_creation


def get_ltokenamt(token_id):
    ltokenamt = cbond_concise.lTokenAmountById(token_id) / (10 ** 18)
    return ltokenamt


def get_syncamt(token_id):
    syncamt = cbond_concise.syncRewardedOnMaturity(token_id) / (10 ** 18)
    return syncamt


def get_bond_creation_timestamp(token_id):
    bond_creation_timestamp = cbond_concise.timestampById(token_id)
    return bond_creation_timestamp


def get_is_divs(token_id):
    is_divs = cbond_concise.gradualDivsById(token_id)
    return is_divs


def get_creation_eth_price():
    with urllib.request.urlopen("https://tokenomics.syncbond.com/eth_price") as url:
        data = json.loads(url.read().decode())
        creation_eth_price = data
        return creation_eth_price


def get_lpt_addr_by_id(token_id):
    lpt_addr_by_id = str(cbond_concise.lAddrById(token_id).lower())
    return lpt_addr_by_id


def get_pair_ts(token_id):
    with urllib.request.urlopen("https://tokenomics.syncbond.com/getTableData") as url:
        data = json.loads(url.read().decode())
        pair_ts = data[get_lpt_addr_by_id(token_id)]['pair_ts']
        return pair_ts


def get_reserve(token_id):
    with urllib.request.urlopen("https://tokenomics.syncbond.com/getTableData") as url:
        data = json.loads(url.read().decode())
        reserve = int(data[get_lpt_addr_by_id(token_id)]['reserveUSD'].replace('$', '').replace(',', ''))
    return reserve


def get_lpt_ratio(token_id):
    lpt_ratio = get_ltokenamt(token_id) / get_pair_ts(token_id)
    return lpt_ratio


def get_lpt_value_usd(token_id):
    lpt_value_usd = get_lpt_ratio(token_id) * get_reserve(token_id)
    return lpt_value_usd


def get_sync_value_usd(token_id):
    sync_value = get_sync_price_at_creation(token_id) * get_syncamt(token_id)
    return sync_value


def get_total_value_usd(token_id):
    total_value_usd = get_lpt_value_usd(token_id) * 2
    total_value_usd = locale.currency(total_value_usd, grouping=True)
    return total_value_usd
