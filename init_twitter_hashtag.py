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
from Logs.Twitter.logger_engine import log_philobot
from urllib3.exceptions import ProtocolError


class StartHashtagExtension:

    def __init__(self):

        get_config = Config()
        """ =========== HASHTAGS =========== """
        self.PHILOBOT_HASHTAG = get_config.PHILOBOT__HASHTAG
        self.PHILOMAKER_HASHTAG = get_config.PHILOMAKER__HASHTAG

        """ =========== SUBLIST =========== """
        self.PHILOBOT__SUBLIST = get_config.PHILOBOT__SUBLIST
        self.PHILOMAKER_SUBLIST = get_config.PHILOMAKER__SUBLIST

        self.TESTEPHILO__SUBLIST = get_config.TESTEPHILO__SUBLIST
        self.TESTMAKER_SUBLIST = get_config.TESTMAKER__SUBLIST

        """=========== SET LOG ==========="""
        self.log = log_philobot(__name__)
        self.start_hashtag_extension()

    def start_hashtag_extension(self):
        self.log.info("Bem-vindo!\n")
        self.log.info("Philosopher BOT por Caio Madeira e Rodrigo Carmo\n")
        self.log.info(">INICIANDO HASHTAG - EXTENSION<")

        from Twitter.Hashtag.hashtag import HashtagClass
        from Credentials.Twitter.Extension.hashtag_credentials_extension import API_HASHTAG_EXTENSION as api_reserva

        try:
            Philobot_Stream = tweepy.Stream(auth=api_reserva.auth,
                                            listener=HashtagClass(self.PHILOBOT__SUBLIST, api_reserva),
                                            include_rts=False)
            Philobot_Stream.filter(track=[self.PHILOBOT_HASHTAG], is_async=True)

        except (Exception, ProtocolError, AttributeError) as stream:
            self.log.error('[X] - ERRO AO INICIAR O STREAM COM A API DO TWITTER')
            self.log.error(stream)


if __name__ == '__main__':
    StartHashtagExtension()
