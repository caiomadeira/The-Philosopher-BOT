"""
Philosopher Bot
---------------
Created by Caio Madeira
Co-worker: Rodrigo Carmo

instagram: @sudomadeira
Twitter: @bot_philospher
Avaliable on Discord too!

"""
import time
import tweepy
from Twitter.Hashtag.philobot_engine import PhiloBot
from Twitter.Hashtag.philomaker_engine import PhiloMaker
from config import *
from Logs.Twitter.logger_engine import log_hashtag
from config import Config
import tempfile


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

            self.log.info('Tweet ID: ' + self.tweetid)
            self.log.info('Tweet USERNAME: ' + self.username)
            self.log.info('Adicionado na fila')
            self.log.info('=======================================================\n')
            time.sleep(5)

            if len(self.q) >= self.QUEUE:
                for i in range(1):
                    self.philobot_engine(self.hashtag_list)
                    break
        except Exception as e_onsts:
            self.log.error("[X] - ERRO AO COLETAR INFORMAÇÕES DO TWEET")
            self.log.error(e_onsts)
            self.log.error("[-] - Ignorando e continuando os tweets\n")
            pass

    def update(self, post, status, post_username):
        number = 1
        try:
            tweepy.Cursor(self.api.user_timeline).items(number)
            self.api.update_with_media(post, status="@" + post_username + " ", auto_populate_reply_metadata=True,
                                       in_reply_to_status_id=status)
            self.log.info('[+] - IMAGEM ENVIADA!')
            time.sleep(3)
        except tweepy.TweepError as e:
            self.log.error("[X] - ERRO! Não foi possível enviar a imagem.")
            self.log.error(e.reason)
            self.log.info("\n==========================")
