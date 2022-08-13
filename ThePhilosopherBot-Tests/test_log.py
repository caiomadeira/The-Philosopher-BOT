"""
Philosopher Bot
---------------
Created by Caio Madeira
Co-worker: Rodrigo Carmo

instagram: @sudomadeira
Twitter: @bot_philospher
Avaliable on Discord too!
"""
import logging
from logging.handlers import TimedRotatingFileHandler
from Test.log_test.path_log_test import PATH_LOG_TEST


log_bot = logging.getLogger()
log_bot.setLevel(logging.INFO)

formatter_bot = logging.Formatter('%(asctime)s - %(levelname)s - TEST --> %(message)s')

file_handler_info = TimedRotatingFileHandler(rf'{PATH_LOG_TEST}\TEST', 'midnight', 1)
file_handler_info.setLevel(logging.DEBUG)
file_handler_info.setFormatter(formatter_bot)

stream_handler_bot = logging.StreamHandler()
stream_handler_bot.setFormatter(formatter_bot)

log_bot.addHandler(file_handler_info)
log_bot.addHandler(stream_handler_bot)
