"""
classe responsavel por fontes, tamanhos posições e toda manipulação de imagem

Guia: http://legacy.python.org/dev/peps/pep-0008/

constantes são escritas com MAISCULAS e usando UNDERSCORE
variaveis são escritas com MINUSCULAS e usando UNDERSCORE
nomes de funções são MINUSCULAS e usando UNDERSCORE
"""

import random
import re
from PIL import Image, ImageDraw, ImageFont
from Lists.img_list import PHILOSOPHERS_LIST
from Hashtag.patterns.font_ import Font
import dotenv, os
from Hashtag.patterns.value import tweet_posX, tweet_posY, textwraped_value, author_posX, author_posY
from Hashtag.patterns.suport_ import Suport
from Templates.New_Img_Manipulation.reference import TEMPLATES_PATH

# O ideal é que o env não seja carregado aqui, pois pode haver mais de um
dotenv.load_dotenv(dotenv.find_dotenv())

# BASE_TEMPLATE_LAYER = Image.open(os.getenv('template_layer_1'))
# myriad = os.getenv('myriad_font')
# times = os.getenv('times_font')
# TXT = random.choices(myriad, times)
# second_font = random.choices(myriad, times)
# BLANK = Image.new('RGB', (269, 194))

BASE_TEMPLATE_LAYER = Image.open(TEMPLATES_PATH)


class Template(Font, Suport):
    # método 1 - default template
    # pra quem ele manda não interessa, apenas o texto do tweet é interessante, porém
    # ele deve passar por outra classe para poder ser instaciado nesta.

    # BASE_TEMPLATE_LAYER = Image.open(os.getenv('template_layer_1'))

    def default_template(self, status_text, sub_list):
        # BASE_TEMPLATE_LAYER = Image.open(os.getenv('template_layer_1'))
        myriad = os.getenv('myriad_font')
        times = os.getenv('times_font')
        TXT = random.choices(myriad, times)
        second_font = random.choices(myriad, times)
        BLANK = Image.new('RGB', (269, 194))
        font_size = 1
        quote_font = ImageFont.truetype(TXT, font_size)

        get_status_text = status_text

        remove_user = re.sub('@[^\s]+', '', get_status_text)
        print('Status - marcações retiradas: ' + remove_user)
        treating_status_1 = re.sub(r'https://.*[\r\n]*', '', remove_user)
        self.drawing = ImageDraw.Draw(BASE_TEMPLATE_LAYER)

        sub_list_config = dict((re.escape(k), v) for k, v in sub_list.items())
        pattern = re.compile("|".join(sub_list_config.keys()))
        self.treating_status_2 = pattern.sub(lambda m: sub_list_config[re.escape(m.group(0))],
                                             treating_status_1).strip()

        self.adjust_tweet_font_size(font_philo_txt=TXT,
                                    blank_layer=BLANK,
                                    font_size_param=font_size,
                                    quote_font=quote_font)

        choose_philosopher = random.choice(PHILOSOPHERS_LIST)
        self.ajust_philosopher_name(choose_philosopher_param=choose_philosopher)

        philosopher_str_to_obj = Image.open(choose_philosopher)
        TEMPLATE_LAYER_2_PHILOSOPHER = philosopher_str_to_obj.resize((449, 584))
        BASE_TEMPLATE_LAYER.paste(TEMPLATE_LAYER_2_PHILOSOPHER, (629, 0))
        TEMPLATE_LAYER_3 = Image.open(os.getenv('template_layer_3'))
        BASE_TEMPLATE_LAYER.paste(TEMPLATE_LAYER_3, (0, 0), TEMPLATE_LAYER_3)

        # DEFAULT VALUE
        # tweet_default_PosX = 38
        # tweet_default_PosY = 105
        # textwraped_value = 25

        if self.treating_status_2.startswith('"') and self.treating_status_2.endswith('"'):
            self.adjust_img_text(status_text=self.treating_status_2,
                                 tweet_posX=tweet_posX(38),
                                 tweet_posY=tweet_posY(105),
                                 textwraped_value=textwraped_value(25),
                                 philosopher_name=self.finish_name_philosopher,
                                 font_philo_text=TXT,
                                 font_philo_name=second_font,
                                 author_posX=author_posX(43),
                                 author_posY=author_posY(512),
                                 has_quotes=True)
        else:
            self.adjust_img_text(status_text=self.treating_status_2,
                                 tweet_posX=tweet_posX(38),
                                 tweet_posY=tweet_posY(105),
                                 textwraped_value=textwraped_value(25),
                                 philosopher_name=self.finish_name_philosopher,
                                 font_philo_text=TXT,
                                 font_philo_name=second_font,
                                 author_posX=author_posX(43),
                                 author_posY=author_posY(512),
                                 has_quotes=False)

        BASE_TEMPLATE_LAYER.save(os.getenv('hashtag_save_path'))
        ###########################
        #
        #   POST
        #
        ###########################

    def adjust_tweet_font_size(self, font_philo_txt, blank_layer, font_size_param, quote_font):

        while (quote_font.getsize(font_philo_txt)[0] < blank_layer.size[0]) and (
                quote_font.getsize(font_philo_txt)[1] < blank_layer.size[1]):
            font_size_param += 1  # AUMENTANDO o valor do tamanho da fonte de acordo com o texto
            quote_font = ImageFont.truetype(font_philo_txt, font_size_param)
        print('Configurando imagem...')
        font_size_param -= 1  # DIMINUINDO o valor do tamanho da fonte de acordo com o texto
        quote_font = ImageFont.truetype(font_philo_txt, font_size_param)
        self.drawing.textsize(font_philo_txt, font=quote_font)
