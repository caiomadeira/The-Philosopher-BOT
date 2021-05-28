import random
import time
import tweepy
from PIL import Image, ImageFont
from _Twitter.Old.functionalities import Functionalities
from Lists.img_list import PHILOSOPHERS_LIST
from Templates.New_Img_Manipulation.reference import TEMPLATES_PATH
from Logs.Twitter.logger_hashtag import log_philobot


class PhiloBot(Functionalities):

    def philobot_engine(self, get_hashtag_list):

        self.log = log_philobot(__name__)

        from _Twitter.Old.hashtag import HashtagClass
        hashtag_list = get_hashtag_list
        self.log.info('----------------------------------------')
        self.log.info('         > STARTING PHILOBOT < ')
        self.log.info('----------------------------------------')
        while len(self.q) > 0:

            last_id = self.q.pop(0)
            self.log.info('ID Coletado: ' + last_id)
            self.img = Image.open(f'{TEMPLATES_PATH}/layer_1.png')
            txt = "Font/myriad.otf"
            self.fontsize = 1
            blank = Image.new('RGB', (269, 194))
            self.font = ImageFont.truetype("Font/myriad.otf", self.fontsize)
            try:
                self.get_status = self.api.get_status(last_id, tweet_mode='extended', include_entities=False)._json[
                    'full_text']
                self.log.info('[ETAPA 1] Status coletado: ' + self.get_status)
            except tweepy.error.TweepError as e:
                self.log.info(e)
                self.log.info('ERRO: FALHA NA PEGA DO ID - TWEET DELETADO')
                self.log.info('----------------------------------------\n')
                self.log.info('>AGUARDANDO NOVOS TWEETS...<')

                time.sleep(2)
                return HashtagClass

            " CHECK RT =================================================================================== "
            try:
                check_rt_func = self.check_rt(LOG=self.log)
                if check_rt_func:
                    self.log.info('----------------------------------------\n')
                    self.log.info('>AGUARDANDO NOVOS TWEETS...<')
                    return HashtagClass

                else:
                    pass

            except Exception as e_check_rt:
                self.log.info('ERRO: FALHA AO VERIFICAR SE É RETWEET')
                self.log.info(e_check_rt)
                return HashtagClass

            """""""""""""""""""""""""""""""""

            [+] TRATANDO O TEXTO
            """""""""""""""""""""""""""""""""
            self.text_treatment(PEG_STATUS=self.get_status, IMG=self.img, SUB_LIST=hashtag_list, LOG=self.log)
            time.sleep(2)

            " CHECK EMPTY STRING ========================================================================= "
            returned_check_philo = self.check_emptystring(last_id=last_id, LOG=self.log, PHILOMAKER=False)

            if returned_check_philo:
                self.log.info('----------------------------------------\n')
                self.log.info('>AGUARDANDO NOVOS TWEETS...<')
                return HashtagClass

            time.sleep(2)

            while (self.font.getsize(txt)[0] < blank.size[0]) and (self.font.getsize(txt)[1] < blank.size[1]):
                self.fontsize += 1
                self.font = ImageFont.truetype("Font/myriad.otf", self.fontsize)
            self.log.info('[ETAPA 4] Configurando imagem...')
            self.fontsize -= 1
            self.font = ImageFont.truetype("Font/myriad.otf", self.fontsize)
            self.drawing.textsize(txt, font=self.font)

            self.choice_philosopher = random.choice(PHILOSOPHERS_LIST)

            """
            [+] AJUSTANDO TEXTO
            """
            try:
                self.text_adjust(choice_philosopher=self.choice_philosopher, LOG=self.log)

            except Exception as e:
                self.log.error('ERRO: FALHA AO REALIZAR AJUSTE DE TEXTO')
                self.log.error(e)

            """
            [+] AJUSTANDO IMAGEM
            """
            try:
                self.img_adjust()
            except Exception as e:
                self.log.error('ERRO: FALHA AO REALIZAR AJUSTE DE IMAGEM')
                self.log.error(e)

            " ========================================================================================= "

            self.log.info('[ETAPA 5] Verificando aspas...')
            if self.get_treated_status.startswith('"') and self.get_treated_status.endswith('"'):

                post_with_quotes = self.img_with_quotes(LOG=self.log, PHILO_NAME=self.finish_name_of_philosopher)

                self.update(post=post_with_quotes, status=last_id, post_username=self.q_username.pop(0))

                self.log.info('Finalizado, ID tratado: ' + last_id)
                self.log.info('Itens restantes: ' + str(len(self.q)))

            else:
                post_without_quotes = self.img_without_quotes(LOG=self.log, PHILO_NAME=self.finish_name_of_philosopher)
                self.update(post=post_without_quotes, status=last_id, post_username=self.q_username.pop(0))

                self.log.info('Finalizado, ID tratado: ' + last_id)
                self.log.info('Itens restantes: ' + str(len(self.q)))
                self.log.info('TWEET TRATADO COM SUCESSO')
        self.log.info('----------------------------------------\n')

        self.log.info('[LIMPANDO LISTAS E MEMÓRIAS...]')
        try:
            self.q_username.clear()
            self.log.info('Limpeza realizada com sucesso!')
        except Exception as e_garbage:
            self.log.error('ERRO: FALHA AO REALIZAR LIMPEZA')
            self.log.error(e_garbage)

        self.log.info("Esperando 20 segundos...")
        time.sleep(20)
        self.log.info('>AGUARDANDO NOVOS TWEETS...<')

        self.log.info('[LOG PARA DEBUG - PROBLEMA MARCAÇÃO ERRADA - TEMPORARIO]')
        self.log.info('ITENS NA LISTA:')
        self.log.info(self.q_username)

        return HashtagClass

    def img_adjust(self):
        philosopher_str_to_obj = Image.open(self.choice_philosopher)
        self.img_2 = philosopher_str_to_obj.resize((449, 584))
        self.img.paste(self.img_2, (629, 0))
        smooth_template = Image.open(f'{TEMPLATES_PATH}/layer_3.png')
        self.img.paste(smooth_template, (0, 0), smooth_template)