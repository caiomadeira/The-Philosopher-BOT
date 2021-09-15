import logging
from logging.handlers import TimedRotatingFileHandler
from Logs.Twitter.logs_hashtag.INFO.path_log_hashtag_info import PATH_LOG_HASHTAG_INFO


# class LogEngine:
#
#     def __init__(self, name, file_date):
#         self.loggers = {}
#         self.name = name
#         self.file_date = file_date
#
#     def log_hashtag(self):
#
#         if self.loggers.get(self.name):
#             return self.loggers.get(self.name)
#
#         else:
#
#             log_hash = logging.getLogger(self.name)
#             log_hash.setLevel(logging.INFO)
#
#             formatter_bot = logging.Formatter('%(asctime)s - %(levelname)s - HASHTAG --> %(message)s')
#
#             # file_handler_info = TimedRotatingFileHandler(rf'{PATH_LOG_HASHTAG_INFO}\HASHTAG.log', when='d', interval=1)
#             file_handler_info = logging.FileHandler(rf'{PATH_LOG_HASHTAG_INFO}\HASHTAG_{self.file_date}.log')
#             file_handler_info.setLevel(logging.DEBUG)
#             file_handler_info.setFormatter(formatter_bot)
#
#             stream_handler_bot = logging.StreamHandler()
#             stream_handler_bot.setFormatter(formatter_bot)
#
#             log_hash.addHandler(file_handler_info)
#             log_hash.addHandler(stream_handler_bot)
#
#             self.loggers[self.name] = log_hash
#
#             return log_hash

loggers = {}


def log_hashtag(name, file_date):

    if loggers.get(name):
        return loggers.get(name)

    else:

        log_hash = logging.getLogger(name)
        log_hash.setLevel(logging.INFO)

        formatter_bot = logging.Formatter('%(asctime)s - %(levelname)s - HASHTAG --> %(message)s')

        # file_handler_info = TimedRotatingFileHandler(rf'{PATH_LOG_HASHTAG_INFO}\HASHTAG.log', when='d', interval=1)
        file_handler_info = logging.FileHandler(rf'{PATH_LOG_HASHTAG_INFO}\HASHTAG_{file_date}.log')
        file_handler_info.setLevel(logging.DEBUG)
        file_handler_info.setFormatter(formatter_bot)

        stream_handler_bot = logging.StreamHandler()
        stream_handler_bot.setFormatter(formatter_bot)

        log_hash.addHandler(file_handler_info)
        log_hash.addHandler(stream_handler_bot)

        loggers[name] = log_hash

        return log_hash
