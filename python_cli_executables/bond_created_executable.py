#!/usr/bin/python

import sys, getopt
from src.Actions import tweet


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "",
                                   ["first-ticker=", "first-qty=", "second-ticker=", "second-qty=", "duration=", "apr=",
                                    "image-path="])
    except getopt.GetoptError as e:
        print(e)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('python3 sync_bot_cli.py --first-ticker ETH --first-qty 2.58 '
                  '--second-ticker SYNC --second-qty 33000 --duration 90 --apr 22.7 --image-path bond.png')
            sys.exit()
        elif opt in "--first-ticker":
            first_ticker = arg
        elif opt in "--first-qty":
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

    tweet_text = "New " + duration + " day $SYNC #CryptoBond created using " \
                 + first_qty + " $" + first_ticker + " and " + second_qty + " $" + second_ticker \
                 + ", yielding an APR of " + apr + "%! Create yours now at https://syncbond.com."

    try:
        tweet.update_status_with_media(tweet_text, image_path)
        message = "Successfully tweeted."
    except Exception as e:
        message = "Failed to tweet."
        print(e)

    print(message)


if __name__ == "__main__":
    main(sys.argv[1:])
