# _*_ coding: utf-8 _*_
"""
Philosopher Bot, 2021
---------------
Created by Caio Madeira
Co-worker: Rodrigo Carmo

instagram: @sudomadeira
Twitter: @bot_philospher
Avaliable on Discord too!
"""

import time, os
from utils.suport_twitter import SuportTwitter


class SuportStreaming(SuportTwitter):

    def save_data_on_txt(self, data):
        """This method is for analysis"""
        content_list = []
        # data type --> __dict__
        time.sleep(0.5)

        data_write = open("raw_data.txt", 'w+')
        data_write.write((str(data)))
        r = data_write.read()
        comma = ','
        for i in r:
            if i == comma:
                i = '\n'
            content_list.append(i)
        j = ''.join(content_list)
        data_write.write(j)
        data_write.close()

    """ DATA MANAGER """

    def verify_queue(self, list, do_func):
        # if  of list is equal or major to queue
        if len(list) == 3:
            print("Itens na lista ", len(list))
            f = do_func

            # for test ----
            if f(type) == str:
                return print(f)
            # --------------
            return f

# S = SuportStreaming()
# S.save_data_on_txt(data='AAAAAAAAAAAA')
