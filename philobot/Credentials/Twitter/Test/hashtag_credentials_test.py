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

CONSUMER_KEY = 'IZgdaQhDTsTaCVAFtAKOwUE37'

CONSUMER_SECRET_KEY = 'Os4wkHVd5GB6ddtjRf4dAPAwJx9io6dySaI2SN5zSM8HtVQoKE'

API_KEY = '1317291421523726342-DBpHBfZcfvkFicetlMKtlVeqVok6W2'

API_SECRET_TOKEN = 'HGyar9Dc8wI9XBrDmizBINEXNyMMc3E2OyIdkiqEWdjJs'

BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAKspMQEAAAAAQJXgPKlsW3GXpWvlESUAhdlBV9o%3DozmhxAPX5orE8kbz6p3F0EIwtiT57k1LkeOiDvjs70Ydv31o0W'


AUTH_HASHTAG_TEST = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
AUTH_HASHTAG_TEST.set_access_token(API_KEY, API_SECRET_TOKEN)

try:
    API_HASHTAG_TEST = tweepy.API(AUTH_HASHTAG_TEST, wait_on_rate_limit=False, wait_on_rate_limit_notify=True)

except tweepy.TweepError as t:
    print(f"Erro: >>>{t}<<<")
    print('Error_Philobot! Falha ao pegar o Token de acesso!')

