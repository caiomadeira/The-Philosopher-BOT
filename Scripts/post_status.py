import time
import uuid
from _Twitter.Authentication.authentication import Authentication
import tweepy as t

auth = Authentication()
auth = auth.getAuthorization()
auth_obj = t.API(auth, wait_on_rate_limit=False, wait_on_rate_limit_notify=True)

def post_status_only_text(text):
    try:
        status_key = ''.join(str(uuid.uuid4()).upper().split('-')[1:])
        status_2 = f'{text} {status_key}'
        time.sleep(1)
        auth_obj.update_status(status_2)
        print(status_2)
        time.sleep(2)
    except Exception as e:
        print(e)

