# _*_ coding: utf-8 _*_
"""
Philosopher Bot, 2021
---------------
Created by Caio Madeira
Co-worker: Rodrigo Carmo

instagram: @sudomadeira
Twitter: @bot_philospher
Avaliable on Discord too!
"""
from tweepy import OAuthHandler, Stream  # OAuth é o manipulador de autenticacao
from tweepy import TweepError
import tweepy


class Authentication:

    def __init__(self):
        # Consumer keys
        self.CONSUMER_KEY = "JJ23qk7QG4XTEa6a6XPII1ZhP"
        self.CONSUMER_KEY_SECRET = "UqNYLgqvIKB8WfSWGOD38NmnHvNIrcdFKOHYDXwkJm84xWXpcc"
        # Authentication Token
        self.ACESS_TOKEN = "1317291421523726342-VDMgaSoqZuAFXXbmKG5stElkMrd58R"
        self.ACESS_TOKEN_SECRET = "gkKYY5OtrCgIPzDUcNYRwUivYqg4leTMxC0dTOCEJknhA"
        self.BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAKspMQEAAAAA3axOG7IgnSJE4oss5sZ42AuBJvs" \
                            "%3DgTomUUezxuGzMazonl9uwYFxJ5LMbtLXeksiEMuXjVuMoTfZqK "

    def getAuthorization(self):
        auth = OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_KEY_SECRET)
        auth.set_access_token(self.ACESS_TOKEN, self.ACESS_TOKEN_SECRET)

        return auth
