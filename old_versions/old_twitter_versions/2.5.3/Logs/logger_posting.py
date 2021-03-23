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
from Logs.logs_posting.path_log_posting import PATH_LOG_POST

log_time = datetime.date.today()
FILENAME = f"\POSTING_LOG--{log_time}.txt"

log_format = "%(asctime)s - %(message)s"
logging.basicConfig(filename=rf"{PATH_LOG_POST}{FILENAME}",
                    level=logging.INFO,
                    datefmt='%d-%m-%y %H:%M:%S',
                    format=log_format,
                    filemode='a')

logster = logging.StreamHandler()
logster.setLevel(logging.INFO)

formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
logster.setFormatter(formatter)
logging.getLogger().addHandler(logster)

log = logging.getLogger()