"""
Philosopher Bot
---------------
Created by Caio Madeira
Co-worker: Rodrigo Carmo

instagram: @sudomadeira
Twitter: @bot_philospher
Avaliable on Discord too!

"""
from Lists.sub_list import *


class Config:

    def __init__(self):
        self.positions = {
            'tweet_default_PosX': 43,
            'tweet_default_PosY': 110,
            'tweet_with_quotes_PosX': 50,
            'tweet_with_quotes_PosY': 120,
            'textwraped_value': 25,
            'author_quote_posX': 43,
            'author_quote_posY': 512
        }
        self.PHILOBOT__HASHTAG = '#Philobot'
        self.TESTEPHILO__HASHTAG = '#Testephilo'
        self.PHILOMAKER__HASHTAG = '#Philomaker'
        self.TESTEMAKER__HASHTAG = '#Testemaker'

        self.OFFICIAL_TIME_POST = 2
        self.EXTENSION_TIME_POST = 2
        self.TEST_TIME_POST = 2

        self.PHILOBOT__SUBLIST = sub_list_philobot
        self.TESTEPHILO__SUBLIST = sub_list_testephilo
        self.PHILOMAKER__SUBLIST = sub_list_philomaker
        self.TESTMAKER__SUBLIST = sub_list_test_philomaker



