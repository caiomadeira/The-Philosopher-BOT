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
from Logs.Twitter.log_engine import LogEngine


class PostingOfficial:

    def __init__(self):
        get_post_config = Config()
        self.log = LogEngine(__name__).log_posting()

        """ =========== POSTING TIME =========== """
        self.OFFICIAL_POST_TIME = get_post_config.OFFICIAL_TIME_POST

    def start_posting_official(self):
        from Credentials.Twitter.Official.main_credentials_official import API_MAIN_OFFICIAL as API
        # from Credentials.Twitter.Test.test_credentials import API_TEST

        self.log.info(f"POSTS DEFINIDOS PARA A CADA {self.OFFICIAL_POST_TIME} HORAS EM 'config.py'\n")

        from Twitter.Posting.posting import PostingClass
        start_posting = PostingClass(API, LOG=self.log)
        PostingClass.timer(start_posting, USE_TEST_POST=self.OFFICIAL_POST_TIME)  # 2 HORAS
        # PostingClass.timer_TEST(start_posting, USE_TEST_POST=self.OFFICIAL_POST_TIME) # 2 SEGUNDOS


if __name__ == '__main__':
    start_app = PostingOfficial()
    start_app.start_posting_official()
