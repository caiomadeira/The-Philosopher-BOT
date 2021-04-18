"""
classe responsavel por fontes, tamanhos posições e toda manipulação de imagem

Guia: http://legacy.python.org/dev/peps/pep-0008/

constantes são escritas com MAISCULAS e usando UNDERSCORE
variaveis são escritas com MINUSCULAS e usando UNDERSCORE
nomes de funções são MINUSCULAS e usando UNDERSCORE
"""

import random
import re
import textwrap

import tweepy
from PIL import Image, ImageDraw, ImageFont
from Lists.img_list import PHILOSOPHERS_LIST
from Hashtag.patterns.font_ import Font
from Logs.Twitter.logger_hashtag import log_philobot
import Hashtag.philobot_engine
import dotenv, os
from Hashtag.patterns.value import tweet_posX, tweet_posY, textwraped_value, author_posX, author_posY
from Hashtag.patterns.suport_ import Suport
from Lists.sub_list import sub_list_philobot
from Templates.New_Img_Manipulation.reference import TEMPLATES_PATH, TEMPLATES_PATH_LAYER_3

# O ideal é que o env não seja carregado aqui, pois pode haver mais de um
dotenv.load_dotenv(dotenv.find_dotenv())


# BASE_TEMPLATE_LAYER = Image.open(os.getenv('template_layer_1'))
# myriad = os.getenv('myriad_font')
# times = os.getenv('times_font')
# TXT = random.choices(myriad, times)
# second_font = random.choices(myriad, times)
# BLANK = Image.new('RGB', (269, 194))


