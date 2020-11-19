"""
posting.py
Philosopher Bot
---------------
Created by Caio Madeira
Co-worker: Rodrigo Carmo

instagram: @sudomadeira
Twitter: @bot_philospher
Avaliable on Discord too!

"""
from Posting.posting import PostDiario
from Credentials.credentials_verify_test import *
from art import tprint
import schedule, time
from config import HOURS, MINUTES ,SECONDS

v = api



def sched_posting():

    schedule.every(SECONDS).seconds.do(PostDiario)  # Activate for test
    # chedule.every(HOURS).hours.do(PostDiario)  # 2 hours define to default

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':

    try:
        (tprint("POSTING"))
        sched_posting()

    except tweepy.error.TweepError as e:
        print(e)
        time.sleep(2)
