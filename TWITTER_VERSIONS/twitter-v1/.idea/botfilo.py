import tweepy
import time

# Autenticadores do twitter (pessoal)
auth = tweepy.OAuthHandler("Vp1n7BXhLaS1tY3dds0BT6Reh", "gKT1C5mkWRdl0BkhvkujWF8LNn8keeFEK3aBt8Dvr7KaYxUfSb")
auth.set_access_token("1263355414248390662-xS5BbMGm6W0P6r4HD73WO0RWEZZSRj", "Wb17D3yWejo4lL4zI3Bw5pLaeKEDTkr9m2wCbXcZoaU5L")

api = tweepy.API(auth) # Criando um objeto do api

FILE_NAME = 'last_seen_id.txt'



print("online fi")

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen(file_name, last_seen_id):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


last_seen_id = retrieve_last_seen_id(FILE_NAME)
mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')

for mention in reversed(mentions):
        print(str(mention.id)+ ' - ' +mention.full_text)
        last_seen_id = mention.id
        store_last_seen(last_seen_id, FILE_NAME)
        if '#PhiloBot' in mention.full_text.lower():
            print('achei')
            print("respondendo...")

