import schedule, time, os, random, tweepy, re, textwrap, datetime, demoji
import emoji
from PIL import Image, ImageFont, ImageDraw
from Lists.accounts import accounts_list
from Lists.img_list import PHILOSOPHERS_LIST
from Credentials.Twitter.Test.test_credentials import API_TEST
from Templates.New_Img_Manipulation.path_reference import template_folder_reference
from Twitter.Posting.uploads.path_reference import upload_folder_reference
from dotenv import load_dotenv


class PostingClass:
    def __init__(self):
        load_dotenv()

        self.uploads_path = upload_folder_reference

        self.date_today = datetime.datetime.now().strftime('%Y%m%d')
        self.time_now = datetime.datetime.now().strftime('%H-%M-%S')

        self.posting_image_name = self.time_now + '_posting.png'
        self.finish_image = fr"{self.uploads_path}\{self.date_today}\{self.posting_image_name}"

        self.philosopher_path = random.choice(PHILOSOPHERS_LIST)
        self.philosopher_name_raw = os.path.basename(self.philosopher_path).replace('.png', '')
        self.philosopher_name = self.clear_philosopher_name()
        self.tweet_text = None
        self.tweet_id = None
        self.api = API_TEST
        self.philosopher_data = {}
        self.name_font_path = r'C:\Users\rodri\Documents\GitHub\The-Philosopher-BOT\Font\times.ttf'
        self.text_font_path = r'C:\Users\rodri\Documents\GitHub\The-Philosopher-BOT\Font\OpenSansEmoji.ttf'

    def start_posting(self):
        # 1 - coletar o texto de algum tweet
        self.create_uploads_folder()

        self.tweet_text = self.select_tweet()

        self.emoji_check()

        breakpoint()

        print(self.tweet_text)
        get_unicode = self.tweet_text.encode('unicode-escape').decode('ASCII')
        print(get_unicode)

        self.text_setting(raw_image=self.build_image())

        self.upload_image()

    def create_uploads_folder(self):
        try:
            self.uploads_path = self.uploads_path + '/'
            os.mkdir(self.uploads_path + self.date_today)
            print('CRIADO!')

        except FileExistsError:
            print('Arquivo ja existe')

        except Exception as create_uploads_folder_err:
            print(create_uploads_folder_err)

    def get_tweet(self):
        tweet_data = self.api.user_timeline(screen_name='syscat_13',
                                            count=1,
                                            tweet_mode='extended',
                                            contributor_details=True,
                                            include_entities=True,
                                            include_rts=False,
                                            trim_user=True,
                                            exclude_replies=True)

        for tweet in tweet_data:
            self.tweet_text = re.sub(r'http\S+', '', tweet.full_text).replace('\n', ' ')
            self.tweet_id = tweet.id
            time.sleep(2)

    def select_tweet(self):
        while True:
            self.get_tweet()

            if self.tweet_text:
                return self.tweet_text

            # time.sleep(10)
            # implementar funcionalidade de mudar de conta escolhida caso o tweet venha em branco

    def emoji_check(self):
        if emoji.emoji_count(self.tweet_text) > 0:
            print(emoji.demojize(self.tweet_text))















    def select_name_font(self):
        if len(self.philosopher_name) <= 20:
            return ImageFont.truetype(self.name_font_path, size=35)

        else:
            return ImageFont.truetype(self.name_font_path, size=30)

    def select_text_font(self):
        if len(self.tweet_text) <= 140:
            wrapper_limit = 21
            print('menos que 140')
            return [ImageFont.truetype(self.text_font_path, size=45), wrapper_limit]

        else:
            wrapper_limit = 30
            return [ImageFont.truetype(self.text_font_path, size=32), wrapper_limit]

    def text_setting(self, raw_image):
        text_adjust = self.select_text_font()

        raw_image_draw = ImageDraw.Draw(raw_image)

        raw_image_draw.text(xy=(43, 500), text=textwrap.fill(str('- ' + self.philosopher_name), 30),
                            fill=(255, 255, 255), font=self.select_name_font())

        print(self.tweet_text)
        # breakpoint()
        # raw_image_draw.text(xy=(68, 120), text=textwrap.fill(self.tweet_text, text_adjust[1]), fill=(255, 255, 255),
        #                     font=text_adjust[0])

        raw_image_draw.text(xy=(68, 120), text=self.tweet_text, fill=(255, 255, 255),
                            font=text_adjust[0])

        raw_image.save(self.finish_image)

    def clear_philosopher_name(self):
        if '(2)' in self.philosopher_name_raw:
            return self.philosopher_name_raw.replace('(2)', '')

        else:
            return self.philosopher_name_raw

    def build_image(self):
        raw_image = Image.open(f'{template_folder_reference}/background_image.png')

        philosopher_image = Image.open(self.philosopher_path).resize((449, 584))
        raw_image.paste(philosopher_image, (629, 0))

        smooth_template = Image.open(f'{template_folder_reference}/smooth_background.png')
        raw_image.paste(smooth_template, (0, 0), smooth_template)

        # build_image.save(r'C:\Users\rodri\Documents\GitHub\The-Philosopher-BOT\Test\image_smooth_test.png')

        return raw_image

    def upload_image(self):
        try:
            upload_image = self.api.update_with_media(self.finish_image)

            tweet_author = self.api.update_status(
                f'Tweet original: twitter.com/syscat_13/status/{self.tweet_id}',
                upload_image.id,
                include_entities=True)

        except Exception as upload_err:
            print('error')
            print(upload_err)

        print('Tweet enviado!')

    def start_timer_test(self):
        schedule.every(2).seconds.do(self.post_engine)

        while True:
            schedule.run_pending()


def select_account():
    return random.choice(accounts_list)


if __name__ == '__main__':
    p = PostingClass()
    p.start_posting()
