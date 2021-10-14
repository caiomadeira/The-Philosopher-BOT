import uuid

from services.authentication.authentication import Authentication
from services.twitter_service import Listener
from tweepy import *
hashtags = ['#testephilo', '#testemaker']


class StartStream:
    # API authentication
    def __init__(self):
        __service = Authentication(is_debug=True)
        __tokens = __service.set_tokens()
        __Oauth = __service.get_authorization(tokens=__tokens)
        __auth_api = Authentication(is_debug=True).setup_auth()

        key = ''.join(str(uuid.uuid4()).upper().split('-')[1:])

        text_bigger = f"#testephilo Lorem54 99I9"

        print(len(text_bigger))

        text_key_10 = f"#testephilo  Lorem I44sum is simply dummy text of the54"
        text_key = f"#testephilo {key}"
        __auth_api.update_status(text_bigger)

        myStream = Stream(auth=__Oauth, listener=Listener())
        myStream.filter(track=hashtags)


StartStream()