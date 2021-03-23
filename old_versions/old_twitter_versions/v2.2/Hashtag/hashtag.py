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
import tweepy, time, random, re, textwrap
from PIL import Image, ImageDraw, ImageFont

from Credentials.credentials_verify import api
from Lists.sub_list import sub_lista
from Lists.img_list import filosofo
from Logs.logger_hashtag import *


log.info("Hashtag.py v2.0")

q = []
q_username = []


def starting_hashtag():
    MyStreamListener()
    the_api = api
    myStream = tweepy.Stream(auth=the_api.auth, listener=MyStreamListener())
    myStream.filter(track=['#PhiloBot'], is_async=True)


class MyStreamListener(tweepy.StreamListener):
    log.info("Esperando....")

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

        if len(q) >= 3:
            log.info('----------------------------------------')
            log.info('_\|/_ STARTING PHILOENGINE 3.0 _\|/_ ')
            log.info('----------------------------------------')
            philoengine()


def update(post, status, username):
    numero = 1
    try:
        tweepy.Cursor(api.user_timeline).items(numero)
        api.update_with_media(post, status="@" + username + " ", auto_populate_reply_metadata=True, in_reply_to_status_id=status)
        time.sleep(5)
    except tweepy.TweepError as e:
        log.info(e.reason)
        log.info("ERRO! Não foi possivel realizar a ação para o usuário.")
        log.info("\n==========================")


def check_emptystring(lastid):

        log.info('STRING VAZIA DETECTADA!')

        error_collection = ['templates/templateERRO6.png', 'templates/templateERRO1.png', 'templates/templateERRO2.png',
                            'templates/templateERRO3.png', 'templates/templateERRO4.png', 'templates/templateERRO5.png',
                            'templates/templateGIFERRO.gif']

        escolher_img = random.randrange(0, len(error_collection))
        img_selecionada = error_collection[escolher_img]

        user = q_username.pop(0)
        log.info('ENVIANDO TEMPLATE DE AJUDA PARA O @{}.'.format(user))

        update(post=img_selecionada, status=lastid, username=user)
        log.info('Voltando a ouvir tweets...')

def philoengine():
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
        try:
            pegando_status = api.get_status(lastid, tweet_mode='extended')._json['full_text']
            log.info('STATUS CONVERTIDO: ' + pegando_status)
        except tweepy.error.TweepError:
            log.info('TRATAMENTO CANCELADO - TWEET DELETADO')
            q_username.clear()
            log.info('Voltando a ouvir tweets...')
            return MyStreamListener

        # ------------------------------------------------------------------------------------------
        # -------------------------- TRATAMENTO DO TEXTO -------------------------------------------
        # ------------------------------------------------------------------------------------------

        retirando_user = re.sub('@[^\s]+', '', pegando_status)
        log.info('STATUS TRATADO: ' + retirando_user)
        tratando_status = re.sub(r'https://.*[\r\n]*', '', retirando_user)
        escrever = ImageDraw.Draw(img)
        sub_list = dict((re.escape(k), v) for k, v in sub_lista.items())
        pattern = re.compile("|".join(sub_list.keys()))
        pegando_status2 = pattern.sub(lambda m: sub_list[re.escape(m.group(0))], tratando_status).strip()
        # ------------------------------------------------------------------------------------------
        # -------------------------- VERIFICA STRING VAZIA  ----------------------------------------
        # ------------------------------------------------------------------------------------------

        if not pegando_status2:
            check_emptystring(lastid)
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

        random_philo = random.choice(filosofo)
        img.paste(random_philo, (0, 0), random_philo)
        img.save('hashtag.png')
        update(post='hashtag.png', status=lastid, username=q_username.pop(0))
        log.info("Enviado corretamente!")
        log.info("=================================================================================")

        log.info('Finalizado, enviando: ' + lastid)
        log.info('Itens restantes: ' + str(len(q)))
        log.info('--------------------------------------------------------')

    log.info('Lista tratada com sucesso.')
    log.info('Voltando a ouvir tweets...')
    log.info('----------------------------------------')
    log.info('_\|/_ TURNING OFF PHILOENGINE 3.0 _\|/_ ')
    log.info('----------------------------------------')
