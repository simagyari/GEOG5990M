# Import statements
import random

# Assigning variables
y0 = 50
x0 = 50

y1 = 50
x1 = 50

# Random movement for y0 and x0
if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1

if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1

print(y0, x0)

# Second step for 0s
if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1

if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1

print(y0, x0)

# Random movement for y1 and x1
if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1

if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1

print(y1, x1)

# Second step for 1s
if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1

if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1

print(y1, x1)

# Calculate Euclidean distance between points
distance = ((y0 - y1)**2 + (x0 - x1)**2)**0.5
print("Distance of the points is", distance)
