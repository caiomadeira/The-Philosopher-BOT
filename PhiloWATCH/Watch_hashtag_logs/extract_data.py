from datetime import datetime
import glob
import os
from dotenv import load_dotenv
import time
from PhiloWATCH.Logs_pw.logger import log


def open_file(attempts):
    load_dotenv()
    log_file_path = os.getenv('log_file_path')[1:].strip('"')

    log.info(log_file_path)

    list_of_files = glob.glob(log_file_path + r"\*.log")

    latest_file = max(list_of_files, key=os.path.getctime)

    log.info("[!] - Arquivo de log coletado: " + latest_file + "\n")

    try:
        with open(latest_file, 'r') as log_line:
            data_log = log_line.readlines()[-1]
            if len(data_log) < 3:  # Caso a linha que o programa pegue, seja uma linha em branco (utilizada para espaçar)
                attempts_update = attempts + 1

                if attempts_update <= int(os.getenv('attempts')):
                    log.error("[X] - Linha vazia detectada!")
                    log.error(f"[!] - Tentativa {attempts_update} de {int(os.getenv('attempts'))}")
                    log.info(f"[!] - Aguardando {os.getenv('wait_to_check_again')} segundos e tentando novamente...")

                    time.sleep(int(os.getenv('wait_to_check_again')))
                    return open_file(attempts=attempts_update)

                else:
                    log.info("[X] - Foram realizadas 5 tentavidas de coleta de log, porém nenhuma linha coletada havia informação.")
                    exit()

            else:
                return data_log

    except Exception as read_file_error:
        log.info("[X] - Erro ao tentar ler o arquivo")
        log.info(read_file_error)


def extract_date_log(use_data_log):
    log = use_data_log

    log_time = log.split()[1]
    log_date = log.split()[0]

    date_and_time = log_date + log_time

    converted_log = datetime.strptime(date_and_time, '%Y-%m-%d%H:%M:%S,%f')

    return converted_log