import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
from PIL import Image, ImageDraw, ImageFont, ImageOps
import random
import os
import re
import json
import textwrap
import schedule
#from win32con import TEXT
# Autenticadores do twitter (pessoal)
auth = OAuthHandler("Vp1n7BXhLaS1tY3dds0BT6Reh", "gKT1C5mkWRdl0BkhvkujWF8LNn8keeFEK3aBt8Dvr7KaYxUfSb")
auth.set_access_token("1263355414248390662-4td7amcj7vMWiHwWQxhILZT7eczLa9","qhQCTPZz13ro1IwB9OWsNUliDOzTGUUqLf7stpo7VWdAG")

api = tweepy.API(auth, wait_on_rate_limit=False, wait_on_rate_limit_notify=True)  # Criando um objeto do api


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        if status_code == 420:
            return False


if __name__ == "__main__":
    my_streamer = MyStreamListener()
    the_api = api
    myStream = tweepy.Stream(auth=the_api.auth, listener=MyStreamListener())
    myStream.filter(track=['#PhiloBot'])