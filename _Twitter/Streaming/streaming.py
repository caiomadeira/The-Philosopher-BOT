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

# Connect to Twitter keys
from tweepy import StreamListener, Stream  # OAuth is the o manipulator of authentication
import json

# Imports suport class
from _Twitter.Streaming.suport_streaming import SuportStreaming
from _Twitter.Streaming.template_manager import Template_Manager
from _Twitter.Streaming.DataObtainer.data_obtainer import DataObtainer


# listener herance of Stream Listener
class Listener(StreamListener, SuportStreaming, DataObtainer):
    def __init__(self):
        super().__init__()

        # init all attributtes of streaming like lists and variables
        self.queue = 1

    # get All data about status, user, etc with means for HEAVY ANALYSIS
    # on_data() handles: replies to status, deletes, events, direct messages, friends, limits, disconnects and warnings

    def on_data(self, raw_data):
        data = json.loads(raw_data)

        """ This callback is for analysis """
        data_to_str = str(data)
        self.save_data_on_txt(data=data_to_str)

        # Send data to Class DataObteriner
        self.data_userinfo_organized(data=data)
        self.data_statusinfo_organized(data=data)
        self.data_statussituation_organized(data=data)

        # Check hashtag type (Philobot or PhiloMaker)
        # instance of method which_hashtag which means that the method is no a class method and and has no inheritance
        print('Check hashtag type (Philobot or PhiloMaker)')
        manager = Template_Manager(data=data)
        manager.which_hashtag()

        return True

    # on_status() just handles statuses. Use for basic analysis
    def on_status(self, status):
        # handle connection exceptions temporally
        if isinstance(ValueError, ConnectionError) is True:
            return Listener()

    def on_error(self, status):
        if status == 200:
            print(status + "Sucesso")
            return True
        elif status == 420:
            print(status + "Falha")
            return False
        else:
            print(status)
            return True

    def on_timeout(self):
        # time out method
        return Listener()
