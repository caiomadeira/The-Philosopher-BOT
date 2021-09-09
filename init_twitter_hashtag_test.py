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
from config import Config
from Logs.Twitter.logger_hashtag import log_bot
from urllib3.exceptions import ProtocolError


class StartHashtagExtension:

    def __init__(self):

        get_config = Config()
        """ =========== HASHTAGS =========== """
        self.PHILOBOT_HASHTAG = get_config.PHILOBOT__HASHTAG
        self.TESTEPHILO_HASHTAG = get_config.TESTEPHILO__HASHTAG
        self.PHILOMAKER_HASHTAG = get_config.PHILOMAKER__HASHTAG

        """ =========== SUBLIST =========== """
        self.PHILOBOT__SUBLIST = get_config.PHILOBOT__SUBLIST
        self.PHILOMAKER_SUBLIST = get_config.PHILOMAKER__SUBLIST

        self.TESTEPHILO__SUBLIST = get_config.TESTEPHILO__SUBLIST
        self.TESTMAKER_SUBLIST = get_config.TESTMAKER__SUBLIST

        """=========== SET LOG ==========="""
        self.log = log_bot
        self.start_hashtag_extension()

    def start_hashtag_extension(self):
        self.log.info("Bem-vindo!\n")
        self.log.info("Philosopher BOT por Caio Madeira e Rodrigo Carmo\n")
        self.log.info(">INICIANDO HASHTAG - TESTE<")
        self.log.info('HASHTAG EXTENSION ESCOLHIDA, INICIANDO #TESTEPHILO...')

        from Credentials.Twitter.Test.test_credentials import API_TEST
        from Twitter.Hashtag.hashtag import HashtagClass

        try:
            # TESTEPHILO
            Philobot_Stream = tweepy.Stream(auth=API_TEST.auth,
                                            listener=HashtagClass(hashtag_list=self.TESTEPHILO__SUBLIST, get_hash_api=API_TEST),
                                            include_rts=False)
            Philobot_Stream.filter(track=[self.TESTEPHILO_HASHTAG], is_async=True)

        except (Exception, ProtocolError, AttributeError) as call_test:
            self.log.info("[X] - ERRO AO INICIAR STREAM DE TESTE")
            self.log.info(call_test)


if __name__ == '__main__':
    StartHashtagExtension()
