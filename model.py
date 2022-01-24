# Import statements
import random


agents = []

# Assigning variables
y0 = random.randint(0, 99)
x0 = random.randint(0, 99)
agents.append([y0, x0])

y1 = random.randint(0, 99)
x1 = random.randint(0, 99)
agents.append([y1, x1])

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
print("Distance of the points is", distance)
