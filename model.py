import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import agentframework
import agentstorage
import csv
import random
import argparse


# Updates agents one by one
def update(frame_number):
    """
    Update agent position and behaviour.

    Parameters:
    -----------
    frame_number : int (set automatically to equal number of model iterations, only used in animation)

    Returns:
    --------
    None

    """
    fig.clear()  # clears scatter points from earlier iteration
    random.shuffle(agents)  # shuffle agents to eliminate position-based advantages
    for a in range(num_of_agents):
        agents[a].eat()
    for a in range(num_of_agents):
        agents[a].move()
    for a in range(num_of_agents):
        agents[a].share_with_neighbours(neighbourhood)
    for a in range(num_of_agents):
        agents[a].share_eater()
    for a in range(num_of_agents):
        agents[a].sick()
    # Plot agents on a scatterplot recursively adding points onto the environment raster (only on single model run)
    plt.imshow(environment)
    for b in range(num_of_agents):
        plt.scatter(agents[b].x, agents[b].y)


# # Create command-line functionality (needs positional arguments from command line to run)
# parser = argparse.ArgumentParser(description='Simulate random moving agents grazing a field and sharing food')
# # Add arguments
# parser.add_argument('agents', help='Number of agents (integer)', type=int)
# parser.add_argument('iterations', help='Number of iterations (integer)', type=int)
# parser.add_argument('neighbourhood', help='Radius of agent communication zone (integer)', type=int)
# parser.add_argument('--multirun', help='Specifies if the model is run as a subprocess or not (integer, defult: 0)',
#                     type=int, required=False, default=0)

# Create command-line functionality (needs positional arguments from command line to run)
parser = argparse.ArgumentParser(description='Simulate random moving agents grazing a field and sharing food')
# Add arguments
parser.add_argument('--agents', help='Number of agents (integer)', type=int, required=False, default=10)
parser.add_argument('--iterations', help='Number of iterations (integer)', type=int, required=False, default=100)
parser.add_argument('--neighbourhood', help='Radius of agent communication zone (integer)', type=int, required=False, default=20)
parser.add_argument('--multirun', help='Specifies if the model is run as a subprocess or not (integer, defult: 0)',
                    type=int, required=False, default=0)

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

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(i, environment, agents))

# Create figure for animated plotting
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_autoscale_on(False)  # Does not scale automatically

# Only shows results if it isn't inside a subprocess
if multirun == 0:
    # Defining animation part with stopping at num_of_iterations and no looping
    animation = FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
    plt.show()
else:
    for i in range(num_of_iterations):
        update(frame_number=range(num_of_iterations))

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
