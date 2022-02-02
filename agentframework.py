import random


# Defines Agent class, containing agents for abm
class Agent:

    # Instance variables of the class objects
    def __init__(self, environment):
        self.__x = random.randint(0, 99)
        self.__y = random.randint(0, 99)
        self.environment = environment
        self.store = 0

    # Getter and setter functions for name-mangled variables
    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, value):
        self.__x = value

    def set_y(self, value):
        self.__y = value

    # Property values for name-mangled variables
    x = property(get_x, set_x, "I'm the 'x' property!")
    y = property(get_y, set_y, "I'm the 'y' property!")

    # Moves agent (y and x coordinates respectively) in a Torus space of 100x100 units
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100

    def eat(self): # can you make it eat what is left?
        # If the cell has more food than 10, eats 10 of it (subtract and store)
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10

    def __str__(self):
        return 'I am an agent with location: Y = ' + str(self.y) + ' and X = ' + str(self.x) + ' storing ' + str(self.store)
