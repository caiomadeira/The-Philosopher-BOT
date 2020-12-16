"""
Philosopher Bot
---------------
Created by Caio Madeira
Co-worker: Rodrigo Carmo

instagram: @sudomadeira
Twitter: @bot_philospher
Avaliable on Discord too!

"""
import random
import re
import textwrap
import time
import tweepy
from PIL import Image, ImageDraw, ImageFont
import requests
from Lists.img_list import PHILOSOPHERS_LIST
from Lists.sub_list import sub_list_testephilo, sub_list_philobot, sub_list_test_philomaker
from Logs.logger_hashtag import *
from config import FILA, VERSION

q = []
q_username = []


def choose_account():
    global api
    global ACCOUNT
    global SUBLIST_CONFIG
    global HASHTAG_CONFIG
    global PHILOMAKER_CONFIG
    global SUBLIST_CONFIG_MAKER

    TOKEN_CHOICE = input("Escolha a conta para iniciar a HASHTAG: \n "
                         "[1] - TWITTER OFICIAL \n "
                         "[2] - TWITTER EXTENSION \n "
                         "[3] - TWITTER TESTE \n "
                         " Digite aqui: ")

    if TOKEN_CHOICE == "1":
        from Credentials.credentials_verify_oficial import api_oficial
        api = api_oficial
        HASHTAG_CONFIG = '#PhiloBot'
        PHILOMAKER_CONFIG = '#PhiloMaker'
        SUBLIST_CONFIG = sub_list_philobot
        ACCOUNT = "OFICIAL"

    if TOKEN_CHOICE == "2":
        from Credentials.credentials_verify_reserva import api_reserva
        api = api_reserva
        HASHTAG_CONFIG = '#PhiloBot'
        PHILOMAKER_CONFIG = '#PhiloMaker'
        SUBLIST_CONFIG = sub_list_philobot
        ACCOUNT = "EXTENSION"

    if TOKEN_CHOICE == "3":
        from Credentials.credentials_verify_test import api_test
        api = api_test
        HASHTAG_CONFIG = '#TestePhilo'
        PHILOMAKER_CONFIG = '#TesteMaker'
        SUBLIST_CONFIG_MAKER = sub_list_test_philomaker
        SUBLIST_CONFIG = sub_list_testephilo
        ACCOUNT = "TESTE"

    return api


def starting_hashtag():
    global myStream_PhiloBot
    global myStream_PhiloMaker

    choose_account()
    log.info("\nCONTA ESCOLHIDA")
    log.info("--------------------------------------")
    log.info(f"INICIANDO HASHTAG NA CONTA {ACCOUNT}")
    print(f'Versão: {VERSION}')
    time.sleep(2)
    log.info(f"Escutando tweets da Hashtag: {HASHTAG_CONFIG} e {PHILOMAKER_CONFIG}....")
    time.sleep(2)
    MyStreamListener()
    the_api = api

    myStream_PhiloBot = tweepy.Stream(auth=the_api.auth, listener=MyStreamListener())
    myStream_PhiloBot.filter(track=[HASHTAG_CONFIG], is_async=True)

    myStream_PhiloMaker = tweepy.Stream(auth=the_api.auth, listener=MyStreamListener())
    myStream_PhiloMaker.filter(track=[PHILOMAKER_CONFIG], is_async=True)


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        log.info("========== NOVO TWEET ENCONTRADO ===========")

        username = status.user.screen_name
        tweetid = str(status.id)
        q.append(tweetid)
        q_username.append(username)

        log.info('Tweet ID: ' + tweetid)
        log.info('Tweet USERNAME: ' + username)
        log.info('Aguardando o próximo tweet')
        log.info('--------------------------------------------\n')
        time.sleep(20)

        if len(q) >= FILA:
            philobot_engine()


def update(post, status, username):
    numero = 1
    try:
        tweepy.Cursor(api.user_timeline).items(numero)
        api.update_with_media(post, status="@" + username + " ", auto_populate_reply_metadata=True,
                              in_reply_to_status_id=status)
        time.sleep(5)
    except tweepy.TweepError as e:
        log.info(e.reason)
        log.info("ERRO! Não foi possivel realizar a ação para o usuário.")
        log.info("\n==========================")


