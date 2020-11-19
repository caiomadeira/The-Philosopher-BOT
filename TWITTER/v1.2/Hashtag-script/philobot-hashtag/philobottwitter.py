import tweepy
from tweepy import Cursor
import time
from PIL import Image, ImageDraw, ImageFont, ImageOps
import random
import os
import re
import textwrap
import json
import schedule

# Autenticadores do twitter (pessoal)
from win32netcon import TEXT

#auth = tweepy.OAuthHandler("Vp1n7BXhLaS1tY3dds0BT6Reh", "gKT1C5mkWRdl0BkhvkujWF8LNn8keeFEK3aBt8Dvr7KaYxUfSb")
#auth.set_access_token("1263355414248390662-4td7amcj7vMWiHwWQxhILZT7eczLa9","qhQCTPZz13ro1IwB9OWsNUliDOzTGUUqLf7stpo7VWdAG")

 # Criando um objeto do api

def postdiario():
    auth = tweepy.OAuthHandler("Vp1n7BXhLaS1tY3dds0BT6Reh", "gKT1C5mkWRdl0BkhvkujWF8LNn8keeFEK3aBt8Dvr7KaYxUfSb")
    auth.set_access_token("1263355414248390662-4td7amcj7vMWiHwWQxhILZT7eczLa9",
                          "qhQCTPZz13ro1IwB9OWsNUliDOzTGUUqLf7stpo7VWdAG")
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    contas = ["felipeneto", "jairbolsonaro", "SF_Moro", "AbrahamWeint", 'cellbit', 'deborista', 'psicoshow',
              'nilmoretto', 'whindersson', 'CarlosBolsonaro', 'lucasinutilismo', 'peixeaquatico', 'joaoamoedonovo',
              'Brunozor', 'maisa', 'maiconkusterkkk', 'Haddad_Fernando']

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

    img = Image.open('templates/templateNovo.png')
    fonte = ImageFont.truetype("font/myriad.otf", 37)

    contas = ['felipeneto', 'CarlosBolsonaro', 'lucasinutilismo', 'oproprioolavo', 'AbrahamWeint', 'SF_Moro',
              'jairbolsonaro', 'whindersson', 'psicoshow', 'anonimosbrs', 'momorsa', 'gazetheabyss', 'tweetsfelipe',
              'cotore', '_SaraWinter', 'deborista', 'luide', 'oednaldopereira', 'alefrota77', "opropriolavo",'BolsonaroSP']


    def obter_tweets(usuario, limite=1, items=1):
        resultados = api.user_timeline(screen_name=usuario, count=limite, tweet_mode='extended', contributor_details=False,
                                       include_entities=False, include_rts=False, trim_user=False, exclude_replies=True)
        tweets = []  # lista de tweets inicialmente vazia
        for r in resultados:
            # utiliza expressão regular para remover a URL do tweet
            # http pega o início da url
            # \S+ pega os caracteres não brancos (o final da URL)
            tweet = re.sub(r'http\S+', '', r.full_text)
            tweets.append(tweet.replace('\n', ' '))  # adiciona na lista
            time.sleep(2)
        return tweets  # retorna a lista de tweets


    randomcontas = random.choice(contas)
    escrever = ImageDraw.Draw(img)
    tweets = obter_tweets(random.choice(contas), limite=1)  # limite se da a quantos tweets pegar
    print(tweets)
    for status in tweepy.Cursor(api.user_timeline).items(1):
        items = ("\n".join(tweets))
        # print(textwrap.wrap(tweeto, 2))
        print("daily post enviado")
        escrever.text(xy=(75, 128), text=textwrap.fill(items, 30), fill=(255, 255, 255), font=fonte)
        # textwrap corta as linhas
    # lines = textwrap.wrap(tweeto)
    # api.update_status((''.join(tweets[7])))
    randomfilo = random.choice(filosofo)
    img.paste(randomfilo, (0, 0), randomfilo)
    img.save('cit.png')
    api.update_with_media('cit.png')
    return

def main():
    #schedule.every(3).seconds.do(postdiario)
    schedule.every().day.at("07:00").do(postdiario)

    schedule.every().day.at("09:00").do(postdiario)

    schedule.every().day.at("12:00").do(postdiario)

    schedule.every().day.at("15:00").do(postdiario)

    schedule.every().day.at("19:00").do(postdiario)

    schedule.every().day.at("19:27").do(postdiario)

    schedule.every().day.at("22:00").do(postdiario)

    schedule.every().day.at("00:00").do(postdiario)

    schedule.every().day.at("02:00").do(postdiario)

    while True:
        schedule.run_pending()
        time.sleep(1)
    return


if __name__ == '__main__':
    main()