"""
hashtag.py
Philosopher Bot
---------------
Created by Caio Madeira
Co-worker: Rodrigo Carmo

instagram: @sudomadeira
Twitter: @bot_philospher
Avaliable on Discord too!

"""

import time
import tweepy
from config import VERSION_HASHTAG


def hashtag_oficial():
    try:
        print("HASHTAG - OFICIAL ACCOUNT")
        print(f'Versão: {VERSION_HASHTAG}')
        time.sleep(2)
        from Hashtag.hashtag import starting_hashtag
        starting_hashtag()

    except tweepy.error.TweepError as e:
        print(e)


if __name__ == '__main__':
    hashtag_oficial()
