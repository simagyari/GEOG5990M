import unittest
import agentframework


# Create testing class, inheriting from unittest TestCase class
class TestAgentframework(unittest.TestCase):
    """Tests agentframework functions using unittest library."""

    # Test get_x function to return x
    def test_getx(self):
        a = agentframework.Agent(1, [[1,2,3], [1,2,3], [1,2,3]], [], 1, 2)  # initialise agent
        self.assertEqual(a.x, 2, "Should be 2")

    # Test get_y function to return y
    def test_gety(self):
        a = agentframework.Agent(1, [[1,2,3], [1,2,3], [1,2,3]], [], 1, 2)  # initialise agent
        self.assertEqual(a.y, 1, "Should be 1")

    # Test setting function of x
    def test_setx(self):
        a = agentframework.Agent(1, [[1,2,3], [1,2,3], [1,2,3]], [], 1, 2)  # initialise agent
        a.x = 1  # Set x attribute
        self.assertEqual(a.x, 1, "Should be 1")

    def test_sety(self):
        a = agentframework.Agent(1, [[1,2,3], [1,2,3], [1,2,3]], [], 1, 2)  # initialise agent
        a.y = 0  # set y attribute
        self.assertEqual(a.y, 0, "Should be 0")

    # Test x for raising correct error (ValueError) on setting to non-integer
    def test_setx_error(self):
        a = agentframework.Agent(1, [[1,2,3], [1,2,3], [1,2,3]], [], 1, 2)  # initialise agent
        # Test if error is raised when setting x to string
        with self.assertRaises(ValueError, msg="Should be ValueError!"):
            a.x = "String"

    # Test y for raising correct error (ValueError) on setting to non-integer
    def test_sety_error(self):
        a = agentframework.Agent(1, [[1,2,3], [1,2,3], [1,2,3]], [], 1, 2)  # initialise agent
        # Test if error is raised when setting y to string
        with self.assertRaises(ValueError, msg="Should be ValueError"):
            a.y = "String"

    # Test eating function to increase store with the appropriate amount
    def test_eat(self):
        a = agentframework.Agent(1, [[1,2,3], [1,2,3], [1,2,3]], [], 1, 2)  # initialise agent
        a.eat()  # make agent eat, if correct, returns 3 in store instead of max 10 per eating
        self.assertEqual(a.store, 3, "Should be 3")

    # Test overwrite of inbuilt __str__ property
    def test_str_overwrite(self):
        a = agentframework.Agent(1, [[1,2,3], [1,2,3], [1,2,3]], [], 1, 2)  # initialise agent
        self.assertEqual(str(a), 'I am agent 1 with location: Y = 1 and X = 2 storing 0', "Not appropriate string")

    # Test sickness property
    def test_sick(self):
        a = agentframework.Agent(1, [[1,2,3], [1,2,3], [1,2,3]], [], 1, 2)  # initialise agent
        a.store = 99  # Set store to below sickness threshold
        a.eat()  # Eats three of environment
        a.sick()  # Above-100 store induces sickness
        self.assertEqual(a.store, 0, "Should be 0")

    # Test moving function
    def test_move(self):
        a = agentframework.Agent(1, [[1,2,3], [1,2,3], [1,2,3]], [], 1, 2)  # initialise agent
        a.move()  # Moves the agents inside the toroid
        # Value must be 0, 1, or 2 regardless of starting coordinates in this case, due to toroid
        self.assertIn(a.y, [0, 1, 2], "Should be 0, 1, or 2")
        self.assertIn(a.x, [0, 1, 2], "Should be 0, 1, or 2")

    # Test sharing function with neighbours
    def test_share_with_neighbours(self):
        # Initiate four agents for neighbour sharing to cover all situations (0, 1, multiple neighbours)
        agents = []
        a = agentframework.Agent(1, [[1,2,3], [1,2,3], [1,2,3]], agents, 1, 2)
        b = agentframework.Agent(2, [[1,2,3], [1,2,3], [1,2,3]], agents, 0, 1)
        c = agentframework.Agent(3, [[1,2,3], [1,2,3], [1,2,3]], agents, 2, 0)
        d = agentframework.Agent(4, [[1,2,3], [1,2,3], [1,2,3]], agents, 1, 1)
        agents.extend([a, b, c, d])
        # Populate stores
        a.store = 10
        b.store = 20
        c.store = 30
        d.store = 40
        # Test share_with_neighbours
        for agent in agents:
            agent.share_with_neighbours(neighbourhood=1)  # Might fail sometimes due to imperfect floats compared to integers
        self.assertEqual(a.received, 10, "Should be 10")  # Gets half of d.store
        self.assertEqual(b.received, 10, "Should be 10")  # Gets half of d.store
        self.assertEqual(c.received, 0, "Should be 0")  # No received
        self.assertEqual(d.received, 15, "Should be 15")  # Gets half of a.store and b.store

    # Test eating the received food from sharing
    def test_share_eater(self):
        # Initiate four agents for neighbour sharing to cover all situations (0, 1, multiple neighbours)
        agents = []  # Store agents in list
        a = agentframework.Agent(1, [[1,2,3], [1,2,3], [1,2,3]], agents, 1, 2)
        b = agentframework.Agent(2, [[1,2,3], [1,2,3], [1,2,3]], agents, 0, 1)
        c = agentframework.Agent(3, [[1,2,3], [1,2,3], [1,2,3]], agents, 2, 0)
        d = agentframework.Agent(4, [[1,2,3], [1,2,3], [1,2,3]], agents, 1, 1)
        agents.extend([a, b, c, d])
        # Populate stores
        a.store = 10
        b.store = 20
        c.store = 30
        d.store = 40
        # Make agents share
        for agent in agents:
            agent.share_with_neighbours(neighbourhood=1)  # Might fail sometimes due to imperfect floats compared to integers
        # Test share_eater, should add received amount to store
        for agent in agents:
            agent.share_eater()
        self.assertEqual(a.store, 15, "Should be 15")
        self.assertEqual(b.store, 20, "Should be 20")
        self.assertEqual(c.store, 30, "Should be 30")
        self.assertEqual(d.store, 35, "Should be 35")

    # Test distance measuring function
    def test_distance_between(self):
        # Initiate four agents
        a = agentframework.Agent(1, [[1,2,3], [1,2,3], [1,2,3]], [], 1, 2)
        b = agentframework.Agent(2, [[1,2,3], [1,2,3], [1,2,3]], [], 0, 1)
        c = agentframework.Agent(3, [[1,2,3], [1,2,3], [1,2,3]], [], 2, 0)
        d = agentframework.Agent(4, [[1,2,3], [1,2,3], [1,2,3]], [], 1, 1)
        # Test distance_between on every combination of agents
        self.assertEqual(a.distance_between(a), 0, "Should be 0")
        self.assertEqual(a.distance_between(b), 2**0.5, "Should be the sqrt of 2")
        self.assertEqual(a.distance_between(c), (1**2 + 2**2)**0.5, "Should be (1**2 + 2**2)**0.5")
        self.assertEqual(a.distance_between(d), 1, "Should be 1")
        self.assertEqual(b.distance_between(b), 0, "Should be 0")
        self.assertEqual(b.distance_between(c), (1**2 + 2**2)**0.5, "Should be the sqrt of 2")
        self.assertEqual(b.distance_between(d), 1, "Should be 1")
        self.assertEqual(c.distance_between(c), 0, "Should be 0")
        self.assertEqual(c.distance_between(d), 2**0.5, "Should be the sqrt of 2")
        self.assertEqual(d.distance_between(d), 0, "Should be 0")


if __name__ == "__main__":
    unittest.main()
