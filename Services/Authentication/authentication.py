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
from tweepy import OAuthHandler
from models.twitter.twitter import TwitterService
import dotenv
import os

dotenv.load_dotenv(dotenv.find_dotenv())


class Authentication(TwitterService):

    def __init__(self, is_test=None, is_primary=None, is_secondary=None):
        self.__is_test = is_test
        self.__is_primary = is_primary
        self.__is_secondary = is_secondary

    def __set_tokens(self):
        if self.__is_test:
            self.tokens['consumer_key'] = os.getenv("TEST_CONSUMER_KEY")
            self.tokens['consumer_key_secret'] = os.getenv("CONSUMER_KEY_SECRET")
            self.tokens['acess_token'] = os.getenv("TEST_ACESS_TOKEN")
            self.tokens['acess_token_secret'] = os.getenv("TEST_ACESS_TOKEN_SECRET")
            self.tokens['bearer_token'] = os.getenv("TEST_BEARER_TOKEN")
            return self.tokens
        if self.__is_primary:
            self.tokens['consumer_key'] = os.getenv("PRIMARY_CONSUMER_KEY")
            self.tokens['consumer_key_secret'] = os.getenv("PRIMARY_CONSUMER_KEY_SECRET")
            self.tokens['acess_token'] = os.getenv("PRIMARY_ACESS_TOKEN")
            self.tokens['acess_token_secret'] = os.getenv("PRIMARY_ACESS_TOKEN_SECRET")
            self.tokens['bearer_token'] = os.getenv("PRIMARY_BEARER_TOKEN")
            return self.tokens
        if self.__is_secondary:
            self.tokens['consumer_key'] = os.getenv("SECONDARY_CONSUMER_KEY")
            self.tokens['consumer_key_secret'] = os.getenv("SECONDARY_CONSUMER_KEY_SECRET")
            self.tokens['acess_token'] = os.getenv("SECONDARY_ACESS_TOKEN")
            self.tokens['acess_token_secret'] = os.getenv("SECONDARY_ACESS_TOKEN_SECRET")
            self.tokens['bearer_token'] = os.getenv("SECONDARY_BEARER_TOKEN")
            return self.tokens
        else:
            print("No tokens allowed.")

    def get_authorization(self):
        tokens = self.__set_tokens()
        auth = OAuthHandler(tokens['consumer_key'], tokens['consumer_key_secret'])
        auth.set_access_token(tokens['acess_token'], tokens['acess_token_secret'])
        return auth
