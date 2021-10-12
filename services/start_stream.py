from services.authentication.authentication import Authentication
from services.twitter_service import Listener, Stream
from utils.Scripts.post_status import post_status_only_text
hashtags = ['#testephilo', '#testemaker']


class StartStream:
    # API authentication
    def __init__(self):
        auth = Authentication()

        print("Autorização bem sucedida.")
        print(f"Usuário: {auth.username}")
        post_status_only_text("#testephilo")
        # Listen a Stream by topic
        myStreamListener = Listener()
        myStream = Stream(auth=auth, listener=myStreamListener)
        myStream.filter(track=hashtags)

