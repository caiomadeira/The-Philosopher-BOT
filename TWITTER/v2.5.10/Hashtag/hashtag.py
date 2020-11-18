"""
posting.py
Philosopher Bot
---------------
Created by Caio Madeira (@sudomaidera)
Co-worker: Rodrigo Carmo @rodrigoblock

instagram: @sudomadeira
Twitter: @bot_philospher
Avaliable on Discord too!

"""
# -*- coding: utf-8 -*-
import tweepy, time
from Credentials.credentials_verify import api
from Logs.logger_hashtag import *
from config import HASHTAG, VERSION_HASHTAG

__VERSION__ = VERSION_HASHTAG

log.info("Hashtag.py v2.0")

q = []
q_username = []


def starting_hashtag():
    MyStreamListener()
    the_api = api
    myStream = tweepy.Stream(auth=the_api.auth, listener=MyStreamListener())
    myStream.filter(track=[HASHTAG], is_async=True)


class MyStreamListener(tweepy.StreamListener):
    log.info("Esperando....")

    def on_status(self, status):
        log.info("========== NOVO TWEET ENCONTRADO ===========")

        username = status.user.screen_name
        tweetid = str(status.id)
        q.append(tweetid)
        q_username.append(username)

        log.info('Tweet ID: ' + tweetid)
        log.info('Tweet USERNAME: ' + username)
        log.info('Aguardando o próximo tweet')
        log.info('--------------------------------------------\n')
        time.sleep(15)

        if len(q) >= 1:
            log.info('----------------------------------------')
            log.info('_\|/_ STARTING PHILOENGINE 3.0 _\|/_ ')
            log.info('----------------------------------------')
            from Hashtag.PhiloEngine import philoengine
            philoengine()



def update(post, status, username):
    numero = 1
    try:
        tweepy.Cursor(api.user_timeline).items(numero)
        api.update_with_media(post, status="@" + username + " ", auto_populate_reply_metadata=True,
                              in_reply_to_status_id=status)
        time.sleep(5)
    except tweepy.TweepError as e:
        log.info(e.reason)
        log.info("ERRO! Não foi possivel realizar a ação para o usuário.")
        log.info("\n==========================")


