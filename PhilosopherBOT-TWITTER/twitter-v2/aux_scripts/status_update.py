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

auth = tweepy.OAuthHandler("Vp1n7BXhLaS1tY3dds0BT6Reh", "gKT1C5mkWRdl0BkhvkujWF8LNn8keeFEK3aBt8Dvr7KaYxUfSb")
auth.set_access_token("1263355414248390662-4td7amcj7vMWiHwWQxhILZT7eczLa9",
                      "qhQCTPZz13ro1IwB9OWsNUliDOzTGUUqLf7stpo7VWdAG")

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)



# ----------------------------------------------------


while True:
    print("::::::::::::::::::::::::::::::::")
    print(" STATUS PHILOBOT UPDATE HASHTAG")
    print("::::::::::::::::::::::::::::::::")
    print(" 1 = ON // 2 = OFF")

    Digitar = int(input("Digite o status desejado:"))

    if Digitar == 1:
        print("=========================================")
        print("Atualizando o Status do BOT: ATIVO")
        description = "Tweets aleatoriamente atribuídos a personagens históricos.\n \
        Updates e informações no SITE.\n Status: ONLINE\n Time: @sudomadeira | @rodrigoblock4 | @Tiago_Linharess\n | #Philobot |"
        name = 'Philosopher BOT'
        url = ''
        location = ''
        api.update_profile(name, url, location, description)
    if Digitar == 2:
        print("=========================================")
        print("Atualizando o Status do BOT: INATIVO")
        description = "Tweets aleatoriamente atribuídos a personagens históricos.\n \
                Updates e informações no SITE.\n Status: OFFLINE\n Time: @sudomadeira | @rodrigoblock4 | @Tiago_Linharess \n | #Philobot |"
        name = 'Philosopher BOT'
        url = ''
        location = ''
        api.update_profile(name, url, location, description)

