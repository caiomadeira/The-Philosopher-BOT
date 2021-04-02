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
from Logs.Twitter.logger_hashtag import log_hashtag


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
        self.log = log_hashtag(__name__)
        self.start_hashtag_extension()

    def start_hashtag_extension(self):
        self.log.info("Bem-vindo!\n")
        self.log.info("Philosopher BOT por Caio Madeira e Rodrigo Carmo\n")
        self.log.info(">INICIANDO HASHTAG - EXTENSION<")

        from Hashtag.hashtag import HashtagClass


        self.log.info('HASHTAG EXTENSION ESCOLHIDA, INICIANDO #PHILOBOT E #PHILOMAKER...')

        # from Credentials.Extension.main_credentials_extension import API_MAIN_EXTENSION as api_reserva
        # from Credentials.Extension.main_credentials_extension import API_MAIN_EXTENSION as api_reserva
        from Credentials.Twitter.credentials import API_HASHTAG_EXTENSION as api_reserva
        # from Credentials.Official.posting_credentials_official import API_POSTING_OFFICIAL as api_reserva

        try:

            Philobot_Stream = tweepy.Stream(auth=api_reserva.auth,
                                            listener=HashtagClass(self.PHILOBOT__SUBLIST, api_reserva),
                                            include_rts=False)
            Philobot_Stream.filter(track=['#Philobot'], is_async=True)
            """
            # TESTEMAKER
            Philobot_Stream = tweepy.Stream(auth=api_reserva.auth,
                                            listener=HashtagClass(self.PHILOMAKER_SUBLIST, api_reserva),
                                            include_rts=False)
            Philobot_Stream.filter(track=['#Philomaker'], is_async=True)
            """

        except Exception as stream:
            self.log.error('ERRO AO INICIAR O STREAM COM A API DO TWITTER')
            self.log.error(stream)


if __name__ == '__main__':
    StartHashtagExtension()
