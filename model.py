import matplotlib.pyplot as plt
import agentframework
import agentstorage
import csv


# Reading raster data
with open('in.txt', 'r') as f:
    environment = []
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)  # QUOTE_NONNUMERIC changes everything to float
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
        environment.append(rowlist)


# Declare number of agents and iterations, along with neighbourhood size
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
agents = []  # Initialise list of agents

# Initialise single agent as test case
a = agentframework.Agent(environment, agents)
type(a)  # Check if it is an agentframework agent
print(a.y, a.x)  # To check if instance attributes are recognised
a.move()  # Moves agent
print(a.y, a.x)

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))

# Move and make the agents eat, then sick if 100+ is stored
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        agents[i].sick()  # Challenge 6

# Plot agents on a scatterplot recursively adding points onto the environment raster
plt.xlim(0, len(environment[0]))
plt.ylim(0, len(environment))
plt.imshow(environment)
for i in range(num_of_agents):
    plt.scatter(agents[i].x, agents[i].y)
plt.show()


# Challenges:
# 1. Write environment out at the end to a file
with open('out.txt', 'w') as f:
    writer = csv.writer(f)
    for line in environment:
        writer.writerow(line)

# 2. Write total amounts stored by all agents to a line, append to file for every run
agentstorage.all_storage_writer(agents)
agentstorage.agent_storage_writer(agents)

# 3. Overwrite __str__ method of agents to print location and storage
for agent in agents:
    print(agent)