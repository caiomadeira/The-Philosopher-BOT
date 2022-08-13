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
from Logs.Twitter.logs_hashtag.INFO.path_log_hashtag_info import PATH_LOG_HASHTAG_INFO

loggers = {}


def log_hashtag(name):

    if loggers.get(name):
        return loggers.get(name)

    else:

        log_bot = logging.getLogger(name)
        log_bot.setLevel(logging.INFO)

        formatter_bot = logging.Formatter('%(asctime)s - %(levelname)s - HASHTAG --> %(message)s')

        file_handler_info = TimedRotatingFileHandler(rf'{PATH_LOG_HASHTAG_INFO}\HASHTAG', 'midnight', 1)
        file_handler_info.setLevel(logging.DEBUG)
        file_handler_info.setFormatter(formatter_bot)

        stream_handler_bot = logging.StreamHandler()
        stream_handler_bot.setFormatter(formatter_bot)

        log_bot.addHandler(file_handler_info)
        log_bot.addHandler(stream_handler_bot)

        loggers[name] = log_bot

        return log_bot
