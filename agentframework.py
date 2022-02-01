import random


class Agent:

    def __init__(self):
        self.__x = random.randint(0, 99)
        self.__y = random.randint(0, 99)

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, value):
        self.__x = value

    def set_y(self, value):
        self.__y = value

    x = property(get_x, set_x, "I'm the 'x' property!")
    y = property(get_y, set_y, "I'm the 'y' property!")

    def move(self):
        if random.random() < 0.5:
            self.__y = (self.__y + 1) % 100
        else:
            self.__y = (self.__y - 1) % 100

        if random.random() < 0.5:
            self.__x = (self.__x + 1) % 100
        else:
            self.__x = (self.__x - 1) % 100
