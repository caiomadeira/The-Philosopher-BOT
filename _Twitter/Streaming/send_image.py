import time
import tweepy as t

from _Twitter.Authentication.authentication import Authentication


class SendImage:

    @staticmethod
    def update(img_path, status, post_username):
        number = 1
        try:
            auth = Authentication()
            auth = auth.getAuthorization()
            auth_obj = t.API(auth, wait_on_rate_limit=False, wait_on_rate_limit_notify=True)

            t.Cursor(auth_obj.user_timeline).items(number)
            auth_obj.update_with_media(img_path, status="@" + post_username + " ", auto_populate_reply_metadata=True,
                                       in_reply_to_status_id=status)
            print('\nImagem enviada.\n')
            time.sleep(3)
        except t.TweepError as e:
            print(e.reason)
            print("\nERRO! Não foi possivel realizar a ação para o usuário.\n")
