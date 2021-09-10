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
# import tweepy
# import os
# from Logs.Twitter.logger_engine import log_philobot
#
# """=========== SET LOG ==========="""
# log = log_philobot(__name__)
#
# """=========== GET KEYs FROM S.O ENV ==========="""
# ACCESS_TOKEN_PW = os.getenv('ACCESS_TOKEN_PW')
#
# ACCESS_SECRET_TOKEN_PW = os.getenv('ACCESS_SECRET_TOKEN_PW')
#
# API_KEY_PW = os.getenv('API_KEY_PW')
#
# API_SECRET_KEY_PW = os.getenv('API_SECRET_KEY_PW')
#
# BEARER_TOKEN_PW = os.getenv('BEARER_TOKEN_PW')
#
#
# AUTH_PW = tweepy.OAuthHandler(API_KEY_PW, API_SECRET_KEY_PW)
# AUTH_PW.set_access_token(ACCESS_TOKEN_PW, ACCESS_SECRET_TOKEN_PW)
#
#
# try:
#     API_PW = tweepy.API(auth_handler=AUTH_PW)
#
# except tweepy.TweepError as auth_pw_error:
#     log.error('[X] - Erro ao se autenticar com as credenciais de teste!')
#     log.error(auth_pw_error)

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
