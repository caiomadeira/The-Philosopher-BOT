import textwrap
from PIL import Image, ImageFont

import dotenv, os

# O ideal é que o env não seja carregado aqui, pois pode haver mais de um
import Hashtag.patterns.template_

dotenv.load_dotenv(dotenv.find_dotenv())


class Font(object):

    # // Lembre-se de definir valores pra posições x y default/sem aspas e com aspas

    def adjust_img_text(self, status_text, tweet_posX, tweet_posY, textwraped_value,
                        philosopher_name, font_philo_name, font_philo_text,
                        author_posX, author_posY, has_quotes=None):
        print('[ETAPA 5] Verificando aspas...')
        # Caso ASPAS sejam VERDADEIRAS
        if has_quotes:
            # Maior ou IGUAL que 240 caracteres
            if len(status_text) > 240:
                print("Tweet MAIOR que 240 caracteres, ajustando texto...")
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
                                      has_quotes=True)

                self.put_name_of_philosopher(philosopher_name=philosopher_name,
                                             font_philosopher_name=font_philo_name,
                                             author_posX=author_posX,
                                             author_posY=author_posY,
                                             has_quotes=True)

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
                                      has_quotes=True)

                self.put_name_of_philosopher(philosopher_name=philosopher_name,
                                             font_philosopher_name=font_philo_name,
                                             author_posX=author_posX,
                                             author_posY=author_posY,
                                             has_quotes=True)

            return has_quotes == True

        # Caso ASPAS sejam FALSAS
        else:
            if len(status_text) > 240:
                print("Tweet MAIOR que 240 caracteres, ajustando texto...")
                font_size = 30
                ImageFont.truetype(font_philo_text, font_size)
                # INT = DEFAULT
                # X =  38
                # Y = 105
                # textwrap = 25

                self.put_tweet_in_img(status_text=status_text,
                                      tweet_posX=tweet_posX,
                                      tweet_posY=tweet_posY,
                                      textwraped_value=textwraped_value,
                                      font_philosopher_text=font_philo_text,
                                      has_quotes=False)

                self.put_name_of_philosopher(philosopher_name=philosopher_name,
                                             font_philosopher_name=font_philo_name,
                                             author_posX=author_posX,
                                             author_posY=author_posY,
                                             has_quotes=False)

            # MENOR ou IGUAL que 25 caracteres
            elif len(status_text) <= 25:
                print("Tweet MENOR que 25 caracteres, ajustando texto...")
                font_size = 50
                ImageFont.truetype(font_philo_text, font_size)
                # INT = DEFAULT // INT = SPECIFIC
                # X -> 38 - 80 =
                # Y -> 105 - 150 =
                # textwrap -> 25 - 20 =
                self.put_tweet_in_img(status_text=status_text,
                                      tweet_posX=abs(tweet_posX - 42),
                                      tweet_posY=abs(tweet_posY - 45),
                                      textwraped_value=(textwraped_value - 5),
                                      font_philosopher_text=font_philo_text,
                                      has_quotes=False)

                self.put_name_of_philosopher(philosopher_name=philosopher_name,
                                             font_philosopher_name=font_philo_name,
                                             author_posX=author_posX,
                                             author_posY=author_posY,
                                             has_quotes=False)

                return has_quotes == False

    def put_name_of_philosopher(self, philosopher_name, font_philosopher_name, author_posX, author_posY,
                                has_quotes=None):

        # Caso ASPAS sejam VERDADEIRAS
        if has_quotes:

            # Nome do filosofo
            size_philosopher_name = 30
            self.drawing.text(xy=(author_posX, author_posY),
                              text=textwrap.fill(str(philosopher_name)),
                              fill=(255, 255, 255),
                              font=ImageFont.truetype(font_philosopher_name, size_philosopher_name))
        # Caso ASPAS sejam FALSAS
        else:

            # Nome do filosofo
            size_philosopher_name = 30
            self.drawing.text(xy=(author_posX, author_posX),
                              text=textwrap.fill(str(philosopher_name)),
                              fill=(255, 255, 255),
                              font=ImageFont.truetype(font_philosopher_name, size_philosopher_name))

    def put_tweet_in_img(self, status_text, tweet_posX, tweet_posY, textwraped_value, font_philosopher_text,
                         has_quotes=None):

        open_quote = Image.open(os.getenv('open_quotes'))
        close_quote = Image.open(os.getenv('close_quotes'))
        open_quote_resized = open_quote.resize((60, 60))
        close_quote_resized = close_quote.resize((60, 60))

        if has_quotes:
            # Citação -- texto do tweet
            size_tweet_text = 50
            self.drawing.text(xy=(tweet_posX, tweet_posY),
                              text=textwrap.fill(str(status_text), textwraped_value),
                              fill=(255, 255, 255),
                              font=ImageFont.truetype(font_philosopher_text, size_tweet_text))

            Hashtag.patterns.template_.Template.BASE_TEMPLATE_LAYER.paste(open_quote_resized, (50, 30), open_quote_resized)
            Hashtag.patterns.template_.Template.BASE_TEMPLATE_LAYER.paste(close_quote_resized, (500, 400), close_quote_resized)

        # Caso ASPAS sejam FALSAS
        else:
            size_tweet_text = 50
            self.drawing.text(xy=(tweet_posX, tweet_posY),
                              text=textwrap.fill(str(status_text), textwraped_value),
                              fill=(255, 255, 255),
                              font=ImageFont.truetype(font_philosopher_text, size_tweet_text))

    def ajust_philosopher_name(self, choose_philosopher_param):
        # choose philosopher

        remove_path_filename = os.path.basename(choose_philosopher_param)
        print(f"Imagem do filósofo escolhida: {remove_path_filename}")
        remove_extension_filename = remove_path_filename.replace('.png', '')

        if f'({int})' in remove_extension_filename:
            print("Removendo lixo no nome da imagem do filosofo...")
            remove_number_in_name = remove_extension_filename.replace(f'({int})', '')
            self.finish_name_philosopher = f'- {remove_number_in_name}'
            print(f'Nome do filósofo tratado: {self.finish_name_philosopher}')
        else:
            self.finish_name_philosopher = f'- {remove_extension_filename}'
            print("Nenhum lixo no nome da imagem encontrado. Prosseguindo normalmente...")
            print(f'Nome do filósofo tratado: {self.finish_name_philosopher}')

        return self.finish_name_philosopher

    def adjust_tweet_font_size(self, font_philo_txt, blank_layer, font_size_param, quote_font):
        while (quote_font.getsize(font_philo_txt)[0] < blank_layer.size[0]) and (
                quote_font.getsize(font_philo_txt)[1] < blank_layer.size[1]):
            font_size_param += 1
            quote_font = ImageFont.truetype(font_philo_txt, font_size_param)
        font_size_param -= 1
        quote_font = ImageFont.truetype(font_philo_txt, font_size_param)
        self.drawing.textsize(font_philo_txt, font=quote_font)
