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
#from acess_tokens import *
from acess_tokens_reserva import *
from posting import PostDiario

auth = tweepy.OAuthHandler(acess1, acess2)
auth.set_access_token(acess3, acess4)

wait1 = wait_on_rate_limit = False
wait2 = wait_on_rate_limit_notify = True

api = tweepy.API(auth, wait1, wait2)

c = PostDiario()
c.sched_posting()


