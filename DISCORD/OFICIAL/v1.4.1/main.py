""""""""""""""""""""""
PHILOSOPHER BOT DISCORD 1.2
---------------
Criado por Caio Madeira (@sudomaidera)
Disponível no Discord e no Twitter!
2020

"""""""""""""""""""""""
from bot import *


def ler_token():
    with open("Credentials/token.txt", "r") as f:
        linhas = f.readlines()
        return linhas[0].strip()


TOKEN = ler_token()

if __name__ == '__main__':
    client.run(TOKEN)
