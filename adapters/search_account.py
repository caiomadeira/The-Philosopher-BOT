"""
Philosopher Bot
---------------
Created by Caio Madeira
Co-worker: Rodrigo Carmo

Twitter: @bot_philospher
Avaliable on Discord too!
"""

from resources.localizable.accounts.path import path

with open(f'{path}/usernames.txt', 'r') as f:
    accounts_list = [line.strip() for line in f]


