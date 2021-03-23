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


CONSUMER_KEY = 'K4pPEVChE5ODuSWwPLY75jq3P'

CONSUMER_SECRET_KEY = 'hqr7SdcFM78LVkm6HcguxkzK7XUssuRVpVxhmOI93lA76pkvGl'

API_KEY = '1317291421523726342-qKhKdyoXLch2Gw4EjPj34w8XCQ3q5k'

API_SECRET_TOKEN = 'u9mX4Q8FeERbHOUALFE1SSGJWyhSFRz4VHcmGaBHgEtOt'

BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAM1XMQEAAAAAi5UVArrc6bGqblCJrWf8UMGEIKY%3D1zLtACnlknpeZS7RB4osPRQOwq2vBQYHPT1xRzqYTdn0OF13Zl'


AUTH_MAIN_TEST = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
AUTH_MAIN_TEST.set_access_token(API_KEY, API_SECRET_TOKEN)


try:
    API_MAIN_TEST = tweepy.API(AUTH_MAIN_TEST, wait_on_rate_limit=False, wait_on_rate_limit_notify=True)

except tweepy.TweepError as t:
    print(f"Erro: >>>{t}<<<")
    print('Error_Philobot! Falha ao pegar o Token de acesso!')

