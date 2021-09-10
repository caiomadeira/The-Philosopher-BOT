import logging
import datetime
import os
from dotenv import load_dotenv
from logging.handlers import TimedRotatingFileHandler

load_dotenv()
log_path = os.getenv('log_app_path')[1:].strip('"')

log = logging.getLogger()
log.setLevel(logging.DEBUG)

formatter_log_watch =logging.Formatter('%(asctime)s - PHILOWATCH --> %(message)s')

file_name = datetime.date.today()

# file_handler = logging.FileHandler(fr"{log_path}\PHILOWATCH LOG - {file_name}.log")
file_handler = TimedRotatingFileHandler(fr"{log_path}\PHILOWATCH LOG - {file_name}.log", when="midnight", interval=1)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter_log_watch)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter_log_watch)

log.addHandler(file_handler)
log.addHandler(stream_handler)

