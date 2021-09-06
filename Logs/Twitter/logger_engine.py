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
import datetime
from Logs.Twitter.logs_hashtag.INFO.path_log_hashtag_info import PATH_LOG_HASHTAG_INFO
from Logs.Twitter.logs_posting.INFO.path_log_posting_info import PATH_LOG_POST_INFO

loggers = {}


def log_philobot(name):

    if loggers.get(name):
        return loggers.get(name)

    else:

        log_bot = logging.getLogger(name)
        log_bot.setLevel(logging.DEBUG)

        formatter_bot = logging.Formatter('%(asctime)s - %(levelname)s - HASHTAG --> %(message)s')

        file_name = datetime.date.today()

        file_handler_info = logging.FileHandler(rf'{PATH_LOG_HASHTAG_INFO}\HASHTAG - {file_name}.log')
        file_handler_info.setLevel(logging.DEBUG)
        file_handler_info.setFormatter(formatter_bot)

        stream_handler_bot = logging.StreamHandler()
        stream_handler_bot.setFormatter(formatter_bot)

        log_bot.addHandler(file_handler_info)
        log_bot.addHandler(stream_handler_bot)

        loggers[name] = log_bot

        return log_bot


def log_posting(name):

    if loggers.get(name):
        return loggers.get(name)

    else:

        log_post = logging.getLogger(name)
        log_post.setLevel(logging.DEBUG)

        formatter_hash = logging.Formatter('%(asctime)s  - %(levelname)s - POSTING --> %(message)s')

        file_name = datetime.date.today()

        file_handler_info = logging.FileHandler(rf'{PATH_LOG_POST_INFO}\POSTING - {file_name}.log')
        file_handler_info.setLevel(logging.DEBUG)
        file_handler_info.setFormatter(formatter_hash)

        stream_handler_hash = logging.StreamHandler()
        stream_handler_hash.setFormatter(formatter_hash)

        log_post.addHandler(file_handler_info)
        log_post.addHandler(stream_handler_hash)

        loggers[name] = log_post

        return log_post
