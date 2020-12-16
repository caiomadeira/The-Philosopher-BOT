"""
posting.py
Philosopher Bot
---------------
Created by Caio Madeira (@sudomaidera)
Co-worker: Rodrigo Carmo @rodrigoblock

instagram: @sudomadeira
Twitter: @bot_philospher
Avaliable on Discord too!

"""
# -*- coding: utf-8 -*-
import tweepy, textwrap, random, time, re
from PIL import Image, ImageDraw, ImageFont

from Lists.accounts import contas_list
from Lists.img_list import filosofo
from Credentials.credentials_verify import api
from Logs.logger_posting import *


class PostDiario:

    def __init__(self):
        self.posting()
        self.api = api

    def posting(self):

        global escrever, random_conta
        img = Image.open('Templates/template.png')
        txt = "Font/myriad.otf"
        fontsize = 1
        _ = img.size
        blank = Image.new('RGB', (269, 194))
        fonte = ImageFont.truetype("Font/myriad.otf", fontsize)
        try:
            escrever = ImageDraw.Draw(img)
            log.info("------------------------")
            random_conta = random.choice(contas_list)
            tweets_conta = self.obter_tweets(api, random_conta)
            log.info("TWEET SELECIONADO:")
            log.info(tweets_conta)
            log.info("Analisando Texto...")
            time.sleep(2)
        except tweepy.error.TweepError:
            pass

        for _ in tweepy.Cursor(api.user_timeline).items(1):

            items = ("\n".join(tweets))
            if items == '':
                log.info('String vazia detectada!')
                log.info('Retornando aos tweets novamente...')
                log.info('----------------------')
                return tweets

            while (fonte.getsize(txt)[0] < blank.size[0]) and (fonte.getsize(txt)[1] < blank.size[1]):
                fontsize += 1
                fonte = ImageFont.truetype("Font/myriad.otf", fontsize)

            fontsize -= 1
            escrever.textsize(txt, font=fonte)
            escrever.text(xy=(43, 105), text=textwrap.fill(items, 30), fill=(255, 255, 255), font=fonte)
            random_philo = random.choice(filosofo)
            img.paste(random_philo, (0, 0), random_philo)
            img.save('posting.png')
            post = api.update_with_media('posting.png')
            ori_tweet = api.update_status(f'Tweet Original: twitter.com/{random_conta}/status/{r.id}', post.id,
                                          include_entities=True)
            log.info(f'TWEET ORIGINAL ENVIADO: {ori_tweet.text}')
            log.info("> DAILY POST ENVIADO! <")
            log.info("===================================================")

            return

    @staticmethod  # obter tweets is now a static method from class
    def obter_tweets(api, user):

        global tweets
        resultados = api.user_timeline(screen_name=user,
                                       count=1,
                                       tweet_mode='extended',
                                       contributor_details=True,
                                       include_entities=True,
                                       include_rts=False,
                                       trim_user=True,
                                       exclude_replies=True)
        tweets = []
        global r
        for r in resultados:
            tweet = re.sub(r'http\S+', '', r.full_text)
            tweets.append(tweet.replace('\n', ' '))
            time.sleep(2)
        return tweets


pass
