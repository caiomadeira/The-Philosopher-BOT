import dotenv
import os


class SuportTwitter:
    def __init__(self):
        dotenv.load_dotenv(dotenv.find_dotenv())

    def e(self, key):
        return os.getenv(key=key)