class Template(Font, Suport):
    # método 1 - default template
    # pra quem ele manda não interessa, apenas o texto do tweet é interessante, porém
    # ele deve passar por outra classe para poder ser instaciado nesta.

    # BASE_TEMPLATE_LAYER = Image.open(os.getenv('template_layer_1'))

    def default_template(self, status_text, LOG, clear_users_param):
        BASE_TEMPLATE_LAYER = Image.open(TEMPLATES_PATH)
        TEMPLATE_LAYER_3 = Image.open(TEMPLATES_PATH_LAYER_3)
        # BASE_TEMPLATE_LAYER = Image.open(os.getenv('template_layer_1'))
        LOG.info("DEFAULT_TEMPLATE -> Iniciando")
        LOG.info("DEFAULT_TEMPLATE -> Pass myriad")
        LOG.info("DEFAULT_TEMPLATE -> Pass times")
        TXT = '../Font/myriad.otf'
        LOG.info("DEFAULT_TEMPLATE -> Pass TXT")
        BLANK = Image.new('RGB', (269, 194))
        LOG.info("DEFAULT_TEMPLATE -> Pass SECOND FONT AND BLANK")
        font_size = 1
        LOG.info("DEFAULT_TEMPLATE -> Pass font size")
        font = ImageFont.truetype('../Font/myriad.otf', font_size)
        LOG.info("DEFAULT_TEMPLATE -> Pass QUOTE FONTE")
        LOG.info("DEFAULT_TEMPLATE -> Primeira forma do status pega")
        LOG.info("DEFAULT_TEMPLATE -> ENTRANDO NA BASIC TREATATMENT")

        try:
            LOG.info("BASIC TEXT TREATMENT -> Entrou na função basic_text_treatment")
            remove_user = re.sub('@[^\s]+', '', status_text)
            LOG.info("BASIC TEXT TREATMENT -> Passou de self.remove_user")
            LOG.info('BASIC TEXT TREATMENT -> marcações retiradas: ')
            LOG.info("BASIC TEXT TREATMENT -> " + remove_user)
            LOG.info("BASIC TEXT TREATMENT -> Passou do LOG")
            treating_status = re.sub(r'https://.*[\r\n]*', '', remove_user)
            self.drawing = ImageDraw.Draw(BASE_TEMPLATE_LAYER)

            sub_list_config = dict((re.escape(k), v) for k, v in sub_list_philobot.items())
            pattern = re.compile("|".join(sub_list_config.keys()))
            self.get_treated_status = pattern.sub(lambda m: sub_list_config[re.escape(m.group(0))],
                                                  treating_status).strip()

        except tweepy.error.TweepError as e:
            LOG.error(e)
            LOG.info("BASIC TEXT TREATMENT -> TRATAMENTO DE TEXTO CANCELADO - TWEET DELETADO")
            clear_users_param.clear()
        # self.basic_text_treatment(get_status_param=status_text, image_param=BASE_TEMPLATE_LAYER, sub_list_param=sub_list_philobot, LOG=LOG, clear_users_param=self.q_username)

        LOG.info("DEFAULT_TEMPLATE ->ENTRANDO NA FONT SUIZE AJDUST")
        # self.adjust_tweet_font_size(font_philo_txt=TXT,
        #                             blank_layer=BLANK,
        #                             font_size_param=font_size,
        #                             LOG=LOG)

        choose_philosopher = random.choice(PHILOSOPHERS_LIST)
        LOG.info("CHOOSE PHILOSPHER ->Pass randmom choose philo")
        LOG.info("Entrando no ajust_philosopher_name")

        self.ajust_philosopher_name(LOG=LOG, choose_philosopher_param=choose_philosopher)

        LOG.info("img_paste -> Indo entrar")

        LOG.info("1 img_paste -> Entrou")
        philosopher_str_to_obj = Image.open(choose_philosopher)
        LOG.info("2 img_paste -> Passou de philosopher_str_to_obj = Image.open(choose_philo_param)")
        TEMPLATE_LAYER_2_PHILOSOPHER = philosopher_str_to_obj.resize((449, 584))
        LOG.info("3 img_paste -> Passou de TEMPLATE_LAYER_2_PHILOSOPHER = philosopher_str_to_obj.resize((449, 584))")
        BASE_TEMPLATE_LAYER.paste(TEMPLATE_LAYER_2_PHILOSOPHER, (629, 0))
        LOG.info("4 img_paste -> Passou de BASE_TEMPLATE_LAYER.paste(TEMPLATE_LAYER_2_PHILOSOPHER, (629, 0))")
        LOG.info("5 img_paste -> Passou de TEMPLATE_LAYER_3 = Image.open(os.getenv('template_layer_3'))")
        BASE_TEMPLATE_LAYER.paste(TEMPLATE_LAYER_3, (0, 0), TEMPLATE_LAYER_3)
        LOG.info("6 img_paste -> Passou de BASE_TEMPLATE_LAYER.paste(TEMPLATE_LAYER_3, (0, 0), TEMPLATE_LAYER_3)")
        LOG.info("7 img_paste -> Saiu")
        LOG.info("img_paste -> SAIU ESTANDO NO TEMPLATE")
        # DEFAULT VALUE
        # tweet_default_PosX = 38
        # tweet_default_PosY = 105
        # textwraped_value = 25

        if self.get_treated_status.startswith('"') and self.get_treated_status.endswith('"'):
            LOG.info("ASPAS DETECTADAS - ENTRANDO NA WITH QUOTES")
            self.with_quotes(status_text=self.get_treated_status,
                             tweet_posX=tweet_posX(38),
                             tweet_posY=tweet_posY(105),
                             textwraped_value=textwraped_value(25),
                             font_philo_text=ImageFont.truetype('../Font/myriad.otf', font_size),
                             LOG=LOG, drawing_p=self.drawing)

        else:
            self.no_quotes(status_text=self.get_treated_status,
                           tweet_posX=tweet_posX(38),
                           tweet_posY=tweet_posY(105),
                           textwraped_value=textwraped_value(25),
                           font_philo_text=ImageFont.truetype('../Font/myriad.otf', font_size),
                           LOG=LOG, drawing_p=self.drawing)

        LOG.info("Colocando nome do philosopher")
        # self.put_name_of_philosopher(self, philosopher_name=self.ajust_philosopher_name(LOG=LOG,
        #                              choose_philosopher_param=choose_philosopher),
        #                              font_philosopher_name=font,
        #                              author_posX=author_posX(43),
        #                              author_posY=author_posY(512),
        #                              drawing_p=self.drawing)

        size_philosopher_name = 30

        self.drawing.text(xy=(author_posX, author_posY),
                       text=textwrap.fill(str(self.finish_name_philosopher)),
                       fill=(255, 255, 255),
                       font=ImageFont.truetype('../Font/myriad.otf', size_philosopher_name))

        BASE_TEMPLATE_LAYER.save("Hashtag.png")
        BASE_TEMPLATE_LAYER.show()
        self.img_saved = "Hashtag.png"
        LOG.info("img_saved - Salvo com sucesso")

        from Hashtag.hashtag import HashtagClass
        LOG.info("Retornando img_saved")

        return self.img_saved
