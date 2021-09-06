"""
Philosopher Bot
---------------
Created by Caio Madeira
Co-worker: Rodrigo Carmo

instagram: @sudomadeira
Twitter: @bot_philospher
Avaliable on Discord too!

"""
# -*- coding: utf-8 -*-
import time
import tweepy
from termcolor import colored
import schedule
from config import *
from Logs.Twitter.logger_engine import log_general
from Twitter.Posting.posting import PostingClass
from urllib3.exceptions import ProtocolError


class HashtagOrPosting:

    def __init__(self):

        get_config = Config()
        """ =========== HASHTAGS =========== """
        self.PHILOBOT_HASHTAG = get_config.PHILOBOT__HASHTAG
        self.TESTEPHILO_HASHTAG = get_config.TESTEPHILO__HASHTAG
        self.PHILOMAKER_HASHTAG = get_config.PHILOMAKER__HASHTAG
        self.TESTEMAKER_HASHTAG = get_config.TESTEMAKER__HASHTAG

        """ =========== POSTING TIME =========== """
        self.OFFICIAL_POST_TIME = get_config.OFFICIAL_TIME_POST
        self.EXTENSION_POST_TIME = get_config.EXTENSION_TIME_POST
        self.TEST_POST_TIME = get_config.TEST_TIME_POST

        """ =========== SUBLIST =========== """
        self.PHILOBOT__SUBLIST = get_config.PHILOBOT__SUBLIST
        self.TESTEPHILO__SUBLIST = get_config.TESTEPHILO__SUBLIST
        self.TESTMAKER_SUBLIST = get_config.TESTMAKER__SUBLIST

        """=========== SET LOG ==========="""
        self.log = log_general(__name__)

    def hash_or_posting(self):
        self.log.info("Bem-vindo!\n")
        self.log.info("Philosopher BOT por Caio Madeira e Rodrigo Carmo\n")
        self.log.info(colored("Para acessar o PhiloBot Manager digite [1]\n", "green"))
        self.log.info("Escolha qual script função rodar: HASHTAG OU POSTING\n")
        question = input("Digite 'HASHTAG' para executar a Hashtag\nDigite 'POSTING' para executar o Posting\n")

        from Twitter.Hashtag.hashtag import HashtagClass
        if question.upper() == 'HASHTAG':
            try:
                self.log.info('Qual HASHTAG voce deseja iniciar?')
                self.log.info('[ 1 ] - HASHTAG OFICIAL')
                self.log.info('[ 2 ] - HASHTAG EXTENSION')
                self.log.info('[ 3 ] - HASHTAG DE TESTE')

                get_hash = input('Digite o numero da sua escolha:\n')

                '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

                                             O F I C I A L - HASHTAG

                '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

                if get_hash == '1':
                    self.log.info('HASHTAG OFICIAL ESCOLHIDA, INICIANDO #PHILOBOT...')

                    from Credentials.Twitter.Official import API_HASHTAG_OFFICIAL as api_oficial

                    # TESTEPHILO
                    while True:
                        try:
                            Philobot_Stream = tweepy.Stream(auth=api_oficial.auth,
                                                            listener=HashtagClass(self.TESTEPHILO__SUBLIST, api_oficial),
                                                            include_rts=False)
                            Philobot_Stream.filter(track=[self.PHILOBOT_HASHTAG], is_async=True)
                        except (Exception, ProtocolError, AttributeError) as call_official:
                            self.log.error("[X] - ERRO AO INICIAR STREAM OFICIAL")
                            self.log.error(call_official)
                            continue
                    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

                                                E X T E N S I O N - HASHTAG

                    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

                elif get_hash == '2':
                    self.log.info('HASHTAG EXTENSION ESCOLHIDA, INICIANDO #PHILOBOT...')

                    from Credentials.Twitter.Extension.hashtag_credentials_extension import API_HASHTAG_EXTENSION as api_reserva

                    # TESTEPHILO
                    while True:
                        try:
                            Philobot_Stream = tweepy.Stream(auth=api_reserva.auth,
                                                            listener=HashtagClass(self.TESTEPHILO__SUBLIST, api_reserva),
                                                            include_rts=False)
                            Philobot_Stream.filter(track=[self.PHILOBOT_HASHTAG], is_async=True)

                        except (Exception, ProtocolError, AttributeError) as call_ext:
                            self.log.info("[X] - ERRO AO INICIAR STREAM EXTENSION")
                            self.log.info(call_ext)
                            continue

                    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                                                        
                                                        T E S T E - HASHTAG
    
                    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

                elif get_hash == '3':
                    self.log.info(
                        f'HASHTAG TESTE ESCOLHIDA, INICIANDO {self.TESTEPHILO_HASHTAG} e {self.TESTEMAKER_HASHTAG}...\n')

                    from Credentials.Twitter.Test.test_credentials import API_TEST
                    from Twitter.Hashtag.hashtag import HashtagClass

                    # TESTEPHILO
                    while True:
                        try:
                            Philobot_Stream = tweepy.Stream(auth=API_TEST.auth,
                                                            listener=HashtagClass(hashtag_list=self.TESTEPHILO__SUBLIST, get_hash_api=API_TEST),
                                                            include_rts=False)
                            Philobot_Stream.filter(track=[self.TESTEPHILO_HASHTAG], is_async=True)

                        except (Exception, ProtocolError, AttributeError) as call_test:
                            self.log.error("[X] - ERRO AO INICIAR STREAM DE TESTE")
                            self.log.error(call_test)
                            continue

                else:
                    self.log.info('OPÇÃO INVÁLIDA')
                    return get_hash

            except tweepy.error.TweepError as e:
                self.log.exception(e)
                time.sleep(2)

        elif question.upper() == 'POSTING':
            TOKEN_CHOICE = '3'
            # ORIGINAL ACCOUNT
            if TOKEN_CHOICE == '1':
                from Credentials.Twitter.Test.test_credentials import API_TEST

                self.log.info(f"\nPOSTS DEFINIDOS PARA A CADA {self.OFFICIAL_POST_TIME} HORAS EM 'config.py'\n")

                schedule.every(self.OFFICIAL_POST_TIME).hours.do(PostingClass(API_TEST))
                while True:
                    schedule.run_pending()
                    time.sleep(1)

            # EXTENSION ACCOUNT
            if TOKEN_CHOICE == '2':
                from Credentials.Twitter.Extension.hashtag_credentials_extension import AUTH_HASHTAG_EXTENSION
                self.log.info("============ A V I S O ================")
                question = input("Você selecionou a conta EXTENSION, ela não constuma a fazer postagens. \n Se "
                                 "tem certeza que deseja continuar digite [1] \n Se quiser voltar para o menu, digite [2]\n")

                if question == "1":
                    self.log.info(f"\nPOSTS DEFINIDOS PARA A CADA {self.EXTENSION_POST_TIME} HORAS EM 'config.py'\n")
                    self.log.info("==================================")
                    time.sleep(2)
                    schedule.every(self.EXTENSION_POST_TIME).seconds.do(PostingClass(AUTH_HASHTAG_EXTENSION))

                    while True:
                        schedule.run_pending()
                        time.sleep(1)

                if question == "2":
                    self.log.info("Voltando...")
                    self.log.info("=============================")
                    return TOKEN_CHOICE

            # TEST ACCOUNT
            if TOKEN_CHOICE == '3':
                from Credentials.Twitter.Test.test_credentials import API_TEST

                start_posting = PostingClass(API_TEST)

                self.log.info(f"POSTS DEFINIDOS PARA A CADA {self.TEST_POST_TIME} SEGUNDOS EM 'config.py'\n")
                time.sleep(1)
                PostingClass.timer(start_posting, USE_TEST_POST=self.TEST_POST_TIME)

"""        elif question == '1':
            try:
                from EnvironmentUtil.philobot_manager import instructions
                instructions()
            except Exception as e:
                self.log.exception(e)
                time.sleep(2)

        else:
            self.log.info("Comando não registrado.\n")
            self.log.info("Deseja encerrar?\n")
            question_2 = input("Digite [1] para NÃO \nDigite [2] para SIM\n")
            if question_2 == '1':
                self.log.info("\nRetornando ao inicio...\n")
                return HashtagOrPosting()
            elif question_2 == '2':
                self.log.info("Finalizando...")
                quit()
"""

if __name__ == '__main__':
    start_app = HashtagOrPosting()
    start_app.hash_or_posting()
