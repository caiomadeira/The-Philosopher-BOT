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

CONSUMER_KEY = 'rs4fLSFEKBmb2Z5fwrZU05eJr'

CONSUMER_SECRET_KEY = 'DOy4jZbfhBxBAIixTh5N8q4PAxYSjgRUFze7kWVNnoudAplq8f'

API_KEY = '1192621203455905792-Qds4frgeAvDgKLoFo8Ewxq11cAgvPV'

API_SECRET_TOKEN = 'KXYXByop7sLt3zrZXKyXXEvr42iUQt9ZMf0K7Ta2hf6sz'

BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAEcENQEAAAAA3cvf5yLz%2FFmLQsv%2BBGSDw7BIThI%3DQ6fDJZ75lcSXdsrVjmtTH2LjAICtF7bO9ug6gJa1TIQhkw0szg'


AUTH_HASHTAG_EXTENSION = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
AUTH_HASHTAG_EXTENSION.set_access_token(API_KEY, API_SECRET_TOKEN)

try:
    API_HASHTAG_EXTENSION = tweepy.API(AUTH_HASHTAG_EXTENSION, wait_on_rate_limit=False, wait_on_rate_limit_notify=True)

except tweepy.TweepError:
    print('Error_Philobot! Falha ao pegar o Token de acesso!')

