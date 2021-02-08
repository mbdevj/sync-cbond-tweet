from web3 import Web3
from web3.contract import ConciseContract
from urllib import parse
import os
import urllib.request, json


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
            lpt_pair = "$" + i[1] + " / $" + i[2]
            return lpt_pair


def get_apr(token_id):
    with urllib.request.urlopen("https://tokenomics.syncbond.com/currentMaturedValue?id=" + str(token_id)) as url:
        data = json.loads(url.read().decode())
        apr = ("{:.2f}".format(data['numeric']['sync_percent_change']))
        # print("{:.2f}".format(data['numeric']['sync_percent_change']))
        # print(data['numeric']['sync_percent_change'])
        return apr


def get_duration(token_id):
    URL = cbond_concise.tokenURI(token_id)
    data = dict(parse.parse_qsl(parse.urlsplit(URL).query))
    # print(int(int(data['termLength'])/86400))
    # print(data)
    duration = int(int(data['termLength'])/86400)
    return duration


# {"lpt_percent_change":"+122.83%","lpt_value_usd":"$10,786.23","numeric":{"lpt_percent_change":122.8267650373482,"lpt_value_usd":10786.230291581316,"mature_amount_sync":152772.59141876735,"original_amount_sync":98321,"sync_percent_change":43.86780407904322,"sync_value_usd":2717.129415941753,"total_percent_change":39.479868273239525,"total_value_usd":13503.359707523068},"sync_percent_change":"-43.87%","sync_value_usd":"$2,717.13","total_percent_change":"+39.48%","total_value_usd":"$13,503.36"}

# get_lpt_value("804")
# get_total_value_of_bonded_sync("804")
# get_apr("804")
# get_duration(804)
# get_lpt_pair("804")
