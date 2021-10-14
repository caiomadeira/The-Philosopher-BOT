import random


class RandomUtils:

    @staticmethod
    def random_function(func1, func2):
        number = random.randint(0, 1)
        if number == 0:
            return func1
        elif number == 1:
            return func2
