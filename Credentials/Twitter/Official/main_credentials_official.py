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
from Logs.Twitter.logger_hashtag import log_bot

"""=========== SET LOG ==========="""
log = log_bot

"""=========== GET KEYs FROM S.O ENV ==========="""
ACCESS_TOKEN_OFFICIAL = os.getenv('ACCESS_TOKEN_OFFICIAL')

ACCESS_SECRET_TOKEN_OFFICIAL = os.getenv('ACCESS_SECRET_TOKEN_OFFICIAL')

API_KEY_OFFICIAL = os.getenv('API_KEY_OFFICIAL')

API_SECRET_KEY_OFFICIAL = os.getenv('API_SECRET_KEY_OFFICIAL')

BEARER_TOKEN_OFFICIAL = os.getenv('BEARER_TOKEN_OFFICIAL')


AUTH_MAIN_OFFICIAL = tweepy.OAuthHandler(API_KEY_OFFICIAL, API_SECRET_KEY_OFFICIAL)
AUTH_MAIN_OFFICIAL.set_access_token(ACCESS_TOKEN_OFFICIAL, ACCESS_SECRET_TOKEN_OFFICIAL)


try:
    API_MAIN_OFFICIAL = tweepy.API(AUTH_MAIN_OFFICIAL, wait_on_rate_limit=False, wait_on_rate_limit_notify=True)

except tweepy.TweepError as auth_official:
    log.error('[X] - Erro ao se autenticar com as credenciais do oficial!')
    log.error(auth_official)
