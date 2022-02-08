import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import agentframework
import agentstorage
import csv
import random
import argparse


# Updates agents one by one
def update(frame_number):
    fig.clear()  # clears scatter points from earlier iteration
    for i in range(num_of_agents):
        random.shuffle(agents)  # shuffle agents to eliminate position-based advantages
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        agents[i].sick()  # Challenge 6
    # Plot agents on a scatterplot recursively adding points onto the environment raster (only single model run)
    plt.imshow(environment)
    for i in range(num_of_agents):
        plt.scatter(agents[i].x, agents[i].y)

# Create command-line functionality (needs positional arguments from command line to run)
parser = argparse.ArgumentParser(description='Simulate random moving agents grazing a field and sharing food')
# Add arguments
parser.add_argument('agents', help='Number of agents (integer)', type=int)
parser.add_argument('iterations', help='Number of iterations (integer)', type=int)
parser.add_argument('neighbourhood', help='Radius of agent communication zone (integer)', type=int)
parser.add_argument('--multirun', help='Specifies if the model is run as a subprocess or not (integer, defult: 0)', type=int, required=False, default=0)

# Reading raster data
with open('in.txt', 'r') as f:
    environment = []
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)  # QUOTE_NONNUMERIC changes everything to float
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
        environment.append(rowlist)


# Declare number of agents and iterations, along with neighbourhood size (all from argparse cmd)
num_of_agents = parser.parse_args().agents
num_of_iterations = parser.parse_args().iterations
neighbourhood = parser.parse_args().neighbourhood
multirun = parser.parse_args().multirun
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

# Create figure for animated plotting
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_autoscale_on(False)  # Does not scale automatically

# Move and make the agents eat, then sick if 100+ is stored
# for j in range(num_of_iterations):
#     update()

# Defining animation part
animation = FuncAnimation(fig, update, interval=1)
plt.show()
# Only shows results if it isn't inside a subprocess
# if multirun == 0:
#     plt.show()


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