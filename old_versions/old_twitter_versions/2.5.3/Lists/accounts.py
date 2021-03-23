"""
Philosopher Bot
---------------
Created by Caio Madeira
Co-worker: Rodrigo Carmo

instagram: @sudomadeira
Twitter: @bot_philospher
Avaliable on Discord too!

"""
from Data.reference_path import DATA_PATH

with open(f'{DATA_PATH}/accounts.txt', 'r') as f:
    contas_list = [line.strip() for line in f]
    print(contas_list)


