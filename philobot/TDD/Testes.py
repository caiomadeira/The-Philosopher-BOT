import time
import tweepy
from TDD.LOG_TESTE.logger_hashtag_teste import *


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        log.info("=============== NOVO TWEET ENCONTRADO ================")
        tweetid = str(status.id)

        log.info('TRATANDO TWEET...')

        update(use_pegando_status='TOMA ESSA MERDA', use_tweetid=tweetid)


def update(use_pegando_status, use_tweetid):
    log.info('Twittando...')
    try:
        api.update_status(use_pegando_status, in_reply_to_status_id=use_tweetid, auto_populate_reply_metadata=True)
        log.info('TWEET ENVIADO C COM SUCESSO!')

    except Exception:
        log.exception('DEU BOSTA')

    log.info('Twittado!')
    log.info('Aguardando proximo tweet...')
    time.sleep(5)


if __name__ == '__main__':

    from Credentials.Test.main_credentials_test import api_test

    api = api_test
    HASHTAG_CONFIG = '#Testephilo'

    try:
        MyStreamListener()
        the_api = api
        myStream_PhiloBot = tweepy.Stream(auth=the_api.auth, listener=MyStreamListener(), include_rts=False)
        myStream_PhiloBot.filter(track=[HASHTAG_CONFIG], is_async=True)
        log.info('PhiloTESTE iniciado.. aguardando script de teste')
    except Exception as e_main:
        log.info('ERRO')
        log.info(e_main)
