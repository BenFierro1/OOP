import random

"""
class Insect:
    def __init__(self):
        self.__wings = 2
        self.__legs = 4
        self.__flight = 0

    def flight_length(self):
        self.__flight = random.randint(1, 10)
        return self.__flight

    def __str__(self):
        return str(self.__flight)


"""


class Insect:
    def __init__(self, w, l, f):
        self.__wings = w
        self.__legs = l
        self.__flight = f

    def flight_length(self):
        self.__flight = random.randint(1, 10)
        return self.__flight

    def get_wings(self):
        return self.__wings

    def get_legs(self):
        return self.__legs

    def __str__(self):
        return print(
            "Wings:",
            str(self.__wings),
            "\n",
            "legs:",
            str(self.__legs),
        )
