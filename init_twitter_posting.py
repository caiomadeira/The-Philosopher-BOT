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
        self.log = LogEngine(__name__).log_posting()

        """ =========== POSTING TIME =========== """
        self.POST_TIME = 2

    def start_posting_official(self):
        from Credentials.Twitter.Official.main_credentials_official import API_MAIN_OFFICIAL

        self.log.info(f"POSTS DEFINIDOS PARA A CADA {self.OFFICIAL_POST_TIME} HORAS\n")

        from Twitter.Posting.posting import PostingClass
        start_posting = PostingClass(API_MAIN_OFFICIAL, LOG=self.log)
        PostingClass.start_timer_official(start_posting, USE_TEST_POST=self.OFFICIAL_POST_TIME)  # 2 HORAS

    def start_posting_test(self):
        from Credentials.Twitter.Test.test_credentials import API_TEST

        self.log.info(f"POSTS DEFINIDOS PARA A CADA {self.POST_TIME} SEGUNDOS\n")

        from Twitter.Posting.posting import PostingClass
        PostingClass(get_post_api=API_TEST, LOG=self.log).start_timer_test(USE_TEST_POST=self.POST_TIME)  # 2 SEGUNDOS


if __name__ == '__main__':
    # PostingOfficial().start_posting_official()
    PostingOfficial().start_posting_test()
