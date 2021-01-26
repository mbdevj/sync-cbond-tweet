#!/usr/bin/python

import sys, getopt
import tweepy

CONSUMER_KEY = "XXXXXX"
CONSUMER_SECRET = "XXXXXX"   
ACCESS_KEY = "XXXXXX"    
ACCESS_SECRET = "XXXXXX"

def main(argv):
    first_ticker = ''
    first_qty = ''
    second_ticker = ''
    second_qty = '' 
    duration = ''
    apr = ''
    image_path= ''
    try:
        opts, args = getopt.getopt(argv,"",["first-ticker=","first-qty=", "second-ticker=", "second-qty=", "duration=", "apr=", "image-path="])
    except getopt.GetoptError as e:
        print (e)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('python3 sync-bond-created-tweet.py --first-ticker ETH --first-qty 2.58 --second-ticker SYNC --second-qty 33000 --duration 90 --apr 22.7 --image-path bond.png')
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

    first_ticker = first_ticker.upper()
    second_ticker = second_ticker.upper()

    tweet_text = "New " + duration + " day $SYNC #CryptoBond created using " \
    + first_qty + " $" + first_ticker + " and " + second_qty + " $" + second_ticker \
    + ", yielding an APR of " + apr + "%! Create yours now at https://syncbond.com." 


    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

    api.update_with_media(image_path, tweet_text)
    # api.update_status(status=tweet_text)

if __name__ == "__main__":
   main(sys.argv[1:])
