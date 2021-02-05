from web3 import Web3, HTTPProvider
import time


w3 = Web3(HTTPProvider("https://mainnet.infura.io/v3/337d7f32be2f4356bc28b30d5917312b"))

#cbond
checksum_address = w3.toChecksumAddress("0xc6c11f32d3ccc3beaac68793bc3bfbe82838ca9f")

#sync
# checksum_address = w3.toChecksumAddress("0xb6ff96b8a8d214544ca0dbc9b33f7ad6503efd32")

def handle_event(event):
    print(event)


def log_loop(event_filter, poll_interval):
    while True:
        for event in event_filter.get_new_entries():
            handle_event(event)
        time.sleep(poll_interval)


def main():
    event_filter = w3.eth.filter({"address": checksum_address})
    block_filter = w3.eth.filter('latest')
    log_loop(event_filter, 2)


if __name__ == '__main__':
    main()