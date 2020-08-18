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
import tweepy
import time
import schedule
from posting import postdiario
from acess_tokens import *


auth = tweepy.OAuthHandler(acess1, acess2)
auth.set_access_token(acess3, acess4)

wait1 = wait_on_rate_limit = False
wait2 = wait_on_rate_limit_notify = True

api = tweepy.API(auth, wait1, wait2)


def main():

    schedule.every(2).hours.do(postdiario)
    # schedule.every(3).seconds.do(postdiario) --> for test

    while True:
        schedule.run_pending()
        time.sleep(10)
    return


if __name__ == '__main__':
    main()

