import matplotlib.pyplot
import agentframework

# Measures distance between agents
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) +
        ((agents_row_a.y - agents_row_b.y)**2))**0.5

# Initialise single agent
a = agentframework.Agent()
type(a)  # Check if it is an agentframework agent
print(a.y, a.x)  # To check if instance attributes are recognised
a.move()  # Moves agent
print(a.y, a.x)

# Declare number of agents and iterations
num_of_agents = 10
num_of_iterations = 100
agents = []  # Initialise list of agents

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent())

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()

# Plot agents on a scatterplot recursively adding points
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
matplotlib.pyplot.show()

# Recursively measure distances
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
