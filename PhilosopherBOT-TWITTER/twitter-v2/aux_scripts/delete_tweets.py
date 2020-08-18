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
from pip._vendor.distlib.compat import raw_input

auth = tweepy.OAuthHandler("XXXXXXXXXXXXXXXXXXXX", "XXXXXXXXXXXXXXXXXXXX")
auth.set_access_token("XXXXXXXXXXXXXXXXXXXXXXXXX", "XXXXXXXXXXXXXXXXXXX")


api = tweepy.API(auth, wait_on_rate_limit = False, wait_on_rate_limit_notify = True)


api = tweepy.API(auth, wait_on_rate_limit = False, wait_on_rate_limit_notify = True)

# ----------------------------------------------------
print("::::::::::::::::::::::::::::::::")
print(" DELETE PHILOBOT TWEETS")
print("::::::::::::::::::::::::::::::::")

user = api.me()

print("Nome do seu perfil : " + user.name)
print("Sua ID : " + str(user.id))
print("Seu nome de usuário : " + user.screen_name)
print("Sua localização : " + user.location)
print("-----------------------------------------")

confirmar_delete = raw_input("> ")

if confirmar_delete.lower() == 'sim':
    for status in tweepy.Cursor(api.user_timeline).items():
        try:
            api.destroy_status(status.id)
            print("Deletado!", status.id)
        except:

           print("Falha ao deletar:", status.id)

print("Finalizado!")