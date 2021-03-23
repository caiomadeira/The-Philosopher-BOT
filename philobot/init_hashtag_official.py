import time
import tweepy
from termcolor import colored
import schedule
from config import *
from Logs.logger_hashtag import log_hashtag
from Posting.posting import PostingClass

class StartHashtagOfficial:

    def __init__(self):

        get_config = Config()
        """ =========== HASHTAGS =========== """
        self.PHILOBOT_HASHTAG = get_config.PHILOBOT__HASHTAG
        self.PHILOMAKER_HASHTAG = get_config.PHILOMAKER__HASHTAG

        """ =========== SUBLIST =========== """
        self.PHILOBOT__SUBLIST = get_config.PHILOBOT__SUBLIST
        self.PHILOMAKER_SUBLIST = get_config.PHILOMAKER__SUBLIST

        self.TESTEPHILO__SUBLIST = get_config.TESTEPHILO__SUBLIST
        self.TESTMAKER_SUBLIST = get_config.TESTMAKER__SUBLIST

        """=========== SET LOG ==========="""
        self.log = log_hashtag(__name__)

    def start_hashtag_official(self):

        self.log.info("Bem-vindo!\n")
        self.log.info("Philosopher BOT por Caio Madeira e Rodrigo Carmo\n")
        self.log.info(">INICIANDO HASHTAG - OFFICIAL<")

        from Hashtag.hashtag import HashtagClass

        self.log.info('HASHTAG OFICIAL ESCOLHIDA, INICIANDO #PHILOBOT...')

        from Credentials.Official.main_credentials_official import API_MAIN_OFFICIAL as api_oficial
        #from Credentials.Test.main_credentials_test import API_MAIN_TEST as api_teste

        # TESTEPHILO
        Philobot_Stream = tweepy.Stream(auth=api_oficial.auth,
                                        listener=HashtagClass(self.PHILOBOT__SUBLIST, api_oficial),
                                        include_rts=False)

        Philobot_Stream.filter(track=['#Philobot'], is_async=True)

        # TESTEMAKER
        Philomaker_Stream = tweepy.Stream(auth=api_oficial.auth,
                                        listener=HashtagClass(self.PHILOMAKER_SUBLIST, api_oficial),
                                        include_rts=False)
        Philomaker_Stream.filter(track=['#Philomaker'], is_async=True)


if __name__ == '__main__':
    start_app = StartHashtagOfficial()
    start_app.start_hashtag_official()
