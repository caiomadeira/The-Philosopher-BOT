import tweepy
import time
from PIL import Image, ImageDraw, ImageFont, ImageOps
import random
import os
import re
import json
import textwrap

# Autenticadores do twitter (pessoal)
auth = tweepy.OAuthHandler("Vp1n7BXhLaS1tY3dds0BT6Reh", "gKT1C5mkWRdl0BkhvkujWF8LNn8keeFEK3aBt8Dvr7KaYxUfSb")
auth.set_access_token("1263355414248390662-4td7amcj7vMWiHwWQxhILZT7eczLa9",
                      "qhQCTPZz13ro1IwB9OWsNUliDOzTGUUqLf7stpo7VWdAG")

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)  # Criando um objeto do api

filosofo = [
    Image.open('images/adamsmith.png'),
    Image.open('images/alanturing.png'),
    Image.open('images/anyrand.png'),
    Image.open('images/aristoteles.png'),
    Image.open('images/bakunin.png'),
    Image.open('images/castro.png'),
    Image.open('images/chaplin.png'),
    Image.open('images/che.png'),
    Image.open('images/curie.png'),
    Image.open('images/dalailama.png'),
    Image.open('images/descartes.png'),
    Image.open('images/FUKO.png'),
    Image.open('images/jesus.png'),
    Image.open('images/karnal.png'),
    Image.open('images/lenin.png'),
    Image.open('images/MANDELA.png'),
    Image.open('images/maquiavel.png'),
    Image.open('images/martin.png'),
    Image.open('images/marx.png'),
    Image.open('images/mussolini.png'),
    Image.open("images/neto.png"),
    Image.open("images/neymar.png"),
    Image.open("images/niet.png"),
    Image.open("images/pascal.png"),
    Image.open("images/platao.png"),
    Image.open("images/rousseau.png"),
    Image.open("images/stalin.png"),
    Image.open("images/winston.png"),
]
FILE_NAME = 'last_seen.txt'


def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id


def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return


search = "#PhiloBot"
numero = 1

img = Image.open('templates/templateNovo.png')
fonte = ImageFont.truetype("font/myriad.otf", 37)
escrever = ImageDraw.Draw(img)
tweetos = []
for tweet in tweepy.Cursor(api.search, search).items(numero):
    try:
        status = next(tweepy.Cursor(api.user_timeline).items(numero), None)
        lastid = status.id
        laststatus = (api.get_status(lastid).text).replace("#PhiloBot", "").replace("@", " ")
        print("nome do usuario:@" + tweet.user.screen_name)
        # text = api.get_status(read_last_seen(FILE_NAME), tweet_mode='extended')._json['full_text']
        # print(text)
        print("status:" + laststatus)
        escrever.text(xy=(75, 128), text=textwrap.fill(str(laststatus), 30), fill=(255, 255, 255), font=fonte)
        randomfilo = random.choice(filosofo)
        img.paste(randomfilo, (10, 0), randomfilo)
        img.save('cit.png')
        api.update_with_media('cit.png', in_reply_to_status_id=tweet.id)
        # api.update_status("@"+ tweet.user.screen_name + "oi", in_reply_to_status_id=tweet.id)
        print("Enviado corretamente")
        time.sleep(2)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
