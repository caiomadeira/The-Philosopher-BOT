from Services.Authentication.authentication import Authentication
from Services.Streaming.streaming import Listener, Stream
from Utils.Scripts.post_status import post_status_only_text
hashtags = ['#testephilo', '#testemaker']


class StartStream:
    # API Authentication
    def __init__(self):
        auth = Authentication()
        auth = auth.getAuthorization()

        print("Autorização bem sucedida.")
        print(f"Usuário: {auth.username}")
        post_status_only_text("#testephilo")
        # Listen a Stream by topic
        myStreamListener = Listener()
        myStream = Stream(auth=auth, listener=myStreamListener)
        myStream.filter(track=hashtags)