def check_emptystring(lastid):
    log.info('STRING VAZIA DETECTADA!')

    error_collection = ['Templates/templateERRO6.png', 'Templates/templateERRO1.png',
                        'Templates/templateERRO2.png', 'Templates/templateERRO3.png',
                        'Templates/templateERRO4.png', 'Templates/templateERRO5.png',
                        'Templates/templateGIFERRO.gif']

    escolher_img = random.randrange(0, len(error_collection))
    img_selecionada = error_collection[escolher_img]

    user = q_username.pop(0)
    log.info('ENVIANDO TEMPLATE DE AJUDA PARA O @{}.'.format(user))

    update(post=img_selecionada, status=lastid, username=user)
    log.info('Voltando a ouvir tweets...')


def philobot_engine():
    global txt, img, fontsize, lastid
    global blank
    global fonte

    log.info('----------------------------------------')
    log.info('_\|/_ STARTING PHILO_BOT_ENGINE _\|/_ ')
    log.info('----------------------------------------')
    while len(q) > 0:

        fila = len(q)
        log.info('TAMANHO FILA: ' + str(fila))
        lastid = q.pop(0)
        log.info('Motor atuando: ' + lastid)

        img = Image.open('Templates/template.png')
        txt = "Font/myriad.otf"
        fontsize = 1
        _ = img.size
        blank = Image.new('RGB', (269, 194))
        fonte = ImageFont.truetype("Font/myriad.otf", fontsize)

        # ------------------------------------------------------------------------------------------
        # -------------------------- PEGANDO O STATUS  --------------------------------------------
        # ------------------------------------------------------------------------------------------

        pegando_status = api.get_status(lastid, tweet_mode='extended')._json['full_text']
        log.info('STATUS CONVERTIDO: ' + pegando_status)
        # ============================================================================
        if 'testemaker' in pegando_status:
            text_treatment(PEG_STATUS=pegando_status, IMG=img, SUB_LIST=SUBLIST_CONFIG_MAKER)
            philomaker(PEG_STATUS=pegando_status, IMG=img, FONT_SIZE=fontsize, LAST_ID=lastid)

        # ------------------------------------------------------------------------------------------
        # -------------------------- TRATAMENTO DO TEXTO -------------------------------------------
        # ------------------------------------------------------------------------------------------

        text_treatment(PEG_STATUS=pegando_status, IMG=img, SUB_LIST=SUBLIST_CONFIG)

        # ------------------------------------------------------------------------------------------
        # -------------------------- VERIFICA STRING VAZIA  ----------------------------------------
        # ------------------------------------------------------------------------------------------
        try:
            if not pegando_status2:
                check_emptystring(lastid)
                return MyStreamListener
        except tweepy.error.TweepError as e:
            print(e)
            log.info('ERRO AO MANDAR MENSAGEM DE ERRO')
            q_username.clear()
            log.info('Voltando a ouvir tweets...')
            return MyStreamListener

        # ------------------------------------------------------------------------------------------
        # -------------------------- AJUSTE DE FONTE E TEXTO   ------------------------------------
        # ------------------------------------------------------------------------------------------

        while (fonte.getsize(txt)[0] < blank.size[0]) and (fonte.getsize(txt)[1] < blank.size[1]):
            fontsize += 1
            fonte = ImageFont.truetype("Font/myriad.otf", fontsize)

        fontsize -= 1
        fonte = ImageFont.truetype("Font/myriad.otf", fontsize)
        escrever.textsize(txt, font=fonte)

        # ----------------------------------------------------------------------------
        # ----------------------- ESCREVE O TEXTO NA IMAGEM  --------------------------
        # -----------------------------------------------------------------------------

        escrever.text(xy=(43, 110), text=textwrap.fill(str(pegando_status2), 28),
                      fill=(255, 255, 255), font=fonte)

        # ------------------------------------------------------------------------
        # ------------------ TRATAMENTO DE IMAGEM E POSTAGEM ---------------------
        # ------------------------------------------------------------------------

        random_philo = random.choice(PHILOSOPHERS_LIST)
        img.paste(random_philo, (0, 0), random_philo)
        img.save('Hashtag/hashtag.png')
        update(post='Hashtag/hashtag.png', status=lastid, username=q_username.pop(0))
        log.info("Enviado corretamente!")
        log.info("=================================================================================")

        log.info('Finalizado, enviando: ' + lastid)
        log.info('Itens restantes: ' + str(len(q)))
        log.info('--------------------------------------------------------')

    log.info('Lista tratada com sucesso.')
    log.info('Voltando a ouvir tweets...')
    log.info('-----------------------------------------')
    log.info('_\|/_ TURNING OFF PHILO_BOT_ENGINE _\|/_ ')
    log.info('-----------------------------------------')


