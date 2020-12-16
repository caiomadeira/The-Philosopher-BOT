from PIL import Image, ImageDraw, ImageFont
from Hashtag_Extension.hashtagExtension import MyStreamListener
from Lists.sub_list import sub_lista
from Lists.img_list import filosofo
from Logs.logger_hashtag import *
import re, textwrap, random
from Credentials.credentials_verify_reserva import api
from Hashtag.EmptyString import check_emptystring
from Hashtag_Extension.hashtagExtension import q, q_username, update_extension, starting_hashtag_extension

v = api


def philoengineextension():
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
        global pegando_status
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
        global retirando_user

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
        # -------------------------- VERIFICA UNICODE    ----------------------------------------
        # ------------------------------------------------------------------------------------------

        #  check_unicode(pegando_status2)

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
        update_extension(post='hashtag.png', status=lastid, username=q_username.pop(0))
        log.info("Enviado corretamente!")
        log.info("=================================================================================")

        log.info('Finalizado, enviando: ' + lastid)
        log.info('Itens restantes: ' + str(len(q)))
        log.info('--------------------------------------------------------')

    log.info('Lista tratada com sucesso.')
    log.info('Voltando a ouvir tweets...')
    log.info('----------------------------------------')
    log.info('_\|/_ TURNING OFF PHILOENGINE 2.1 _\|/_ ')
    log.info('----------------------------------------')

    return starting_hashtag_extension()
