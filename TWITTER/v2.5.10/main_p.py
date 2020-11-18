"""
posting.py
Philosopher Bot
---------------
Created by Caio Madeira (@sudomaidera)
Co-worker: Rodrigo Carmo @rodrigoblock

instagram: @sudomadeira
Twitter: @bot_philospher
Avaliable on Discord too!

"""
from Posting.posting import *
from Credentials.credentials_verify import *
from art import tprint
import schedule, time

v = api


def sched_posting():
    schedule.every(5).seconds.do(PostDiario)  # Activate for test
    # schedule.every(3).seconds.do(self.posting)  # Activate for test
    # schedule.every(4).hours.do(self.posting())  # 4 hours define to default

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':

    try:
        (tprint("POSTING V2.1"))
        sched_posting()

    except tweepy.error.TweepError as e:
        print(e)
        time.sleep(2)

    finally:
        sched_posting()
