import random


# Defines Agent class, containing agents for abm
class Agent:

    # Instance variables of the class objects
    def __init__(self, identity: int, environment: list, agents: list, y=None, x=None) -> None:
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
        if x == None:
            self.__x = random.randint(0, len(self.environment[0]) - 1)  # get environment width (challenge 4)
        else:
            self.__x = x
        if y == None:
            self.__y = random.randint(0, len(self.environment) - 1)  # get environment height (challenge 4)
        else:
            self.__y = y
        self.store = 0
        self.received = 0  # amount received from other agents in sharing session
        self.agents = agents


    # Getter and setter functions for name-mangled variables
    def get_x(self) -> int:
        return self.__x


    def get_y(self) -> int:
        return self.__y


    def set_x(self, value: int) -> None:
        self.__x = value


    def set_y(self, value: int) -> None:
        self.__y = value


    # Property values for name-mangled variables
    x = property(get_x, set_x, "I'm the 'x' property!")
    y = property(get_y, set_y, "I'm the 'y' property!")


    # Moves agent (y and x coordinates respectively) in a Torus space of the environment (challenge 4)
    def move(self) -> None:
        """
        Make agents move in a Torus space of the environment with different speed depending on their stored food.

        Parameters:
        -----------
        None

        Returns:
        --------
        None
        
        """
        # Change speed if there's lot of food in store (if sheep feels full, can jump two)
        if self.store > 50:
            speed = 2
        else:
            speed = 1
        
        # Randomly change x and y coordinates by speed (every direction enabled)
        if random.random() > 0.75:
            self.y = (self.y + speed) % len(self.environment)
        elif random.random() < 0.25:
            self.y = (self.y - speed) % len(self.environment)
        else:
            pass

        if random.random() > 0.75:
            self.x = (self.x + speed) % len(self.environment[0])
        elif random.random() < 0.25:
            self.x = (self.x - speed) % len(self.environment[0])
        else:
            pass


    def eat(self) -> None: # can you make it eat what is left?
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
    def __str__(self) -> str:
        """
        Overwrite the in-built string method to print the id, coordinates and storage of the agent.

        Parameters:
        -----------
        None

        Returns:
        --------
        str : printed agent attributes
        
        """
        return 'I am agent ' + str(self.id) + ' with location: Y = ' + str(self.y) + \
               ' and X = ' + str(self.x) + ' storing ' + str(self.store)


    # Make agents to sick up their store if it goes over 100 (challenge 6)
    def sick(self) -> None:
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
    def share_with_neighbours(self, neighbourhood: int) -> None:
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
    def share_eater(self) -> None:
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
    def distance_between(self, agent) -> float:
        """
        Measure the distance between self and agent.

        Parameters:
        -----------
        agent : agentframework.Agent object

        Returns:
        --------
        float : distance between self and agent in pixel

        """
        return (((self.x - agent.x)**2) +
            ((self.y - agent.y)**2))**0.5
