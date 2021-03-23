"""
posting.py
Philosopher Bot
---------------
Created by Caio Madeira (@sudomaidera)
Co-worker: Rodrigo Carmo @rodrigoblock

instagram: @sudomadeira
Twitter: @bot_philospher
Avaliable on Discord too!

"""
from Hashtag.hashtag import starting_hashtag
from Credentials.credentials_verify import *
from art import tprint
import time


v = api


if __name__ == '__main__':

    try:
        (tprint("HASHTAG V2.1"))
        starting_hashtag()

    except tweepy.error.TweepError as e:
        print(e)
        time.sleep(2)


