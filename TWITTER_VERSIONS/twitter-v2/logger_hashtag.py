import logging
import datetime
log_time = datetime.date.today()

log_format = "%(asctime)s - %(message)s"
logging.basicConfig(filename=rf"C:\Users\caiom\Desktop\Python Projects\Philospher-Bot-Project\Teste-PhiloBot\TEST-BOT\logs\{log_time} - hashtag_log.txt",
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