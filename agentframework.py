import random


# Defines Agent class, containing agents for abm
class Agent:

    # Instance variables of the class objects
    def __init__(self, identity, environment, agents):
        """
        None

        Parameters:
        -----------
        None

        Returns:
        --------
        None
        
        """
        self.id = identity
        self.environment = environment
        self.__x = random.randint(0, len(self.environment[0]) - 1)  # get environment width (challenge 4)
        self.__y = random.randint(0, len(self.environment) - 1)  # get environment height (challenge 4)
        self.store = 0
        self.received = 0  # amount received from other agents in sharing session
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
        """
        Make agents move in a Torus space of the environment.

        Parameters:
        -----------
        None

        Returns:
        --------
        None
        
        """
        if random.random() < 0.5:
            self.y = (self.y + 1) % len(self.environment)
        else:
            self.y = (self.y - 1) % len(self.environment)

        if random.random() < 0.5:
            self.x = (self.x + 1) % len(self.environment[0])
        else:
            self.x = (self.x - 1) % len(self.environment[0])

    def eat(self): # can you make it eat what is left?
        """
        Make agents eat by increasing stored value and decreasing cell value.

        Parameters:
        -----------
        None

        Returns:
        --------
        None
        
        """
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
        """
        Overwrite the in-built string method to print the id, coordinates and storage of the agent.

        Parameters:
        -----------
        None

        Returns:
        --------
        Agent attributes text : str
        
        """
        return 'I am agent ' + str(self.id) + ' with location: Y = ' + str(self.y) + \
               ' and X = ' + str(self.x) + ' storing ' + str(self.store)

    # Make agents to sick up their store if it goes over 100 (challenge 6)
    def sick(self):
        """
        Make agent deposit stored amount if it exceeds 100 units.

        Parameters:
        -----------
        None

        Returns:
        --------
        None
        
        """
        if self.store > 100:
            self.environment[self.y][self.x] += self.store
            self.store = 0

    # Share food with other agents in the neighbourhood
    def share_with_neighbours(self, neighbourhood):
        """
        Obtain the list of agents in the neighbourhood and give them equal shares of half the stored value

        Parameters:
        -----------
        neighbourhood : int (defines the radius of neighbourhood in pixels)

        Returns:
        --------
        None

        """
        # Loop through agents
        neighbours = []  # list of neighbours
        for agent in self.agents:
            distance = self.distance_between(agent)
            if distance <= neighbourhood and agent.id != self.id:  # check to not add yourself
                neighbours.append(agent)  # populate neighbour list
        # Loop through neighbour list
        for neighbour in neighbours:
            neighbour.received += self.store / len(neighbours) / 2  # Divide up half the storage equally
        self.store /= 2  # Halve stored amount as it has been shared

    # Add received food to storage
    def share_eater(self):
        """
        Add the content of the received attribute to the store attribute, then set received to 0.

        Parameters:
        -----------
        None

        Returns:
        --------
        None

        """
        self.store += self.received
        self.received = 0

    # Distance measuring method
    """
    Measure the distance between self and agent.

    Parameters:
    -----------
    None

    Returns:
    --------
    None

    """
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) +
            ((self.y - agent.y)**2))**0.5
