import random


class Calculator:
    def sum(self, a, b):
        return a + b

    @staticmethod
    def get_random(start, end):
        return random.randint(0, 9)