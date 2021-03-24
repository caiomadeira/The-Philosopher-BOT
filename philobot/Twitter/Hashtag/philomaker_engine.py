import random
import re
import textwrap
import time
import tweepy
import urllib
from urllib import request
from PIL import Image, ImageDraw, ImageFont
from Lists.error_img_list import PHILOMAKER_ERROR_IMAGE_COLLECTION
from Templates.New_Img_Manipulation.reference import TEMPLATES_PATH
from Logs.Twitter.logger_hashtag import log_philomaker
import os
from Twitter.Hashtag.functionalities import Functionalities


class PhiloMaker(Functionalities):

    def philomaker_engine(self, get_hashtag_list):

        self.log = log_philomaker(__name__)

        hashtag_list = get_hashtag_list
        from Twitter.Hashtag.hashtag import HashtagClass
        self.log.info('----------------------------------------')
        self.log.info('       > STARTING PHILOMAKER < ')
        self.log.info('----------------------------------------')
        while len(self.q) > 0:

            self.last_id = self.q.pop(0)
            self.log.info('ID Coletado: ' + self.last_id)
            txt = "Font/myriad.otf"
            fontsize = 1
            blank = Image.new('RGB', (269, 194))
            font = ImageFont.truetype("Font/myriad.otf", fontsize)
            font2 = ImageFont.truetype("Font/times.ttf")
            self.img = Image.open(f'{TEMPLATES_PATH}/layer_1.png')

            " GET TWEET TEXT ========================================================================= "
            try:
                self.get_status = self.api.get_status(self.last_id, tweet_mode='extended', include_entities=True)._json[
                    'full_text']
                self.log.info('[ETAPA 1] Status coletado: ' + self.get_status)
            except tweepy.error.TweepError as e:
                self.log.error(e)
                self.log.error('ERRO: FALHA NA COLETA DO ID - TWEET DELETADO')
                self.q_username.clear()
                self.log.info('----------------------------------------\n')
                self.log.info('>AGUARDANDO NOVOS TWEETS...<')

                time.sleep(2)
                return HashtagClass

            " TEXT HANDLER =============================================================================== "
            self.text_treatment(PEG_STATUS=self.get_status, IMG=self.img, SUB_LIST=hashtag_list, LOG=self.log)
            time.sleep(2)

            " CHECK RT =================================================================================== "
            try:
                check_rt_func = self.check_rt(LOG=self.log)
                if check_rt_func:
                    self.log.info('----------------------------------------\n')
                    self.log.info('>AGUARDANDO NOVOS TWEETS...<')
                    return HashtagClass

                else:
                    pass

            except Exception as e_check_rt:
                self.log.info('ERRO: FALHA AO VERIFICAR SE É RETWEET')
                self.log.info(e_check_rt)
                return HashtagClass

            " CHECK EMPTY STRING ========================================================================= "
            check_empty_string = self.check_emptystring(last_id=self.last_id, LOG=self.log, PHILOMAKER=True)

            if check_empty_string:
                self.log.info('----------------------------------------\n')
                self.log.info('>AGUARDANDO NOVOS TWEETS...<')
                return HashtagClass

            time.sleep(2)

            " IMAGE ADJUST ================================================================================"
            self.log.info("[ETAPA 5] Ajustando tamanho do texto para imagem...")
            while (font.getsize(txt)[0] < blank.size[0]) and (font.getsize(txt)[1] < blank.size[1]):
                fontsize += 1
                font = ImageFont.truetype("Font/myriad.otf", fontsize)

            fontsize -= 1

            font = ImageFont.truetype("Font/myriad.otf", fontsize)

            " GET USER MENTIONS =============================================================================== "
            check_user_mention = self.user_mentions()
            if check_user_mention:
                self.log.info('----------------------------------------\n')
                self.log.info('>AGUARDANDO NOVOS TWEETS...<')
                return HashtagClass

            " GET MEDIA ========================================================================= "
            self.get_media()

            try:
                philosopher = Image.open('Hashtag/twitter_philo_img.png')
                img_2 = philosopher.resize((449, 584))
                self.img.paste(img_2, (629, 0))
                smooth_template = Image.open(f'{TEMPLATES_PATH}/layer_3.png')
                self.img.paste(smooth_template, (0, 0), smooth_template)

                " CHECK QUOTES ========================================================================= "
                self.log.info('[ETAPA 5] Verificando aspas...')
                if self.get_treated_status.startswith('"') and self.get_treated_status.endswith('"'):

                    post_with_quotes_philomaker = self.img_with_quotes(LOG=self.log, PHILO_NAME=self.user_mentioned_profile_name)
                    self.update(post=post_with_quotes_philomaker, status=self.last_id,
                                username=self.q_username.pop(0))

                    self.log.info('Finalizado, ID tratado: ' + self.last_id)
                    self.log.info('Itens restantes: ' + str(len(self.q)))

                else:
                    post_without_quotes_philomaker = self.img_without_quotes(LOG=self.log, PHILO_NAME=self.user_mentioned_profile_name)
                    self.update(post=post_without_quotes_philomaker, status=self.last_id, username=self.q_username.pop(0))
                    self.log.info('Finalizado, ID tratado: ' + self.last_id)
                    self.log.info('Itens restantes: ' + str(len(self.q)))
                    self.log.info('TWEET TRATADO COM SUCESSO')

            except FileNotFoundError as f:
                self.log.error('ERRO: IMAGEM NÃO ENCONTRADA')
                self.log.error(f)
                self.send_error_philomaker(LAST_ID=self.last_id)
                self.log.info('----------------------------------------\n')
                self.log.info('>AGUARDANDO NOVOS TWEETS...<')
                return HashtagClass

            try:
                os.remove('Hashtag/twitter_philo_img.png')
                self.log.info("Imagem removida")
            except OSError as o:
                self.log.error('ERRO: FALHA AO DELETAR IMAGEM')
                self.log.error(o)

            self.log.info('Finalizado, ID tratado: ' + self.last_id)
            self.log.info('Itens restantes: ' + str(len(self.q)))
            self.log.info('TWEET TRATADO COM SUCESSO')
            self.log.info('----------------------------------------\n')
            self.log.info('>AGUARDANDO NOVOS TWEETS...<')

    def user_mentions(self):
        try:
            search_mentions_extended = str(self.get_metadata)

            if 'extended_tweet' in search_mentions_extended:
                get_extended_entities = self.get_metadata.extended_tweet['entities'] # tupla
                get_extended_user_mentions = get_extended_entities['user_mentions']
                store_extended_name = []

                for extended_name in get_extended_user_mentions:
                    store_extended_name.append(extended_name['name'])

                self.user_mentioned_profile_name = f"- {store_extended_name[0]}"

            else:
                get_name_of_mention = self.get_metadata.entities['user_mentions']  # tupla
                store_name = []
                for name in get_name_of_mention:
                    store_name.append(name['name'])

                self.user_mentioned_profile_name = f"- {store_name[0]}"

            try:
                self.log.info(f'[ETAPA 6] Nome do filósofo coletado: {self.user_mentioned_profile_name}')
            except UnicodeEncodeError as u:
                self.log.error("ERRO: UNICODE, IGNORANDO...")
                self.log.error(u)
                pass

        except UnicodeEncodeError:
            self.log.error("ERRO: UNICODE, IGNORANDO...")
            pass

        except IndexError:
            self.log.error("ERRO: NENHUM USUARIO MENCIONADO!")
            self.send_error_philomaker(LAST_ID=self.last_id)
            return True

    def get_media(self):
        from Twitter.Hashtag.hashtag import HashtagClass
        try:

            search_img_extended = str(self.get_metadata)
            if 'extended_tweet' in search_img_extended:
                get_extended_img = self.get_metadata.extended_tweet['entities']  # tupla
                get_extended_img_media = get_extended_img['media']

                for extended_media_range in range(1):
                    for extended_media in get_extended_img_media:
                        self.log.info(f"[ETAPA 7] Coletando URL da imagem: {extended_media['media_url']}")
                        urllib.request.urlretrieve(extended_media['media_url'], "Hashtag/twitter_philo_img.png")

            elif 'media' in self.get_metadata.entities:
                for media in range(1):
                    for media in self.get_metadata.extended_entities['media']:
                        self.log.info(f"[ETAPA 7] Coletando URL da imagem: {media['media_url']}")
                        urllib.request.urlretrieve(media['media_url'], "Hashtag/twitter_philo_img.png")

            else:
                pass

        except FileNotFoundError:
            self.log.error('ERRO: IMAGEM NÃO ENCONTRADA')
            self.send_error_philomaker(LAST_ID=self.last_id)
            self.log.info('----------------------------------------\n')
            self.log.info('>AGUARDANDO NOVOS TWEETS...<')
            return HashtagClass
        except Exception as e:
            self.log.error(e)
            self.log.info('----------------------------------------\n')
            time.sleep(20)
            self.log.info("Esperando 20 segundos...")
            self.log.info('>AGUARDANDO NOVOS TWEETS...<')

            return HashtagClass

    def send_error_philomaker(self, LAST_ID):
        try:

            choice_error_img = random.choice(PHILOMAKER_ERROR_IMAGE_COLLECTION)

            user = self.q_username.pop(0)
            self.log.info('Enviando imagem de ajuda para o @{}.'.format(user))

            self.update(post=choice_error_img, status=LAST_ID, username=user)

        except Exception as e:
            self.log.error('ERRO: NÃO POSSIVEL ENVIAR IMAGEM PARA O USUARIO')
            self.log.error(e)