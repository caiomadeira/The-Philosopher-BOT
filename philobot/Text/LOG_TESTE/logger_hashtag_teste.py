import logging
import datetime
from TDD.LOG_TESTE.LOGS_TESTE.ERROR_LOGS.path_log_hashtag_teste_error import PATH_LOG_HASHTAG_TESTE_ERROR
from TDD.LOG_TESTE.LOGS_TESTE.INFO_LOGS.path_log_hashtag_teste_info import PATH_LOG_HASHTAG_TESTE_INFO

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(message)s')

file_name = datetime.date.today()

file_handler_error = logging.FileHandler(rf'{PATH_LOG_HASHTAG_TESTE_ERROR}\HASHTAG_ERROR - {file_name}.log')
file_handler_error.setLevel(logging.ERROR)
file_handler_error.setFormatter(formatter)

file_handler_info = logging.FileHandler(rf'{PATH_LOG_HASHTAG_TESTE_INFO}\HASHTAG_INFO - {file_name}.log')
file_handler_info.setLevel(logging.INFO)
file_handler_info.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

log.addHandler(file_handler_error)
log.addHandler(file_handler_info)
log.addHandler(stream_handler)
