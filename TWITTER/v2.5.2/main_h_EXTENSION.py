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

import time
from Hashtag_Extension.hashtagExtension import starting_hashtag_extension
import tweepy

if __name__ == '__main__':

    try:
        print("HASHTAG 2.1.10 - EXTENSION ACCOUNT")
        time.sleep(2)
        starting_hashtag_extension()

    except tweepy.error.TweepError as e:
        print(e)