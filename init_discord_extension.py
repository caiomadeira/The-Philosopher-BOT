"""
Philosopher Bot
---------------
Created by Caio Madeira
Co-worker: Rodrigo Carmo

instagram: @sudomadeira
Twitter: @bot_philospher
Avaliable on Discord too!

"""
from Discord.bot import *


def ler_token_extension():
    with open(os.getenv("token_extension"), "r") as f:
        linhas = f.readlines()
        return linhas[0].strip()


TOKEN = ler_token_extension()


if __name__ == '__main__':
    client.run(TOKEN)
