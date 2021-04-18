"""
Philosopher Bot
---------------
Created by Caio Madeira
Co-worker: Rodrigo Carmo

instagram: @sudomadeira
Twitter: @bot_philospher
Avaliable on Discord too!
# --------------------------------------------------------------

DEVELOPER - ONLY FOR TESTS

"""
import tweepy.api
import os

# Consumer keys
API_KEY = "JJ23qk7QG4XTEa6a6XPII1ZhP"

API_KEY_SECRET = "UqNYLgqvIKB8WfSWGOD38NmnHvNIrcdFKOHYDXwkJm84xWXpcc"

# Authentication Token
ACESS_TOKEN = "1317291421523726342-VDMgaSoqZuAFXXbmKG5stElkMrd58R"

ACESS_TOKEN_SECRET = "gkKYY5OtrCgIPzDUcNYRwUivYqg4leTMxC0dTOCEJknhA"

BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAKspMQEAAAAA3axOG7IgnSJE4oss5sZ42AuBJvs" \
               "%3DgTomUUezxuGzMazonl9uwYFxJ5LMbtLXeksiEMuXjVuMoTfZqK "


AUTH_TEST = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
AUTH_TEST.set_access_token(ACESS_TOKEN, ACESS_TOKEN_SECRET)

try:
    API_TEST = tweepy.API(AUTH_TEST, wait_on_rate_limit=False, wait_on_rate_limit_notify=True)
    print("Connected")

except tweepy.TweepError:
    print('Error_Philobot! Falha ao pegar o Token de acesso!')
