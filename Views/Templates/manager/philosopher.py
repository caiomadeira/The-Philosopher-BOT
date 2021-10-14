import os
import random
from adapters.search_img import PHILOSOPHERS_LIST


class RandomPhilosopher:

    @staticmethod
    def philosopher_image():
        return random.choice(PHILOSOPHERS_LIST)

    @staticmethod
    def philosopher_name(philosopher_img):
        rm_path = os.path.basename(philosopher_img)
        rm_extension = rm_path.replace('.png', '')
        if '(2)' in rm_extension:
            rm_num = rm_extension.replace('(2)', '')
            name = f'- {rm_num}'
            return name
        else:
            name = f'- {rm_extension}'
            return name
