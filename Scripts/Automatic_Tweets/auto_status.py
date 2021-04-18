from Tests.Credentials.twitter_credentials_test import API_TEST as API
import time
import uuid
import random

api = API


def post_status_with_media(IMG_PATH):
    for i in range(1):
        status_test = input("\nDigite o status que deseja postar:")

        api.update_with_media(IMG_PATH, status=status_test)

        time.sleep(3)
        break


def post_status_only_text():
    try:
        status_key = ''.join(str(uuid.uuid4()).upper().split('-')[1:])
        status_2 = f'#TestePhilo {status_key}'
        status_3 = f'#TestePhilo "{status_key}"'
        status_4 = f'#TestePhilo "{status_key}{status_key}{status_key}"'

        api.update_status(status_2)
        print(status_2)
        time.sleep(2)
    except Exception as e:
        print(e)


def AUTO_post_status_with_media(IMG_PATH):
    for i in range(1):
        status_key = ''.join(str(uuid.uuid4()).upper().split('-')[1:])

        NEW_STATUS = api.update_with_media(IMG_PATH, status=f'#Testemaker {status_key}' + ' @felipeneto')
        NEW_STATUS_GET_ID = NEW_STATUS.id
        time.sleep(1.5)
        return NEW_STATUS_GET_ID
