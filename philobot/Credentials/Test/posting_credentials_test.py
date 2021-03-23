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

CONSUMER_KEY = '0ucMYqUYkAPJGbSTTnlxodKkm'

CONSUMER_SECRET_KEY = 'ix7N51XUDiLFF9PXMvCvO6FLo5PSAs4cSFz4E8EP6K0bkOictK'

API_KEY = '1317291421523726342-m9RuydHKxz9qPJeGCQPmoy79vBEOwR'

API_SECRET_TOKEN = 'KCcs9rJtWOaDIJVN9X92br3HzU9jMatcvLlgVlYC1kkKC'

BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAFc%2BMgEAAAAAKWqGyGM9q03Vv6ABhgFibOvsP1E%3DTQp5oEK1v19Rju7J4oysQXLCwYVfAOUHr2VWk9c2MTcIz0MBuP'



AUTH_POSTING_TEST = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
AUTH_POSTING_TEST.set_access_token(API_KEY, API_SECRET_TOKEN)

try:
    API_POSTING_TEST = tweepy.API(AUTH_POSTING_TEST, wait_on_rate_limit=False, wait_on_rate_limit_notify=True)

except tweepy.TweepError as t:
    print(f"Erro: >>>{t}<<<")
    print('Error_Philobot! Falha ao pegar o Token de acesso!')


