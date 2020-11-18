from Logs.logger_hashtag import log
import random
from Hashtag.hashtag import update, q_username


def check_emptystring(lastid):
    log.info('STRING VAZIA DETECTADA!')

    error_collection = ['templates/templateERRO6.png', 'templates/templateERRO1.png', 'templates/templateERRO2.png',
                        'templates/templateERRO3.png', 'templates/templateERRO4.png', 'templates/templateERRO5.png',
                        'templates/templateGIFERRO.gif']

    escolher_img = random.randrange(0, len(error_collection))
    img_selecionada = error_collection[escolher_img]

    user = q_username.pop(0)
    log.info('ENVIANDO TEMPLATE DE AJUDA PARA O @{}.'.format(user))

    update(post=img_selecionada, status=lastid, username=user)
    log.info('Voltando a ouvir tweets...')
