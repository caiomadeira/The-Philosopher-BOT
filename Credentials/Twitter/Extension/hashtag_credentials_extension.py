"""
Philosopher Bot
---------------
Created by Caio Madeira
Co-worker: Rodrigo Carmo

instagram: @sudomadeira
Twitter: @bot_philospher
Avaliable on Discord too!
# --------------------------------------------------------------
ORDER

CONSUMER KEY
CONSUMER SECRET KEY
API KEY | ACESS TOKEN
API SECRET KEY | ACESS TOKEN SECRET
BEARER_TOKEN

"""
import tweepy.api
import os

ACCESS_TOKEN_EXT = os.getenv('ACCESS_TOKEN_EXT')

ACCESS_SECRET_TOKEN_EXT = os.getenv('ACCESS_SECRET_TOKEN_EXT')

API_KEY_EXT = os.getenv('API_KEY_EXT')

API_SECRET_KEY_EXT = os.getenv('API_SECRET_KEY_EXT')

BEARER_TOKEN_EXT = os.getenv('BEARER_TOKEN_EXT')


AUTH_HASHTAG_EXTENSION = tweepy.OAuthHandler(API_KEY_EXT, API_SECRET_KEY_EXT)
AUTH_HASHTAG_EXTENSION.set_access_token(ACCESS_TOKEN_EXT, ACCESS_SECRET_TOKEN_EXT)


try:
    API_HASHTAG_EXTENSION = tweepy.API(AUTH_HASHTAG_EXTENSION, wait_on_rate_limit=False, wait_on_rate_limit_notify=True)

except tweepy.TweepError:
    print('Error_Philobot! Falha ao pegar o Token de acesso!')

