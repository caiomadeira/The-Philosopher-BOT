import time

import tweepy
from PIL import Image
import os
from Logs.Twitter.logger_hashtag import log_philobot
from Hashtag.localizable.strings import philobot_strings
from Hashtag.patterns.template_ import Template
from Lists.sub_list import sub_list_philobot
from Hashtag.patterns.suport_ import Suport
from Templates.New_Img_Manipulation.reference import TEMPLATES_PATH, TEMPLATES_PATH_LAYER_3


class PhiloBot(Template, Suport):
    log = log_philobot(__name__)

    def philobot_engine(self):

        self.log.info(philobot_strings['div1'])
        self.log.info(philobot_strings['start'])
        self.log.info(philobot_strings['div1'])
        while len(self.q) > 0:

            last_id = self.q.pop(0)
            self.log.info('LAST ID:' + last_id)
            # self.log.info(philobot_strings['ID_Col'] + last_id)

            try:
                get_status = self.api.get_status(last_id, tweet_mode='extended', include_entities=False)._json[
                    'full_text']
                self.log.info('[ETAPA 1] Status coletado: ' + get_status)
            except tweepy.error.TweepError as e:
                self.log.info(e)
                self.log.info('ERRO: FALHA NA PEGA DO ID - TWEET DELETADO')
                self.log.info('----------------------------------------\n')
                self.log.info('>AGUARDANDO NOVOS TWEETS...<')
                from Hashtag.hashtag import HashtagClass
                return HashtagClass

            # " CHECK RT =================================================================================== "
            # self.check_rt_SAFE(LOG=self.log, q_tweet_info=self.q_tweet_info.pop(0),
            #                    q_username_pop=self.q_username.pop(0))
            # self.log.info("Saiu na check RT")
            " TEXT TREATMENT ============================================================================== "

            " CHECK EMPTY STRING ========================================================================= "
            # self.check_emptystring(LAST_ID=last_id,
            #                        LOG=self.log,
            #                        clear_users_param=self.q_username,
            #                        philobot_hashtag='#PhiloBot',
            #                        philomaker_hashtag='#PhiloMaker',
            #                        remove_user_from_list=self.q_username.pop(0),
            #                        first_status_param=get_status)

            " TEMPLATE 1 // DEFAULT  ======================================================================= "
            self.default_template(status_text=get_status, LOG=self.log, clear_users_param=self.q_username)

            " POST IMAGE =================================================================================== "
            self.update(post=self.img_saved, status=last_id, post_username=self.q_username.pop(0))


        self.log.info(philobot_strings['div1'])
        " CLEAR USERNAME LIST =============================================================================== "
        self.clear_user_list(LOG=self.log, clear_users_param=self.q_username)
        " TIME OUT ========================================================================================== "
        self.time_to_rest(LOG=self.log, start=1, stop=20, clear_users_param=self.q_username)

        from Hashtag.hashtag import HashtagClass
        return HashtagClass

    def update(self, post, status, post_username):
        number = 1
        try:
            tweepy.Cursor(self.api.user_timeline).items(number)
            self.api.update_with_media(post, status="@" + post_username + " ", auto_populate_reply_metadata=True,
                                       in_reply_to_status_id=status)
            self.log.info('Estatos postado')
            self.log.info('update -> IMAGEM ENVIADA!')
            self.log.info('update -> Finalizado, ID tratado: ' + status)
            self.log.info('update -> Itens restantes: ' + str(len(self.q)))
            self.log.info('update -> TWEET TRATADO COM SUCESSO')
            time.sleep(3)
        except tweepy.TweepError as e:
            self.log.info(e.reason)
            self.log.info("update -> ERRO! Não foi possivel realizar a ação para o usuário.")
            self.log.info("\n==========================")
