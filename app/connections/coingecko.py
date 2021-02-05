#!/usr/bin/python3

from pycoingecko import CoinGeckoAPI
import json
import decimal


cg = CoinGeckoAPI()


def get_price(coin, vs_currency):
    data = cg.get_price(ids=coin, vs_currencies=vs_currency)
    json_str = json.dumps(data)
    resp = (json.loads(json_str))
    price = float(resp[coin][vs_currency])
    return price


# get_price("ethereum", "usd")