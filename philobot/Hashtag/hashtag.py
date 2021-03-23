"""
Philosopher Bot
---------------
Created by Caio Madeira
Co-worker: Rodrigo Carmo

instagram: @sudomadeira
Twitter: @bot_philospher
Avaliable on Discord too!

"""
from http import client
import urllib3
import time
import tweepy
from Hashtag.philobot_engine import PhiloBot
from Hashtag.philomaker_engine import PhiloMaker
from config import *
from Logs.logger_hashtag import log_hashtag
from config import Config


class HashtagClass(tweepy.StreamListener, PhiloBot, PhiloMaker, Config):
    def __init__(self, hashtag_list, get_hash_api):
        super().__init__()
        instance = Config()
        self.positions = instance.positions
        self.q = []
        self.q_username = []
        self.q_tweet_info = []
        self.api = get_hash_api
        self.QUEUE = 1
        self.hashtag_list = hashtag_list
        self.log = log_hashtag(__name__)
        time.sleep(5)

    def on_status(self, status):
        try:
            self.log.info("=============== NOVO TWEET ENCONTRADO ================")

            self.username = status.user.screen_name
            self.tweetid = str(status.id)
            self.get_ID_not_string = status.id
            self.tweet_info = str(status)
            self.get_metadata = status

            self.q.append(self.tweetid)
            self.q_username.append(self.username)
            self.q_tweet_info.append(self.tweet_info)

            self.log.info('[LOG PARA DEBUG - PROBLEMA MARCAÇÃO ERRADA - TEMPORARIO]')
            self.log.info('ITENS NA LISTA:')
            self.log.info(self.q_username)

            self.log.info('Tweet ID: ' + self.tweetid)
            self.log.info('Tweet USERNAME: ' + self.username)
            self.log.info('Adicionado na fila')
            self.log.info('=======================================================\n')
            time.sleep(5)

            if len(self.q) >= self.QUEUE:
                for i in range(1):
                    self.philobot_engine(self.hashtag_list)
                    break
        except Exception:
            pass
            '''
            for hash_maker in sub_list_philomaker:
                if hash_maker in self.tweet_info:
                    for i in range(1):
                        if len(self.q) >= self.QUEUE:
                            time.sleep(20)
                            log.info("Esperando 20 segundos...")
                            self.philomaker_engine(self.hashtag_list)
                        break

            for hash_philo in sub_list_philobot:
                if hash_philo in self.tweet_info:
                    for i in range(1):
                        if len(self.q) >= self.QUEUE:
                            time.sleep(20)
                            log.info("Esperando 20 segundos...")
                            self.philobot_engine(self.hashtag_list)
                        break

            except Exception:
            pass
            '''

    def update(self, post, status, post_username):
        number = 1
        try:
            tweepy.Cursor(self.api.user_timeline).items(number)
            self.api.update_with_media(post, status="@" + post_username + " ", auto_populate_reply_metadata=True,
                                       in_reply_to_status_id=status)
            self.log.info('IMAGEM ENVIADA!')
            time.sleep(3)
        except tweepy.TweepError as e:
            self.log.info(e.reason)
            self.log.info("ERRO! Não foi possivel realizar a ação para o usuário.")
            self.log.info("\n==========================")
