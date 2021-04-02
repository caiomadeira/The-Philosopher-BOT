"""
Philosopher Bot
---------------
Created by Caio Madeira
Co-worker: Rodrigo Carmo

instagram: @sudomadeira
Twitter: @bot_philospher
Avaliable on Discord too!

"""
import tweepy
from Logs.Twitter.logger_hashtag import log_hashtag
from Lists.sub_list import sub_list_philobot


class StartHashtag:

    def __init__(self, sub_list):
        self.__sub_list = sub_list

        """=========== SET LOG ==========="""
        self.log = log_hashtag(__name__)
        self.start_hashtag_extension()

    def start_hashtag_extension(self):
        self.log.info("Bem-vindo!\n")
        self.log.info("Philosopher BOT por Caio Madeira e Rodrigo Carmo\n")
        self.log.info(">INICIANDO HASHTAG - EXTENSION<")

        from Hashtag.hashtag import HashtagClass

        self.log.info('HASHTAG Test ESCOLHIDA, INICIANDO #PHILOBOT')

        from Tests.Credentials.twitter_credentials_test import API_TEST as API
        from Scripts.Automatic_Tweets.auto_status import post_status_only_text

        try:
            # TESTEPHILO
            Philobot_Stream = tweepy.Stream(auth=API.auth,
                                            listener=HashtagClass(self.__sub_list, API),
                                            include_rts=False)
            Philobot_Stream.filter(track=['#TestePhilo'], is_async=True)
            import time
            time.sleep(3)
            post_status_only_text()
            return Philobot_Stream

        except Exception as stream:
            self.log.error('ERRO AO INICIAR O STREAM COM A API DO TWITTER')
            self.log.error(stream)

    def sub_list(self):
        return self.__sub_list


if __name__ == '__main__':
    StartHashtag(sub_list=sub_list_philobot)
