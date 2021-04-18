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
from Hashtag.philobot_engine import PhiloBot
from Logs.Twitter.logger_hashtag import log_hashtag


class HashtagClass(tweepy.StreamListener, PhiloBot):
    def __init__(self, hashtag_list, get_hash_api):
        super().__init__()
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
                    self.philobot_engine()
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
    # @staticmethod
    # def get_status_func(self, last_id_param):
    #     try:
    #         get_status = self.api.get_status(last_id_param, tweet_mode='extended', include_entities=False)._json[
    #             'full_text']
    #         self.log.info('[ETAPA 1] Status coletado: ' + get_status)
    #     except tweepy.error.TweepError as e:
    #         self.log.info(e)
    #         self.log.info('ERRO: FALHA NA PEGA DO ID - TWEET DELETADO')
    #         self.log.info('----------------------------------------\n')
    #         self.log.info('>AGUARDANDO NOVOS TWEETS...<')
    #
    #         time.sleep(2)
    #         return HashtagClass


