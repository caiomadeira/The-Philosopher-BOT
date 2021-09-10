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
from Logs.Twitter.logs_posting.INFO.path_log_posting_info import PATH_LOG_POST_INFO


log_post = logging.getLogger()
log_post.setLevel(logging.INFO)

formatter_post = logging.Formatter('%(asctime)s  - %(levelname)s - POSTING --> %(message)s')

file_handler_info = TimedRotatingFileHandler(rf'{PATH_LOG_POST_INFO}\POSTING', 'midnight', 1)
file_handler_info.setLevel(logging.DEBUG)
file_handler_info.setFormatter(formatter_post)

stream_handler_post = logging.StreamHandler()
stream_handler_post.setFormatter(formatter_post)

log_post.addHandler(file_handler_info)
