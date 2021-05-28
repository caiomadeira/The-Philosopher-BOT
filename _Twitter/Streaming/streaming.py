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
from tweepy import StreamListener, Stream  # OAuth é o manipulador de autenticacao
import json

# Imports suport class
from _Twitter.Streaming.suport_streaming import SuportStreaming


# listener herance of Stream Listener
class Listener(StreamListener, SuportStreaming):
    def __init__(self):
        super().__init__()

        # init all attributtes of streaming like lists and variables
        self.queue = 1

    # get All data about status, user, etc with means for HEAVY ANALYSIS
    # on_data() handles: replies to statuses,deletes ,events,direct messages,friends,limits, disconnects and warnings

    def on_data(self, raw_data):
        data = json.loads(raw_data)

        data_to_str = str(data)
        self.save_data_on_txt(data=data_to_str)

        # User information
        get_screen_name = data['user']['screen_name']
        get_user_id = data['user']['id']
        get_user_id_str = data['user']['id_str']
        is_truncated = data['truncated']

        # Status Information
        get_status_text = data['text']
        get_hashtag_from_status = data['entities']['hashtags']  # the hashtag format (lower, upper, etc) writes by user
        get_status_id = data['id']  # type is int
        get_status_id_str = data['id_str']

        # Status situation
        get_status_language = data['lang']
        is_status_retweeted = data['retweeted']
        reply_to_status_id = data['in_reply_to_status_id']
        reply_to_status_id_str = data['in_reply_to_status_id_str']
        reply_to_user_id = data['in_reply_to_user_id']
        in_reply_to_user_id_str = data['in_reply_to_user_id_str']
        in_reply_to_screen_name = data['in_reply_to_screen_name']

        # Append in respectives dictionarys
        user_information = {"User Name": get_screen_name,
                            "User ID": get_user_id,
                            "User ID Str": get_user_id_str,
                            "Is Truncated": is_truncated}

        status_information = {"Status Text": get_status_text,
                              "Status ID": get_status_id,
                              "Status ID Str": get_status_id_str,
                              "Status Hashtag Typed": get_hashtag_from_status}

        status_situation = {"Status Language": get_status_language,
                            "Is retweeted": is_status_retweeted,
                            "Reply Status ID": reply_to_status_id,
                            "Reply Status ID Str": reply_to_status_id_str,
                            "Reply User ID": reply_to_user_id,
                            "Reply User ID Str": in_reply_to_user_id_str,
                            "Reply Screen Name": in_reply_to_screen_name, }

        print("User Information: ", user_information)
        print("Status Information: ", status_information)
        print("Status Situation: ", status_situation)

        # exec random template
        # exec_func = self.verify_queue(list=self.status_information, do_func='Executando Philobot')
        return True

    # on_status() just handles statuses. Use for basic analysis
    def on_status(self, status):
        pass

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
