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
from services.analytics.Logs.Twitter.logs_hashtag.ERROR.path_log_hashtag_error import PATH_LOG_HASHTAG_ERROR
from services.analytics.Logs.Twitter.logs_hashtag.INFO.path_log_hashtag_info import PATH_LOG_HASHTAG_INFO
from services.analytics.Logs.Twitter.logs_posting.ERROR.path_log_posting_error import PATH_LOG_POST_ERROR
from services.analytics.Logs.Twitter.logs_posting.INFO.path_log_posting_info import PATH_LOG_POST_INFO
from services.analytics.Logs.Twitter.logs_general.path_log_general import PATH_LOG_GENERAL

loggers = {}


def log_philobot(name):

    if loggers.get(name):
        return loggers.get(name)

    else:

        log_bot = logging.getLogger(name)
        log_bot.setLevel(logging.DEBUG)

        formatter_bot = logging.Formatter('%(asctime)s - PHILOBOT --> %(message)s')

        file_name = datetime.date.today()

        file_handler_error = logging.FileHandler(rf'{PATH_LOG_HASHTAG_ERROR}\HASHTAG_ERROR - {file_name}.log')
        file_handler_error.setLevel(logging.ERROR)
        file_handler_error.setFormatter(formatter_bot)

        file_handler_info = logging.FileHandler(rf'{PATH_LOG_HASHTAG_INFO}\HASHTAG_INFO - {file_name}.log')
        file_handler_info.setLevel(logging.INFO)
        file_handler_info.setFormatter(formatter_bot)

        stream_handler_bot = logging.StreamHandler()
        stream_handler_bot.setFormatter(formatter_bot)

        log_bot.addHandler(file_handler_error)
        log_bot.addHandler(file_handler_info)
        log_bot.addHandler(stream_handler_bot)

        loggers[name] = log_bot

        return log_bot


def log_philomaker(name):

    if loggers.get(name):
        return loggers.get(name)

    else:

        log_maker = logging.getLogger(name)
        log_maker.setLevel(logging.DEBUG)

        formatter_maker = logging.Formatter('%(asctime)s - PHILOMAKER --> %(message)s')

        file_name = datetime.date.today()

        file_handler_error = logging.FileHandler(rf'{PATH_LOG_HASHTAG_ERROR}\HASHTAG_ERROR - {file_name}.log')
        file_handler_error.setLevel(logging.ERROR)
        file_handler_error.setFormatter(formatter_maker)

        file_handler_info = logging.FileHandler(rf'{PATH_LOG_HASHTAG_INFO}\HASHTAG_INFO - {file_name}.log')
        file_handler_info.setLevel(logging.INFO)
        file_handler_info.setFormatter(formatter_maker)

        stream_handler_maker = logging.StreamHandler()
        stream_handler_maker.setFormatter(formatter_maker)

        log_maker.addHandler(file_handler_error)
        log_maker.addHandler(file_handler_info)
        log_maker.addHandler(stream_handler_maker)

        loggers[name] = log_maker

        return log_maker


def log_general(name):

    if loggers.get(name):
        return loggers.get(name)

    else:
        log_main = logging.getLogger(name)
        log_main.setLevel(logging.DEBUG)

        formatter_main = logging.Formatter('%(asctime)s - GENERAL --> %(message)s')

        file_name = datetime.date.today()

        file_handler_info = logging.FileHandler(rf'{PATH_LOG_GENERAL}\HASHTAG_INFO - {file_name}.log')
        file_handler_info.setLevel(logging.DEBUG)
        file_handler_info.setFormatter(formatter_main)

        stream_handler_main = logging.StreamHandler()
        stream_handler_main.setFormatter(formatter_main)

        log_main.addHandler(file_handler_info)
        log_main.addHandler(stream_handler_main)

        loggers[name] = log_main

        return log_main


def log_hashtag(name):

    if loggers.get(name):
        return loggers.get(name)

    else:

        log_hash = logging.getLogger(name)
        log_hash.setLevel(logging.DEBUG)

        formatter_hash = logging.Formatter('%(asctime)s - HASHTAG --> %(message)s')

        file_name = datetime.date.today()

        file_handler_error = logging.FileHandler(rf'{PATH_LOG_HASHTAG_ERROR}\HASHTAG_ERROR - {file_name}.log')
        file_handler_error.setLevel(logging.ERROR)
        file_handler_error.setFormatter(formatter_hash)

        file_handler_info = logging.FileHandler(rf'{PATH_LOG_HASHTAG_INFO}\HASHTAG_INFO - {file_name}.log')
        file_handler_info.setLevel(logging.INFO)
        file_handler_info.setFormatter(formatter_hash)

        stream_handler_hash = logging.StreamHandler()
        stream_handler_hash.setFormatter(formatter_hash)

        log_hash.addHandler(file_handler_error)
        log_hash.addHandler(file_handler_info)
        log_hash.addHandler(stream_handler_hash)

        loggers[name] = log_hash

        return log_hash


def log_posting(name):

    if loggers.get(name):
        return loggers.get(name)

    else:

        log_post = logging.getLogger(name)
        log_post.setLevel(logging.DEBUG)

        formatter_hash = logging.Formatter('%(asctime)s - POSTING --> %(message)s')

        file_name = datetime.date.today()

        file_handler_error = logging.FileHandler(rf'{PATH_LOG_POST_ERROR}\HASHTAG_ERROR - {file_name}.log')
        file_handler_error.setLevel(logging.ERROR)
        file_handler_error.setFormatter(formatter_hash)

        file_handler_info = logging.FileHandler(rf'{PATH_LOG_POST_INFO}\HASHTAG_INFO - {file_name}.log')
        file_handler_info.setLevel(logging.INFO)
        file_handler_info.setFormatter(formatter_hash)

        stream_handler_hash = logging.StreamHandler()
        stream_handler_hash.setFormatter(formatter_hash)

        log_post.addHandler(file_handler_error)
        log_post.addHandler(file_handler_info)
        log_post.addHandler(stream_handler_hash)

        loggers[name] = log_post

        return log_post
