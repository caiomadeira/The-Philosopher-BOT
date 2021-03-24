from Credentials.Twitter.Test import api_test
from Credentials.main_credentials_extension import api_reserva
from Credentials.Twitter.Official.main_credentials_official import api_oficial
from EnvironmentUtil.Code_Design.design import GREEN, YELLOW, RED
import time
import tweepy


def init():
    global ACCOUNT, API_SELECTED

    GREEN('[+] TWEET DELET - Philosopher Bot\n\n')

    select_api = input("[>] Qual conta deseja?\n"
                       "[1] - Oficial\n"
                       "[2] - Extension\n"
                       "[3] - Teste\n>")

    for i in range(1):
        if select_api == '1':
            API_SELECTED = api_oficial

            """
            AUTH_URL = auth_oficial.get_authorization_url()
            verify_code = input("Autenticacao %s requer codigod e verificacao > " % AUTH_URL)
            auth_oficial.get_access_token(verify_code)
            print(verify_code)
            """

            ACCOUNT = 'CONTA OFICIAL'
            YELLOW(f"\n[+] {ACCOUNT} SELECIONADA!\n")

            delet_tweets()

        elif select_api == '2':
            API_SELECTED = api_reserva

            """
            AUTH_URL = auth_reserva.get_authorization_url()
            verify_code = input("Autenticacao %s requer codigod e verificacao > " % AUTH_URL)
            auth_reserva.get_access_token(verify_code)
            print(verify_code)
            """

            ACCOUNT = 'CONTA EXTENSION'
            YELLOW(f"\n[+] {ACCOUNT} SELECIONADA!\n")
            delet_tweets()

        elif select_api == '3':
            API_SELECTED = api_test

            """
            AUTH_URL = auth_test.get_authorization_url()
            verify_code = input("Autenticacao %s requer codigod e verificacao > " % AUTH_URL)
            auth_test.get_access_token(verify_code)
            print(verify_code)
            """

            ACCOUNT = 'CONTA TESTE'
            YELLOW(f"\n[+] {ACCOUNT} SELECIONADA!\n")
            delet_tweets()

        else:
            RED('[x] Opção inválida.')
            RED('-------------------------------')
            time.sleep(0.5)
            restart_question = input("[>] Deseja escolher de novo?\n"
                                     "[1] - Sim\n"
                                     "[2] - Não\n"
                                     ">")
            if restart_question == '1':
                return init()
            elif restart_question == '2':
                break
            else:
                return init()


def delet_tweets():
    YELLOW(f'\nATENÇÃO!\nTweets da {ACCOUNT} serão deletados.\n')
    q = input("[+] Deseja continuar?\n"
              "[1] - Sim\n"
              "[2] - Nao\n"
              ">")

    if q == '1':

        YELLOW("Deletando todos os tweets da conta @%s." % API_SELECTED.verify_credentials().screen_name)
        from datetime import datetime, timedelta
        test_mode = False
        verbose = False
        delete_tweets = True
        days_to_keep = 0

        cutoff_date = datetime.utcnow() - timedelta(days=days_to_keep)

        if delete_tweets:
            # pegando todos os tweets
            print("Procurando tweets da timeline para deletar....")
            timeline = tweepy.Cursor(API_SELECTED.user_timeline).items()
            deletion_count = 0
            ignored_count = 0
            tweets_to_save = []


            for tweet in timeline:

                if tweet.id not in tweets_to_save and tweet.created_at < cutoff_date:
                    if verbose:
                        print("[+] DELETANDO %d: [%s] %s" % (tweet.id, tweet.created_at, tweet.text))
                    if not test_mode:
                        API_SELECTED.destroy_status(tweet.id)

                    deletion_count += 1
                    time.sleep(60*1)

                else:
                    ignored_count += 1

            GREEN("[+] Deletados: %d tweets, Ignorados: %d" % (deletion_count, ignored_count))

        else:
            RED("[x] Tweets NAO foram deletados")

    elif q == '2':
        RED('[X] VOLTANDO AO INICIO...\n')
        time.sleep(2)
        GREEN('-------------------------------')
        init()


if __name__ == '__main__':
    init()
