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

"""ORDER

CONSUMER KEY
CONSUMER SECRET KEY
API KEY | ACESS TOKEN
API SECRET KEY | ACESS TOKEN SECRET
BEARER_TOKEN"""


import tweepy.api

CONSUMER_KEY = 'I38Do8tgqZ3uFcGRNruLP1kr3'

CONSUMER_SECRET_KEY = 'e3br5IuMzuvjUTN1iDA9Z2ADkMPCpVdkcJlBBtP2hHeNR2JHJq'

API_KEY = '1192621203455905792-8yhaiIwMrj7Bwhb6wIG8M4RcgWcCf0'

API_SECRET_TOKEN = 'AMlBbscsaGStsswx8ch7n66NYrLBcTn1rXBipjqnFT6Dp'

BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAM1XMQEAAAAAi5UVArrc6bGqblCJrWf8UMGEIKY%3D1zLtACnlknpeZS7RB4osPRQOwq2vBQYHPT1xRzqYTdn0OF13Zl'


AUTH_MAIN_EXTENSION = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
AUTH_MAIN_EXTENSION.set_access_token(API_KEY, API_SECRET_TOKEN)

try:
    API_MAIN_EXTENSION = tweepy.API(AUTH_MAIN_EXTENSION, wait_on_rate_limit=False, wait_on_rate_limit_notify=True)

except tweepy.TweepError:
    print('Error_Philobot! Falha ao pegar o Token de acesso!')
