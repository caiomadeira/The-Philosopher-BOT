import random
import re
import tweepy
import time
from PIL import ImageDraw
from Lists.error_img_list import PHILOBOT_ERROR_IMAGE_COLLECTION
from Lists.error_img_list import PHILOMAKER_ERROR_IMAGE_COLLECTION


class Suport():

    def check_emptystring(self, LAST_ID, LOG, first_status_param, clear_users_param, philobot_hashtag,
                          philomaker_hashtag, remove_user_from_list):
        LOG.info("CHECK EMPTYSTRING -> Checando string vazia...")
        try:
            if not self.get_treated_status:
                if first_status_param == philobot_hashtag:

                    choice_error_img = random.choice(PHILOMAKER_ERROR_IMAGE_COLLECTION)
                    user = remove_user_from_list
                    LOG.info('CHECK EMPTYSTRING -> ENVIANDO TEMPLATE DE AJUDA PARA O @{}.'.format(user))

                    self.update(post=choice_error_img, status=LAST_ID, post_username=user)

                    LOG.info('CHECK EMPTYSTRING ->----------------------------------------\n')
                    LOG.info('CHECK EMPTYSTRING -> >AGUARDANDO NOVOS TWEETS...<')
                    from Hashtag.hashtag import HashtagClass
                    return HashtagClass

                elif first_status_param == philomaker_hashtag:

                    choice_error_img = random.choice(PHILOBOT_ERROR_IMAGE_COLLECTION)
                    user = remove_user_from_list
                    LOG.info('CHECK EMPTYSTRING -> ENVIANDO TEMPLATE DE AJUDA PARA O @{}.'.format(user))

                    self.update(post=choice_error_img, status=LAST_ID, post_username=user)

                    LOG.info('CHECK EMPTYSTRING ->----------------------------------------\n')
                    LOG.info('CHECK EMPTYSTRING -> >AGUARDANDO NOVOS TWEETS...<')
                    from Hashtag.hashtag import HashtagClass
                    return HashtagClass
                else:
                    LOG.info('CHECK EMPTYSTRING -> Imagem não enviada.')
        except Exception:
            from Hashtag.hashtag import HashtagClass
            LOG.info('CHECK EMPTYSTRING -> ERRO: FALHA AO CHECAR SE A STRING É VAZIA')
            self.clear_user_list(LOG=LOG, clear_users_param=clear_users_param)

            LOG.info('CHECK EMPTYSTRING ->----------------------------------------\n')
            LOG.info('CHECK EMPTYSTRING -> >AGUARDANDO NOVOS TWEETS...<')
            return HashtagClass

    # def basic_text_treatment(self, get_status_param, image_param, sub_list_param, LOG, clear_users_param):
    #
    #     try:
    #         LOG.info("BASIC TEXT TREATMENT -> Entrou na função basic_text_treatment")
    #         self.remove_user = re.sub('@[^\s]+', '', get_status_param)
    #         LOG.info("BASIC TEXT TREATMENT -> Passou de self.remove_user")
    #         LOG.info('BASIC TEXT TREATMENT -> marcações retiradas: ')
    #         LOG.info("BASIC TEXT TREATMENT -> " + self.remove_user)
    #         LOG.info("BASIC TEXT TREATMENT -> Passou do LOG")
    #         self.treating_status = re.sub(r'https://.*[\r\n]*', '', self.remove_user)
    #         drawing = ImageDraw.Draw(image_param)
    #
    #         sub_list_config = dict((re.escape(k), v) for k, v in sub_list_param.items())
    #         pattern = re.compile("|".join(sub_list_config.keys()))
    #         get_treated_status = pattern.sub(lambda m: sub_list_config[re.escape(m.group(0))],
    #                                               self.treating_status).strip()
    #
    #         return get_treated_status, drawing
    #     except tweepy.error.TweepError as e:
    #         LOG.error(e)
    #         LOG.info("BASIC TEXT TREATMENT -> TRATAMENTO DE TEXTO CANCELADO - TWEET DELETADO")
    #         clear_users_param.clear()

    def check_rt(self, LOG, q_tweet_info, q_username_pop):

        LOG.info("check_rt -> Checando se é RT...")
        verify_rt_info = q_tweet_info
        if 'retweeted_status' in verify_rt_info:
            print('\n')
            LOG.info('check_rt -> RETWEET ENCONTRADO, IGNORANDO... - USER: {}'.format(q_username_pop))
            return True
        else:
            LOG.info("check_rt -> Nenhum RT Encontrado. Passando...")
            pass

    def check_rt_SAFE(self, LOG, q_tweet_info, q_username_pop):
        try:
            check_rt_func = self.check_rt(LOG=LOG, q_tweet_info=q_tweet_info, q_username_pop=q_username_pop)
            if check_rt_func:
                LOG.info('check_rt_SAFE -> ----------------------------------------\n')
                LOG.info('check_rt_SAFE -> >AGUARDANDO NOVOS TWEETS...<')
                from Hashtag.hashtag import HashtagClass
                return HashtagClass
            else:
                LOG.info("check_rt_SAFE -> Saindo da CHECK RT SAFE")
                pass

        except Exception as e_check_rt:
            LOG.info('check_rt_SAFE -> ERRO: FALHA AO VERIFICAR SE É RETWEET')
            LOG.info(e_check_rt)
            from Hashtag.hashtag import HashtagClass
            return HashtagClass

    def clear_user_list(self, LOG, clear_users_param):
        try:
            clear_users_param.clear()
            LOG.info('clear_user_list -> Limpeza de lista realizada com sucesso!')
        except Exception as e_garbage:
            LOG.error('clear_user_list -> ERRO: FALHA AO REALIZAR LIMPEZA')
            LOG.error(e_garbage)
            from Hashtag.hashtag import HashtagClass
            return HashtagClass

    @staticmethod  # "Out" of class
    def time_to_rest(LOG, clear_users_param, start, stop):
        LOG.info("time_to_rest -> Esperando 20 segundos...")

        cont_range = range(start, stop)
        for number in reversed(cont_range):
            time.sleep(1)
            print(f'time_to_rest -> {number} Segundos restantes')
        LOG.info('time_to_rest -> >AGUARDANDO NOVOS TWEETS...<')
        LOG.info('time_to_rest -> ITENS NA LISTA:' + clear_users_param.__dict__, width=40)
