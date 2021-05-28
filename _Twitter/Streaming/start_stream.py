from _Twitter.Authentication.authentication import Authentication
from _Twitter.Streaming.streaming import Listener, Stream
from Scripts.post_status import post_status_only_text
hashtags = ['#testephilo', '#testemaker']


class StartStream:
    # API Authentication
    auth = Authentication()
    auth = auth.getAuthorization()

    print("Autorização bem sucedida.")
    print(f"Usuário: {auth.username}")
    post_status_only_text("#testephilo")
    # Listen a Stream by topic
    myStreamListener = Listener()
    myStream = Stream(auth=auth, listener=myStreamListener)
    myStream.filter(track=hashtags)

