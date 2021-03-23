import random
from filosofo_list import special_choice
import acess_tokens
import tweepy
from PIL import Image, ImageDraw, ImageFont
from logging import *
import textwrap

auth = tweepy.OAuthHandler(acess_tokens.acess1, acess_tokens.acess2)
auth.set_access_token(acess_tokens.acess3, acess_tokens.acess4)

wait1 = wait_on_rate_limit = False
wait2 = wait_on_rate_limit_notify = True

api = tweepy.API(auth, wait1, wait2)






def comunismo():
    special_keys = ["comunismo é foda pra caralho manooww!!!"]

    if "comunismo" in special_keys:

        img = Image.open('templates/templateNovo2.png')
        fonte = ImageFont.truetype("font/myriad.otf")
        escrever = ImageDraw.Draw(img)
        escrever.text(xy=(43, 105), text=textwrap.fill(str(special_keys), 30), fill=(255, 255, 255), font=fonte)
        get_philo = 'images/stalin.png'
        img.paste((0, 0), get_philo )
        img.save('posting.png')
        api.update_with_media('posting.png')
        print("> SPECIAL ENVIADO! <")
        print("===================================================")





if __name__ == '__main__':
    comunismo()
    print("postado")