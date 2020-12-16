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
from config import HASHTAG_CHOICE, POSTING_CHOICE
from termcolor import colored



def hash_or_posting():
    print("Bem-vindo!\n")
    print("Philosopher BOT por Caio Madeira e Rodrigo Carmo\n")
    print(colored("Para acessar o PhiloBot Manager digite [1]\n", "green"))
    time.sleep(2)
    print("Escolha qual script função rodar: HASHTAG OU POSTING\n")
    question = input("Digite 'HASHTAG' para executar a Hashtag\nDigite 'POSTING' para executar o Posting\n")

    if question == HASHTAG_CHOICE.lower().upper():
        try:
            from Hashtag.hashtag import starting_hashtag
            starting_hashtag()

        except tweepy.error.TweepError as e:
            print(e)
            time.sleep(2)

    elif question == POSTING_CHOICE.lower().upper():
        try:
            from Posting.posting import choose_account
            choose_account()
        except tweepy.error.TweepError as e:
            print(e)
            time.sleep(2)

    elif question == '1':
        try:
            from philobot_manager import instructions
            instructions()
        except Exception as e:
            print(e)
            time.sleep(2)

    else:
        print("Comando não registrado.\n")
        print("Deseja encerrar?\n")
        question_2 = input("Digite [1] para NÃO \nDigite [2] para SIM\n")
        if question_2 == '1':
            print("\nRetornando ao inicio...\n")
            return hash_or_posting()
        elif question_2 == '2':
            print("Finalizando...")
            quit()


if __name__ == '__main__':
    hash_or_posting()