def text_treatment(PEG_STATUS, IMG, SUB_LIST):
    global escrever
    global pegando_status2

    try:
        retirando_user = re.sub('@[^\s]+', '', PEG_STATUS)
        log.info('STATUS TRATADO: ' + retirando_user)
        tratando_status = re.sub(r'https://.*[\r\n]*', '', retirando_user)
        escrever = ImageDraw.Draw(IMG)
        sub_list = dict((re.escape(k), v) for k, v in SUB_LIST.items())
        pattern = re.compile("|".join(sub_list.keys()))
        pegando_status2 = pattern.sub(lambda m: sub_list[re.escape(m.group(0))], tratando_status).strip()
    except tweepy.error.TweepError as e:
        print(e)
        log.info('TRATAMENTO DE TEXTO CANCELADO - TWEET DELETADO')
        q_username.clear()
        log.info('Voltando a ouvir tweets...')
        return MyStreamListener


def philomaker(PEG_STATUS, IMG, FONT_SIZE, LAST_ID):
    global fonte

    try:
        if not pegando_status2:
            check_emptystring(LAST_ID)
            return MyStreamListener
    except tweepy.error.TweepError as e:
        print(e)
        log.info('ERRO AO MANDAR MENSAGEM DE ERRO')
        q_username.clear()
        log.info('Voltando a ouvir tweets...')
        return MyStreamListener

        # ------------------------------------------------------------------------------------------
        # -------------------------- AJUSTE DE FONTE E TEXTO   ------------------------------------
        # ------------------------------------------------------------------------------------------

    while (fonte.getsize(txt)[0] < blank.size[0]) and (fonte.getsize(txt)[1] < blank.size[1]):
        FONT_SIZE += 1
        fonte = ImageFont.truetype("Font/myriad.otf", FONT_SIZE)

    FONT_SIZE -= 1
    fonte = ImageFont.truetype("Font/myriad.otf", FONT_SIZE)
    escrever.textsize(txt, font=fonte)
    # ----------------------------------------------------------------------------
    # ----------------------- ESCREVE O TEXTO NA IMAGEM  --------------------------
    # -----------------------------------------------------------------------------
    escrever.text(xy=(43, 110), text=textwrap.fill(str(pegando_status2), 28),
                  fill=(255, 255, 255), font=fonte)
    # ------------------------------------------------------------------------
    # ------------------ TRATAMENTO DE IMAGEM E POSTAGEM ---------------------
    # ------------------------------------------------------------------------
    # =====================================
    # ======= NOME DO FILOSOFO ============
    template = Image.open('Templates/template.png')

    fonte_2 = ImageFont.truetype("font/myriad.otf", 25)
    escrever_2 = ImageDraw.Draw(template)
    escrever_2.text(xy=(50, 516), text=f'- TESTE AAAAA', fill=(255, 255, 255), font=fonte_2)

    # =====================================
    # ======= FOTO DO FILOSOFO ============
    timeline = api.user_timeline(count=10, screen_name="sudomadeira")
    for tweet in timeline:
        for media in tweet.entities.get("media", [{}]):
            print(media)
            # checks if there is any media-entity
            if media.get("type", None) == "photo":
                # checks if the entity is of the type "photo"
                image_content = requests.get(media["media_url"])
                filo = Image.open(str(image_content))
                filo2 = filo.resize((449, 584))
                IMG.paste(filo2, (629, 0))  # try: img.filename or img
                IMG.save('Hashtag/philomaker.png')
                update(post='Hashtag/philomaker.png', status=LAST_ID, username=q_username.pop(0))
                log.info("Enviado corretamente!")
                log.info("=================================================================================")

                log.info('Finalizado PHILOMAKER, enviando: ' + LAST_ID)
                log.info('Itens restantes: ' + str(len(q)))
                log.info('--------------------------------------------------------')
