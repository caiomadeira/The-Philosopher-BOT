"""
hashtagExtension.py
Philosopher Bot
---------------
Created by Caio Madeira
Co-worker: Rodrigo Carmo

instagram: @sudomadeira
Twitter: @bot_philospher
Avaliable on Discord too!

"""
import time
from config import VERSION_HASHTAG_EXTENSION
import tweepy


def hashtag_extension():
    try:
        print("HASHTAG - EXTENSION ACCOUNT")
        print(f'Versão: {VERSION_HASHTAG_EXTENSION}')
        time.sleep(2)
        from Hashtag_Extension.hashtagExtension import starting_hashtag_extension
        starting_hashtag_extension()

    except tweepy.error.TweepError as e:
        print(e)


if __name__ == '__main__':
    hashtag_extension()
