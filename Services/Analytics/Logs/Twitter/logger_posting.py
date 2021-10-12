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
from services.analytics.Logs.Twitter.logs_posting.ERROR.path_log_posting_error import PATH_LOG_POST_ERROR
from services.analytics.Logs.Twitter.logs_posting.INFO.path_log_posting_info import PATH_LOG_POST_INFO

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(message)s')

file_name = datetime.date.today()

file_handler_error = logging.FileHandler(rf'{PATH_LOG_POST_ERROR}\HASHTAG_ERROR - {file_name}.log')
file_handler_error.setLevel(logging.ERROR)
file_handler_error.setFormatter(formatter)

file_handler_info = logging.FileHandler(rf'{PATH_LOG_POST_INFO}\HASHTAG_INFO - {file_name}.log')
file_handler_info.setLevel(logging.INFO)
file_handler_info.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(formatter)

log.addHandler(file_handler_error)
log.addHandler(file_handler_info)
log.addHandler(stream_handler)
