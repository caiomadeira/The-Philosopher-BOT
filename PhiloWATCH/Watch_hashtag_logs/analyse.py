import time
import datetime
from PhiloWATCH.Logs_pw.logger import log
import os
from dotenv import load_dotenv
from PhiloWATCH.Alert.email_module import send_alert
from PhiloWATCH.Watch_hashtag_logs.rescue import heartbeat
from PhiloWATCH.Watch_hashtag_logs.extract_data import open_file, extract_date_log


def analyse_data(use_data, signal):
    now = datetime.datetime.now()

    count = now - use_data

    log.info("---------------------------------------------")
    log.info("[!] - Horário coletado no log para análise:")
    log.info(use_data)
    log.info("---------------------------------------------\n")
    log.info("---------------------------------------------")
    log.info("[!] - Horário atual:")
    log.info(now)
    log.info("---------------------------------------------\n")
    log.info("---------------------------------------------")
    log.info("[!] - Quanto o tempo o bot ficou sem postar: ")
    log.info(count)
    log.info("---------------------------------------------\n")

    load_dotenv()
    try:
        if count > datetime.timedelta(seconds=int(os.getenv('tolerance_time'))):
            log.info(f"[!] - Função HASHTAG completou {os.getenv('tolerance_time')} minutos sem utilização")

            if signal:
                log.info("[!] - Reiniciando script para renovar conexão...\n")

                script_location = os.getenv('script_location')[1:]
                project_location = os.getenv('project_location')[1:]

                log.info(project_location)

                try:
                    os.system(f'start cmd /c "cd {project_location} & python {script_location}"')
                    log.info("[+] - Script reiniciado com sucesso!")
                    log.info("[!] - Enviando e-mail de informação...")
                    send_alert(os.getenv('subject_recovey'))
                    log.info("--------------------------------------------------\n")

                except Exception as exe_cmd_error:
                    log.error("[X] - Erro ao executar o script para rodar comando.")
                    log.error(exe_cmd_error)
                    log.info("-------------------------------------------------\n")
                    log.info("[!] - Enviando e-mail de alerta...")
                    send_alert(os.getenv('subject_total_fail'))

            else:

                log.info("[!] - Enviando tweet de HEARTBEAT para verificar sinais vitais do bot...")

                get_response_hb = heartbeat()

                log.info("[!] - Aguardando tempo de tratativa do bot")
                time.sleep(10)

                after_heartbeat(get_response_hb=get_response_hb)

        elif signal:
            log.info(f"[!] - BOT está VIVO e respondendo aos HEARTBEATS")
            log.info("[+] - Hashtag em funcionamento. Apenas o HEARTBEAT foi enviado para verificação.\n")

        else:
            log.info(f"[!] - Logs estão normais, foram atualizados em menos de {os.getenv('tolerance_time')} minutos.")
            log.info("[+] - Hashtag em funcionamento. Nenhuma ação foi tomada\n")

    except Exception as analyse_error:
        log.info("[X] - Erro encontrado ao tentar analisar os dados coletados!")
        log.info(analyse_error)
        log.info("-------------------------------------------------\n")
        log.info("[!] - Enviando e-mail de alerta...")
        send_alert(os.getenv('subject_total_fail'))


def after_heartbeat(get_response_hb):

    if not get_response_hb:
        log.info("[!] - Reiniciando script para renovar conexão...\n")

        script_location = os.getenv('script_location')[1:]

        try:
            os.system(f'start cmd /c "python {script_location}"')
            log.info("[+] - Script reiniciado com sucesso!")
            log.info("[!] - Enviando e-mail de informação...")
            send_alert(os.getenv('subject_recovey'))
            log.info("--------------------------------------------------\n")

        except Exception as exe_cmd_error:
            log.error("[X] - Erro ao executar o script para rodar comando novamente.")
            log.error(exe_cmd_error)
            log.info("-------------------------------------------------\n")
            log.info("[!] - Enviando e-mail de alerta...")
            send_alert(os.getenv('subject_total_fail'))

    if get_response_hb:
        log.info("[!] - Verificando se o bot está vivo...")
        try:
            data_info_after_HB = extract_date_log(use_data_log=open_file(attempts=0))
            analyse_data(data_info_after_HB, signal=True)

        except Exception as check_bot_again_error:
            log.error("[X] - Ocorreu um erro desconhecido ao tentar verificar os logs do bot após o HEARTBEAT")
            log.error(check_bot_again_error)
            log.info("-------------------------------------------------\n")
            log.info("[!] - Enviando e-mail de alerta...")
            send_alert(os.getenv('subject_total_fail'))
