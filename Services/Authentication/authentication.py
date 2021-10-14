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
import tweepy
from tweepy import OAuthHandler, API
from models.twitter.twitter import TwitterService
import dotenv
import os
import sys

dotenv.load_dotenv(dotenv.find_dotenv())


class Authentication(TwitterService):

    def __init__(self, is_debug=None, is_primary=False, is_secondary=False):
        self.__is_debug = is_debug
        self.__is_primary = is_primary
        self.__is_secondary = is_secondary

    def set_tokens(self):
        if self.__is_debug:
            self.tokens['consumer_key'] = os.getenv("TEST_CONSUMER_KEY")
            self.tokens['consumer_key_secret'] = os.getenv("TEST_CONSUMER_KEY_SECRET")
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
        elif self.__is_debug is False and self.__is_primary is False and self.__is_secondary is False:
            print("No parameters passed.")
            sys.exit()

    @staticmethod
    def get_authorization(tokens, debug=False):
        if debug:
            print("Showing TOKENS:", tokens)
            pass
        else:
            pass
        try:
            auth = OAuthHandler(tokens['consumer_key'], tokens['consumer_key_secret'])
            auth.set_access_token(tokens['acess_token'], tokens['acess_token_secret'])
            return auth
        except TypeError:
            print("No tokens allowed.")
            sys.exit()

    def get_api(self, auth):
        api = API(auth)
        return api

    def setup_auth(self):
        auth_class = Authentication(is_debug=self.__is_debug, is_primary=self.__is_primary, is_secondary=self.__is_secondary)
        tokens = auth_class.set_tokens()
        auth = auth_class.get_authorization(tokens=tokens, debug=True)
        auth_obj = tweepy.API(auth, wait_on_rate_limit=False, wait_on_rate_limit_notify=True)
        return auth_obj
