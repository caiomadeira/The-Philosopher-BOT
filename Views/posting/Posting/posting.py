import os
import re
import time
import random
import datetime
import textwrap
from dotenv import load_dotenv
from Lists.accounts import accounts_list
from PIL import Image, ImageFont, ImageDraw
from Lists.img_list import PHILOSOPHERS_LIST
from Twitter.Posting.uploads.path_reference import upload_folder_reference
from Templates.New_Img_Manipulation.path_reference import template_folder_reference


class PostingClass:
    def __init__(self, post_api, log):
        load_dotenv()

        try:
            self.uploads_path = upload_folder_reference

            self.date_today = datetime.datetime.now().strftime('%Y%m%d')
            self.time_now = datetime.datetime.now().strftime('%H-%M-%S')

            self.posting_image_name = self.time_now + '_posting.png'
            self.finish_image = fr"{self.uploads_path}\{self.date_today}\{self.posting_image_name}"

            self.philosopher_path = random.choice(PHILOSOPHERS_LIST)
            self.philosopher_name_raw = os.path.basename(self.philosopher_path).replace('.png', '')
            self.philosopher_name = self.clear_philosopher_name()

            self.log = log

            self.raw_image_draw = None
            self.smooth_template = None
            self.philosopher_image = None
            self.raw_image = None
            self.random_account = None
            self.tweet_text = None
            self.tweet_id = None
            self.api = post_api
            self.name_font_path = os.getenv("times_font")
            self.text_font_path = os.getenv("opensansemoji")

            self.log.info('[OK] - Variables initialized successfully!\n')

        except Exception as init_posting_err:
            self.log.info('[ERROR] - Error when tying to initialize variables!')
            self.log.info(init_posting_err)

    def start_posting(self):
        self.log.info('[!] - Creating folder to save posting images...')
        self.create_uploads_folder()

        self.log.info('[!] - Setting tweet text to variable...')
        self.tweet_text = self.select_tweet()

        self.log.info('[!] - Calling image and text constructor functions...')
        self.text_setting(raw_image=self.build_image())

        self.log.info('[!] - Calling upload to twitter function...')
        self.upload_image()

    def create_uploads_folder(self):
        try:
            self.uploads_path = self.uploads_path + '/'
            os.mkdir(self.uploads_path + self.date_today)
            self.log.info('[OK] - Folder created successfully!\n')

        except FileExistsError:
            self.log.info('[OK] - Folder already exists!\n')

        except Exception as create_uploads_folder_err:
            self.log.info('[ERROR] - Error when trying to create folder!\n')
            self.log.info(create_uploads_folder_err)

    def get_tweet(self):
        self.log.info('[!] - Starting search for tweet...')
        try:
            tweet_data = self.api.user_timeline(screen_name=self.random_account,
                                                count=1,
                                                tweet_mode='extended',
                                                contributor_details=True,
                                                include_entities=True,
                                                include_rts=False,
                                                trim_user=True,
                                                exclude_replies=True)
            self.log.info('[OK] - Tweet found successfully!\n')

            for tweet in tweet_data:
                self.tweet_text = re.sub(r'http\S+', '', tweet.full_text).replace('\n', ' ')
                self.tweet_id = tweet.id
                time.sleep(2)

        except Exception as get_tweet_err:
            self.log.info('[ERROR] - Error when trying to start api from twitter!')
            self.log.info(get_tweet_err)

    def select_tweet(self):
        self.log.info('[!] - Initializing tweet collector...')
        while True:
            self.log.info('[!] - Randomly selecting account...')
            self.select_account()

            self.log.info('[!] - Calling twitter function...')
            self.get_tweet()

            self.log.info('[!] - Checking if we have text from tweet...')
            if self.tweet_text:
                self.log.info(f'[OK] - Tweet text - {self.tweet_text}')
                self.log.info(f'[OK] - Tweet id - {self.tweet_id}')
                self.log.info('[OK] - Success!\n')
                return self.tweet_text

            else:
                self.log.info('[ERROR] - Text not found, trying another Twitter account...')
                self.log.info('[ZZZ] - Sleeping for security reasons [10 seconds]...\n')
                time.sleep(10)

    def select_name_font(self):
        self.log.info(f'[OK] - Philosopher selected - {self.philosopher_name}\n')
        self.log.info('[!] - Defining the font size...')
        if len(self.philosopher_name) <= 20:
            self.log.info('[!] - Philosopher name is smaller than 20 characters!')
            return ImageFont.truetype(self.name_font_path, size=35)

        else:
            self.log.info('[!] - Philosopher name is bigger than 20 characters!')
            return ImageFont.truetype(self.name_font_path, size=30)

    def select_text_font(self):
        self.log.info('[!] - Checking text size...')
        if len(self.tweet_text) <= 140:
            self.log.info('[!] - Text smaller than 140 characters!')
            self.log.info('[!] - Variables set: font size = 45, wrapper limit = 21, text height = 80')
            self.log.info('[OK] - Success!\n')

            text_height = 90
            wrapper_limit = 21
            return [ImageFont.truetype(self.text_font_path, size=45), wrapper_limit, text_height]

        else:
            self.log.info('[!] - Text bigger than 140 characters!')
            self.log.info('[!] - Variables set: font size = 32, wrapper limit = 30, text height = 60')
            self.log.info('[OK] - Success!\n')
            text_height = 60
            wrapper_limit = 30
            return [ImageFont.truetype(self.text_font_path, size=32), wrapper_limit, text_height]

    def text_setting(self, raw_image):
        self.log.info('[!] - Calling font selector function...')
        text_adjust = self.select_text_font()

        self.log.info('[!] - Transforming image base into an object...')
        try:
            self.raw_image_draw = ImageDraw.Draw(raw_image)
            self.log.info('[OK] - Success!\n')

        except Exception as img_objct_err:
            self.log.info('[ERROR] - Error when trying to transform image into an object!')
            self.log.info(img_objct_err)

        self.log.info('[!] - Writing the philosopher name...')
        try:
            self.raw_image_draw.text(xy=(43, 500), text=textwrap.fill(str('- ' + self.philosopher_name), 30),
                                     fill=(255, 255, 255), font=self.select_name_font())
            self.log.info('[OK] - Success!\n')

        except Exception as write_name_err:
            self.log.info('[ERROR] - Error when trying to write the philosopher name on the image!')
            self.log.info(write_name_err)

        self.log.info('[!] - Writing the tweet text...')
        try:
            self.raw_image_draw.text(xy=(68, text_adjust[2]), text=textwrap.fill(self.tweet_text, text_adjust[1]),
                                     fill=(255, 255, 255),
                                     font=text_adjust[0])
            self.log.info('[OK] - Success!\n')

        except Exception as write_text_err:
            self.log.info('[ERROR] - Error when trying to write the tweet text on the image!')
            self.log.info(write_text_err)

        self.log.info('[!] - Saving posting image...')

        try:
            raw_image.save(self.finish_image)
            self.log.info('[OK] - Success!\n')

        except Exception as save_post_img:
            self.log.info('[ERROR] - Error when trying to save image!')
            self.log.info(save_post_img)

    def clear_philosopher_name(self):
        if '(2)' in self.philosopher_name_raw:
            return self.philosopher_name_raw.replace('(2)', '')

        else:
            return self.philosopher_name_raw

    def build_image(self):
        self.log.info('[!] - Opening background image...')
        try:
            self.raw_image = Image.open(f'{template_folder_reference}/background_image.png')
            self.log.info('[OK] - Success!\n')

        except Exception as bg_img_err:
            self.log.info('[ERROR] - Error when trying to open background image!')
            self.log.info(bg_img_err)

        self.log.info('[!] - Opening philosopher image...')
        try:
            self.philosopher_image = Image.open(self.philosopher_path).resize((449, 584))
            self.log.info('[OK] - Success!\n')

        except Exception as ph_img_err:
            self.log.info('[ERROR] - Error when trying to open philosopher image!')
            self.log.info(ph_img_err)

        self.log.info('[!] - Pasting philosopher image into the background image...')
        try:
            self.raw_image.paste(self.philosopher_image, (629, 0))
            self.log.info('[OK] - Success!\n')

        except Exception as paste_img_err:
            self.log.info('[ERROR] - Error when trying to paste image!')
            self.log.info(paste_img_err)

        self.log.info('[!] - Opening smooth template...')
        try:
            self.smooth_template = Image.open(f'{template_folder_reference}/smooth_background.png')
            self.log.info('[OK] - Success!\n')

        except Exception as smooth_img_err:
            self.log.info('[ERROR] - Error when trying to open smooth template!')
            self.log.info(smooth_img_err)

        self.log.info('[!] - Pasting smooth template...')
        try:
            self.raw_image.paste(self.smooth_template, (0, 0), self.smooth_template)
            self.log.info('[OK] - Success!\n')

        except Exception as paste_smooth_err:
            self.log.info('[ERROR] - Error when trying to paste image!')
            self.log.info(paste_smooth_err)

        return self.raw_image

    def upload_image(self):
        self.log.info('[!] - Uploading image...')
        try:
            upload_image = self.api.update_with_media(self.finish_image)

            self.api.update_status(
                f'Tweet original: twitter.com/{self.random_account}/status/{self.tweet_id}',
                upload_image.id,
                include_entities=True)

            self.log.info('[OK] - Success!\n')
            self.log.info(f'[OK] - Tweet sent! Tweet author: {self.random_account} | Philosopher: {self.philosopher_name}')
            self.log.info(f'[OK] - Tweet text: {self.tweet_text}')

        except Exception as upload_err:
            self.log.info('[ERROR] - Error when trying to upload image!')
            self.log.info(upload_err)

    def select_account(self):
        try:
            self.random_account = random.choice(accounts_list)
            self.log.info(f'[OK] - Account selected successfully! - {self.random_account}\n')

        except Exception as select_random_account_err:
            self.log.info('[ERROR] -  Error when trying to select an account!')
            self.log.info(select_random_account_err)
