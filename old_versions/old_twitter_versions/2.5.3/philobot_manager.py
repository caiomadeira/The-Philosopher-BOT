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
from Credentials.credentials_verify_test import api_test as api_teste
from Credentials.credentials_verify_oficial import api_oficial as api_oficial
from Credentials.credentials_verify_reserva import api_reserva as api_extension
from art import tprint

__version__ = 1.0

oficial_account = api_oficial

test_account = api_teste

extension_account = api_extension


def instructions():
    tprint("Philosopher Bot - Manager")
    print(f"Versão: {__version__}")
    print("Número de Seguidores - [Aperte 1]\n")
    print("Ver Tweets Públicos de Contas do PhiloBot (Teste, Oficial e Extension - [Aperte 2]\n")
    print("Listar Seguidores da conta por nome - [Aperte 3]\n")
    print("Postar um status (Texto apenas) - [Aperte 4]\n")
    print("Ultimos tweets com #PhiloBot - [Aperte 5]\n")
    print("Atualizar Status da aplicação - [Aperte 6]\n")
    print("Ver LOGINS - [Aperte 7]\n")

    choose_func = input("Digite aqui:")
    if choose_func == "1":
        followers_count_func()
    if choose_func == "2":
        see_public_tweets()
    if choose_func == "3":
        followers_names()
    if choose_func == "4":
        posting_status()
    if choose_func == "5":
        search_philobot()
    if choose_func == "6":
        status_service_post()
    if choose_func == "7":
        info_accounts()


def info_accounts():
    question = input("Digite [1] para ver os logins do TWITTER: \nDigite [2] para ver os logins do HEROKU:")

    if question == "1":
        f = open(f"Data/twitter_accounts_logins.txt", "r")
        print(f.read())
    if question == "2":
        f = open(f"Data/heroku_accounts_logins.txt", "r")
        print(f.read())
    else:
        retornar_question()


def status_service_post():
    question = input(" [1] - Oficial \n [2] - Extension \n [3] - Teste \n Digite aqui:")

    status_off = "STATUS DA APLICAÇÃO: OFFLINE. \n Em breve ela volta :)"
    status_on = "STATUS DA APLICAÇÃO: ONLINE. \n"

    if question == "1":
        print("CONTA ESCOLHIDA: OFICIAL (@bot_philosopher)")
        print("Aguarde...")

        print("[1] - STATUS ONLINE \n[2] - STATUS OFFLINE")
        service = input("Digite o status da aplicação para ser postado:")
        if service == "1":
            status_post = oficial_account.update_status(status_on)
            print("Status Service atualizado:")
            print(status_post.text)
        if service == "2":
            status_post = oficial_account.update_status(status_off)
            print("Status Service atualizado:")
            print(status_post.text)

    if question == "2":
        print("CONTA ESCOLHIDA: EXTENSION (@philo_extension)")
        print("Aguarde...")

        print("[1] - STATUS ONLINE \n[2] - STATUS OFFLINE")
        service = input("Digite o status da aplicação para ser postado:")
        if service == "1":
            status_post = extension_account.update_status(status_on)
            print("Status Service atualizado:")
            print(status_post.text)
        if service == "2":
            status_post = extension_account.update_status(status_off)
            print("Status Service atualizado:")
            print(status_post.text)

    if question == "3":
        print("CONTA ESCOLHIDA: OFICIAL (@TestePhiloBot)")
        print("Aguarde...")

        print("[1] - STATUS ONLINE \n[2] - STATUS OFFLINE")
        service = input("Digite o status da aplicação para ser postado:")
        if service == "1":
            status_post = test_account.update_status(status_on)
            print("Status Service atualizado:")
            print(status_post.text)
        if service == "2":
            status_post = test_account.update_status(status_off)
            print("Status Service atualizado:")
            print(status_post.text)
    retornar_question()


def search_philobot():
    word = '#PhiloBot'

    for tweet in tweepy.Cursor(api_teste.search, q=word).items(10):
        print(tweet.text)

    retornar_question()


