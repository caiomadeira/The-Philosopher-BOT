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
from Logs.Twitter.logger_engine import log_philobot

"""=========== SET LOG ==========="""
log = log_philobot(__name__)

"""=========== GET KEYs FROM S.O ENV ==========="""
ACCESS_TOKEN_EXT = os.getenv('ACCESS_TOKEN_EXT')

ACCESS_SECRET_TOKEN_EXT = os.getenv('ACCESS_SECRET_TOKEN_EXT')

API_KEY_EXT = os.getenv('API_KEY_EXT')

API_SECRET_KEY_EXT = os.getenv('API_SECRET_KEY_EXT')

BEARER_TOKEN_EXT = os.getenv('BEARER_TOKEN_EXT')


AUTH_HASHTAG_EXTENSION = tweepy.OAuthHandler(API_KEY_EXT, API_SECRET_KEY_EXT)
AUTH_HASHTAG_EXTENSION.set_access_token(ACCESS_TOKEN_EXT, ACCESS_SECRET_TOKEN_EXT)


try:
    API_HASHTAG_EXTENSION = tweepy.API(AUTH_HASHTAG_EXTENSION, wait_on_rate_limit=False, wait_on_rate_limit_notify=True)

except tweepy.TweepError as auth_ext:
    log.error('[X] - Erro ao se autenticar com as credenciais do extension!')
    log.error(auth_ext)
