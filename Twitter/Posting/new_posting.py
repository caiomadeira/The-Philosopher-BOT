import schedule, time, os, random, tweepy
from PIL import Image, ImageFont
from Lists.accounts import accounts_list
from Lists.img_list import PHILOSOPHERS_LIST
from Credentials.Twitter.Test.test_credentials import API_TEST


class PostingClass:
    def __init__(self):
        self.FONT_PATH = os.getenv('myriad_font')
        self.api = API_TEST
        pass

    def get_tweets(self):
        return self.api.user_timeline(screen_name='rodrigoblock4',
                                        count=1,
                                        tweet_mode='extended',
                                        contributor_details=True,
                                        include_entities=True,
                                        include_rts=False,
                                        trim_user=True,
                                        exclude_replies=True)

    def post_engine(self):
        # new_image = Image.new('RGB', (269, 194))
        # font = ImageFont.truetype(self.FONT_PATH, 1)
        v1 = random.choice(PHILOSOPHERS_LIST)
        v2 = os.path.basename(v1).replace('.png', '')


        print(v2)

    def start_timer_test(self):
        schedule.every(2).seconds.do(self.post_engine)

        while True:
            schedule.run_pending()


def select_account():
    return random.choice(accounts_list)


if __name__ == '__main__':
    PostingClass().post_engine()
