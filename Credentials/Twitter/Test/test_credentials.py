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


ACCESS_TOKEN_TEST = os.getenv('ACCESS_TOKEN_TEST')

ACCESS_SECRET_TOKEN_TEST = os.getenv('ACCESS_SECRET_TOKEN_TEST')

API_KEY_TEST = os.getenv('API_KEY_TEST')

API_SECRET_KEY_TEST = os.getenv('API_SECRET_KEY_TEST')

BEARER_TOKEN_TEST = os.getenv('BEARER_TOKEN_TEST')


API_TEST = tweepy.OAuthHandler(API_KEY_TEST, API_SECRET_KEY_TEST)
API_TEST.set_access_token(ACCESS_TOKEN_TEST, ACCESS_SECRET_TOKEN_TEST)


try:
    API_TEST = tweepy.API(auth_handler=API_TEST)

except tweepy.TweepError as t:
    print(f"Erro: >>>{t}<<<")
    print('Error_Philobot! Falha ao pegar o Token de acesso!')
