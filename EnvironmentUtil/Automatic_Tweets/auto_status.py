from Credentials.Twitter.Test import API_MAIN_TEST
import time
import uuid

api = API_MAIN_TEST


def post_status_with_media(IMG_PATH):
    for i in range(1):
        status_test = input("\nDigite o status que deseja postar:")

        api.update_with_media(IMG_PATH, status=status_test)

        time.sleep(3)
        break


def post_status_only_text():
    status_test = input("\nDigite o status que deseja postar:")

    api.update_status(f'{status_test}  @felipeneto')

    time.sleep(3)


def AUTO_post_status_with_media(IMG_PATH):

    for i in range(1):
        status_key = ''.join(str(uuid.uuid4()).upper().split('-')[1:])

        NEW_STATUS = api.update_with_media(IMG_PATH, status=f'#Testemaker {status_key}' + ' @felipeneto')
        NEW_STATUS_GET_ID = NEW_STATUS.id
        time.sleep(1.5)
        return NEW_STATUS_GET_ID



def choose_auto_tweet():
    question = input("[1] - Escrever status com foto(já definida)\n"
                     "[2] - Escrever só status\n"
                     "[3] - STATUS (UUID HASH) COM IMAGEM TUDO AUTOMATICO\n>")
    if question == '1':
        from EnvironmentUtil.Automatic_Tweets.reference import IMG_TEST_PATH
        IMG_PATH = fr'{IMG_TEST_PATH}/test_img2.png'
        post_status_with_media(IMG_PATH=IMG_PATH)

    elif question == '2':
        post_status_only_text()

    elif question == '3':
        from EnvironmentUtil.Automatic_Tweets.reference import IMG_TEST_PATH
        IMG_PATH = fr'{IMG_TEST_PATH}/test_img2.png'
        AUTO_post_status_with_media(IMG_PATH=IMG_PATH)
    else:
        import sys
        print("Encerrando")
        sys.exit(1)

