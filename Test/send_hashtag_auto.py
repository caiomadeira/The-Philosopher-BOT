import secrets
import time


def generate_status():
    status_key = "#Testephilo " + secrets.token_hex(16)

    return status_key


def send_auto_tt(status):
    try:
        from Credentials.Twitter.Test.test_credentials import API_TEST
        API_TEST.update_status(status)
        print("Post aleatório feito com sucesso!")

    except Exception as e_posting:
        print(e_posting)


if __name__ == '__main__':

    while True:
        send_auto_tt(status=generate_status())
        time.sleep(60)
