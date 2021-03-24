import textwrap
import random
from Lists.img_list import PHILOSOPHERS_LIST, PHILOSOPHERS_NAME
from PIL import Image, ImageDraw, ImageFont
import tweepy
import os
from Credentials.Twitter.Test import API_MAIN_TEST
from Templates.New_Img_Manipulation.reference import TEMPLATES_PATH

api = API_MAIN_TEST

status = '#testemaker cu'
img = Image.open('New_Img_Manipulation/layer_1.png')
# blank = Image.new('RGB', (269, 194))
fontsize = 28
font = ImageFont.truetype("myriad.otf", fontsize)
drawing = ImageDraw.Draw(img)
drawing_mention_name = ImageDraw.Draw(img)

choice_philosopher = random.choice(PHILOSOPHERS_LIST)  # separa a imagem e salva em string
print(choice_philosopher)

remove_path_of_filename = os.path.basename(choice_philosopher)  # remove o path do nome da imagem
print(remove_path_of_filename)

remove_extension_of_filename = remove_path_of_filename.replace('.png', '')  # remove a extensao .png
print(remove_extension_of_filename)

if '(2)' in remove_extension_of_filename:
    remove_number_in_name = remove_extension_of_filename.replace('(2)', '')
    print("Removendo (2) do nome da imagem do filosofo...")
    print(remove_number_in_name)
    finish_name_of_philosopher = f'- {remove_number_in_name}'  # finaliza o nome do filosofo
    print(finish_name_of_philosopher)
else:
    finish_name_of_philosopher = f'- {remove_extension_of_filename}'  # finaliza o nome do filosofo
    print("Nenhum (2) encontrado. Prosseguindo normal.")
    print(finish_name_of_philosopher)

philosopher_str_to_obj = Image.open(choice_philosopher)  # abre a imagem como local na memoria ao inves de string

filo2 = philosopher_str_to_obj.resize((449, 584))
img.paste(filo2, (629, 0))
smooth_template = Image.open('New_Img_Manipulation/layer_3.png')
img.paste(smooth_template, (0, 0), smooth_template)

open_quote = Image.open('open_quote.png')
close_quote = Image.open('close_quote.png')
open_quote_resized = open_quote.resize((60, 60))
close_quote_resized = close_quote.resize((60, 60))

custom_text = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' \
              'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' \
              'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' \
              'AAAAAAAAAAAAAAAAA '

# texto do filosofo
drawing.text(xy=(75, 120), text=textwrap.fill(str(custom_text), 28), fill=(255, 255, 255), font=font)

img.paste(open_quote_resized, (50, 30), open_quote_resized)
img.paste(close_quote_resized, (500, 400), close_quote_resized)

# nome do filosofo
fontsize = 15
font = ImageFont.truetype("Font/times.ttf", fontsize)
drawing.text(xy=(43, 514), text=textwrap.fill(str(finish_name_of_philosopher), 30), fill=(255, 255, 255), font=font)

img.save('test_hashtag.png')

print("postado")
