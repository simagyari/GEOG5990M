# Import statements
import random
import operator
import matplotlib.pyplot as plt

# Initialising empty agent coordinates list
agents = []

# Filling agent coordinate list
agents.append([random.randint(0, 99), random.randint(0, 99)])  # Assigning y0 and x0 to the list
agents.append([random.randint(0, 99), random.randint(0, 99)])  # Assigning y1 and x1 to the list

print(agents)

# Random movement for y0 and x0
if random.random() < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1

if random.random() < 0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1

print(agents[0][0], agents[0][1])

# Second step for 0s
if random.random() < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1

if random.random() < 0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1

print(agents[0][0], agents[0][1])

# Random movement for y1 and x1
if random.random() < 0.5:
    agents[1][0] += 1
else:
    agents[1][0] -= 1

if random.random() < 0.5:
    agents[1][1] += 1
else:
    agents[1][1] -= 1

print(agents[1][0], agents[1][1])

# Second step for 1s
if random.random() < 0.5:
    agents[1][0] += 1
else:
    agents[1][0] -= 1

if random.random() < 0.5:
    agents[1][1] += 1
else:
    agents[1][1] -= 1

print(agents[1][0], agents[1][1])

# Calculate Euclidean distance between points
distance = ((agents[0][0] - agents[1][0])**2 + (agents[0][1] - agents[1][1])**2)**0.5
print('Distance of the points is', distance)

# Print the maximum of the two lists by the first element
print(max(agents))

# Print the maximum of the two lists by the second element
print(max(agents, key=operator.itemgetter(1)))

# Plotting the random points
plt.ylim(0, 99)
plt.xlim(0, 99)
plt.scatter(agents[0][1], agents[0][0], color='red')
plt.scatter(agents[1][1], agents[1][0], color='blue')
plt.show()