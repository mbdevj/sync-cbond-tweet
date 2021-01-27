#!/usr/bin/python

import sys, getopt
from utilities import sync_bond_tweet

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"",["first-ticker=","first-qty=", "second-ticker=", "second-qty=", "duration=", "apr=", "image-path="])
    except getopt.GetoptError as e:
        print (e)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('python3 sync_bot_cli.py --first-ticker ETH --first-qty 2.58 --second-ticker SYNC --second-qty 33000 --duration 90 --apr 22.7 --image-path bond.png')
            sys.exit()
        elif opt in ("--first-ticker"):
            first_ticker = arg
        elif opt in ("--first-qty"):
            first_qty = arg
        elif opt in "--second-ticker":
            second_ticker = arg
        elif opt in "--second-qty":
            second_qty = arg 
        elif opt in "--duration":
            duration = arg
        elif opt in "--apr":
            apr = arg
        elif opt in "--image-path":
            image_path = arg

    try:
        sync_bond_tweet.tweet(first_ticker, first_qty, second_ticker, second_qty, duration, apr, image_path)
        message = "Successfully tweeted."
    except Exception as e:
        message = "Failed to tweet."
        print(e)

    print(message)

if __name__ == "__main__":
   main(sys.argv[1:])