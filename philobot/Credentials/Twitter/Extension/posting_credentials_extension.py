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
import sys

import tweepy.api
import os


PATH = os.path.dirname(os.path.abspath(__file__))

POSTING_TOKEN_PATH = f'{PATH}/Tokens/posting_tokens.txt'

try:
    with open(POSTING_TOKEN_PATH, "r") as h:

        list_tokens = h.readlines()
        print(list_tokens)

        CONSUMER_KEY = list_tokens[0]

        CONSUMER_SECRET_KEY = list_tokens[1]

        API_KEY = list_tokens[2]

        API_SECRET_TOKEN = list_tokens[3]

        BEARER_TOKEN = list_tokens[4]
except FileNotFoundError:
    print("ERRO: Arquivo txt com os tokens não foi encontrado. Certifique se o caminho está correto.\n")
    sys.exit(1)
except IndexError:
    print("ERRO: FALTAM TOLKENS!\n")
    sys.exit(1)


AUTH_POSTING_EXTENSION = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
AUTH_POSTING_EXTENSION.set_access_token(API_KEY, API_SECRET_TOKEN)

try:
    API_POSTING_EXTENSION = tweepy.API(AUTH_POSTING_EXTENSION, wait_on_rate_limit=False, wait_on_rate_limit_notify=True)

except tweepy.TweepError:
    print('Error_Philobot! Falha ao pegar o Token de acesso!')

