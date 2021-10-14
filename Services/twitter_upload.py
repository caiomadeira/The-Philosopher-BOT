import random
from services.authentication.authentication import Authentication


class TwitterUpload:
    def __init__(self):
        super().__init__()
        self.__OAuth = Authentication(is_debug=True)
        self.auth = self.__OAuth.setup_auth()

    def update(self, status, image, user):
        __USER_PREFIX = "@"
        self.auth.update_with_media(image, status=__USER_PREFIX + user,
                                    auto_populate_reply_metadata=True,
                                    in_reply_to_status_id=status)

        print('\nThe image has send.\n')

    """ Suport methods. """
    @staticmethod
    def hashable_name():
        name = random.getrandbits(128)
        print("Image saved as a new name:", name)
        return str(name)

