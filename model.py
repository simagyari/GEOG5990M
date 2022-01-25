# Import statements
import random
import operator
import matplotlib.pyplot as plt

# Add number of agents
num_of_agents = 10
num_of_iterations = 100

# Initialising empty agent coordinates list
agents = []

# Filling agent coordinate list
for i in range(num_of_agents):
    agents.append([random.randint(0, 99), random.randint(0, 99)])  # Add one set of coordinates to the list

print(agents)

# Random movement for agent coordinates
# Loop through every movement instance
for i in range(num_of_iterations):
    # Loop through every agent in the agents list
    for k in range(num_of_agents):
        # Create random movement for y coordinate
        # Implementing Torus space by adding modulo of 100, agents placed tp other side if wandering off
        if random.random() < 0.5:
            agents[k][0] = (agents[k][0] + 1) % 100
        else:
            agents[k][0] = (agents[k][0] - 1) % 100
        # Create random movement for x coordinate
        if random.random() < 0.5:
            agents[k][1] = (agents[k][1] + 1) % 100
        else:
            agents[k][1] = (agents[k][1] - 1) % 100

# # Calculate Euclidean distance between points
# distance = ((agents[0][0] - agents[1][0])**2 + (agents[0][1] - agents[1][1])**2)**0.5
# print('Distance of the points is', distance)

# Print the maximum of the two lists by the first element
print('The maximum of elements by y coordinates:', max(agents))

# Print the maximum of the two lists by the second element
print('The maximum of elements by x coordinates: ', max(agents, key=operator.itemgetter(1)))

# Plotting the random points
plt.ylim(0, 99)  # Height limit of figure
plt.xlim(0, 99)  # Width limit of figure
# Add points recursively
for i in range(num_of_agents):
    plt.scatter(agents[i][1], agents[i][0])
plt.show()  # Show figure