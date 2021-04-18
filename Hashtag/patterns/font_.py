import textwrap
from PIL import Image, ImageFont

import dotenv, os

# O ideal é que o env não seja carregado aqui, pois pode haver mais de um
import Hashtag.patterns.template_
from Templates.New_Img_Manipulation.reference import TEMPLATES_PATH

dotenv.load_dotenv(dotenv.find_dotenv())


class Font():

    # // Lembre-se de definir valores pra posições x y default/sem aspas e com aspas

    def with_quotes(self, LOG, status_text, tweet_posX, tweet_posY, textwraped_value, font_philo_text, drawing_p):
        LOG.info('[ETAPA 5] Verificando aspas...')
        # Caso ASPAS sejam VERDADEIRAS
        LOG.info("Entrou no if has quotes  =yttrue")
        # Maior ou IGUAL que 240 caracteres
        if len(status_text) > 240:
            LOG.info("Tweet MAIOR que 240 caracteres, ajustando texto...")
            font_size = 30
            ImageFont.truetype(font_philo_text, font_size)
            # INT = DEFAULT // INT = SPECIFIC
            # X -> 38 - 70 = - 32
            # Y -> 105 - 115 = -10
            # textwrap -> 25 - 25 = 0

            self.put_tweet_in_img(status_text=status_text,
                                  tweet_posX=abs(tweet_posX - 70),
                                  tweet_posY=abs(tweet_posY - 115),
                                  textwraped_value=textwraped_value - 25,
                                  font_philosopher_text=font_philo_text,
                                  has_quotes=True, drawing_p=drawing_p)
            LOG.info("Passou de put tweet in img")

            # from Hashtag.patterns.template_ import Template
            # return Template
        # MENOR ou IGUAL que 25 caracteres
        elif len(status_text) <= 25:

            print("Tweet MENOR que 25 caracteres, ajustando texto...")
            font_size = 50
            ImageFont.truetype(font_philo_text, font_size)
            # INT = DEFAULT // INT = SPECIFIC
            # X -> 38 - 80 = -42
            # Y -> 105 - 128 = -23
            # textwrap -> 25 - 20 = 5

            self.put_tweet_in_img(status_text=status_text,
                                  tweet_posX=abs(tweet_posX - 80),
                                  tweet_posY=abs(tweet_posY - 128),
                                  textwraped_value=(textwraped_value - 20),
                                  font_philosopher_text=font_philo_text,
                                  has_quotes=True, drawing_p=drawing_p)
            LOG.info("Passou de put tweet in img")

        # from Hashtag.patterns.template_ import Template
        # return Template

    def no_quotes(self, LOG, status_text, tweet_posX, tweet_posY, textwraped_value, font_philo_text, drawing_p):
        # Caso ASPAS sejam FALSAS
        if len(status_text) > 240:
            LOG.info("Tweet MAIOR que 240 caracteres, ajustando texto...")
            font_size = 30
            ImageFont.truetype(font_philo_text, font_size)
            # INT = DEFAULT
            # X =  38
            # Y = 105
            # textwrap = 25

            return self.put_tweet_in_img(status_text=status_text,
                                         tweet_posX=tweet_posX,
                                         tweet_posY=tweet_posY,
                                         textwraped_value=textwraped_value,
                                         font_philosopher_text=font_philo_text,
                                         has_quotes=False, drawing_p=drawing_p)


        # MENOR ou IGUAL que 25 caracteres
        elif len(status_text) <= 25:
            LOG.info("Tweet MENOR que 25 caracteres, ajustando texto...")
            font_size = 50
            ImageFont.truetype(font_philo_text, font_size)
            # INT = DEFAULT // INT = SPECIFIC
            # X -> 38 - 80 =
            # Y -> 105 - 150 =
            # textwrap -> 25 - 20 =
            return self.put_tweet_in_img(status_text=status_text,
                                         tweet_posX=abs(tweet_posX - 42),
                                         tweet_posY=abs(tweet_posY - 45),
                                         textwraped_value=(textwraped_value - 5),
                                         font_philosopher_text=font_philo_text,
                                         has_quotes=False, drawing_p=drawing_p)

    def put_name_of_philosopher(self, LOG, philosopher_name, font_philosopher_name, author_posX, author_posY,
                                drawing_p):
        LOG.info("put name of philosopher")
        # Caso ASPAS sejam VERDADEIRAS
        # Nome do filosofo
        size_philosopher_name = 30

        drawing_p.text(xy=(author_posX, author_posY),
                              text=textwrap.fill(str(philosopher_name)),
                              fill=(255, 255, 255),
                              font=ImageFont.truetype(font_philosopher_name, size_philosopher_name))

        return drawing_p

    def put_tweet_in_img(self, status_text, tweet_posX, tweet_posY, textwraped_value, font_philosopher_text,
                         drawing_p, has_quotes=None):
        BASE_TEMPLATE_LAYER = Image.open(TEMPLATES_PATH)
        open_quote = Image.open(os.getenv('open_quotes'))
        close_quote = Image.open(os.getenv('close_quotes'))
        open_quote_resized = open_quote.resize((60, 60))
        close_quote_resized = close_quote.resize((60, 60))

        if has_quotes:
            # Citação -- texto do tweet
            size_tweet_text = 50
            self.draw_t = drawing_p.text(xy=(tweet_posX, tweet_posY),
                                         text=textwrap.fill(str(status_text), textwraped_value),
                                         fill=(255, 255, 255),
                                         font=ImageFont.truetype(font_philosopher_text, size_tweet_text))

            self.quote_1_paste = BASE_TEMPLATE_LAYER.paste(open_quote_resized, (50, 30), open_quote_resized)
            self.quote_2_paste = BASE_TEMPLATE_LAYER.paste(close_quote_resized, (500, 400), close_quote_resized)

            return self.draw_t, self.quote_1_paste, self.quote_2_paste, has_quotes

        # Caso ASPAS sejam FALSAS
        else:
            size_tweet_text = 50
            self.draw_t = drawing_p.text(xy=(tweet_posX, tweet_posY),
                                         text=textwrap.fill(str(status_text), textwraped_value),
                                         fill=(255, 255, 255),
                                         font=ImageFont.truetype(font_philosopher_text, size_tweet_text))

            return self.draw_t, has_quotes

    def ajust_philosopher_name(self, LOG, choose_philosopher_param):
        # choose philosopher
        LOG.info("ajust_philosopher_name -> Entrou")
        remove_path_filename = os.path.basename(choose_philosopher_param)
        LOG.info(f"Imagem do filósofo escolhida: {remove_path_filename}")
        remove_extension_filename = remove_path_filename.replace('.png', '')

        if f'({int})' in remove_extension_filename:
            LOG.info("Removendo lixo no nome da imagem do filosofo...")
            remove_number_in_name = remove_extension_filename.replace(f'({int})', '')
            self.finish_name_philosopher = f'- {remove_number_in_name}'
            LOG.info(f'Nome do filósofo tratado: {self.finish_name_philosopher}')

            return self.finish_name_philosopher
        else:
            self.finish_name_philosopher = f'- {remove_extension_filename}'
            LOG.info("Nenhum lixo no nome da imagem encontrado. Prosseguindo normalmente...")
            LOG.info(f'Nome do filósofo tratado: {self.finish_name_philosopher}')
        LOG.info("ajust_philosopher_name -> Saindo")
        return self.finish_name_philosopher

    def adjust_tweet_font_size(self, font_philo_txt, blank_layer, font_size_param, quote_font):
        while (quote_font.getsize(font_philo_txt)[0] < blank_layer.size[0]) and (
                quote_font.getsize(font_philo_txt)[1] < blank_layer.size[1]):
            font_size_param += 1
            quote_font = ImageFont.truetype(font_philo_txt, font_size_param)
        font_size_param -= 1
        quote_font = ImageFont.truetype(font_philo_txt, font_size_param)
        self.drawing.textsize(font_philo_txt, font=quote_font)
