from Watch_hashtag_logs.extract_data import extract_date_log, open_file
from Watch_hashtag_logs.analyse import analyse_data
from Alert.email_module import send_alert
from PhiloWATCH.Logs_pw.logger import log
import os
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()
    log.info("[!] - Iniciando análise de logs...")
    log.info("[!] - Chamando funções...\n")
    try:
        data_info = extract_date_log(use_data_log=open_file(attempts=0))
        analyse_data(use_data=data_info, signal=False)

    except Exception as main_error:
        log.info("[X] - Encountered an error trying to analyse collected data:")
        log.info(main_error)
        log.info("-------------------------------------------------\n")
        log.info("[!] - Enviando e-mail de alerta...")
        send_alert(os.getenv('subject_total_fail'))

