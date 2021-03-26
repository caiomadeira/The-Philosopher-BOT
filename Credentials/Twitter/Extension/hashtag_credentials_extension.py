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

"""CONSUMER_KEY = os.environ.get('CONSUMER_KEY', None)

CONSUMER_SECRET_KEY = os.environ.get('CONSUMER_SECRET_KEY', None)

API_KEY = os.environ.get('API_KEY', None)

API_SECRET_TOKEN = os.environ.get('API_SECRET_TOKEN', None)

BEARER_TOKEN = os.environ.get('BEARER_TOKEN', None)"""

API_KEY = 'gyg6cCfa1W3XWM3kWFZpOxT91'

API_SECRET_KEY = 'Eu9nLCPivXSU5BMwCfQ6TLVTEHiorKEamZ4L6VoHiVAmTGrJcO'

BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAEcENQEAAAAA7Rf8u67NFu2F2KoACBUrphZkWec%3DiBKgGmS7ydmEgHEX28plkLCSXdFTEwJQOvHQUVR9T4yBsxG9iy'

ACCESS_TOKEN = '1192621203455905792-WmN8g3zb8TjPUgwEZmqLo9hEhBwAfJ'

ACCESS_SECRET_TOKEN = 'U8PZ9m57KqhRszLao9IPtikiG7DVBVNPVr1R9vba686Ye'


AUTH_HASHTAG_EXTENSION = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
AUTH_HASHTAG_EXTENSION.set_access_token(ACCESS_TOKEN, ACCESS_SECRET_TOKEN)

try:
    API_HASHTAG_EXTENSION = tweepy.API(AUTH_HASHTAG_EXTENSION, wait_on_rate_limit=False, wait_on_rate_limit_notify=True)

except tweepy.TweepError:
    print('Error_Philobot! Falha ao pegar o Token de acesso!')

