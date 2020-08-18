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
import time
from PIL import Image, ImageDraw, ImageFont
import random
import re
import textwrap
from contas import contas_list
from acess_tokens import *
from filosofo_list import filosofo, filosofo_special
from logger_posting import *
from art import *

(tprint("PHILOBOT V2.0"))
time.sleep(2)
log.info("Posting.py v2.0")


def postdiario():
    auth = tweepy.OAuthHandler(acess1, acess2)
    auth.set_access_token(acess3, acess4)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    img = Image.open('templates/templateNovo2.png')
    txt = "font/myriad.otf"
    fontsize = 1
    W, H = img.size
    blank = Image.new('RGB', (269, 194))
    fonte = ImageFont.truetype("font/myriad.otf", fontsize)
    log.info(img.size)
    log.info(blank.size)

    def obter_tweets(usuario, limite=1):
        resultados = api.user_timeline(screen_name=usuario, count=limite, tweet_mode='extended',
                                       contributor_details=False, include_entities=False, include_rts=False,
                                       trim_user=False, exclude_replies=True)
        tweets = []
        for r in resultados:
            tweet = re.sub(r'http\S+', '', r.full_text)
            tweets.append(tweet.replace('\n', ' '))
            time.sleep(2)
        return tweets

    escrever = ImageDraw.Draw(img)
    tweets = obter_tweets(random.choice(contas_list), limite=1)
    log.info("------------------------")
    log.info("TWEET SELECIONADO:")
    log.info(tweets)
    log.info("Analisando Texto...")

    for status in tweepy.Cursor(api.user_timeline).items(1):
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

    chance = (random.randint(1, 100))
    if chance <= 10:
        random_philo = random.choice(filosofo_special)
        img.paste(random_philo, (0, 0), random_philo)
        img.save('posting.png')
        api.update_with_media('posting.png')
        log.info("> DAILY POST ENVIADO! <")
        log.info("===================================================")


    elif chance > 10:

        random_philo = random.choice(filosofo)
        img.paste(random_philo, (0, 0), random_philo)
        img.save('posting.png')
        api.update_with_media('posting.png')
        log.info("> DAILY POST ENVIADO! <")
        log.info("===================================================")
    return
