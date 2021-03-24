""""""""""""""""""""""
PHILOSOPHER BOT DISCORD 1.2
---------------
Criado por Caio Madeira (@sudomaidera)
Disponível no Discord e no Twitter!
2020

"""""""""""""""""""""""
from Discord.bot import *


def ler_token_extension():
    with open(os.getenv("token_extension"), "r") as f:
        linhas = f.readlines()
        return linhas[0].strip()


TOKEN = ler_token_extension()


if __name__ == '__main__':
    client.run(TOKEN)
