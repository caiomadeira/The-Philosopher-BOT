"""
Philosopher Bot
---------------
Created by Caio Madeira
Co-worker: Rodrigo Carmo

instagram: @sudomadeira
Twitter: @bot_philospher
Avaliable on Discord too!

"""
import schedule
import datetime
import time
from Logs.Twitter.log_engine import LogEngine


class PostingOfficial:

    def __init__(self):
        self.log = LogEngine(__name__).log_posting()

        """ =========== POSTING TIME =========== """
        self.POST_TIME = 4
        self.official_posting_account_name = 'bot_philosopher'
        self.test_posting_account_name = 'syscat_13'

    def start_posting_official(self):
        from Credentials.Twitter.Official.main_credentials_official import API_MAIN_OFFICIAL
        if self.check_last_post(api=API_MAIN_OFFICIAL, account=self.official_posting_account_name):
            from Twitter.Posting.posting import PostingClass
            self.log.info(f"POSTING MODULE [OFFICIAL] RUNNING, EXECUTING EVERY {self.POST_TIME} HOURS\n")

            PostingClass(post_api=API_MAIN_OFFICIAL, log=self.log).start_posting()

    def start_posting_test(self):
        from Credentials.Twitter.Test.test_credentials import API_TEST
        if self.check_last_post(api=API_TEST, account=self.test_posting_account_name):
            from Twitter.Posting.posting import PostingClass
            self.log.info(f"POSTING MODULE [TEST] RUNNING, EXECUTING EVERY {self.POST_TIME} SECONDS\n")

            PostingClass(post_api=API_TEST, log=self.log).start_posting()

    def check_last_post(self, api, account):
        self.log.info('[!] - Collecting the last post...')

        try:
            last_tweet = api.user_timeline(screen_name=account,
                                           count=1,
                                           contributor_details=True,
                                           include_entities=True,
                                           include_rts=False,
                                           trim_user=True,
                                           exclude_replies=True)[0]
            self.log.info(last_tweet)
            self.log.info('[OK] - Success!\n')


            self.log.info(f'[!] - Checking if the last post happened more than {self.POST_TIME} hours ago...')
            the_moment = datetime.datetime.now()
            tweet_time = last_tweet.created_at.replace(tzinfo=datetime.timezone.utc).astimezone(tz=None).replace(
                tzinfo=None)
            correct_time = datetime.timedelta(hours=self.POST_TIME)
            result_time = the_moment - tweet_time

            if result_time >= correct_time:
                self.log.info(f'[OK] - Last post happened more than {self.POST_TIME} hours ago: {result_time}')
                self.log.info('[!] - Start posting!\n')
                time.sleep(10)
                return True

            else:
                self.log.info(f'[ERROR] - Last post happened less than {self.POST_TIME} hours ago: {result_time}')
                self.log.info('[!] - Abort posting!')
                return False

        except Exception as check_last_post_err:
            self.log.info('[ERROR] - Error while trying to collect the last post!')
            self.log.info(check_last_post_err)
            choice = input(self.log.info('[?] - Do you want to proceed anyway and post now?[Y / N]'))

            if choice.upper() == 'Y':
                self.log.info('[!] - Start posting!\n')
                return True

            elif choice.upper() == 'N':
                self.log.info('[!] - Abort posting!')
                return False

            else:
                self.log.info('[WTF?] - Sorry, wrong answer.')


if __name__ == '__main__':
    PostingOfficial().start_posting_official()
    # PostingOfficial().start_posting_test()
