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
#from win32con import TEXT
# Autenticadores do twitter (pessoal)


#auth = tweepy.OAuthHandler("Vp1n7BXhLaS1tY3dds0BT6Reh", "gKT1C5mkWRdl0BkhvkujWF8LNn8keeFEK3aBt8Dvr7KaYxUfSb")
#auth.set_access_token("1263355414248390662-4td7amcj7vMWiHwWQxhILZT7eczLa9","qhQCTPZz13ro1IwB9OWsNUliDOzTGUUqLf7stpo7VWdAG")

 # Criando um objeto do api

def postdiario():
    auth = tweepy.OAuthHandler("Vp1n7BXhLaS1tY3dds0BT6Reh", "gKT1C5mkWRdl0BkhvkujWF8LNn8keeFEK3aBt8Dvr7KaYxUfSb")
    auth.set_access_token("1263355414248390662-4td7amcj7vMWiHwWQxhILZT7eczLa9",
                          "qhQCTPZz13ro1IwB9OWsNUliDOzTGUUqLf7stpo7VWdAG")
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


    filosofo = [
        Image.open('images/adamsmith.png'),
        Image.open('images/alanturing.png'),
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
        Image.open("images/albert.png"),
        Image.open("images/anyrand.png"),
        Image.open("images/bauman.png"),
        Image.open("images/camus.png"),
        Image.open("images/clarice.png"),
        Image.open("images/dilma.png"),
        Image.open("images/fiodor.png"),
        Image.open("images/freud.png"),
        Image.open("images/hannah.png"),
        Image.open("images/hawk.png"),
        Image.open("images/jobs.png"),
        Image.open("images/kimjonun.png"),
        Image.open("images/mao.png"),
        Image.open("images/newton.png"),
        Image.open("images/olavo.png"),
        Image.open("images/schop.png"),
        Image.open("images/simone.png"),
        Image.open("images/socrates.png"),
        Image.open("images/voltaire.png"),
        Image.open("images/disney.png"),
        Image.open("images/galileu.png"),
        Image.open("images/getulio.png"),
        Image.open("images/kant.png"),
        Image.open("images/lula.png"),
        Image.open("images/nikola.png"),
        Image.open("images/pitagoras.png"),
        Image.open("images/papa.png"),
        Image.open("images/troskt.png"),
        Image.open("images/beethoven.png"),
        Image.open("images/carlsagan.png"),
        Image.open("images/darwin.png"),
        Image.open("images/davinci.png"),
        Image.open("images/dompedro2.png"),
        Image.open("images/durkheim.png"),
        Image.open("images/euclides.png"),
        Image.open("images/evomorales.png"),
        Image.open("images/henriqueviii.png"),
        Image.open("images/hobbes.png"),
        Image.open("images/johnlocke.png"),
        Image.open("images/lutero.png"),
        Image.open("images/maome.png"),
        Image.open("images/marighella.png"),
        Image.open("images/michelangelo.png"),
        Image.open("images/nicolasmaduro.png"),
        Image.open("images/pasteur.png"),
        Image.open("images/robespierre.png"),
        Image.open("images/sankara.png"),
        Image.open("images/santoagostinho.png"),
        Image.open("images/sartre.png"),
        Image.open("images/shakespper.png"),
        Image.open("images/trump.png"),
        Image.open("images/vangogh.png"),
        Image.open("images/zaratruta.png"),
        Image.open("images/angeladavis.png"),
        Image.open("images/billgates.png"),
        Image.open("images/carlosdrummond.png"),
        Image.open("images/engelgs.png"),
        Image.open("images/fernandopessoa.png"),
        Image.open("images/ford.png"),
        Image.open("images/freire.png"),
        Image.open("images/kafka.png"),
        Image.open("images/lemisnki.png"),
        Image.open("images/loncoln.png"),
        Image.open("images/morgan.png"),
        Image.open("images/obama.png"),
        Image.open("images/orwell.png"),
        Image.open("images/seneca.png"),
        Image.open("images/suntzu.png"),
    ]

    img = Image.open('templates/templateNovo2.png')
    fonte = ImageFont.truetype("font/myriad.otf", 37)

    contas = ['felipeneto',
              'CarlosBolsonaro',
              'lucasinutilismo',
              'oproprioolavo',
              'AbrahamWeint',
              'SF_Moro',
              'whindersson',
              'psicoshow',
              'anonimosbrs',
              'momorsa',
              'gazetheabyss',
              'tweetsfelipe',
              'cotore',
              'deborista',
              'luide',
              'oednaldopereira',
              'alefrota77',
              "opropriolavo",
              'BolsonaroSP',
              'gabahn',
              '0800FABI',
              'jakkkkkjj',
              'guizin_jeferson',
              'reaisNhoras',
              'CarlosBolsonaro',
              'lucasinutilismo',
              'peixeaquatico',
              'joaoamoedonovo',
              'Brunozor',
              'maiconkusterkkk',
              'Haddad_Fernando',
              'OlavoOpressor',
              'Rconstantino',
              'LulaOficial',
              'wwwmlna',
              'brusnos',
              'FatosEx',
              'vxtakaki',
              'silvazuao',
              'joaoalmeidaovo',
              'moura_101',
              'rolealeatorio',
              'fravineas',
              'blckjoy_',
              'perinazzzo',
              'legadaodamassa',
              'Philipe_peters',
              'tralhasdojon',
              'Fimosehead',
              'DrTelaskoAvara',
              'BoniroBot',
              "raufitoo",
              'rbcgaia',
              'PortoAncap',
              'anamaryb'

     ]


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


    randomcontas = random.choices(contas)
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
    img.paste(randomfilo, (29, 0), randomfilo)
    img.save('cit.png')
    api.update_with_media('cit.png')
    return


def main():
    schedule.every(3).seconds.do(postdiario)
    #schedule.every(1).hour.do(postdiario)
    #schedule.every(2).hours.do(postdiario)

    while True:
        schedule.run_pending()
        time.sleep(1)
    return


if __name__ == '__main__':
    main()
