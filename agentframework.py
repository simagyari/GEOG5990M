import random


# Defines Agent class, containing agents for abm
class Agent:

    # Instance variables of the class objects
    def __init__(self, environment, agents):
        self.environment = environment
        self.__x = random.randint(0, len(self.environment[0]))  # get environment width (challenge 4)
        self.__y = random.randint(0, len(self.environment))  # get environment height (challenge 4)
        self.store = 0
        self.agents = agents

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

    # Moves agent (y and x coordinates respectively) in a Torus space of the environment (challenge 4)
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % len(self.environment)
        else:
            self.y = (self.y - 1) % len(self.environment)

        if random.random() < 0.5:
            self.x = (self.x + 1) % len(self.environment[0])
        else:
            self.x = (self.x - 1) % len(self.environment[0])

    def eat(self): # can you make it eat what is left?
        # If the cell has more food than 10, eats 10 of it (subtract and store)
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        # Else, if the cell has food remaining, eat all and shrink cell to zero (challenge 5)
        elif self.environment[self.y][self.x] > 0:
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0

    # Overwriting inbuilt str method to print agent properties instead (challenge 3)
    def __str__(self):
        return 'I am an agent with location: Y = ' + str(self.y) + ' and X = ' + str(self.x) + ' storing ' + str(self.store)

    # Make agents to sick up their store if it goes over 100 (challenge 6)
    def sick(self):
        if self.store > 100.0:  # Must be integer to sort out 100.0x values that don't trigger sickness
            self.environment[self.y][self.x] += self.store
            self.store = 0

    # Share food with other agents in the neighbourhood
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            distance = self.distance_between(agent)
            if distance <= neighbourhood:
                average = (self.store + agent.store) / 2
                self.store = average
                agent.store = average

    # Distance measuring method
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) +
            ((self.y - agent.y)**2))**0.5

