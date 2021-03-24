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

CONSUMER_KEY = os.environ.get('CONSUMER_KEY', None)

CONSUMER_SECRET_KEY = os.environ.get('CONSUMER_SECRET_KEY', None)

API_KEY = os.environ.get('API_KEY', None)

API_SECRET_TOKEN = os.environ.get('API_SECRET_TOKEN', None)

BEARER_TOKEN = os.environ.get('BEARER_TOKEN', None)


AUTH_HASHTAG_EXTENSION = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
AUTH_HASHTAG_EXTENSION.set_access_token(API_KEY, API_SECRET_TOKEN)

try:
    API_HASHTAG_EXTENSION = tweepy.API(AUTH_HASHTAG_EXTENSION, wait_on_rate_limit=False, wait_on_rate_limit_notify=True)

except tweepy.TweepError:
    print('Error_Philobot! Falha ao pegar o Token de acesso!')

