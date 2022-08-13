import logging
import datetime
from logging.handlers import TimedRotatingFileHandler
from Logs.Twitter.logs_hashtag.INFO.path_log_hashtag_info import PATH_LOG_HASHTAG_INFO
from Logs.Twitter.logs_posting.INFO.path_log_posting_info import PATH_LOG_POST_INFO


class LogEngine:

    def __init__(self, name):
        self.loggers = {}
        self.name = name

    def log_hashtag(self):

        if self.loggers.get(self.name):
            return self.loggers.get(self.name)

        else:

            log_hash = logging.getLogger(self.name)
            log_hash.setLevel(logging.INFO)

            formatter_bot = logging.Formatter('%(asctime)s - %(levelname)s - HASHTAG --> %(message)s')

            file_handler_info = TimedRotatingFileHandler(rf'{PATH_LOG_HASHTAG_INFO}\HASHTAG.log', when='midnight', interval=1, encoding='utf8')
            file_handler_info.setLevel(logging.DEBUG)
            file_handler_info.setFormatter(formatter_bot)

            stream_handler_bot = logging.StreamHandler()
            stream_handler_bot.setFormatter(formatter_bot)

            log_hash.addHandler(file_handler_info)
            log_hash.addHandler(stream_handler_bot)

            self.loggers[self.name] = log_hash

            return log_hash

    def log_posting(self):

        if self.loggers.get(self.name):
            return self.loggers.get(self.name)

        else:

            log_post = logging.getLogger(self.name)
            log_post.setLevel(logging.INFO)

            formatter_bot = logging.Formatter('%(asctime)s - %(levelname)s - POSTING --> %(message)s')

            file_handler_info = TimedRotatingFileHandler(rf'{PATH_LOG_POST_INFO}\POSTING.log', when='d', interval=1, encoding='utf8')
            file_handler_info.setLevel(logging.DEBUG)
            file_handler_info.setFormatter(formatter_bot)

            stream_handler_bot = logging.StreamHandler()
            stream_handler_bot.setFormatter(formatter_bot)

            log_post.addHandler(file_handler_info)
            log_post.addHandler(stream_handler_bot)

            self.loggers[self.name] = log_post

            return log_post
# loggers = {}
#
#
# def log_hashtag(name):
#
#     if loggers.get(name):
#         return loggers.get(name)
#
#     else:
#
#         log_hash = logging.getLogger(name)
#         log_hash.setLevel(logging.INFO)
#
#         formatter_bot = logging.Formatter('%(asctime)s - %(levelname)s - HASHTAG --> %(message)s')
#
#         file_handler_info = TimedRotatingFileHandler(rf'{PATH_LOG_HASHTAG_INFO}\HASHTAG.log', when='d', interval=1)
#         # file_handler_info = logging.FileHandler(rf'{PATH_LOG_HASHTAG_INFO}\HASHTAG_{datetime.date.today()}.log')
#         file_handler_info.setLevel(logging.DEBUG)
#         file_handler_info.setFormatter(formatter_bot)
#
#         stream_handler_bot = logging.StreamHandler()
#         stream_handler_bot.setFormatter(formatter_bot)
#
#         log_hash.addHandler(file_handler_info)
#         log_hash.addHandler(stream_handler_bot)
#
#         loggers[name] = log_hash
#
#         return log_hash
