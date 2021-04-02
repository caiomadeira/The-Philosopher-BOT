import random
import re
import tweepy
import time
from PIL import ImageDraw

from Lists.error_img_list import PHILOBOT_ERROR_IMAGE_COLLECTION
from Lists.error_img_list import PHILOMAKER_ERROR_IMAGE_COLLECTION


class Suport(object):

    def check_emptystring(self, last_id, LOG, PHILOMAKER,clear_users_param ):
        LOG.info("[ETAPA 4] Checando string vazia...")
        try:
            if not self.get_treated_status:
                if PHILOMAKER:
                    self.send_error_empty_string(LAST_ID=last_id, LOG=LOG, PHILOMAKER=PHILOMAKER)
                    return True
                else:
                    self.send_error_empty_string(LAST_ID=last_id, LOG=LOG, PHILOMAKER=PHILOMAKER)
                    return True
        except Exception:
            from Hashtag.hashtag import HashtagClass
            LOG.error('ERRO: FALHA AO CHECAR SE A STRING É VAZIA')
            self.clear_user_list(LOG=LOG, clear_users_param=clear_users_param)

            LOG.info('----------------------------------------\n')
            LOG.info('>AGUARDANDO NOVOS TWEETS...<')
            return HashtagClass

    def send_error_empty_string(self, LAST_ID, LOG, PHILOMAKER):
        try:
            LOG.info('STRING VAZIA DETECTADA!')
            if PHILOMAKER:
                choice_error_img = random.choice(PHILOMAKER_ERROR_IMAGE_COLLECTION)
            else:
                choice_error_img = random.choice(PHILOBOT_ERROR_IMAGE_COLLECTION)

            user = self.q_username.pop(0)
            LOG.info('ENVIANDO TEMPLATE DE AJUDA PARA O @{}.'.format(user))

            self.update(post=choice_error_img, status=LAST_ID, post_username=user)

        except Exception as e:
            LOG.exception('ERRO AO ENVIAR IMAGEM DE ERRO PARA O USUARIO!')
            LOG.exception(e)

    def basic_text_treatment(self, get_status_param, image_param, sub_list_param, LOG, clear_users_param):
        print("nem entro no try da basic_text")
        try:
            print("Entrou na função basic_text_treatment")
            self.remove_user = re.sub('@[^\s]+', '', get_status_param)
            print("Passou de self.remove_user")
            LOG.info('[ETAPA 2] Status - marcações retiradas: ')
            print(self.remove_user)
            print("Passou do LOG")
            self.treating_status = re.sub(r'https://.*[\r\n]*', '', self.remove_user)
            self.drawing = ImageDraw.Draw(image_param)

            sub_list_config = dict((re.escape(k), v) for k, v in sub_list_param.items())
            pattern = re.compile("|".join(sub_list_config.keys()))
            self.get_treated_status = pattern.sub(lambda m: sub_list_config[re.escape(m.group(0))],
                                                  self.treating_status).strip()
        except tweepy.error.TweepError as e:
            LOG.error(e)
            LOG.error('TRATAMENTO DE TEXTO CANCELADO - TWEET DELETADO')
            clear_users_param.clear()

    def check_rt(self, LOG, q_tweet_info, q_username_pop):

        LOG.info("[ETAPA 3] Checando se é RT...")
        verify_rt_info = q_tweet_info
        if 'retweeted_status' in verify_rt_info:
            print('\n')
            LOG.info('RETWEET ENCONTRADO, IGNORANDO... - USER: {}'.format(q_username_pop))
            return True
        else:
            LOG.info("Nenhum RT Encontrado. Passando...")
            pass

    def check_rt_SAFE(self, LOG, q_tweet_info, q_username_pop):
        try:
            check_rt_func = self.check_rt(LOG=LOG, q_tweet_info=q_tweet_info, q_username_pop=q_username_pop)
            if check_rt_func:
                LOG.info('----------------------------------------\n')
                LOG.info('>AGUARDANDO NOVOS TWEETS...<')
                from Hashtag.hashtag import HashtagClass
                return HashtagClass
            else:
                LOG.info("Saindo da CHECK RT SAFE")
                pass

        except Exception as e_check_rt:
            LOG.info('ERRO: FALHA AO VERIFICAR SE É RETWEET')
            LOG.info(e_check_rt)
            from Hashtag.hashtag import HashtagClass
            return HashtagClass

    def clear_user_list(self, LOG, clear_users_param):
        try:
            clear_users_param.clear()
            LOG.info('Limpeza de lista realizada com sucesso!')
        except Exception as e_garbage:
            LOG.error('ERRO: FALHA AO REALIZAR LIMPEZA')
            LOG.error(e_garbage)
            from Hashtag.hashtag import HashtagClass
            return HashtagClass

    @staticmethod   # "Out" of class
    def time_to_rest(LOG, clear_users_param, start, stop):
        LOG.info("Esperando 20 segundos...")

        cont_range = range(start, stop)
        for number in reversed(cont_range):
            time.sleep(1)
            print(f'{number} Segundos restantes')
        LOG.info('>AGUARDANDO NOVOS TWEETS...<')
        LOG.info('ITENS NA LISTA:' + clear_users_param.__dict__, width=40)