def posting_status():
    question = input(" [1] - Oficial \n [2] - Extension \n [3] - Teste \n Digite aqui:")

    if question == "1":
        print("CONTA ESCOLHIDA: OFICIAL (@bot_philosopher)")
        print("Aguarde...")
        status_write = input("Digite o status:")

        status_post = oficial_account.update_status(status_write)
        print("Status postando:")
        print(status_post.text)

    if question == "2":
        print("CONTA ESCOLHIDA: EXTENSION (@philo_extension)")
        print("Aguarde...")
        status_write = input("Digite o status:")

        status_post = extension_account.update_status(status_write)
        print("Status postando:")
        print(status_post.text)

    if question == "3":
        print("CONTA ESCOLHIDA: OFICIAL (@TestePhiloBot)")
        print("Aguarde...")
        status_write = input("Digite o status:")

        status_post = test_account.update_status(status_write)
        print("Status postando:")
        print(status_post.text)

    retornar_question()


def followers_names():
    question = input(" [1] - Oficial \n [2] - Extension \n [3] - Teste \n Digite aqui:")

    if question == "1":
        account = '@bot_philosopher'

        user = api_oficial.get_user(account)

        print(f"Nome de usuário:{user.screen_name}\n")
        print(f"Numero de Seguidores: {user.followers_count} seguidores\n")
        print(f"Usuários que {account} segue:")
        for friend in user.friends():
            print(friend.screen_name)

    if question == "2":
        account = '@philo_extension'

        user = api_extension.get_user(account)

        print(f"Nome de usuário:{user.screen_name}\n")
        print(f"Numero de Seguidores: {user.followers_count} seguidores\n")
        print(f"Usuários que {account} segue:")
        for friend in user.friends():
            print(friend.screen_name)

    if question == "3":
        account = '@TestePhilobot'

        user = api_teste.get_user(account)

        print(f"Nome de usuário:{user.screen_name}\n")
        print(f"Numero de Seguidores: {user.followers_count} seguidores\n")
        print(f"Usuários que {account} segue:")
        for friend in user.friends():
            print(friend.screen_name)

    retornar_question()


def see_public_tweets():
    question = input("Qual conta você deseja ver os Tweets Públicos?\n [1] - Oficial \n [2] - Extension \n [3] - "
                     "Teste \n Digite aqui:")

    if question == "1":
        public_tweets_oficial = oficial_account.home_timeline()
        print("CONTA ESCOLHIDA: OFICIAL (@bot_philosopher)")
        print("Aguarde...")
        for tweet in public_tweets_oficial:
            print(f"{tweet.text}\n")
            print("===========================")

    if question == "2":
        public_tweets_extension = extension_account.home_timeline()
        print("CONTA ESCOLHIDA: EXTENSION (@philo_extension)")
        print("Aguarde...")
        for tweet in public_tweets_extension:
            print(f"{tweet.text}\n")
            print("===========================")

    if question == "3":
        public_tweets_test = test_account.home_timeline()
        print("CONTA ESCOLHIDA: OFICIAL (@TestePhiloBot)")
        print("Aguarde...")
        for tweet in public_tweets_test:
            print(f"{tweet.text}\n")
            print("===========================")

    retornar_question()


def followers_count_func():
    question = input("Deseja continuar com a operação? Sim ou Não.")
    if question == 'Sim' or 'sim':
        ids = []
        screen_input = input("Digite o nome de usuário que deseja:")
        for page in tweepy.Cursor(api_teste.followers_ids, screen_name=screen_input).pages():  # numero de seguidores
            ids.extend(page)

        print(f"Usuário {screen_input}")
        print(f"Número de Seguidores: {len(ids)}")

    elif question == 'Não' or 'não' or 'nao' or 'Nao':
        return instructions()


def retornar_question():
    print("\nDeseja retornar para o inicio?\n")
    question = input("Sim ou não?")

    if question == 'Sim' or 'sim':
        return instructions()

    else:
        print("Finalizando programa")
        pass


