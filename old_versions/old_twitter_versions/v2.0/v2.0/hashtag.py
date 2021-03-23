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
#from acess_tokens import *
from acess_tokens_reserva import *
from filosofo_list import filosofo, filosofo_special
from logger_hashtag import log
from sub_list import sub_lista
from sub_list import sub_lista

auth = tweepy.OAuthHandler(acess1, acess2)
auth.set_access_token(acess3, acess4)

api = tweepy.API(auth, wait_on_rate_limit=False, wait_on_rate_limit_notify=True)

log.info("Hashtag.py v2.0")


class MyStreamListener(tweepy.StreamListener):
    log.info("Esperando....")

    def on_status(self, status):

        log.info("========== NOVO TWEET ENCONTRADO ===========")
        log.info("Tweet:" + status.text)

        numero = 1
        search = '#PhiloBot'

        img = Image.open('templates/templateNovo2.png')
        txt = "font/myriad.otf"
        fontsize = 1
        W, H = img.size
        blank = Image.new('RGB', (269, 194))
        fonte = ImageFont.truetype("font/myriad.otf", fontsize)

        for tweet in tweepy.Cursor(api.search, search, since='2019-06-03').items(numero):

            try:
                tweepy.Cursor(api.user_timeline).items(numero)
                lastid = status.id
                log.info("ID pego:" + str(status.id))

                # ----------------------------------------------------------------------
                # ----------------------- GET STATUS TEXT  ----------------------------

                pegando_status = api.get_status(lastid, tweet_mode='extended')._json['full_text']
                log.info("STATUS CONVERTIDO:" + pegando_status)

                # ----------------------------------------------------------------------
                # ----------------------- TEXT TREATMENT  ----------------------------

                retirando_user = re.sub('@[^\s]+', '', pegando_status)
                log.info("STATUS TRATADO 1 :" + retirando_user)
                tratando_status = re.sub(r'https://.*[\r\n]*', '', retirando_user)
                log.info("STATUS TRATADO 2 :" + tratando_status)
                escrever = ImageDraw.Draw(img)

                # -------------------------------------------------------------------------------
                # ---------------------- TEXT TREATMENT -----------------------------------------
                sub_list = dict((re.escape(k), v) for k, v in sub_lista.items())
                pattern = re.compile("|".join(sub_list.keys()))
                pegando_status2 = pattern.sub(lambda m: sub_list[re.escape(m.group(0))], tratando_status)
                # ------------------------------------------------------------------------------
                if pegando_status2 == '':
                    log.info("String vazia!")
                    erro_img_list = ['templates/templateERRO1.png', 'templates/templateERRO2.png']
                    erro_img = random.choice(erro_img_list)
                    api.update_with_media(str(erro_img), status="@" + tweet.user.screen_name + " ",
                                          in_reply_to_status_id=status.id)

                    log.info("Enviado mensagem de erro!")
                    log.info("---------------------------")
                    log.info("Retornando para a busca novamente")
                    log.info("\n===================================")
                    return tweet

                # ----------------------- TEXT SIZE ADJUST FOR IMAGE ---------------------------------

                while (fonte.getsize(txt)[0] < blank.size[0]) and (fonte.getsize(txt)[1] < blank.size[1]):
                    fontsize += 1
                    fonte = ImageFont.truetype("font/myriad.otf", fontsize)

                fontsize -= 1
                fonte = ImageFont.truetype("font/myriad.otf", fontsize)
                w, h = escrever.textsize(txt, font=fonte)

                # ----------------------------------------------------------------------
                # ----------------------- WRITE TEXT IN IMAGE ---------------------
                escrever.text(xy=(43, 110), text=textwrap.fill(str(pegando_status2), 28),
                              fill=(255, 255, 255), font=fonte)

                # ------------------------------------------------------------------------
                # ----------------------- PHILOSOPHER PLACE AND POST ---------------------


                random_philo = random.choice(filosofo)
                img.paste(random_philo, (0, 0), random_philo)
                img.save('hashtag.png')
                api.update_with_media('hashtag.png', status="@" + tweet.user.screen_name + " ",
                                      in_reply_to_status_id=status.id)
                log.info("Enviado corretamente!")
                log.info("\n===========================")
                time.sleep(30)

            # ---------------------------------------------------------
            # ----------------------- ERRO EXECPT ---------------------
            except tweepy.TweepError as e:
                log.info(e.reason)
                log.info("ERRO! Não foi possivel realizar a ação para o usuário.")
                log.info("\n==========================")
            except StopIteration:
                break


if __name__ == "__main__":
    my_streamer = MyStreamListener()
    the_api = api
    myStream = tweepy.Stream(auth=the_api.auth, listener=MyStreamListener())
    myStream.filter(track=['#PhiloBot'])
