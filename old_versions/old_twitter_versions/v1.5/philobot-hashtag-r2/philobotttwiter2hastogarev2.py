import tweepy
import time
from PIL import Image, ImageDraw, ImageFont, ImageOps
import random
import os
import re
import json
import textwrap
import schedule
#from win32con import TEXT
# Autenticadores do twitter (pessoal)
auth = tweepy.OAuthHandler("Vp1n7BXhLaS1tY3dds0BT6Reh", "gKT1C5mkWRdl0BkhvkujWF8LNn8keeFEK3aBt8Dvr7KaYxUfSb")
auth.set_access_token("1263355414248390662-4td7amcj7vMWiHwWQxhILZT7eczLa9",
                      "qhQCTPZz13ro1IwB9OWsNUliDOzTGUUqLf7stpo7VWdAG")

api = tweepy.API(auth, wait_on_rate_limit=False, wait_on_rate_limit_notify=True)  # Criando um objeto do api

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print("Achei esse tweet:" + status.text)

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

        img = Image.open('templates/templateNovo2.png')
        fonte = ImageFont.truetype("font/myriad.otf", 45)
        escrever = ImageDraw.Draw(img)
        #tweetos = []


        for tweet in tweepy.Cursor(api.search, search, since='2019-06-03').items(numero):
                try:

                        #status = next(tweepy.Cursor(api.user_timeline).items(numero), None)
                    tweepy.Cursor(api.user_timeline).items(numero)
                    print("---- NOVO STATUS ENCONTRADO -----")
                    lastid = tweet.id
                    print("id pego:" + str(tweet.id))
                    laststatus = api.get_status(lastid, tweet_mode='extended')._json['full_text'].replace("#PhiloBot", "").replace("#philobot", " ").replace("#PHILOBOT", " ")
                    laststatus2 = re.sub('@[^\s]+', '', laststatus)
                    print("nome do usuario:@" + tweet.user.screen_name)
                        # text = api.get_status(read_last_seen(FILE_NAME), tweet_mode='extended')._json['full_text']
                        # print(text)
                    print("status:" + laststatus)
                    escrever.text(xy=(43, 115), text=textwrap.fill(str(laststatus2), 28), fill=(255, 255, 255), font=fonte)
                    randomfilo = random.choice(filosofo)
                    img.paste(randomfilo, (29, 0), randomfilo)
                    img.save('cit.png')
                    api.update_with_media('cit.png', status="@" + tweet.user.screen_name + " ", in_reply_to_status_id=status.id)
                        # api.update_status("@"+ tweet.user.screen_name + "oi", in_reply_to_status_id=tweet.id)
                    print("Enviado corretamente")

                    print("-----------------------------")
                    time.sleep(2)


                except tweepy.TweepError as e:
                    print(e.reason)
                    print("nao foi possivel coletar id")
                except StopIteration:
                    break


#def main():
    #schedule.every(3).seconds.do(hashtag)
    #schedule.every(5).minutes.do(hashtag)

    #while True :
        #schedule.run_pending()
        #time.sleep(1)
    #return


if __name__ == "__main__":
    my_streamer = MyStreamListener()
    the_api = api
    myStream = tweepy.Stream(auth=the_api.auth, listener=MyStreamListener())
    myStream.filter(track=['#PhiloBot'])