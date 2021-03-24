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


CONSUMER_KEY = '0cntJAsPOV0hks9CQSeURRcEB'

CONSUMER_SECRET_KEY = 'rvr2Ysy0kZviDHSjQkNBJt907MUamTuIajlUo7mPxmX7WXTjOE'

API_KEY = '1263355414248390662-IEbCMivZ3cuC1YSLT146rzuWxvNP1O'

API_SECRET_TOKEN = 'hDQdl5n58TL35f04Uf8XoM1v6lInQXhGJKfDW01icNYG5'

BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAOoXIAEAAAAADaa5oBsJbeTBy1p3yAg7nhJqq1g%3DeWgsrxaT2io5XQmK1AcNkB1sawtGF3GUeek7wsOBemKvukRQ9L'


AUTH_MAIN_OFFICIAL = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
AUTH_MAIN_OFFICIAL.set_access_token(API_KEY, API_SECRET_TOKEN)


try:
    API_MAIN_OFFICIAL = tweepy.API(AUTH_MAIN_OFFICIAL, wait_on_rate_limit=False, wait_on_rate_limit_notify=True)

except tweepy.TweepError as t:
    print(f"Erro: >>>{t}<<<")
    print('Error_Philobot! Falha ao pegar o Token de acesso!')

