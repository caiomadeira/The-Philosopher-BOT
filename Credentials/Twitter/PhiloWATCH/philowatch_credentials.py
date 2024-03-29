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
import tweepy
import os
from PhiloWATCH.Logs_pw.logger import log

"""=========== GET KEYs FROM S.O ENV ==========="""
ACCESS_TOKEN_TEST = os.getenv('ACCESS_TOKEN_TEST')

ACCESS_SECRET_TOKEN_TEST = os.getenv('ACCESS_SECRET_TOKEN_TEST')

API_KEY_TEST = os.getenv('API_KEY_TEST')

API_SECRET_KEY_TEST = os.getenv('API_SECRET_KEY_TEST')

BEARER_TOKEN_TEST = os.getenv('BEARER_TOKEN_TEST')


AUTH_API = tweepy.OAuthHandler(API_KEY_TEST, API_SECRET_KEY_TEST)
AUTH_API.set_access_token(ACCESS_TOKEN_TEST, ACCESS_SECRET_TOKEN_TEST)


try:
    API_TEST = tweepy.API(auth_handler=AUTH_API)

except tweepy.TweepError as auth_test:
    log.error('[X] - Erro ao se autenticar com as credenciais de teste!')
    log.error(auth_test)
