"""
Philosopher Bot
---------------
Created by Caio Madeira
Co-worker: Rodrigo Carmo

instagram: @sudomadeira
Twitter: @bot_philospher
Avaliable on Discord too!

"""
# -*- coding: utf-8 -*-
import tweepy, textwrap, random, time, re, schedule
from PIL import Image, ImageDraw, ImageFont
import os
from Lists.accounts import accounts_list
from Lists.img_list import PHILOSOPHERS_LIST
from Twitter.Hashtag import Functionalities
from Templates.New_Img_Manipulation.reference import TEMPLATES_PATH
from Logs.Twitter.logger_hashtag import log_posting


class PostingClass(tweepy.StreamListener, Functionalities):
    def __init__(self, get_post_api):
        super().__init__()

        self.q = []
        self.q_username = []
        self.q_tweet_info = []
        self.api = get_post_api
        self.ACCOUNT = "OFICIAL"
        self.QUEUE = 1
        self.VERSION = '3.0'
        self.log = log_posting(__name__)

    def obter_tweets(self, api, USERNAME_ACCOUNT):

        self.results = api.user_timeline(screen_name=USERNAME_ACCOUNT,
                                         count=1,
                                         tweet_mode='extended',
                                         contributor_details=True,
                                         include_entities=True,
                                         include_rts=False,
                                         trim_user=True,
                                         exclude_replies=True)
        self.tweets = []

        for self.r in self.results:
            tweet = re.sub(r'http\S+', '', self.r.full_text)
            self.tweets.append(tweet.replace('\n', ' '))
            time.sleep(2)
        return self.tweets

    def posting(self):

        global random_account

        try:
            self.img = Image.open(f'{TEMPLATES_PATH}/layer_1.png')
            self.TEMPLATE_PATH = 'Templates/template.png'
            self.FONT_PATH = "Font/myriad.otf"
            self.POSTING_FINISHED_PATH = 'Posting/posting.png'
            txt = self.FONT_PATH
            fontsize = 1
            blank = Image.new('RGB', (269, 194))
            fonte = ImageFont.truetype(self.FONT_PATH, fontsize)

            self.log.info("--------------------------------------")
            self.log.info(f"[+] INICIANDO POSTAGEM NA CONTA {self.ACCOUNT}")
            self.log.info(f'[+] Versão: {self.VERSION}')
            time.sleep(2)

            try:

                self.log.info("------------------------")
                time.sleep(2)
                random_account = random.choice(accounts_list)
                try:
                    self.tweet_account = self.obter_tweets(self.api, random_account)

                except tweepy.error.TweepError as t:
                    self.log.info(t)
                    self.log.info('[x] Erro - Não autorizado\n[x] Ignorando...')
                    pass

                self.log.info("[+] TWEET SELECIONADO:")

                try:
                    self.log.info(self.tweet_account)

                except UnicodeEncodeError as u:
                    self.log.info('[x] Erro - UNICODE não pode ser codificado.\nIgnorando...')
                    self.log.info(u)

                self.log.info("[+] Analisando Texto...")
                time.sleep(2)
            except tweepy.error.TweepError as build_image_error:
                self.log.exception(build_image_error)
                pass

            for _ in tweepy.Cursor(self.api.user_timeline).items(1):
                try:
                    self.get_treated_status = ("\n".join(self.tweets))
                    if self.get_treated_status == '':
                        self.log.info('[!] String vazia detectada!')
                        self.log.info('[+] Retornando aos tweets novamente...')
                        self.log.info('----------------------')
                        return self.tweets
                except AttributeError as e:
                    self.log.info(e)
                    self.log.info('[x] Erro de Atributo.\nIgnorando...')
                    return self.posting

                while (fonte.getsize(txt)[0] < blank.size[0]) and (fonte.getsize(txt)[1] < blank.size[1]):
                    fontsize += 1
                    fonte = ImageFont.truetype(self.FONT_PATH, fontsize)

                fontsize -= 1
                self.drawing = ImageDraw.Draw(self.img)

                choice_philosopher = random.choice(PHILOSOPHERS_LIST)  # separa a imagem e salva em string
                self.log.info(choice_philosopher)

                remove_path_of_filename = os.path.basename(choice_philosopher)  # remove o path do nome da imagem
                self.log.info(remove_path_of_filename)

                remove_extension_of_filename = remove_path_of_filename.replace('.png', '')  # remove a extensao .png
                self.log.info(remove_extension_of_filename)

                if '(2)' in remove_extension_of_filename:
                    remove_number_in_name = remove_extension_of_filename.replace('(2)', '')
                    self.log.info("Removendo (2) do nome da imagem do filosofo...")
                    self.log.info(remove_number_in_name)
                    finish_name_of_philosopher = f'- {remove_number_in_name}'  # finaliza o nome do filosofo
                    self.log.info(finish_name_of_philosopher)
                else:
                    finish_name_of_philosopher = f'- {remove_extension_of_filename}'  # finaliza o nome do filosofo
                    self.log.info("Nenhum (2) encontrado. Prosseguindo normal.")
                    self.log.info(finish_name_of_philosopher)

                philosopher_str_to_obj = Image.open(choice_philosopher)  # abre a imagem como local na memoria ao inves de string
                IMG_2 = philosopher_str_to_obj.resize((449, 584))
                self.img.paste(IMG_2, (629, 0))
                smooth_template = Image.open(f'{TEMPLATES_PATH}/layer_3.png')
                self.img.paste(smooth_template, (0, 0), smooth_template)

                # texto do filosofo
                self.drawing.text(xy=(68, 120), text=textwrap.fill(str(self.get_treated_status), 30), fill=(255, 255, 255), font=fonte)

                # nome do filosofo
                fontsize = 30
                font = ImageFont.truetype("Font/times.ttf", fontsize)
                self.drawing.text(xy=(43, 514), text=textwrap.fill(str(finish_name_of_philosopher), 30),
                             fill=(255, 255, 255), font=font)


                self.img.save(self.POSTING_FINISHED_PATH)
                post_img = self.api.update_with_media(self.POSTING_FINISHED_PATH)
                tweet_author = self.api.update_status(f'Tweet Original: twitter.com/{random_account}/status/{self.r.id}',
                                                   post_img.id,
                                                   include_entities=True)


                self.log.info(f'[+]Tweet Original enviado: {tweet_author}')
                self.log.info("[+] Post Diário enviado.")
                self.log.info("-------------------------------------------")


                return
        except Exception as e:
            self.log.info(e)

    def timer(self, USE_TEST_POST):

        schedule.every(USE_TEST_POST).hours.do(self.posting)

        while True:
            schedule.run_pending()
            time.sleep(1)

    def timer_TEST(self, USE_TEST_POST):

        schedule.every(USE_TEST_POST).seconds.do(self.posting)

        while True:
            schedule.run_pending()
            time.sleep(1)
