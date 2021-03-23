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

from Lists.accounts import contas_list
from Lists.img_list import PHILOSOPHERS_LIST
from Logs.logger_posting import *
from config import SECONDS, HOURS, VERSION, HOURS_TO_SECONDS


def time_count_to_posting(TIME):
    for i in range(1, TIME):
        FALTAM = TIME - i
        log.info(f"{FALTAM} segundos restantes para a próxima postagem.")
        time.sleep(1)
    return


# ===========================================================================================================
# ===========================================================================================================
# ===========================================================================================================

def choose_account():
    global api
    global ACCOUNT
    global SUBLIST_CONFIG

    TOKEN_CHOICE = input("Escolha a conta para iniciar o POSTING: \n "
                         "[1] - TWITTER OFICIAL \n "
                         "[2] - TWITTER EXTENSION \n "
                         "[3] - TWITTER TESTE \n "
                         " Digite aqui: ")

    # ORIGINAL ACCOUNT

    if TOKEN_CHOICE == "1":
        from Credentials.credentials_verify_oficial import api_oficial
        api = api_oficial
        ACCOUNT = "OFICIAL"
        log.info(f"\nPOSTS DEFINIDOS PARA A CADA {HOURS} HORAS EM 'config.py'\n")
        time.sleep(2)
        schedule.every(HOURS).hours.do(posting)
        # time_count_to_posting(TIME=HOURS_TO_SECONDS)
        while True:
            schedule.run_pending()
            time.sleep(1)

    # EXTENSION ACCOUNT

    if TOKEN_CHOICE == "2":
        from Credentials.credentials_verify_reserva import api_reserva
        api = api_reserva
        ACCOUNT = "EXTENSION"
        print("============ A V I S O ================")
        question = input("Você selecionou a conta EXTENSION, ela não constuma a fazer postagens. \n Se "
                         "tem certeza que deseja continuar digite [1] \n Se quiser voltar para o menu, digite [2]\n")
        if question == "1":
            log.info(f"\nPOSTS DEFINIDOS PARA A CADA {HOURS} HORAS EM 'config.py'\n")
            print("==================================")
            time.sleep(2)
            schedule.every(HOURS).seconds.do(posting)
            # time_count_to_posting(TIME=HOURS_TO_SECONDS)
            while True:
                schedule.run_pending()
                time.sleep(1)

        if question == "2":
            print("Voltando...")
            print("=============================")
            return choose_account()

    # TEST ACCOUNT

    if TOKEN_CHOICE == "3":
        from Credentials.credentials_verify_test import api_test
        api = api_test
        ACCOUNT = "TESTE"
        log.info(f"POSTS DEFINIDOS PARA A CADA {SECONDS} SEGUNDOS EM 'config.py'\n")
        time.sleep(1)
        schedule.every(SECONDS).seconds.do(posting)
        # time_count_to_posting(TIME=SECONDS)
        while True:
            schedule.run_pending()
            time.sleep(1)

    return api


# ===========================================================================================================
# ===========================================================================================================
# ===========================================================================================================

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


# ===========================================================================================================
# ===========================================================================================================
# ===========================================================================================================

def posting():
    global escrever, random_conta
    img = Image.open('Templates/template.png')
    txt = "Font/myriad.otf"
    fontsize = 1
    _ = img.size
    blank = Image.new('RGB', (269, 194))
    fonte = ImageFont.truetype("Font/myriad.otf", fontsize)

    log.info("--------------------------------------")
    log.info(f"INICIANDO POSTAGEM NA CONTA {ACCOUNT}")
    log.info(f'Versão: {VERSION}')
    time.sleep(2)

    try:
        escrever = ImageDraw.Draw(img)
        log.info("------------------------")
        time.sleep(2)
        random_conta = random.choice(contas_list)
        tweets_conta = obter_tweets(api, random_conta)
        log.info("TWEET SELECIONADO:")
        log.info(tweets_conta)
        log.info("Analisando Texto...")
        time.sleep(2)
    except tweepy.error.TweepError:
        pass

    for _ in tweepy.Cursor(api.user_timeline).items(1):
        try:
            items = ("\n".join(tweets))
            if items == '':
                log.info('String vazia detectada!')
                log.info('Retornando aos tweets novamente...')
                log.info('----------------------')
                return tweets
        except Exception as e:
            print(e)
        pass

        while (fonte.getsize(txt)[0] < blank.size[0]) and (fonte.getsize(txt)[1] < blank.size[1]):
            fontsize += 1
            fonte = ImageFont.truetype("Font/myriad.otf", fontsize)

        fontsize -= 1
        escrever.textsize(txt, font=fonte)
        escrever.text(xy=(43, 105), text=textwrap.fill(items, 30), fill=(255, 255, 255), font=fonte)
        random_philo = random.choice(PHILOSOPHERS_LIST)
        img.paste(random_philo, (0, 0), random_philo)
        img.save('Posting/posting.png')
        post = api.update_with_media('Posting/posting.png')
        ori_tweet = api.update_status(f'Tweet Original: twitter.com/{random_conta}/status/{r.id}', post.id,
                                      include_entities=True)
        log.info(f'TWEET ORIGINAL ENVIADO: {ori_tweet.text}')
        log.info("> DAILY POST ENVIADO! <")
        log.info("===================================================")

        return
