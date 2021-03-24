"""
Philosopher Bot
---------------
Created by Caio Madeira
Co-worker: Rodrigo Carmo

instagram: @sudomadeira
Twitter: @bot_philospher
Avaliable on Discord too!

"""
from config import Config
from Twitter.Posting.posting import PostingClass
from Logs.Twitter.logger_hashtag import log_posting


class PostingOfficial:

    def __init__(self):
        get_post_config = Config()
        self.log = log_posting(__name__)

        """ =========== POSTING TIME =========== """
        self.OFFICIAL_POST_TIME = get_post_config.OFFICIAL_TIME_POST

    def start_posting_official(self):
        from Credentials.Twitter.Official.main_credentials_official import API_MAIN_OFFICIAL as API
        # from Credentials.Test.main_credentials_test import API_MAIN_TEST as API

        self.log.info(f"POSTS DEFINIDOS PARA A CADA {self.OFFICIAL_POST_TIME} HORAS EM 'config.py'\n")

        start_posting = PostingClass(API)

        PostingClass.timer(start_posting, USE_TEST_POST=self.OFFICIAL_POST_TIME)  # 2 HORAS
        # PostingClass.timer_TEST(start_posting, USE_TEST_POST=self.OFFICIAL_POST_TIME) # 2 SEGUNDOS


if __name__ == '__main__':
    start_app = PostingOfficial()
    start_app.start_posting_official()
