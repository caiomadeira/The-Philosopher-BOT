import secrets
from PhiloWATCH.Logs_pw.logger import log


def heartbeat():
    hb_key = "#Philobot HEARTBEAT " + secrets.token_hex(16)

    try:
        from Credentials.Twitter.PhiloWATCH.philowatch_credentials import API_TEST
        API_TEST.update_status(hb_key)
        log.info("[+] - HEARTBEAT enviado com sucesso!")
        log.info("------------------------------------------\n")

        return True

    except Exception as send_hb_error:
        log.error("[X] - Ocorreu um erro ao enviar o heatbeat:")
        log.error(send_hb_error)
        log.error("------------------------------------------\n")

        return False
