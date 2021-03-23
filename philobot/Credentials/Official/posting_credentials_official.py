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


CONSUMER_KEY = '2ljStz9SV0cWsF7An53Jz2srH'

CONSUMER_SECRET_KEY = 'wbxVHS8Wm2TykSM1tPkmUV40ZeBsDZY40dsiG9j0VCqdKacJaS'

API_KEY = '1263355414248390662-AIEg8yn1o4hGR6QJoZh4jlrfTsmspf'

API_SECRET_TOKEN = '7niuy47CJhfYS7MViwaKEI3x93txcJjYSu8hvKMglURtq'

BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAPQqMQEAAAAABkNK0Q1gU3%2BtgAaIAwXcwphf7PU%3DoZHxgmD52uSPqvW4JtBqvTpV8FiSkWY9WPIKxdoG7z8gg3uW0o'


AUTH_POSTING_OFFICIAL = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
AUTH_POSTING_OFFICIAL.set_access_token(API_KEY, API_SECRET_TOKEN)


try:
    API_POSTING_OFFICIAL = tweepy.API(AUTH_POSTING_OFFICIAL, wait_on_rate_limit=False, wait_on_rate_limit_notify=True)

except tweepy.TweepError as t:
    print(f"Erro: >>>{t}<<<")
    print('Error_Philobot! Falha ao pegar o Token de acesso!')