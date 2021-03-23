"""
Philosopher Bot
---------------
Created by Caio Madeira
Co-worker: Rodrigo Carmo

instagram: @sudomadeira
Twitter: @bot_philospher
Avaliable on Discord too!

"""
from Lists.Account_List.account_path_reference import ACCOUNT_PATH

with open(f'{ACCOUNT_PATH}/accounts.txt', 'r') as f:
    accounts_list = [line.strip() for line in f]


