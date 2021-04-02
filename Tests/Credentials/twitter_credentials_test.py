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
API_KEY = "Zdo4ttxKNgqgluH6ojomAtNRR"

API_KEY_SECRET = "TdZR5jpDrPFDtrj8lmeCr9G3ITA0VZi8afaHUeAJpXtqMXLyEA"

# Authentication Token
ACESS_TOKEN = "1317291421523726342-xd5dzp2HxsR7vBtefFvklPA8FyQYIK"

ACESS_TOKEN_SECRET = "1RIPcy61VyOYj9A1MT80Q6aj8TEOcmTY6o8JU1L7YRVAT"

BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAM1XMQEAAAAAU%2FEQ1cwKy8oVikyDAR6rjV%2F9kfE" \
               "%3DWhm61Du8bt3fu1cY37fSN1mNHlNb2UxlKtUlGN7kIIQv1R8xNK "


AUTH_TEST = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
AUTH_TEST.set_access_token(ACESS_TOKEN, ACESS_TOKEN_SECRET)

try:
    API_TEST = tweepy.API(AUTH_TEST, wait_on_rate_limit=False, wait_on_rate_limit_notify=True)
    print("Connected")

except tweepy.TweepError:
    print('Error_Philobot! Falha ao pegar o Token de acesso!')
