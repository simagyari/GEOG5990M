# Import statements
import random
import operator
import matplotlib.pyplot as plt
import time

# Setting the seed of the random module
random.seed(42)

# Define function for pythagorean distance
def distance_between(agents_row_a, agents_row_b):
    return ((agents_row_a[0] - agents_row_b[0])**2 + (agents_row_a[1] - agents_row_b[1])**2)**0.5


# Add number of agents (min 2 for timing)
num_of_agents = [2, 20, 200, 400, 600, 800, 1000]
num_of_iterations = 100

# Initialising empty agent coordinates list
agents = []

# Loop through agent numbers
for num in num_of_agents:
# Filling agent coordinate list
    for i in range(num):
        agents.append([random.randint(0, 99), random.randint(0, 99)])  # Add one set of coordinates to the list

    print(agents)

    # Torus space size constraint
    space = 100

    # Random movement for agent coordinates
    # Loop through every movement instance
    for i in range(num_of_iterations):
        # Loop through every agent in the agents list
        for k in range(num):
            # Create random movement for y coordinate
            # Implementing Torus space by adding modulo of the space constraint, agents placed to other side if wandering off
            if random.random() < 0.5:
                agents[k][0] = (agents[k][0] + 1) % space
            else:
                agents[k][0] = (agents[k][0] - 1) % space
            # Create random movement for x coordinate
            if random.random() < 0.5:
                agents[k][1] = (agents[k][1] + 1) % space
            else:
                agents[k][1] = (agents[k][1] - 1) % space

    # Calculate Euclidean distance between points
    start = time.process_time()  # Timing of distance starts
    min_dist = distance_between(agents[0], agents[1])
    max_dist = distance_between(agents[0], agents[1])
    for i in range(num):
        for j in range(i+1, num, 1):  # Search optimised to consider every pair once and neglect identical point pairs
            dist = distance_between(agents[i], agents[j])
            # print('Distance between agents', i, 'and', j, 'is:', dist)
            min_dist = min(min_dist, dist)
            max_dist = max(max_dist, dist)
    end = time.process_time()  # Timing of distance ends
    print('Time of distance function:', str(end - start))
    print('The minimum distance between agents is', min_dist)
    print('The maximum distance between agents is', max_dist)
    plt.scatter(num, end-start)  # Add time point to scatter plot

    # # Print the maximum of the two lists by the first element
    # print('The maximum of elements by y coordinates:', max(agents))

    # # Print the maximum of the two lists by the second element
    # print('The maximum of elements by x coordinates: ', max(agents, key=operator.itemgetter(1)))

    # # Plotting the random points
    # plt.ylim(0, 99)  # Height limit of figure
    # plt.xlim(0, 99)  # Width limit of figure
    # # Add points recursively
    # for i in range(num):
    #     plt.scatter(agents[i][1], agents[i][0])
    # plt.show()  # Show figure
plt.xlabel('Number of agents')
plt.ylabel('Time spent by calculating distance')
plt.show()