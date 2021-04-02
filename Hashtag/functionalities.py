import random
import re
import tweepy
import time
import textwrap
import os
from config import Config
from PIL import Image, ImageDraw, ImageFont
from Lists.error_img_list import PHILOBOT_ERROR_IMAGE_COLLECTION
from Lists.error_img_list import PHILOMAKER_ERROR_IMAGE_COLLECTION


class Functionalities(Config):

    def check_emptystring(self, last_id, LOG, PHILOMAKER):
        LOG.info("[ETAPA 4] Checando string vazia...")
        try:
            if not self.get_treated_status:
                if PHILOMAKER:
                    self.send_error_empty_string(LAST_ID=last_id, LOG=LOG, PHILOMAKER=PHILOMAKER)
                    return True
                else:
                    self.send_error_empty_string(LAST_ID=last_id, LOG=LOG, PHILOMAKER=PHILOMAKER)
                    return True
        except Exception:
            from Hashtag.hashtag import HashtagClass
            LOG.error('ERRO: FALHA AO CHECAR SE A STRING É VAZIA')
            self.q_username.clear()

            LOG.info('----------------------------------------\n')
            LOG.info('>AGUARDANDO NOVOS TWEETS...<')
            return HashtagClass

    def send_error_empty_string(self, LAST_ID, LOG, PHILOMAKER):
        try:
            LOG.info('STRING VAZIA DETECTADA!')
            if PHILOMAKER:
                choice_error_img = random.choice(PHILOMAKER_ERROR_IMAGE_COLLECTION)
            else:
                choice_error_img = random.choice(PHILOBOT_ERROR_IMAGE_COLLECTION)

            user = self.q_username.pop(0)
            LOG.info('ENVIANDO TEMPLATE DE AJUDA PARA O @{}.'.format(user))

            self.update(post=choice_error_img, status=LAST_ID, post_username=user)

        except Exception as e:
            LOG.exception('ERRO AO ENVIAR IMAGEM DE ERRO PARA O USUARIO!')
            LOG.exception(e)

    def text_treatment(self, PEG_STATUS, IMG, SUB_LIST, LOG):

        try:
            self.remove_user = re.sub('@[^\s]+', '', PEG_STATUS)
            LOG.info('[ETAPA 2] Status - marcações retiradas: ' + self.remove_user)
            self.treating_status = re.sub(r'https://.*[\r\n]*', '', self.remove_user)
            self.drawing = ImageDraw.Draw(IMG)

            sub_list_config = dict((re.escape(k), v) for k, v in SUB_LIST.items())
            pattern = re.compile("|".join(sub_list_config.keys()))
            self.get_treated_status = pattern.sub(lambda m: sub_list_config[re.escape(m.group(0))],
                                                  self.treating_status).strip()
        except tweepy.error.TweepError as e:
            LOG.error(e)
            LOG.error('TRATAMENTO DE TEXTO CANCELADO - TWEET DELETADO')
            self.q_username.clear()

    def img_with_quotes(self,PHILO_NAME, LOG):

        LOG.info("[ETAPA 5.1] ASPAS IDENTIFICADAS")
        LOG.info("[ETAPA 5.2] Iniciando manipulação de aspas especiais...")
        time.sleep(0.5)
        remove_quotes_in_text = self.get_treated_status.replace('"', '')
        LOG.info(f"[ETAPA 5.3] Removendo aspas do texto: {remove_quotes_in_text}")

        open_quote = Image.open('Templates/open_quote.png')
        close_quote = Image.open('Templates/close_quote.png')
        open_quote_resized = open_quote.resize((60, 60))
        close_quote_resized = close_quote.resize((60, 60))
        time.sleep(0.5)

        if len(remove_quotes_in_text) > 240:
            LOG.info("[ETAPA 5.4] Tweet MAIOR que 240 caracteres, ajustando texto...")
            fontsize = 30
            font = ImageFont.truetype("Font/myriad.otf", fontsize)
            self.positions['tweet_with_quotes_PosX'] = 70
            self.positions['tweet_with_quotes_PosY'] = 115
            self.positions['textwraped_value'] = 25

        elif len(remove_quotes_in_text) <= 25:
            LOG.info("[ETAPA 5.4] Tweet MENOR que 25 caracteres, ajustando texto...")
            fontsize = 50
            font = ImageFont.truetype("Font/myriad.otf", fontsize)
            self.positions['tweet_with_quotes_PosX'] = 80
            self.positions['tweet_with_quotes_PosY'] = 128
            self.positions['textwraped_value'] = 20

        else:
            pass

        # texto do filosofo
        try:
            fontsize = 50
            font = ImageFont.truetype("Font/myriad.otf", fontsize)
            self.drawing.text(xy=(self.positions['tweet_with_quotes_PosX'], self.positions['tweet_with_quotes_PosY']),
                              text=textwrap.fill(str(remove_quotes_in_text), self.positions['textwraped_value']),
                              fill=(255, 255, 255),
                              font=font)

            LOG.info("[ETAPA 5.5] Colocando as imagens das aspas.")
            self.img.paste(open_quote_resized, (50, 30), open_quote_resized)
            self.img.paste(close_quote_resized, (500, 400), close_quote_resized)

            # nome do filosofo
            fontsize = 30
            font = ImageFont.truetype("Font/times.ttf", fontsize)
            self.drawing.text(xy=(self.positions['tweet_with_quotes_PosX'], self.positions['author_quote_posY']),
                              text=textwrap.fill(str(PHILO_NAME)),
                              fill=(255, 255, 255),
                              font=font)
        except Exception:
            from Hashtag.hashtag import HashtagClass
            LOG.info('PASSANDO PELO ERRO QUE A GENTE NAO QUERIA VER')
            return HashtagClass

        self.img.save('Hashtag/hashtag.png')
        img_update_quotes = 'Hashtag/hashtag.png'

        return img_update_quotes

    def img_without_quotes(self,PHILO_NAME, LOG):

        if len(self.get_treated_status) > 240:
            LOG.info("[ETAPA 6] Tweet MAIOR que 240 caracteres, ajustando texto...\n")
            fontsize = 35
            font = ImageFont.truetype("Font/myriad.otf", fontsize)
            self.positions['tweet_default_PosX'] = 38
            self.positions['tweet_default_PosY'] = 105
            self.positions['textwraped_value'] = 25

        elif len(self.get_treated_status) <= 25:
            LOG.info("[ETAPA 6] Tweet MENOR que 25 caracteres, ajustando texto...")
            fontsize = 50
            font = ImageFont.truetype("Font/myriad.otf", fontsize)
            self.positions['tweet_default_PosX'] = 80
            self.positions['tweet_default_PosY'] = 150
            self.positions['textwraped_value'] = 20
        else:
            pass

        try:
            fontsize = 50
            font = ImageFont.truetype("Font/myriad.otf", fontsize)
            self.drawing.text(xy=(self.positions['tweet_default_PosX'], self.positions['tweet_default_PosY']),
                              text=textwrap.fill(str(self.get_treated_status), self.positions['textwraped_value']),
                              fill=(255, 255, 255),
                              font=font)
            fontsize = 30
            font = ImageFont.truetype("Font/times.ttf", fontsize)
            self.drawing.text(xy=(self.positions['author_quote_posX'], self.positions['author_quote_posY']),
                              text=textwrap.fill(str(PHILO_NAME)),
                              fill=(255, 255, 255),
                              font=font)
        except Exception:
            from Hashtag.hashtag import HashtagClass
            LOG.info('PASSANDO PELO ERRO QUE A GENTE NAO QUERIA VER')
            return HashtagClass
            
        self.img.save('Hashtag/hashtag.png')
        img_update_no_quotes = 'Hashtag/hashtag.png'

        return img_update_no_quotes

    def check_rt(self, LOG):
        LOG.info("[ETAPA 3] Checando se é RT...")
        verify_rt_info = self.q_tweet_info.pop(0)
        if 'retweeted_status' in verify_rt_info:
            print('\n')
            LOG.info('RETWEET ENCONTRADO, IGNORANDO... - USER: {}'.format(self.q_username.pop(0)))
            return True
        else:
            pass

    def text_adjust(self, LOG, choice_philosopher):
        remove_path_of_filename = os.path.basename(choice_philosopher)
        LOG.info(f"Imagem do filósofo escolhida: {remove_path_of_filename}")

        remove_extension_of_filename = remove_path_of_filename.replace('.png', '')
        if '(2)' in remove_extension_of_filename:
            LOG.info("[ETAPA 4.2] Removendo lixo no nome da imagem do filosofo...")
            remove_number_in_name = remove_extension_of_filename.replace('(2)', '')
            self.finish_name_of_philosopher = f'- {remove_number_in_name}'
            LOG.info(f'[ETAPA 4.3] Nome do filósofo tratado: {self.finish_name_of_philosopher}')
        else:
            self.finish_name_of_philosopher = f'- {remove_extension_of_filename}'
            LOG.info("[ETAPA 4.2] Nenhum lixo no nome da imagem encontrado. Prosseguindo normalmente...")
            LOG.info(f'[ETAPA 4.3] Nome do filósofo tratado: {self.finish_name_of_philosopher}')


