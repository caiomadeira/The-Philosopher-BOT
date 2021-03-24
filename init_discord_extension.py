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

TOKEN = os.environ.get('discord_ex_token', None)

if __name__ == '__main__':
    client.run(TOKEN)
