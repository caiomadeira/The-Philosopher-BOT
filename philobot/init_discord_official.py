""""""""""""""""""""""
PHILOSOPHER BOT DISCORD 1.2
---------------
Criado por Caio Madeira (@sudomaidera)
Disponível no Discord e no Twitter!
2020

"""""""""""""""""""""""
from Discord.bot import *


def ler_token():
    TOKEN_CHOICE = input("Digite qual BOT você quer iniciar: \n "
                         "[1] - DISCORD OFICIAL \n "
                         "[2] - DISCORD EXTENSION \n "
                         "[3] - DISCORD TEST \n "
                         " Digite aqui: ")

    if TOKEN_CHOICE == "1":
        with open("Credentials/token_oficial.txt", "r") as f:
            linhas = f.readlines()
            return linhas[0].strip()

    if TOKEN_CHOICE == "2":
        with open("Credentials/token_reserva.txt", "r") as f:
            linhas = f.readlines()
            return linhas[0].strip()

    if TOKEN_CHOICE == "3":
        with open("Credentials/token_teste.txt", "r") as f:
            linhas = f.readlines()
            return linhas[0].strip()


def ler_token_official():
    with open(os.getenv("token_official"), "r") as f:
        linhas = f.readlines()
        return linhas[0].strip()


TOKEN = ler_token_official()

if __name__ == '__main__':
    client.run(TOKEN)
