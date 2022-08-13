import time
from Test.test_log import log_bot

log_bot.info("Iniciando teste de continuidade de registro de logs...\n")

for i in range(100):
    log_bot.info("Este é um log gerado apeas para motivo de teste NUMERO 2...")
    time.sleep(1)
