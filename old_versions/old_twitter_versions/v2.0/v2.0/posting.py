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
import tweepy
from PIL import Image, ImageDraw, ImageFont
import random
import textwrap
from contas import contas_list
#from acess_tokens import *
from acess_tokens_reserva import *
from filosofo_list import filosofo
from logger_posting import *
from art import *
import re
import time

(tprint("PHILOBOT V2.1"))
time.sleep(2)
log.info("Posting.py v2.0")


class PostDiario:

    def __init__(self):
        self.consumer_key = acess3
        self.consumer_secret = acess4
        self.secret = acess2
        self.token = acess1
        self.posting()

    def posting(self):

        auth = tweepy.OAuthHandler(acess1, acess2)
        auth.set_access_token(acess3, acess4)
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

        img = Image.open('templates/templateNovo2.png')
        txt = "font/myriad.otf"
        fontsize = 1
        W, H = img.size
        blank = Image.new('RGB', (269, 194))
        fonte = ImageFont.truetype("font/myriad.otf", fontsize)

        def obter_tweets(usuario, limite=1):
            global tweets
            resultados = api.user_timeline(screen_name=usuario, count=limite, tweet_mode='extended',
                                           contributor_details=True, include_entities=True, include_rts=False,
                                           trim_user=True, exclude_replies=True)
            tweets = []
            global r
            for r in resultados:
                tweet = re.sub(r'http\S+', '', r.full_text)
                tweets.append(tweet.replace('\n', ' '))
                time.sleep(2)
            return tweets

        escrever = ImageDraw.Draw(img)
        random_conta = random.choice(contas_list)
        tweets_conta = obter_tweets(random_conta, limite=1)
        log.info("------------------------")
        log.info("TWEET SELECIONADO:")
        log.info(tweets_conta)
        log.info("Analisando Texto...")

        for _ in tweepy.Cursor(api.user_timeline).items(1):

            items = ("\n".join(tweets))
            if items == '':
                log.info('String vazia detectada!')
                log.info('Retornando aos tweets novamente...')
                log.info('----------------------')
                return tweets

            while (fonte.getsize(txt)[0] < blank.size[0]) and (fonte.getsize(txt)[1] < blank.size[1]):
                fontsize += 1
                fonte = ImageFont.truetype("font/myriad.otf", fontsize)

                # ----------------------------------------------------------------------
            fontsize -= 1
            fonte = ImageFont.truetype("font/myriad.otf", fontsize)
            w, h = escrever.textsize(txt, font=fonte)

            escrever.text(xy=(43, 105), text=textwrap.fill(items, 30), fill=(255, 255, 255), font=fonte)

            random_philo = random.choice(filosofo)
            img.paste(random_philo, (0, 0), random_philo)
            img.save('posting.png')
            post = api.update_with_media('posting.png')
            api.update_status(f'Tweet Original: twitter.com/{random_conta}/status/{r.id}', post.id,
                              include_entities=True)
            log.info('> RESPOSTA DO TWEET ')
            log.info("> DAILY POST ENVIADO! <")
            log.info("===================================================")

            return

    def sched_posting(self):
        import schedule
        import time
        #schedule.every(3).seconds.do(self.posting)
        schedule.every(2).hours.do(self.posting)

        while True:
            schedule.run_pending()
            time.sleep(1)


pass
